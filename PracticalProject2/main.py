# Author: Samatar Abdullahi
# Course: CST8002 Programming Language Research Project
# Professor: Stanley Pieda
# Due date: Oct 18, 2026
# Add full IEEE references for resources you actually consulted.

from pathlib import Path

from business.lake_service import LakeService
from persistence.lake_repository import LakeRepository
from presentation.console_view import ConsoleView


BASE_DIRECTORY = Path(__file__).resolve().parent

DATASET_PATH = (
    BASE_DIRECTORY
    / "vuntut_np_lake_periphyton_community_structure_2012_2016_data.csv"
)

OUTPUT_DIRECTORY = BASE_DIRECTORY / "exports"


def main():
    """Creates application components and starts the console."""
    repository = LakeRepository()

    service = LakeService(
        repository,
        DATASET_PATH,
        OUTPUT_DIRECTORY,
    )

    view = ConsoleView(service)
    view.run()


if __name__ == "__main__":
    main()