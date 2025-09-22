# Launch Log – Hung Jury – JDR Automation Prototype

**Start Date:** Friday, September 19, 2025 (afternoon)
**Stop Date:** Monday, September 22, 2025 (afternoon)

## Day 1 – Friday Afternoon
- Idea: Automate the Annual Jury Data Report.
- Built initial PDF parser with PyMuPDF.
- Extracted some values, but Q9 breakdown scrambled (e.g., Q9D=4415 instead of 0).

## Weekend – Saturday & Sunday
- No work (off days).

## Day 2 – Monday Morning
- Switched to JSON mapping approach (`crystal_mapping_SAMPLE.json`).
- Able to produce Question|Value CSV, but only by manually correcting values.
- Built `lean_jdr.py` to apply all 12 JCC rules. It validated correctly when fed the corrected mapping.

## Day 2 – Monday Afternoon
- Compared outputs against Excel. Confirmed Excel workbook is still the only reliable method.
- Documented vendor issues (Crystal data positioning errors).
- Decision: **Stop full automation.** Excel workbook remains the gold standard for compliance.
- Python QC tool is kept as reference for future systems.

## Conclusion
This project was valuable not for the automation itself, but for the clarity it created:
- Automation is blocked by vendor data quality.
- Excel is defensible and compliant.
- My scripts are “shelf-ready” if structured data becomes available.
