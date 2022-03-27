import os
from typing import List

from fastapi import HTTPException
from fastapi.responses import FileResponse
from lib import markdown
from models.login import Login
from models.user import User


def example_resources_service():
    return {"message": "resources"}


def resources_data():
    def get_dirs_data(initial_dir, resources):
        dir_resources = {
            "id": initial_dir.split('/')[-1],
            "resources": markdown.get_sorted_data(initial_dir),
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
