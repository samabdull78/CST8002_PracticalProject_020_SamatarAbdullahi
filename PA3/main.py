# Author: Samatar Ali Abdullahi
# Reference:
# [3]
# Cody Engel, “How To Write Unit Tests (The Right Way).” YouTube, Feb. 22, 2021. 
# Accessed: Oct. 10, 2026. [Video]. Available: https://www.youtube.com/watch?v=aId-WLZnvkw
#Professor: Stanley Pieda

"""Run the example test suite and display the example author."""

import unittest

from tests.Square_Test import TestSquareArea


def main() -> None:
    """Run both demonstration tests and print the author before exiting."""
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(
        TestSquareArea
    )
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

    print("\nAuthor: Samatar Ali Abdullahi", flush=True)


if __name__ == "__main__":
    main()