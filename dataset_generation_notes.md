# ASAG2026 – Notizen zur Datensatz-Generierung

Diese Seite dokumentiert interne technische Details zur Erstellung des Datensatzes.
---

## Fragenerstellung

- Wochen 1–9: Fragen generiert mit Gemini 2.5
- Wochen 10–14: Fragen generiert mit GPT-5
- GPT-5 antwortete anfänglich auf Englisch → Prompt wurde angepasst
- Es existiert ein Pool nicht verwendeter Fragen
- Der Modellwechsel (Gemini → GPT-5) kann strukturelle Unterschiede im Datensatz verursachen

---

## Manuelle Prüfung und Freigabe

- Alle Fragen wurden von Gérôme manuell geprüft
- Fragen wurden weitergeleitet, erneut überprüft und freigegeben oder abgelehnt (vorhanden in einem Google Sheet)
- Nur freigegebene Fragen wurden in den finalen Datensatz übernommen
- Jede freigegebene Frage enthält eine Referenzantwort (pro Punktevergabe, also Referenzantwort pro Bucket)
- Eine Rubrik wurde in Promptform definiert (Bewertungsanweisung für das Grading-LLM)

---

## Grading-Setup

- Pro studentischer Antwort wurde eines von vier Grading-LLMs verwendet
  - Gemini 2.5-flash
  - Gemini 2.5-pro
  - ChatGPT 5
  - QWEN-3-32b
- Rubrik und/oder Referenzantwort wurden dem Modell mitgegeben
- Das LLM erzeugte:
  - Eine numerische Note
  - Ein Feedback
- Studierende konnten die LLM-Bewertung einsehen
- QWEN wurde im Verlauf des Semesters deaktiviert → Diese Änderung sollte im Datensatz nachvollziehbar sein  
- Es existieren 16 Permutationen im Grading-Setup → Diese müssen separat dokumentiert werden

---

## Strukturelle Besonderheiten

- Geschlossener Grading-Loop (Frage → Antwort → LLM-Bewertung → Feedback sichtbar)
- Prompt-Anpassung während des Semesters (Sprachkorrektur)
- Mögliche Verteilungseffekte durch:
  - Modellwechsel
  - Graderwechsel
  - Promptänderungen

---

## Hinweise für die Analyse

- Noten-Histogramme erstellen (gesamt und pro Grader)
- Prozentuale Verteilungen statt absolute Zahlen verwenden
- Permutationen getrennt analysieren
- Mögliche strukturelle Veränderungen über die Wochen hinweg prüfen

---

## Technische Basis

- Datensatz vor Analyse als `.parquet` einfrieren
- Fokus der Evaluation liegt auf der Genauigkeit der Noten
- Permutationsstruktur klar dokumentieren
