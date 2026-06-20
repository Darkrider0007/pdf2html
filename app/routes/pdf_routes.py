import os
import shutil

from fastapi import (
    APIRouter,
    Request,
    UploadFile,
    File,
    HTTPException
)

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse

from app.config import UPLOAD_DIR
from app.services.pdf_service import (
    extract_pdf
)

from app.config import (
    UPLOAD_DIR,
    OUTPUT_DIR
)

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


@router.post("/api/pdf/convert")
async def convert_pdf(
    file: UploadFile = File(...)
):

    if not file.filename.lower().endswith(".pdf"):

        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    pdf_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(pdf_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    # Convert PDF
    pdf_name = extract_pdf(
        pdf_path
    )

    html_file_path = os.path.join(
        OUTPUT_DIR,
        pdf_name,
        "output.html"
    )

    if not os.path.exists(
        html_file_path
    ):

        raise HTTPException(
            status_code=500,
            detail="Generated HTML file not found."
        )

    with open(
        html_file_path,
        "r",
        encoding="utf-8"
    ) as html_file:

        html_content = html_file.read()

    return JSONResponse(
        {
            "success": True,
            "pdf_name": pdf_name,
            "html": html_content
        }
    )