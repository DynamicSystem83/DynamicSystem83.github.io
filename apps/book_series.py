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
    import tempfile


@app.cell
def _():
    """
    Input form cell.
    """

    bucket = "831273346538-book-series"

    #access_key_id = os.environ["BOOK_SERIES_ACCESS_KEY_ID"]

    output_text = "test"
    output_text_area = mo.ui.code_editor(value=output_text)
    output_text_area

    return output_text_area


if __name__ == "__main__":
    app.run()

