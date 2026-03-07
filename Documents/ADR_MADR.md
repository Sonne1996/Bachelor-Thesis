## Benchmark-Vergleichstabelle
Die Benchmark-Vergleichstabelle dient der strukturierten Gegenüberstellung zentraler Eigenschaften bestehender ASAG-Datensätze, um die Positionierung, Abgrenzung und potenzielle Alleinstellungsmerkmale unseres Datensatzes transparent darzustellen.

# ASAG Benchmark Comparison Tables (Condensed Version)

Legende – Datensätze (Kurzbeschreibung)
* ASAG2024 – Kombinierter Meta-Benchmark aus mehreren klassischen ASAG-Datensätzen
* ASAP-SAS – Grösster klassischer Schul-Benchmark für automatische Kurzantwortbewertung
* SciEntsBank – SemEval-Shared-Task-Datensatz für Schülerantworten in Naturwissenschaften
* BEETLE – Elektronik-spezifischer Tutoring-Datensatz mit Schülererklärungen
* SAS-Bench – Moderner LLM-Benchmark mit schrittweiser Expertenbewertung
* SAF – Datensatz mit ausführlichem menschlichem Feedback zu Kurzantworten
* ASAG2026 – Neuer ZHAW-Benchmark mit LLM-Bewertungsloop aus realem Hochschulkurs (Datenbank)

---

## Table 1 — Dataset Metadata Overview

| Dataset         | Year | Lang  | Domain        | Context              |         Qs |        Ans | Ref Ans   | Scoring           | Feedback       |
| --------------- | ---: | ----- | ------------- | -------------------- | ---------: | ---------: | --------- | ----------------- | -------------- |
| **ASAG2024**    | 2024 | EN    | Multi-domain  | Combined legacy sets |      ~283* |        19k | Yes       | Normalized score  | —              |
| **ASAP-SAS**    | 2012 | EN    | Multi-subject | School exams         | 10 prompts |     17,204 | Rubrics   | Ordinal (0–3)     | —              |
| **SciEntsBank** | 2013 | EN    | Science       | School assessment    |        197 |     ~10.8k | Yes       | 5-way cat.        | —              |
| **BEETLE**      | 2013 | EN    | Electronics   | Tutorial system      |         56 |   ~3k–12k‡ | Multi-ref | 5-way cat.        | —              |
| **SAS-Bench**   | 2025 | ZH    | Multi-subject | National exams       |      1,030 |      4,109 | Yes       | Step-wise + total | Error tags     |
| **SAF**         | 2022 | DE/EN | Multi-domain  | Course settings      |      Mixed |      4,519 | Yes       | Score + label     | Human feedback |
|  |  |  |  |  |  |  |  |  |  |
| **ASAG2026**    | 2026 | TBD   | Univ. course  | Real deployment      |        TBD |     ~31.5k | TBD       | LLM score         | LLM feedback   |

* Open Release weggelassen da alle Datensätze öffentlich zugänglich sind -> Trotzdem im Text festhalten

† Paper vs. Hugging Face release size
‡ Depends on reference-expansion variant

Tabelle 1 – Metadaten
* Lang – Sprache(n) der Antworten
* Domain – Fachgebiet / Themenbereich
* Context – Entstehungskontext (z.B. Prüfung, Kurs)
* Qs – Anzahl Fragen
* Ans – Anzahl Antworten
* Ref Ans – Muster-/Referenzantwort vorhanden
* Scoring – Bewertungsart
* Feedback – Rückmeldetexte vorhanden

---

## Table 2 — Benchmark Capability Overview

| Dataset         | Real Stu. | Real Deploy. | Closed Loop | Q-Split | A-Split | Domain Split | Fine-Grained | Feedback Eval | LLM-Fit | Role             | Live Deployment |
| --------------- | --------- | ------------ | ----------- | ------- | ------- | ------------ | ------------ | ------------- | ------- | ---------------- | --- |
| **ASAG2024**    | ✓         | Mixed        | —           | —       | ✓       | —            | Limited      | —             | ✓✓      | Predecessor      | — | 
| **ASAP-SAS**    | ✓         | ✓            | —           | —       | ✓       | —            | Basic        | —             | ✓       | Legacy anchor    | ✓✓ |
| **SciEntsBank** | ✓         | ✓            | —           | ✓       | ✓       | ✓            | Moderate     | —             | ✓✓      | Shared-task std. | ✓✓ |
| **BEETLE**      | ✓         | ✓            | —           | ✓       | ✓       | —            | Moderate     | —             | ✓✓      | Domain benchmark | ✓✓ |
| **SAS-Bench**   | ✓         | ✓            | —           | —       | —       | —            | ✓✓✓          | Structured    | ✓✓✓     | Modern LLM std.  | ✓ |
| **SAF**         | ✓         | ✓            | —           | ✓       | ✓       | —            | Moderate     | ✓✓✓           | ✓✓      | Feedback std.    | ✓ |
|  |  |  |  |  |  |  |  |  |  |  |  |
| **ASAG2026**    | ✓         | ✓            | ✓           | ✓       | ✓       | —            | Partial      | Auto          | ✓✓✓     | Core benchmark   | ✓✓✓ |

### Legend

* ✓✓✓ = very strong support/Vollständig in realem Kurs
* ✓✓ = strong support/Reale Prüfungsdaten
* ✓ = supported/Reale Kursdaten, aber nicht als Bewertungssystem
* — = not supported/not defined/Kein echter Einsatz

