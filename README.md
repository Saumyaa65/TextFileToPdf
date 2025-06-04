# Text File to PDF Converter

This project provides a simple Python script to **convert multiple plain text files (`.txt`) into a single PDF document**. Each text file is placed on a new page in the PDF, with its filename serving as a title for that page.

## Overview

The "Text File to PDF Converter" streamlines the process of consolidating numerous text documents into a unified, portable PDF format. This is particularly useful for archiving notes, reports, code snippets, or any text-based content into a single, easily shareable file. It automates the layout and formatting within the PDF, saving manual effort.

## Features

* **Batch Conversion:** Converts all `.txt` files found within a specified directory (`Files/`) into one cohesive PDF.
* **Page-per-File:** Each text file starts on a new page in the generated PDF.
* **Dynamic Page Title:** Uses the filename (capitalized) as a bold header for each corresponding page in the PDF, making navigation clear.
* **Customizable Fonts:** Sets distinct fonts for titles (Arial Bold) and main content (Times).
* **Automatic Layout:** Handles text wrapping for long content within the PDF page using `multi_cell`.
* **Single Output PDF:** All converted text files are combined into one `output.pdf` file.

## Technologies Used

* Python
* `fpdf` library (for PDF generation)
* `glob` module (for finding files matching a pattern)
* `pathlib` module (for object-oriented file path manipulation)

## How It Works

The script follows these steps to achieve the conversion:

1.  **File Discovery:**
    * It uses `glob.glob("Files/*.txt")` to find all files ending with `.txt` inside a directory named `Files/`.

2.  **PDF Initialization:**
    * An `FPDF` object is created with portrait orientation, units in millimeters, and A4 paper format.

3.  **Iterate and Convert:**
    * The script then loops through each identified `.txt` file:
        * It extracts the base filename (without the extension or path) and capitalizes it to use as a page title.
        * A new page is added to the PDF for each text file.
        * The filename is set as a bold, Arial font header at the top of the new page.
        * The content of the `.txt` file is read.
        * The font is changed to Times, and the entire content of the text file is added to the PDF page using `multi_cell`, which automatically handles line breaks and pagination within the cell.

4.  **Generate Output PDF:**
    * After processing all text files, the `pdf.output("output.pdf")` command generates the final PDF file named `output.pdf` in the same directory as the script.

## Data Requirements

To use this converter, you need to:

1.  Create a directory named `Files/` in the same location as the Python script.
2.  Place all the plain text files (`.txt`) that you wish to convert into this `Files/` directory.

The script will then process all `.txt` files found within this specific directory.
