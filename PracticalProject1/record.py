#Author: Samatar Abdullahi
# Class: CST8002
class lakerecord:
    """ Stores a singular data row from the lake peri file(csv) """

    def __init__(self,identification,lake_identification,year,species_code,species,percent_abundance):
        self.identification = identification
        self.lake_identification = lake_identification
        self.year = year
        self.species_code = species_code
        self.species = species
        self.percent_abundance = percent_abundance

    def display(self):
        """Allows data to become more readable and return records fields"""
        return (f"ID: {self.identification} | "f"Lake: {self.lake_identification} | "f"Year: {self.year} | "f"Species code: {self.species_code} | "f"Species: {self.species} | "f"Percent abundance: {self.percent_abundance}" )

    