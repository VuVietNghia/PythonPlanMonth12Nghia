import pyfiglet
from typing import Optional

def figlet() -> None:
    font_style: str = input("Enter your font style (or press Enter for default): ").strip()
    text_input: str = input("Input: ")

    if font_style == "":
        print(pyfiglet.figlet_format(text_input))
    else:
        available_fonts = pyfiglet.FigletFont.getFonts()
        if font_style not in available_fonts:
            print(f"Error: Font '{font_style}' not found.")
            print(f"Available fonts: {', '.join(available_fonts[:10])}... (and more)")
            return

        print(pyfiglet.figlet_format(text_input, font=font_style))

if __name__ == "__main__":
    figlet()