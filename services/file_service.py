from fastapi import HTTPException
from fastapi.responses import FileResponse

fake_login_table = {"username": ["admin"], "password": ["admin_"]}


def example_file_service():
    return {"message": "file"}


def file(file_path: str):
    return FileResponse(
        file_path,
        headers={
            "Content-Type": "application/pdf",
            "Content-Disposition": "attachment; filename=CV_bruno_mariz.pdf",
        },
    )
