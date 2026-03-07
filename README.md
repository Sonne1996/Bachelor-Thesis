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

---

## ASAG2026 – Minimaler Projektfahrplan

- **Abstract:** bis 11. Mai, 23:59
- **Paper:** bis 15. Mai, 23:59
- **BA:** 15. Mai → 5. Juni, 18:00

---

# Phase 1 — Referenzbasis sichern (Pflicht, früh), bis 22.03.
Ohne saubere Ground Truth sind alle Experimente schwach

- Inter-Annotation-Agreement (100er-Subset)
- Human-Grading auf ~5 % ausbauen
- Testsplit mit echten Human-Labels definieren
- Expert vs Student Labels trennen -> TBD
- Übersetzen: Deutsch -> Englisch, vice versa
- Auffälligkeiten dokumentieren (fehlendes Feedback etc.)

---

# Phase 2 — Datensatz praktisch testen (Kernexperimente), bis 19.04.
Zeigen, dass der Datensatz sinnvolle Analysen erlaubt

**Stabilität**
- Gleiche Antwort mehrfach bewerten
- Varianz / Mean / Median vergleichen

**Bias**
- Antwortlänge vs Bewertung
- Deutsch vs Englisch
- Note vs Feedback vorhanden (Nutzen des Feedbacks noch unklar)

**Modelle anwenden**
- Mehrere LLMs vergleichen
- LLM-as-a-Judge Tests
- Finetuning (Leistungsobergrenze)
- Cross-Dataset-Tests (Generalisierung)

---

# Phase 3 — Benchmark daraus machen (für Paper entscheidend), bis 11.05.
Aus Tests → reproduzierbarer Benchmark

- Feste Splits (Question-Level & Answer-Level)
- Feste Metriken (MAE/RMSE)
- Einfache Baselines
- Sanity Checks (schlägt Modell einfache Referenzen?)
- Modellvergleiche sauber darstellen
- Praktische Anwendungsfälle zeigen

Parallel: Paper schreiben (Dataset, Protocol, Experimente, Ergebnisse)

---

# Phase 4 — Bachelorarbeit (nach Paper), bis 5. Juni, 18:00
Paper zu Bachelorarbeit umschreiben

- Methoden detaillierter
- Technische Umsetzung
- Erweiterte Diskussion
- ZHAW-Format

---

We made a [project definition](https://github.com/Sonne1996/Bachelor-Thesis/blob/main/Documents/Projektdefinition_ASAG2026.pdf) with additional information.
