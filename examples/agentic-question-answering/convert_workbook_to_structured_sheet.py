import argparse
import csv
import os
import sqlite3
import time
from pathlib import Path

from deeptable import DeepTable


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workbook-path", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument(
        "--formats",
        nargs="+",
        choices=["sqlite", "csv"],
        default=["sqlite"],
    )
    parser.add_argument("--poll-interval-seconds", type=int, default=10)
    return parser.parse_args()


def wait_for_structured_sheet(client: DeepTable, structured_sheet_id: str, poll_interval_seconds: int):
    while True:
        structured_sheet = client.structured_sheets.retrieve(structured_sheet_id)
        if structured_sheet.status not in {"queued", "in_progress"}:
            return structured_sheet
        time.sleep(poll_interval_seconds)


def export_sqlite_tables_to_csv(sqlite_path: Path, csv_dir: Path) -> None:
    csv_dir.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(sqlite_path)
    try:
        table_rows = connection.execute(
            "SELECT name FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%' ORDER BY name"
        ).fetchall()

        for (table_name,) in table_rows:
            output_path = csv_dir / f"{table_name}.csv"
            cursor = connection.execute(f'SELECT * FROM "{table_name}"')
            headers = [description[0] for description in cursor.description or []]
            with output_path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.writer(handle)
                writer.writerow(headers)
                writer.writerows(cursor.fetchall())
    finally:
        connection.close()


def main() -> None:
    args = parse_args()

    workbook_path = Path(args.workbook_path).expanduser().resolve()
    output_dir = Path(args.output_dir).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    client = DeepTable(
        api_key=os.environ.get("DEEPTABLE_API_KEY"),
        base_url=os.environ.get("DEEPTABLE_BASE_URL"),
    )

    uploaded_file = client.files.upload(file=workbook_path)
    structured_sheet = client.structured_sheets.create(file_id=uploaded_file.id)
    structured_sheet = wait_for_structured_sheet(
        client,
        structured_sheet.id,
        args.poll_interval_seconds,
    )

    if structured_sheet.status == "failed":
        raise RuntimeError("DeepTable failed to create the structured sheet.")

    sqlite_path = output_dir / f"{workbook_path.stem}.sqlite"
    sqlite_download = client.structured_sheets.download(structured_sheet.id, format="sqlite")
    sqlite_download.write_to_file(sqlite_path)
    print(f"Downloaded {sqlite_path}")

    if "csv" in args.formats:
        csv_dir = output_dir / "csv"
        export_sqlite_tables_to_csv(sqlite_path, csv_dir)
        print(f"Exported CSV tables to {csv_dir}")


if __name__ == "__main__":
    main()