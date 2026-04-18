# SafeScript

A Python-based OCR system that extracts and processes medical data from documents using image processing and database integration.

---

## Overview

SafeScript is designed to automate the extraction of information from medical documents using Optical Character Recognition (OCR) and convert unstructured data into structured formats.

The project demonstrates:

* OCR pipeline implementation
* Data processing and extraction
* Backend system design
* Integration of multiple libraries

---

## Features

* Extracts text from images and documents using OCR
* Identifies prescriptions and diseases from extracted data
* Processes and structures information
* Integrates with a database for storage and lookup
* Runs as a Flask-based application

---

## Tech Stack

* Python
* Flask
* Tesseract OCR (via pytesseract)
* OpenCV
* Pandas
* pdf2image

---

## Project Structure

```bash id="q9n2fs"
SafeScript/
│── app.py                 # Main Flask application (entry point)
│── ocr_reader.py          # Handles OCR processing and text extraction
│── loaddatabase.py        # Loads and queries the medical dataset
│── createdatabase.py      # Script to create/initialize the database
│── medical_database.xlsx  # Dataset containing medical information
│── requirements.txt       # List of Python dependencies
│── uploaded.png           # Sample input file (optional)
│── report.pdf             # Generated output (optional)
```

---

## Installation

Clone the repository:

```bash id="k7r3ma"
git clone https://github.com/Anik03-cmd/SafeScript.git
cd SafeScript
```

Install dependencies:

```bash id="r4b8jt"
pip install -r requirements.txt
```

Install system dependencies (Linux/Codespaces):

```bash id="w1x9lz"
sudo apt-get update
sudo apt-get install -y tesseract-ocr poppler-utils libgl1
```

---

## Running the Application

```bash id="d2v6kp"
python app.py
```

Open in browser:

```id="z8y4hn"
http://127.0.0.1:5000
```

---

## Workflow

1. Upload an image or document
2. OCR extracts text
3. Data is processed to identify relevant information
4. Results are structured and returned

---

## Future Improvements

* Improved frontend interface
* Additional data extraction capabilities
* Deployment support
* Performance optimization

---

## Author

Anik Biswas
https://github.com/Anik03-cmd
