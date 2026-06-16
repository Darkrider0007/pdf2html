# PDF to HTML Converter

## Overview

PDF to HTML Converter is a FastAPI-based application that converts PDF documents into HTML while preserving:

* Text content
* Font styles (size, color, bold, italic)
* Images and illustrations
* Tables
* External CSS styling

The application is optimized for CPU-only environments and works particularly well with PDFs generated from:

* Microsoft Word
* Google Docs
* Office documents
* Reports and documentation PDFs

The conversion output is organized into a dedicated folder for each PDF, containing:

* Generated HTML
* Extracted images
* Generated CSS

---

## Features

### Text Extraction

* Extracts PDF text using PyMuPDF
* Preserves:

  * Font size
  * Font family
  * Font color
  * Bold styling
  * Italic styling
* Generates reusable CSS classes

### Image Extraction

* Extracts image regions from PDF pages
* Saves images into a dedicated images directory
* References images using HTML `<img>` tags

### Table Extraction

* Detects and extracts tables using pdfplumber
* Converts tables into semantic HTML tables
* Applies CSS styling automatically

### Dynamic CSS Generation

* Creates a dedicated `styles.css`
* Generates reusable CSS classes
* Avoids inline styling whenever possible

### Web Interface

* Upload PDF through browser
* Preview generated HTML
* Download generated output

---

# Technology Stack

| Component        | Technology |
| ---------------- | ---------- |
| Backend          | FastAPI    |
| PDF Processing   | PyMuPDF    |
| Table Extraction | pdfplumber |
| Templates        | Jinja2     |

---

# Project Structure

```text
pdf2html/
│
├── app/
│   │
│   ├── main.py
│   ├── config.py
│   │
│   ├── routes/
│   │   └── pdf_routes.py
│   │
│   ├── services/
│   │   ├── pdf_service.py
│   │   ├── text_extractor.py
│   │   ├── image_extractor.py
│   │   ├── table_extractor.py
│   │   ├── css_generator.py
│   │   └── html_generator.py
│   │
│   ├── utils/
│   │   └── file_utils.py
│   │
│   ├── templates/
│   │   ├── index.html
│   │   └── preview.html
│   │
│   └── static/
│       └── style.css
│
├── uploads/
├── output/
│
├── requirements.txt
├── run.py
├── README.md
└── .gitignore
```

---

# Local Setup

## 1. Clone Repository

```bash
git clone <repository-url>
cd pdf2html
```

---

## 2. Create Conda Environment

```bash
conda create -n pdf2html python=3.11 -y
```

Activate environment:

### Windows

```bash
conda activate pdf2html
```

### Linux / Mac

```bash
source activate pdf2html
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run Application

```bash
python run.py
```

Server starts at:

```text
http://127.0.0.1:8000
```

---

# Usage

## Upload PDF

1. Open browser
2. Navigate to:

```text
http://127.0.0.1:8000
```

1. Upload PDF
2. Click Convert

---

## Generated Output

Example:

```text
output/
└── SamplePDF/
    ├── output.html
    ├── styles.css
    └── images/
        ├── image_1.png
        ├── image_2.png
        └── image_3.png
```

---

# Generated HTML Structure

The application generates:

```html
<link rel="stylesheet" href="styles.css">

<div class="paragraph">
    ...
</div>

<table class="pdf-table">
    ...
</table>

<img src="images/image_1.png">
```

---
# Known Limitations

* Scanned PDFs are not currently supported.
* Complex nested tables may not render perfectly.
* Vector graphics may be exported as images.
* Multi-column layouts may require additional processing.
* Pixel-perfect PDF-to-HTML conversion is not guaranteed.

