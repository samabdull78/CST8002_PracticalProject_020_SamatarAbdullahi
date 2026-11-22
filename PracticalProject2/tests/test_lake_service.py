# Author: Samatar Abdullahi
# Course: CST8002 Programming Language Research Project
# Professor: Stanley Pieda
# Due date: Oct 18, 2026
# [6] Python Software Foundation, "unittest — Unit testing framework,"
#     Python documentation. [Online]. Available:
#     https://docs.python.org/3/library/unittest.html
#     [Accessed: Oct. 18, 2026].

import unittest
from pathlib import Path

from business.lake_service import LakeService
from model.record import LakeRecord


class TestLakeService(unittest.TestCase):
    """Test adding a lake record to the business layer."""

    def test_add_stores_record_fields(self):
        """Verify that add preserves all six record fields."""
        service = LakeService(
            repository=None,
            dataset_path=Path("unused.csv"),
            output_directory=Path("unused_exports"),
        )

        record = LakeRecord(
            identification=99999,
            lake_identification="TEST01",
            year=2026,
            species_code="TEST",
            species="Test species",
            percent_abundance=25.5,
        )

        service.add(record)
        stored_records = service.get_all()

        self.assertEqual(len(stored_records), 1)

        stored = stored_records[0]
        actual = (
            stored.identification,
            stored.lake_identification,
            stored.year,
            stored.species_code,
            stored.species,
            stored.percent_abundance,
        )

        expected = (
            99999,
            "TEST01",
            2026,
            "TEST",
            "Test species",
            25.5,
        )

        self.assertEqual(actual, expected)

    def test_sort_uses_numeric_abundance_and_preserves_insertion_order(self):
        """Checks the number position and then makes the program run in its original sequence"""
        service = LakeService(None, Path("unused.csv"), Path("unused_exports"))
        for identification, abundance in enumerate((10.0, 2.0, 2.0, 0.0), 1):
            service.add(LakeRecord(identification, "TEST", 2026, "T", "Test", abundance))

        ordered = service.get_sorted_by_percent_abundance()

        self.assertEqual([record.identification for record in ordered], [4, 2, 3, 1])
        self.assertEqual(
            [record.identification for record in service.get_all()], [1, 2, 3, 4]
        )

if __name__ == "__main__":
    unittest.main()