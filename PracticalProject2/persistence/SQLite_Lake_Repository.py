import sqlite3
from contextlib import closing

# Import LakeRecord using the same package path as Lake_Repository.py.

CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS lake_records (
    "Identification" INTEGER PRIMARY KEY,
    "Lake identification" TEXT,
    "Year" INTEGER,
    "Species code" TEXT,
    "Species" TEXT,
    "Percent abundance" REAL
)
"""

INSERT_RECORD = """
INSERT INTO lake_records (
    "Identification", "Lake identification", "Year",
    "Species code", "Species", "Percent abundance"
) VALUES (?, ?, ?, ?, ?, ?)
"""


class SQLiteLakeRepository:
    """Store and retrieve periphyton records in SQLite."""

    def __init__(self, database_path):
        """Remember the path to the SQLite database file."""
        self.database_path = database_path

    def _connect(self):
        """Open a connection that supports reading columns by name."""
        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row
        return connection

    @staticmethod
    def _values(record):
        """Return record values in the order expected by INSERT."""
        return (
            record.identification,
            record.lake_identification,
            record.year,
            record.species_code,
            record.species,
            record.percent_abundance,
        )

    @staticmethod
    def _to_record(row):
        """Convert a SQLite result row into a LakeRecord."""
        return LakeRecord(
            identification=row["Identification"],
            lake_identification=row["Lake identification"],
            year=row["Year"],
            species_code=row["Species code"],
            species=row["Species"],
            percent_abundance=row["Percent abundance"],
        )

    def initialize(self, load_original_records):
        """Create and populate the table on the first successful startup."""
        with closing(self._connect()) as connection, connection:
            connection.execute("BEGIN IMMEDIATE")
            table_exists = connection.execute(
                "SELECT 1 FROM sqlite_master "
                "WHERE type = 'table' AND name = ?",
                ("lake_records",),
            ).fetchone()

            if table_exists is None:
                records = load_original_records()
                connection.execute(CREATE_TABLE)
                connection.executemany(
                    INSERT_RECORD, (self._values(record) for record in records)
                )

    def get_all(self):
        """Read all database rows as LakeRecord objects."""
        with closing(self._connect()) as connection:
            rows = connection.execute(
                'SELECT * FROM lake_records ORDER BY "Identification"'
            ).fetchall()
        return [self._to_record(row) for row in rows]

    def get_one(self, identification):
        """Read one record by its dataset identification."""
        with closing(self._connect()) as connection:
            row = connection.execute(
                'SELECT * FROM lake_records WHERE "Identification" = ?',
                (identification,),
            ).fetchone()
        if row is None:
            raise ValueError(f"Record {identification} was not found.")
        return self._to_record(row)

    def add(self, record):
        """Insert a new record and report a duplicate identification."""
        try:
            with closing(self._connect()) as connection, connection:
                connection.execute(INSERT_RECORD, self._values(record))
        except sqlite3.IntegrityError as error:
            raise ValueError(
                f"Record {record.identification} already exists."
            ) from error

    def update(self, identification, replacement):
        """Update the five editable fields of one record."""
        with closing(self._connect()) as connection, connection:
            result = connection.execute(
                """
                UPDATE lake_records
                SET "Lake identification" = ?, "Year" = ?,
                    "Species code" = ?, "Species" = ?,
                    "Percent abundance" = ?
                WHERE "Identification" = ?
                """,
                self._values(replacement)[1:] + (identification,),
            )
            if result.rowcount == 0:
                raise ValueError(f"Record {identification} was not found.")

    def delete(self, identification):
        """Delete the record with the selected identification."""
        with closing(self._connect()) as connection, connection:
            result = connection.execute(
                'DELETE FROM lake_records WHERE "Identification" = ?',
                (identification,),
            )
            if result.rowcount == 0:
                raise ValueError(f"Record {identification} was not found.")

    def replace_all(self, records):
        """Replace the database contents in a single transaction."""
        with closing(self._connect()) as connection, connection:
            connection.execute("DELETE FROM lake_records")
            connection.executemany(
                INSERT_RECORD, (self._values(record) for record in records)
            )