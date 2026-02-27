## Benchmark-Vergleichstabelle
Die Benchmark-Vergleichstabelle dient der strukturierten Gegenüberstellung zentraler Eigenschaften bestehender ASAG-Datensätze, um die Positionierung, Abgrenzung und potenzielle Alleinstellungsmerkmale unseres Datensatzes transparent darzustellen.

| Dataset             | Lang.   | #Samples | Real Students | Score Type | Feedback | Official Split | Q-Level Split | Leakage Analysis | Live Deployment | Open Release |
| ------------------- | ------- | -------- | ------------- | ---------- | -------- | -------------- | ------------- | ---------------- | --------------- | ------------ |
| ASAG (2009)         | EN      | ~2k      | ✓             | Ordinal    | ✗        | ✗              | ✗             | ✗                | ✗               | ✓            |
| ASAP-SAS (2012)     | EN      | ~10k     | ✓             | Ordinal    | ✗        | ✓              | ✗             | ✗                | ✗               | ✓            |
| SemEval SRA (2013)  | EN      | ~5k      | ✓             | Partial    | ✗        | ✓              | ✗             | ✗                | ✗               | ✓            |
| EngSAF (2024)       | EN      | ~1k      | ✓             | Ordinal    | ✓        | ✓              | ✗             | ✗                | ✗               | Partial      |
| ASAG2024 (2024)     | EN      | ~20k     | ✓*            | Ordinal    | ✗        | ✓              | ✗             | ✗                | ✗               | ✓            |
| **ASAG2026 (Ours)** | DE / EN | ~31.5k   | ✓             | Ordinal    | ✓        | ✓              | ✓             | ✓                | ✓               | ✓            |

### Legende

* **#Samples**: Anzahl studentischer Antworten.
* **Real Students**: Authentische studentische Antworten aus realen Lehrveranstaltungen.
* **Score Type**: Bewertungsformat (Binary / Partial / Ordinal / Continuous).
* **Feedback**: Enthält textuelles Feedback zusätzlich zur Punktzahl.
* **Official Split**: Vorgegebene Train/Test-Splits.
* **Q-Level Split**: Leakage-sicherer Question-Level-Split möglich.
* **Leakage Analysis**: Explizite Analyse verschiedener Split-Strategien.
* **Live Deployment**: Daten stammen aus realem Kurseinsatz.
* **Open Release**: Öffentlich zugänglicher Datensatz.

*ASAG2024 aggregiert mehrere bestehende Datensätze.

---

## Datensatz-Spalten/Metadaten
Die Definition der Datensatz-Spalten legt eine konsistente und reproduzierbare Metadatenstruktur fest, die Training, Evaluation, Split-Strategien und weiterführende Analysen systematisch ermöglicht.

| Feldname        | Beschreibung                  | Typ             | Anmerkung                |
| --------------- | ----------------------------- | --------------- | ------------------------ |
| Index           | Eindeutige ID pro Tupel       | Integer         | Primärschlüssel          |
| Question_ID     | Eindeutige ID pro Frage       | Integer         | Mehrere Answers möglich  |
| Question        | Gestellte Frage               | String          |                          |
| Answer_ID       | Eindeutige ID pro Antwort     | Integer         |                          |
| Provided_answer | Studentische Antwort          | String          |                          |
| No_Answer       | Keine Antwort abgegeben       | Boolean         | True bei "leer", "/", "-"|
| Grade           | LLM-Bewertung                 | Float           |                          |
| Weight          | Gewichtung zur Bias-Kontrolle | Float           | Optional                 |
| Used_model      | Bewertendes Modell            | String          | qwen-3-32b. gemini-2.5-flash, gemini-2.5-pro, gpt-5 |
| Rubrik_used     | Rubrik verwendet              | Boolean         |                          |
| Rubrik          | Bewertungsinstruktion         | String          |                          |
| Example_used    | Beispielantwort verwendet     | Boolean         |                          |
| Example         | Beispielantwort               | String          |                          |
| Q-Split         | Question-Level Split          | String          | Train/Val/Test           |
| A-Split         | Answer-Level Split            | String          | Train/Val/Test           |
| Sprache         | Sprache der Antwort           | String          | DE / ENG                 |

---

## Use-Cases/Test-Cases/Praktische Anwedungen
Die definierten Use-Cases beschreiben konkrete Anwendungsszenarien zur systematischen Erprobung, Evaluation und Validierung des Datensatzes in unterschiedlichen Modell- und Evaluationskontexten.

* Mehrfachbewertung identischer Antworten → Untersuchung der Bewertungsstabilität und Kalibrierung
  * Aggregation: Mean
  * Aggregation: Median
  * Varianz-Analyse zwischen Runs

* Einfluss der Antwortlänge auf Bewertung → Analyse möglicher Längen-Bias und struktureller Bewertungsmuster
  * Tokenlänge
  * Zeichenlänge
  * Anzahl Wörter
  * Wörter pro Satz
