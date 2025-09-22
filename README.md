# Hung Jury

** When automation can’t reach a verdict. **

** Automation isn’t always possible, but exploring the limits creates clarity. **

This repository is a scrubbed proof-of-concept showing my attempt to automate the **Judical Council of California's Annual Jury Data Report (JDR)** process.

The project explored extracting data from Crystal Reports PDFs, cleaning it, and validating it against Judicial Council (JCC) business rules.

## 🚦 What I Tried
1. **PDF Parsing**
   - Built a PyMuPDF parser to extract values directly.
   - Result: Failed. Crystal’s PDF output scrambled values (e.g., Q9 sub-questions shifted).

2. **Mapping Extraction**
   - Created a JSON-based mapping to align questions with values.
   - Result: Worked, but only because values were corrected manually — not sustainable.

3. **Lean QC Engine**
   - Built `lean_jdr.py` to apply all 12 JCC Manual rules.
   - Result: Confirmed my colleague’s Excel workbook was already correct, but added an independent validation tool.

## 🧾 What I Learned
- **Source data quality is the real constraint.** Automation broke not because of Python, but because Crystal’s output is unreliable.
- **Excel remains the gold standard.** It already validates correctly against the JCC Manual.
- **Knowing when to stop is as important as starting.** I began this project Friday afternoon and closed it by Monday after testing and building.

## 📂 Repo Contents
- `scripts/` → Python prototypes (scrubbed).
- `sample_data/` → Fake but realistic JSON, CSV, and QC logs.
- `README.md` → Story of the project.
- `LAUNCH_LOG.md` → Journal of what was tried, why it failed, and the decision to stop.

## ⚠️ Disclaimer
This repo uses **synthetic sample data only.**
No proprietary or court data is included.


## 🔧 About the Scripts
This repo includes **stub versions** of the three Python scripts I built (`normalize_pdf.py`, `mapping_extractor.py`, `lean_jdr.py`).  
Sensitive or proprietary logic has been removed, but the structure and comments show how the tools were organized:

- **normalize_pdf.py** → Extracts values from Crystal PDF reports using regex + PyMuPDF.  
- **mapping_extractor.py** → Reads a JSON mapping and outputs Question|Value CSV.  
- **lean_jdr.py** → Runs 12 JCC Manual quality-control rules and exports standardized data.  

These stubs demonstrate the project’s architecture without exposing internal details.
