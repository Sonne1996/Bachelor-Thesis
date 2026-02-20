# Bachelor-Thesis
Bachelor Thesis of Kevin Sonnek and Sercan Ay from 2026

# ASAG2026

ASAG2026 is a real-world dataset for Automatic Short Answer Grading (ASAG), 
containing approximately 31,500 student answers with LLM-based evaluations and feedback.

## Dataset Overview
- ~31,500 student answers
- Multiple review LLMs
- Numerical grades
- Generated feedback texts
- Structured metadata

## Current Stable Version
v1.0 (see CHANGELOG.md)

## Data Format
- .parquet files
- Structured columns (question, answer, score, review_model, etc.)

## Citation
(To be added after acceptance)

## License
See LICENSE file.

## Project-Structure

```text
asag2026/
│
├── README.md
├── LICENSE
├── CHANGELOG.md
│
├── code/
│   ├── preprocessing.py
│   └── baseline.py
│
└── metadata/
    ├── raw_data_joins.py
    ├── data_card.md
    └── croissant_metadata.json

---

onedrive/
│
├── data/
│   ├── asag_v0.1.parquet
│   ├── asag_v0.2.parquet
│   ├── asag_v1.0.parquet
│   └── asag_vx.x.parquet
│
└── splits/
    ├── split_v1.0.json
    └── split_vx.x.json
```
