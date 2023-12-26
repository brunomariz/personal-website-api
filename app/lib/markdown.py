import datetime as dt
import os
import pathlib
from typing import List, Literal

import markdown


def get_datetime(datetime_str):
    return dt.datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")


def get_sorted_data(
    path: str, key: Literal["created", "modified"] = "created"
) -> List[dict]:
    """Gets the metadata from the markdown files in the paths directory

    Parameters
    ----------
    path : str
        Directory containing markdown files
    key : Literal[&quot;created&quot;, &quot;modified&quot;], optional
        Metadata key by which to sort the data, by default "created"

    Returns
    -------
    List[dict]
        Sorted list of dictionaries containing the ids, metadata and entire data of files in path dir
    """

    # Get files in directory
    files = os.listdir(path)
    files = list(filter(lambda file: os.path.isfile(f"{path}/{file}"), files))
    data = []
    meta_md = markdown.Markdown(extensions=["meta"])
    for file in files:
        file_data = pathlib.Path(f"{path}/{file}").read_text(encoding="utf-8")
        meta_md.convert(file_data)
        data.append(
            {"id": file.replace(".md", ""), "data": file_data, "metadata": meta_md.Meta}
        )

    # Get sorted data
    sorted_data = sorted(
        data, key=lambda item: get_datetime(item["metadata"][key][0]), reverse=True
    )

    return sorted_data

