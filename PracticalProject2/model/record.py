# Author: Samatar Abdullahi
# Course: CST8002 Programming Language Research Project
# Professor: Stanley Pieda
# Due date: Oct 18, 2026
# Add full IEEE references for resources you actually consulted.

from dataclasses import dataclass
import math


@dataclass
class LakeRecord:
    """Stores a six criteria identification for one lake. """

    identification: int
    lake_identification: str
    year: int
    species_code: str
    species: str
    percent_abundance: float

    def validate(self):
        """Runs a check for invalid imput types"""
        if type(self.identification) is not int:
            raise ValueError("Identification has to be an integer.")

        if type(self.year) is not int:
            raise ValueError("Year has to be an integer.")

        text_fields = (
            self.lake_identification,
            self.species_code,
            self.species,
        )

        if any(not value.strip() for value in text_fields):
            raise ValueError("Text area cannot be empty.")

        if not math.isfinite(self.percent_abundance):
            raise ValueError("Percent abundance has to be a finite number.")

        if not 0 <= self.percent_abundance <= 100:
            raise ValueError("Percent abundance has to be between 0 and 100.")

    def display(self):
        """Returns a readable version of the record."""
        return (
            f"ID: {self.identification} | "
            f"Lake: {self.lake_identification} | "
            f"Year: {self.year} | "
            f"Species code: {self.species_code} | "
            f"Species: {self.species} | "
            f"Percent abundance: {self.percent_abundance}"
        )