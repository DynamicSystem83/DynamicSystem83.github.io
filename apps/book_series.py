# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo==0.13.15",
#     "botocore",
#     "awscli",
#     "aiobotocore",
#     "boto3",
# ]
# ///
import marimo

__generated_with = "0.10.9"
app = marimo.App(width="medium")

with app.setup:
    import marimo as mo
    import xml.etree.ElementTree as et
    import os
    import tempfile
    import boto3


@app.cell
def _():
    """
    Input form cell.
    """

    bucket = "831273346538-book-series"

    #access_key_id = os.environ["BOOK_SERIES_ACCESS_KEY_ID"]
    #access_key_id = "AKIA4DC6AUXVL7SLYA5L"
    #access_secret_key = "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"

    #s3_client = boto3.client("s3", aws_access_key_id=access_key_id, aws_secret_access_key=access_secret_key)

    lines = []
    #with tempfile.TemporaryFile(mode="wb") as file_handler:
    #    s3_client.download_fileobj("831273346538-book-series", "test_file.txt", file_handler)
    #    lines = file_handler.readlines()

    if len(lines) > 0:
        output_text = "\n".join(lines)
    else:
        output_text = "test"

    output_text_area = mo.ui.code_editor(value=output_text)
    output_text_area

    return output_text_area


if __name__ == "__main__":
    app.run()

