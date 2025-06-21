# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo==0.13.15",
#     "numpy==2.3.0",
# ]
# ///
import marimo

__generated_with = "0.10.9"
app = marimo.App(width="medium")

with app.setup:
    import marimo as mo
    import numpy as np
    import xml.etree.ElementTree as et
    import os


@app.cell
def _():
    """
    Input form cell.
    """

    file = mo.notebook_location() / "public" / "book_series.xml"
    file = "public/book_series.xml"


    with open(file, "r") as xml_file:
        lines = xml_file.readlines()

    print(lines)
    output_text = "test"
    output_text_area = mo.ui.code_editor(value=lines)
    output_text_area

    return output_text_area


if __name__ == "__main__":
    app.run()

