import os
import fitz
import pdfplumber

from app.config import OUTPUT_DIR

from app.utils.file_utils import (
    create_output_folders
)

from app.services.text_extractor import (
    extract_text_blocks
)

from app.services.image_extractor import (
    extract_image_block
)

from app.services.table_extractor import (
    extract_tables
)

from app.services.css_generator import (
    generate_base_css
)

from app.services.html_generator import (
    generate_html
)


def extract_pdf(pdf_path: str):

    pdf_name = os.path.splitext(
        os.path.basename(pdf_path)
    )[0]

    pdf_output_dir, images_dir = (
        create_output_folders(
            OUTPUT_DIR,
            pdf_name
        )
    )

    doc = fitz.open(pdf_path)

    html_parts = []

    css_classes = {}

    css_content = []

    image_counter = 1

    style_counter = 1

    with pdfplumber.open(pdf_path) as plumber_pdf:

        for page_index in range(len(doc)):

            page = doc[page_index]

            plumber_page = (
                plumber_pdf.pages[page_index]
            )

            # =========================
            # TABLES
            # =========================

            (
                table_parts,
                table_regions
            ) = extract_tables(
                plumber_page
            )

            html_parts.extend(
                table_parts
            )

            # =========================
            # BLOCKS
            # =========================

            blocks = page.get_text(
                "dict"
            )["blocks"]

            for block in blocks:

                block_bbox = block.get(
                    "bbox"
                )

                inside_table = False

                if block_bbox:

                    bx0, by0, bx1, by1 = (
                        block_bbox
                    )

                    for tbbox in table_regions:

                        tx0, ty0, tx1, ty1 = (
                            tbbox
                        )

                        if (
                            bx0 >= tx0
                            and bx1 <= tx1
                            and by0 >= ty0
                            and by1 <= ty1
                        ):

                            inside_table = True
                            break

                if inside_table:
                    continue

                # =========================
                # TEXT
                # =========================

                if block["type"] == 0:

                    (
                        text_html,
                        style_counter
                    ) = extract_text_blocks(
                        block,
                        css_classes,
                        css_content,
                        style_counter
                    )

                    html_parts.extend(
                        text_html
                    )

                # =========================
                # IMAGE
                # =========================

                elif block["type"] == 1:

                    (
                        image_html,
                        image_counter
                    ) = extract_image_block(
                        page,
                        block,
                        images_dir,
                        image_counter
                    )

                    html_parts.extend(
                        image_html
                    )

    # =========================
    # CSS
    # =========================

    base_css = generate_base_css()

    final_css = (
        base_css
        + "\n".join(css_content)
    )

    css_path = os.path.join(
        pdf_output_dir,
        "styles.css"
    )

    with open(
        css_path,
        "w",
        encoding="utf-8"
    ) as css_file:

        css_file.write(final_css)

    # =========================
    # HTML
    # =========================

    combined_html = ""

    for item in html_parts:

        if isinstance(item, dict):

            combined_html += (
                item["html"]
            )

        else:

            combined_html += item

    final_html = generate_html(
        pdf_name,
        combined_html
    )

    html_path = os.path.join(
        pdf_output_dir,
        "output.html"
    )

    with open(
        html_path,
        "w",
        encoding="utf-8"
    ) as html_file:

        html_file.write(final_html)

    return pdf_name