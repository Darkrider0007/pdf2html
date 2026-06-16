def generate_base_css():

    return """
body {

    font-family: Arial, sans-serif;

    background: #f5f5f5;

    margin: 0;

    padding: 20px;
}

.container {

    background: white;

    max-width: 1100px;

    margin: auto;

    padding: 30px;

    border-radius: 10px;
}

.paragraph {

    margin-bottom: 16px;

    line-height: 1.7;
}

.image-container {

    margin: 20px 0;
}

.image-container img {

    max-width: 100%;
}

.pdf-table {

    width: 100%;

    border-collapse: collapse;

    margin: 20px 0;
}

.pdf-table td,
.pdf-table th {

    border: 1px solid #333;

    padding: 10px;
}
"""