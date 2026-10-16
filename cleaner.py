import csv
import argparse
from pathlib import Path


def clean_csv(input_file, output_file):
    source = Path(input_file)
    destination = Path(output_file)

    if not source.is_file():
        raise FileNotFoundError(f"Input file not found: {source}")

    if source.resolve() == destination.resolve():
        raise ValueError("Input and output files must be different.")

    with source.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        if not reader.fieldnames:
            raise ValueError("CSV file is empty or missing headers.")

        headers = [name.strip() for name in reader.fieldnames]

        if any(not header for header in headers):
            raise ValueError("CSV contains an empty column name.")

        if len(headers) != len(set(headers)):
            raise ValueError("CSV contains duplicate column names.")

        rows = []

        for row in reader:
            if None in row:
                raise ValueError("CSV row contains more values than headers.")

            cleaned = {
                key.strip(): (value or "").strip()
                for key, value in row.items()
            }

            if any(cleaned.values()):
                rows.append(cleaned)

    destination.parent.mkdir(parents=True, exist_ok=True)

    with destination.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Success: {destination}")
    print(f"Rows saved: {len(rows)}")


def main():
    parser = argparse.ArgumentParser(
        description="Clean whitespace and blank rows in a CSV file."
    )
    parser.add_argument("input", help="Input CSV file")
    parser.add_argument("output", help="Output CSV file")
    args = parser.parse_args()

    try:
        clean_csv(args.input, args.output)
    except (OSError, UnicodeError, csv.Error, ValueError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()