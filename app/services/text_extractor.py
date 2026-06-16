def extract_text_blocks(
    block,
    css_classes,
    css_content,
    style_counter
):

    html_parts = []

    paragraph_html = ""

    for line in block["lines"]:

        line_html = ""

        for span in line["spans"]:

            text = span["text"].strip()

            if not text:
                continue

            font_size = round(
                span["size"]
            )

            font_name = (
                span["font"]
                .replace(" ", "_")
            )

            flags = span["flags"]

            color = span["color"]

            is_bold = bool(flags & 16)

            is_italic = bool(flags & 2)

            hex_color = (
                f"#{color:06x}"
            )

            style_key = (
                font_size,
                font_name,
                is_bold,
                is_italic,
                hex_color
            )

            if style_key not in css_classes:

                class_name = (
                    f"style_{style_counter}"
                )

                css_classes[
                    style_key
                ] = class_name

                css_rule = f"""
.{class_name} {{

    font-size: {font_size}px;

    font-family: '{font_name}';

    color: {hex_color};
"""

                if is_bold:

                    css_rule += """
    font-weight: bold;
"""

                if is_italic:

                    css_rule += """
    font-style: italic;
"""

                css_rule += """
}
"""

                css_content.append(
                    css_rule
                )

                style_counter += 1

            else:

                class_name = (
                    css_classes[
                        style_key
                    ]
                )

            line_html += (
                f'<span class="{class_name}">'
                f'{text}'
                f'</span> '
            )

        if line_html:

            paragraph_html += (
                f"<div>{line_html}</div>"
            )

    if paragraph_html:

        html_parts.append(
            f"""
            <div class="paragraph">
                {paragraph_html}
            </div>
            """
        )

    return (
        html_parts,
        style_counter
    )