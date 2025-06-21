# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo==0.13.15",
#     "numpy==2.3.0",
#     "mendeleev==1.1.0"
# ]
# ///
import marimo

__generated_with = "0.10.9"
app = marimo.App(width="medium")

with app.setup:
    import marimo as mo
    import numpy as np
    from mendeleev import element

    # Create a default random number generator
    rng = np.random.default_rng()


@app.cell
def _():
    """
    Input form cell.
    """
    intro = mo.md(
        """
        # Periodic Table Encoding

        This notebook allows a user to encode/decode using the periodic table.

        Simple: Only alpha and spaces are encoded
        Complex: Alpha, numberic, and " .,!" are encoded
        """
    )

    direction_options = ["Encode", "Decode"]
    type_options = ["Simple", "Complex"]

    direction = mo.ui.radio(options=direction_options, value=direction_options[0], inline=True)
    type = mo.ui.radio(options=type_options, value=type_options[0], inline=True)
    input_text_area = mo.ui.text_area(value="", placeholder="type some text to be encoded ...")

    form = mo.md("""{direction}

        {type}

        {input_text_area}"""
    )

    input = form.batch(direction=direction, type=type, input_text_area=input_text_area).form()
    intro, input

    return intro, input


@app.cell
def _(input):
    """
    Output cell using code UI for copy functionality.
    """
    output_text = ""

    if (input is not None) and (input.value is not None):
        if (input.value["direction"] == "Encode") and (input.value["type"] == "Simple"):
            output_text = encode_simple(input.value["input_text_area"])
        elif  (input.value["direction"] == "Decode") and (input.value["type"] == "Simple"):
            output_text = decode_simple(input.value["input_text_area"])
        elif (input.value["direction"] == "Encode") and (input.value["type"] == "Complex"):
            output_text = encode_complex(input.value["input_text_area"])
        elif  (input.value["direction"] == "Decode") and (input.value["type"] == "Complex"):
            output_text = decode_complex(input.value["input_text_area"])

    output_text_area = mo.ui.code_editor(value=output_text)
    output_text_area

    return output_text_area


@app.function
def atomic_number_to_symbol(number):
    """
    Convert an atomic number to an element symbol. Doubles single character symbols.
    """
    number = int(number)
    symbol = ""
    if (number > 0) and (number < 119):
        symbol = element(number).symbol
    else:
        raise Exception("number out of range")
    
    if len(symbol) == 1:
        symbol = symbol + symbol
    return symbol.upper()


@app.function
def symbol_to_atomic_number(symbol):
    """
    Convert an element symbol to an atomic number. Reduces double symbols into a single symbol.
    """
    if symbol[0] == symbol[1]:
        symbol = symbol[0]
    else:
        symbol = symbol.title()
    number = element(symbol).atomic_number
    return number


@app.function
def encode_simple(text):
    shift_amount = rng.integers(low=1, high=10)
    shift_symbol = element(int(shift_amount)).symbol
    shift_symbol = shift_symbol.upper()

    encoded_text = ""
    encoded_text += shift_symbol

    text = text.lower()
    for character in text:
        if character.isalpha():
            number = ord(character) - ord("a") + 1 # a = 0 + 1, z = 25 + 1
            number = number + shift_amount + rng.integers(low=0, high=4)*27
            encoded_text += atomic_number_to_symbol(number)
        elif character == " ":
            number = 26 + 1 # space = 26 + 1
            number = number + shift_amount + rng.integers(low=0, high=4)*27
            encoded_text += atomic_number_to_symbol(number)
        else:
            encoded_text += character
    return encoded_text


@app.function
def decode_simple(text):
    first_sentence = text.split(".")[0]
    if len(first_sentence)%2 == 0:
        shift_symbol = "".join(first_sentence[0:2])
        text = text[2:]
    else:
        shift_symbol = "".join(first_sentence[0:1])
        text = text[1:]
    shift_symbol = shift_symbol.title()
    shift_amount = element(shift_symbol).atomic_number

    decoded_text = ""
    i = 0
    while i < len(text):
        if text[i] == ".":
            decoded_text += text[i]
            i += 1
        else:
            symbol = "".join(text[i:i+2])
            i += 2
            number = symbol_to_atomic_number(symbol)
            number = number - shift_amount - 1
            number = number%27
            if number == 36:
                decoded_text += " "
            else:
                decoded_text += chr(number + ord("a"))

    return decoded_text


@app.function
def encode_complex(text):
    shift_amount = rng.integers(low=1, high=10)
    shift_symbol = element(int(shift_amount)).symbol
    shift_symbol = shift_symbol.upper()

    encoded_text = ""
    encoded_text += shift_symbol

    text = text.lower()
    for character in text:
        if character.isalpha():
            number = ord(character) - ord("a") + 1 # a = 0 + 1, z = 25 + 1
            number = number + shift_amount + rng.integers(low=0, high=2)*40
            encoded_text += atomic_number_to_symbol(number)
        elif character.isnumeric():
            number = ord(character) - ord("0") + 26 + 1 # 0 = 0 + 26 + 1, 9 = 26 + 9 + 1
            number = number + shift_amount + rng.integers(low=0, high=2)*40
            encoded_text += atomic_number_to_symbol(number)
        elif character == " ":
            number = 26 + 10 + 1 # space = 26 + 10 + 1
            number = number + shift_amount + rng.integers(low=0, high=2)*40
            encoded_text += atomic_number_to_symbol(number)
        elif character == ".":
            number = 26 + 10 + 1 + 1 # space = 26 + 10 + 1 + 1
            number = number + shift_amount + rng.integers(low=0, high=2)*40
            encoded_text += atomic_number_to_symbol(number)
        elif character == ",":
            number = 26 + 10 + 1 + 2 # space = 26 + 10 + 1 + 2
            number = number + shift_amount + rng.integers(low=0, high=2)*40
            encoded_text += atomic_number_to_symbol(number)
        elif character == "!":
            number = 26 + 10 + 1 + 3 # space = 26 + 10 + 1 + 3
            number = number + shift_amount + rng.integers(low=0, high=2)*40
            encoded_text += atomic_number_to_symbol(number)
        else:
            encoded_text += character
    return encoded_text


@app.function
def decode_complex(text):
    first_sentence = text.split(".")[0]
    if len(first_sentence)%2 == 0:
        shift_symbol = "".join(first_sentence[0:2])
        text = text[2:]
    else:
        shift_symbol = "".join(first_sentence[0:1])
        text = text[1:]
    shift_symbol = shift_symbol.title()
    shift_amount = element(shift_symbol).atomic_number

    decoded_text = ""
    i = 0
    while i < len(text):
        symbol = "".join(text[i:i+2])
        i += 2
        print(symbol)
        number = symbol_to_atomic_number(symbol)
        number = number - shift_amount - 1
        number = number%40
        if number == 36:
            decoded_text += " "
        elif number == 37:
            decoded_text += "."
        elif number == 38:
            decoded_text += ","
        elif number == 39:
            decoded_text += "!"
        elif (number >= 25) and (number <= 35):
            decoded_text += chr(number - 26  + ord("0"))
        else:
            decoded_text += chr(number + ord("a"))

    return decoded_text


if __name__ == "__main__":
    app.run()

