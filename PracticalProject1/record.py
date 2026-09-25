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

'''


class lakerecord:
    """ Stores a singular data row from the lake peri file(csv) """

    def __init__(self,identification,lake_identification,year,species_code,species,percent_abundance):
        """ Creates and allows program to use constructors """
        self.identification = identification
        self.lake_identification = lake_identification
        self.year = year
        self.species_code = species_code
        self.species = species
        self.percent_abundance = percent_abundance

    def display(self):
        """Allows data to become more readable and return records fields"""
        return (f"ID: {self.identification} | "f"Lake: {self.lake_identification} | "f"Year: {self.year} | "f"Species code: {self.species_code} | "f"Species: {self.species} | "f"Percent abundance: {self.percent_abundance}" )

    