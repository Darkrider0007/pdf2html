def extract_tables(plumber_page):

    table_parts = []

    table_regions = []

    tables = plumber_page.find_tables()

    for table_obj in tables:

        table_bbox = table_obj.bbox

        table_regions.append(
            table_bbox
        )

        extracted_table = (
            table_obj.extract()
        )

        table_html = (
            '<table class="pdf-table">'
        )

        for row in extracted_table:

            table_html += "<tr>"

            if row:

                for cell in row:

                    cell_text = (
                        cell if cell else ""
                    )

                    table_html += (
                        f"<td>{cell_text}</td>"
                    )

            table_html += "</tr>"

        table_html += "</table>"

        table_parts.append(
            {
                "type": "table",
                "bbox": table_bbox,
                "html": table_html
            }
        )

    return (
        table_parts,
        table_regions
    )