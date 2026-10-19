# Author: Samatar Abdullahi
# Course: CST8002 Programming Language Research Project
# Professor: Stanley Pieda
# Due date: Oct 18, 2026
# [3] Python Software Foundation, "uuid — UUID objects according to RFC 9562,"
#     Python documentation. [Online]. Available:
#     https://docs.python.org/3/library/uuid.html
#     [Accessed: Oct. 18, 2026].
import csv
from pathlib import Path
from uuid import uuid4

from model.record import LakeRecord


FIELDNAMES = (
    "Identification",
    "Lake identification",
    "Year",
    "Species code",
    "Species",
    "Percent abundance",
)


class LakeRepository:
    """Read lake records and save them as CSV files."""

    def load_records(self, filename, limit=100):
        """Reads until the limit records from the original bilingual dataset."""
        records = []

        with open(filename, "r", encoding="cp1252", newline="") as file:
            reader = csv.DictReader(file)

            if reader.fieldnames != list(FIELDNAMES):
                raise ValueError("The dataset column names are incorrect.")

            next(reader, None)

            for row in reader:
                if len(records) >= limit:
                    break

                try:
                    record = LakeRecord(
                        identification=int(row["Identification"]),
                        lake_identification=row["Lake identification"],
                        year=int(row["Year"]),
                        species_code=row["Species code"],
                        species=row["Species"],
                        percent_abundance=float(row["Percent abundance"]),
                    )
                    record.validate()
                except (ValueError, TypeError, AttributeError) as error:
                    raise ValueError(
                        f"Invalid dataset row at CSV line "
                        f"{reader.line_num}: {error}"
                    ) from error

                records.append(record)

        return records

    def save_records(self, records, output_directory):
        """Save all current records to a new UUID-named UTF-8 CSV."""
        directory = Path(output_directory)
        directory.mkdir(parents=True, exist_ok=True)

        output_path = directory / f"{uuid4()}.csv"

        with open(
            output_path, "x", encoding="utf-8", newline=""
        ) as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()

            for record in records:
                writer.writerow({
                    "Identification": record.identification,
                    "Lake identification": record.lake_identification,
                    "Year": record.year,
                    "Species code": record.species_code,
                    "Species": record.species,
                    "Percent abundance": record.percent_abundance,
                })

        return output_path