Tabelle 2 – Benchmark-Fähigkeiten
* Real Stu. – Echte Studierendenantworten
* Real Deploy. – In realem Unterricht/Prüfung eingesetzt
* Closed Loop – Bewertungsprozess vollständig abgebildet
* Q-Split – Trennung nach Fragen möglich (Leakage-sicher)
* A-Split – Trennung nach Antworten möglich
* Domain Split – Trennung nach Fachgebieten möglich
* Fine-Grained – Detaillierte Bewertungsstruktur
* Feedback Eval – Feedback-Qualität evaluierbar
* LLM-Fit – Eignung für LLM-Bewertungsvergleich
* Role – Rolle im Vergleich

---

## Datensatz-Spalten/Metadaten
Die Definition der Datensatz-Spalten legt eine konsistente und reproduzierbare Metadatenstruktur fest, die Training, Evaluation, Split-Strategien und weiterführende Analysen systematisch ermöglicht.

| Feldname | Beschreibung | Typ | Anmerkung |
|----------|-------------|-----|-----------|
|  |  |  |  |
| **IDENTIFIKATION** |  |  |  |
| Answer_ID | Eindeutige ID pro Antwort | String | Primäranker des Datensatzes |
| Question_ID | Zugehörige Frage-ID | String | Mehrere Antworten pro Frage möglich |
|  |  |  |  |
| **FRAGEINFORMATIONEN** |  |  |  |
| Question_Text | Gestellte Prüfungsfrage | String | Originale Aufgabenstellung |
|  |  |  |  |
| **ANTWORTINFORMATIONEN** |  |  |  |
| Provided_Answer | Studentische Antwort | String | Unveränderter Rohtext |
| No_Answer | Keine Antwort abgegeben | Boolean | True bei leerer Eingabe ("", "-", "/") |
| Language | Sprache der Antwort | String | DE / EN |
| Answer_Length_Tokens | Tokenanzahl der Antwort | Integer | Für LLM-Analyse |
| Answer_Length_Words | Wortanzahl der Antwort | Integer | Längenanalyse |
| Answer_Length_Chars | Zeichenanzahl der Antwort | Integer | Längenanalyse |
|  |  |  |  |
| **HUMANBEWERTUNG** |  |  |  |
| Human_Score_1 | Bewertung durch menschlichen Rater 1 | Float | Skala 0–1 |
| Human_Score_2 | Bewertung durch menschlichen Rater 2 | Float | Skala 0–1 |
| Human_Score_3 | Bewertung durch menschlichen Rater 3 | Float | Skala 0–1 |
| Human_Score_4 | Bewertung durch menschlichen Rater 4 | Float | Skala 0–1 |
| Human_Score_5 | Bewertung durch menschlichen Rater 5 | Float | Skala 0–1 |
| Human_Goldstandard | Aggregierte menschliche Referenzbewertung | Float | Mittelwert oder Median |
|  |  |  |  |
| **LLM-BEWERTUNG** |  |  |  |
| Score_GPT5 | Bewertung durch GPT-5 | Float | Automatische Bewertung |
| Score_Gemini_Pro | Bewertung durch Gemini 2.5 Pro | Float | Automatische Bewertung |
| Score_Gemini_Flash | Bewertung durch Gemini 2.5 Flash | Float | Automatische Bewertung |
| Score_Qwen_32B | Bewertung durch Qwen 3-32B | Float | Open-Source-Modell |
| ... | Bewertung durch weitere Modelle | Float | Weitere noch nicht definiert Modelle (Encoder, Llama-8B-Instruct |
| Best_Model_Score | Beste Modellbewertung | Float | Kleinste Abweichung vom Human-Goldstandard |
|  |  |  |  |
| **BEWERTUNGSKONTEXT** |  |  |  |
| Rubric_Used | Bewertungsrubrik verwendet | Boolean | Strukturierte Bewertungsvorgaben |
| Rubric_Text | Bewertungsinstruktion | String | Bestandteil des Bewertungs-Prompts |
| Example_Used | Beispielantworten verwendet | Boolean | Few-Shot Prompting |
| Example_Text | Verwendete Beispielantworten | String | Bestandteil des Bewertungs-Prompts |
|  |  |  |  |
| **TECHNISCHE METADATEN** |  |  |  |
| Input_Tokens | Tokenanzahl der Modelleingabe | Integer | Kostenabschätzung |
| Inference_Time_ms | Bewertungsdauer des Modells | Float | Effizienzanalyse |
| Question_Split* | Question-Level-Datensplit | String | Train / Validation / Test |
| Answer_Split* | Answer-Level-Datensplit | String | Train / Validation / Test |

*Testdaten vermutlich nur die 5% von HumanLabel sein. Die restlichen 95% haben Bewertung des besten LLM.

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

* 4100 haben kein Feedback
  * Eventuell gibt ein Modell kein Feedback -> Vielleicht sogar Notenabhängig
  * Allgemein sind 20% aller Feedbacks leer -> 4100 wurde nicht alle sauber herausgefiltert

* Finetuning einiger Modelle
  * Llama Fine-Tuning auf ASAG2024 → Vergleich mit etabliertem kombinierten Benchmark
  * Llama 8B Fine-Tuning auf ASAG2026 → Maximale Datensatzanpassung und Leistungsobergrenze
  * Encoder-basiertes Modell auf ASAG2026 → Effiziente, stabile Klassifikation für neuen Datensatz
  * Encoder-basiertes Modell auf ASAG2024 → Cross-Dataset-Vergleich und Generalisierungsanalyse
 
