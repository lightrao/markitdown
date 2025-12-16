# MarkItDown Batch Converter

This project provides a simple Python script to batch convert various file formats into Markdown using the [MarkItDown](https://github.com/microsoft/markitdown) library.

## Features

- Automatically creates an output directory (`mdFiles`) if it doesn't exist.
- Iterates through all files in the `rawFiles` directory.
- Converts each file to Markdown format.
- Saves the converted files with a `.md` extension in the `mdFiles` directory.
- Handles errors gracefully for individual files.

## Prerequisites

- Python 3.x
- `markitdown` library

## Installation

1. Clone this repository or download the script.
2. Create and activate a virtual environment (recommended):

   **Windows:**
   ```bash
   python -m venv .venv
   .venv\\Scripts\\activate
   ```

   **macOS/Linux:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the required Python package:

   ```bash
   pip install markitdown
   ```

## Usage

1. Create a folder named `rawFiles` in the same directory as the script (if it doesn't already exist).
2. Place the files you want to convert (e.g., PDF, DOCX, XLSX, PPTX) into the `rawFiles` folder.
3. Run the script:

   ```bash
   python markitdownAll.py
   ```

4. The converted Markdown files will be generated in the `mdFiles` folder.

## Directory Structure

- `markitdownAll.py`: The main conversion script.
- `rawFiles/`: Directory where you place your source files (input).
- `mdFiles/`: Directory where the converted Markdown files will be saved (output).

## Notes

- The script ignores subdirectories within `rawFiles` and only processes files.
- Output files are saved with UTF-8 encoding.
