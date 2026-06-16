import os
import fitz


def extract_image_block(
    page,
    block,
    images_dir,
    image_counter
):

    html_parts = []

    try:

        bbox = block["bbox"]

        rect = fitz.Rect(bbox)

        pix = page.get_pixmap(
            matrix=fitz.Matrix(3, 3),
            clip=rect,
            alpha=False
        )

        image_filename = (
            f"image_{image_counter}.png"
        )

        image_path = os.path.join(
            images_dir,
            image_filename
        )

        pix.save(image_path)

        html_parts.append(
            f"""
            <div class="image-container">
                <img
                    src="images/{image_filename}"
                    alt="image"
                />
            </div>
            """
        )

        image_counter += 1

    except Exception as e:

        print(
            "Image extraction failed:",
            e
        )

    return (
        html_parts,
        image_counter
    )