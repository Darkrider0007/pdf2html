import os


def create_output_folders(output_dir, pdf_name):

    pdf_output_dir = os.path.join(
        output_dir,
        pdf_name
    )

    images_dir = os.path.join(
        pdf_output_dir,
        "images"
    )

    os.makedirs(images_dir, exist_ok=True)

    return pdf_output_dir, images_dir