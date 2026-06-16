def generate_html(
    pdf_name,
    combined_html
):

    return f"""
<!DOCTYPE html>

<html>

<head>

    <meta charset="UTF-8">

    <title>{pdf_name}</title>

    <link
        rel="stylesheet"
        href="styles.css"
    >

</head>

<body>

    <div class="container">

        {combined_html}

    </div>

</body>

</html>
"""