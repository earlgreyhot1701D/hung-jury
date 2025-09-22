#!/usr/bin/env python
"""
Stub: normalize_pdf.py
Purpose: Extract values from Crystal PDF reports into Question|Value CSV.
Library used: PyMuPDF (fitz).
"""

import argparse

def extract_text(pdf_path):
    """Stub function for extracting text from PDF."""
    pass

def parse_questions_from_pdf(text):
    """Stub function for parsing questions and values using regex."""
    pass

def main():
    parser = argparse.ArgumentParser(description="Normalize Crystal PDF into Qid|Value CSV")
    parser.add_argument("--pdf", required=True, help="Crystal report PDF")
    parser.add_argument("--out", required=True, help="Output CSV file")
    args = parser.parse_args()
    # Parsing workflow would be implemented here

if __name__ == "__main__":
    main()
