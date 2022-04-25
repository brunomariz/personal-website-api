import os
from typing import List

from fastapi import HTTPException
from fastapi.responses import FileResponse
from lib import markdown


def example_resources_service():
    return {"message": "resources"}


def resources_data():
    def get_dirs_data(initial_dir, resources):
        dir_resources = {
            "id": initial_dir.split("/")[-1],
            "resources": reversed(markdown.get_sorted_data(initial_dir)),
            "children": [],
        }

        inner_dirs = list(
            filter(
                lambda dir: os.path.isdir(f"{initial_dir}/{dir}"),
                os.listdir(initial_dir),
            )
        )

        for dir in inner_dirs:
            dir_resources["children"].append(
                get_dirs_data(f"{initial_dir}/{dir}", resources)
            )

        return dir_resources

    data = get_dirs_data("resources", {})
    return data


def resources_list_of_paths(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # fullPath = f"resources/{entry}"
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + resources_list_of_paths(fullPath)
        else:
            # Append filename up to -3rd position to remove .md from string
            allFiles.append(f"/resources/{entry[:-3]}")

    return allFiles
