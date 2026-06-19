import hashlib
from pathlib import Path
import argparse
import json
from datetime import datetime

def get_file_hash(file_path):
    
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        while churns := f.read(8192):
            sha256.update(churns)

    return sha256.hexdigest()

def organize_file(target: Path, desti: Path, dry_run: bool=False):

    if not target.exists():
        print(f"Error: Target path {target} does not exist.")
        return
    
    print(f"Organizing files from {target} to {desti} {'(Dry Run)' if dry_run else ''}")

    hash_to_files = {}
    file_records = []
    actions = []
    total_files = 0
    skipped_files = []
    planned_destinations = set()
    ignored_dirs = {".git", "node_modules", "__pycache__"}

    # First pass: scan once and bucket by hash for duplicate detection.
    for file_path in target.rglob("*"):
        if not file_path.is_file():
            continue
        if any(part in ignored_dirs for part in file_path.parts):
            continue

        total_files += 1
        file_hash = get_file_hash(file_path)
        file_stat = file_path.stat()

        file_records.append((file_path, file_hash, file_stat.st_size, file_stat.st_mtime))
        hash_to_files.setdefault(file_hash, []).append(file_path)

    duplicates = {h: paths for h, paths in hash_to_files.items() if len(paths) > 1}
    duplicate_hashes = set(duplicates.keys())

    # Second pass: organize only non-duplicate files.
    for file_path, file_hash, file_size, file_mtime in file_records:
        if file_hash in duplicate_hashes and file_path != duplicates[file_hash][0]:
            skipped_files.append(str(file_path))
            print(f"Skipped duplicate copy: {file_path}")
            continue
        ext = file_path.suffix.lstrip(".").upper() or "NO_EXTENSION"
        date_folder = datetime.fromtimestamp(file_mtime).strftime("%Y-%m-%d")
        dest_folder = desti / ext / date_folder
        dest_path = dest_folder / file_path.name

        # Generate a unique name against existing and planned destinations.
        candidate = dest_path
        i = 0
        while candidate.exists() or candidate in planned_destinations:
            i += 1
            candidate = dest_folder / f"{file_path.stem}_{i}{file_path.suffix}"
        planned_destinations.add(candidate)

        action = {
            "source": str(file_path),
            "destination": str(candidate),
            "size": file_size,
            "hash": file_hash
        }

        if dry_run:
            print(f"Would move {file_path} to {candidate}")
            actions.append(action)
            continue

        dest_folder.mkdir(parents=True, exist_ok=True)
        try:
            file_path.rename(candidate)
            print(f"Moved {file_path} to {candidate}")
            actions.append(action)
        except PermissionError:
            skipped_files.append(str(file_path))
            print(f"Skipped locked file: {file_path}")

    # To save the report
    report = {
        "scanned" : total_files,
        "duplicates_found" : len(duplicates),
        "skipped_files" : skipped_files,
        "actions" : actions,
        "dry_run" : dry_run,
    }

    report_path = desti / "Organizer_report.json"
    if not dry_run:
        desti.mkdir(parents=True, exist_ok=True)
        with open(report_path, "w") as f:
            json.dump(report, f, indent=2)

    print(f"\n{'='*40}")
    print(f"Files Scanned: {total_files}")
    print(f"Duplicates Found: {len(duplicates)}")
    print(f"Files Organized : {len(actions)}")
    print(f"Files Skipped : {len(skipped_files)}")
    if skipped_files:
        print("Skipped locked files:")
        for skipped_file in skipped_files:
            print(f" - {skipped_file}")
    if not dry_run:
        print(f"Report saved to {report_path}")
    print(f"\n{'='*40}")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Smart File Organizer")
    parser.add_argument("--path", type=str, default=str(Path.home() / "Downloads"), help="Path to organize")
    parser.add_argument("--output", type=str, default=str(Path.home() / "Downloads"), help="Where to put organized file.")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without moving files.")

    args = parser.parse_args()

    organize_file(target = Path(args.path), desti = Path(args.output), dry_run = args.dry_run)