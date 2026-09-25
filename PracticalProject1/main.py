'''
Author: Samatar Abdullahi
Professor: Stanley Pieda
Class: CST8002
Due Date: Sep 25 2026
IEEE References: 
[1]
J. Brown, “Git Branching and Merging: A Step-By-Step Guide,” Varonis.com, May 17, 2021. https://www.varonis.com/blog/git-branching-and-merging (accessed Sept. 25, 2026).


[2]
C. Schafer, “Python Tutorial: File Objects - Reading and Writing to Files,” YouTube. Apr. 29, 2016. Accessed: Sept. 25, 2026. [YouTube Video]. Available: https://www.youtube.com/watch?v=Uh2ebFW8OYM

[3]
GeeksforGeeks, “Python Docstrings,” GeeksforGeeks, June 2017. https://www.geeksforgeeks.org/python/python-docstrings/ (accessed Sept. 25, 2026).

[4]
GeeksforGeeks, “Reading CSV files in Python,” GeeksforGeeks, Dec. 16, 2019. https://www.geeksforgeeks.org/pandas/reading-csv-files-in-python/ (accessed Sept. 25, 2026).
'''

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