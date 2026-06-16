import os
import shutil

from fastapi import (
    APIRouter,
    Request,
    UploadFile,
    File
)

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.config import UPLOAD_DIR
from app.services.pdf_service import (
    extract_pdf
)

router = APIRouter()

templates = Jinja2Templates(
    directory="app/templates"
)


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )


@router.post(
    "/upload",
    response_class=HTMLResponse
)
async def upload_pdf(
    request: Request,
    file: UploadFile = File(...)
):

    pdf_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(pdf_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    pdf_name = extract_pdf(pdf_path)

    preview_url = (
        f"/output/{pdf_name}/output.html"
    )

    return templates.TemplateResponse(
        "preview.html",
        {
            "request": request,
            "preview_url": preview_url
        }
    )