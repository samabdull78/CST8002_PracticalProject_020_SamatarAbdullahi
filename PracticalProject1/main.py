# Author: Samatar Abdullahi

import csv
from itertools import islice

from record import lakerecord


CSV_FILE = "vuntut_np_lake_periphyton_community_structure_2012_2016_data.csv"
NUMBER_OF_RECORDS = 5
STUDENT_NAME = "Samatar Abdullahi"


def load_records(filename, limit):
    """Read the first few data rows into a list of LakeRecord objects."""
    records = []

    with open(filename, "r", encoding="cp1252", newline="") as file:
        reader = csv.DictReader(file)

        next(reader, None)

        for row in islice(reader, limit):
            record = lakerecord(identification=int(row["Identification"]),lake_identification=row["Lake identification"],year=int(row["Year"]),species_code=row["Species code"],species=row["Species"],percent_abundance=float(row["Percent abundance"]),
            )
            records.append(record)

    return records


def main():
    print(f"Student: {STUDENT_NAME}")
    print("=" * 70)

    try:
        records = load_records(CSV_FILE, NUMBER_OF_RECORDS)
    except FileNotFoundError:
        print(f"Error: Could not find '{CSV_FILE}'.")
        return
    except OSError as error:
        print(f"Error reading the dataset: {error}")
        return

    for record in records:
        print(record.display())


if __name__ == "__main__":
    main()