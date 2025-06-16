# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo==0.13.15",
#     "altair==4.2.0",
#     "pandas==2.3.0",
#     "numpy==2.3.0"
# ]
# ///
import marimo

__generated_with = "0.10.9"
app = marimo.App(width="medium")

with app.setup:
    import numpy as np
    import marimo as mo


@app.cell
def _():
    mo.md(
        """
        # Interactive Data Visualization

        This notebook demonstrates a simple interactive web app.
        """
    )
    return


@app.cell
def _():
    input_text_area = mo.ui.text_area(placeholder="type some text to be encoded ...")
    input_text_area

    encode_button = mo.ui.run_button("Encode")
    encode_button

    return input_text_area


@app.cell
def _(input_text_area, encode_button):
    mo.stop(not encode_button.value)

    encoded_text = encode(input_text_area.value)
    mo.md(encoded_text)
    return


@app.function
def encode(text):
    text = text + "_encoded"
    return text


if __name__ == "__main__":
    app.run()
