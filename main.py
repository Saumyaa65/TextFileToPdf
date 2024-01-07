import glob
from fpdf import FPDF
from pathlib import Path

filepaths=glob.glob("Files/*.txt")
pdf=FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:

    filename=Path(filepath).stem
    filename=filename.capitalize()

    pdf.add_page()
    pdf.set_font(family="Arial", style="B", size=16)
    pdf.cell(w=10, h=10, txt=filename, align="L", ln=1)

    with open(filepath, "r") as file:
        content=file.read()

    pdf.set_font(family="Times", size=14)
    pdf.multi_cell(w=0, h=8, txt=content)


pdf.output("output.pdf")