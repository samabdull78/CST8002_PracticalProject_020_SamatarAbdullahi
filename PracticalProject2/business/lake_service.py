# Author: Samatar Abdullahi
# Course: CST8002 Programming Language Research Project
# Professor: Stanley Pieda
# Due date: Oct 18, 2026
# Add full IEEE references for resources you actually consulted.

class LakeService:
    """Manage the in-memory list of lake records."""

    def __init__(self, repository, dataset_path, output_directory):
        """Store dependencies and initialize an empty record list."""
        self.repository = repository
        self.dataset_path = dataset_path
        self.output_directory = output_directory
        self.records = []

    def reload(self):
        """Replace current records after successfully reading the dataset."""
        loaded_records = self.repository.load_records(
            self.dataset_path, limit=100
        )

        identifiers = [
            record.identification for record in loaded_records
        ]

        if len(identifiers) != len(set(identifiers)):
            raise ValueError("The dataset contains duplicate identifications.")

        self.records = loaded_records
        return len(self.records)

    def get_all(self):
        """Return a copy of the current record list."""
        return self.records.copy()

    def get_one(self, identification):
        """Return the matching record or raise an error."""
        for record in self.records:
            if record.identification == identification:
                return record

        raise ValueError(
            f"No record has identification {identification}."
        )

    def add(self, record):
        """Validate and append a record with a unique identification."""
        record.validate()

        if any(
            existing.identification == record.identification
            for existing in self.records
        ):
            raise ValueError("That identification already exists.")

        self.records.append(record)

    def update(self, identification, replacement):
        """Replace a selected record while keeping its identification."""
        replacement.validate()

        if replacement.identification != identification:
            raise ValueError(
                "Identification cannot change during editing."
            )

        for index, record in enumerate(self.records):
            if record.identification == identification:
                self.records[index] = replacement
                return

        raise ValueError(
            f"No record has identification {identification}."
        )

    def delete(self, identification):
        """Remove and return a selected record."""
        record = self.get_one(identification)
        self.records.remove(record)
        return record

    def save(self):
        """Ask the repository to persist the current record list."""
        return self.repository.save_records(
            self.records, self.output_directory
        )