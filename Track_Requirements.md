# NeurIPS 2025 – Datasets & Benchmarks Track Requirements (ASAG2026)

## 1. Deadlines

- **Abstract Submission:** May 11, 2025 (AoE*) → Kurze Zusammenfassung des Papers
- **Full Paper Submission:** May 15, 2025 (AoE*) → Vollständiges Paper (Hauptdokument)
- **Technical Appendix / Supplementary:** May 22, 2025 (AoE*) → Zusätzliche Materialien wie erweiterte Experimente, Details zur Methodik, zusätzliche Tabellen, Beweise oder Implementierungsdetails, die nicht ins Seitenlimit des Hauptpapers passen.
- **Author Notification:** September 18, 2025 → Datum, an dem wir erfahren, ob das Paper angenommen, abgelehnt oder mit Revision versehen wurde.
- **Camera-Ready:** October 23, 2025 → Finale, überarbeitete Version des Papers nach Reviewer-Feedback, die offiziell in den Konferenz-Proceedings veröffentlicht wird.

*(AoE = Anywhere on Earth – spätestmögliche Zeitzone weltweit)

⚠️ Wichtig: Zum Zeitpunkt der Full Submission müssen Dataset und Code bereits zugänglich sein.

---

## 2. Paper Length & Formatting Rules

The NeurIPS 2025 Datasets & Benchmarks Track follows the formatting rules of the Main Track.

### Page Limit

- **Main Paper:** Maximum 9 pages  
- **References:** Do not count toward the page limit
- **Supplementary Material:** Separate PDF, not included in the 9-page limit

### Important Notes

- The Datasets & Benchmarks Track uses the same official NeurIPS LaTeX template as the Main Track.
- Section titles are flexible and may be adapted (e.g., replacing "Methods").
- No table of contents, list of figures, or list of tables is required.
- The supplementary material is submitted separately and may contain extended analyses, dataset statistics, additional figures, prompt templates, or implementation details.

⚠️ All formatting must strictly follow the official NeurIPS template.

---

## 3. Submission Portal

OpenReview Portal:  
[https://openreview.net/group?id=NeurIPS.cc/2025/Datasets_and_Benchmarks_Track](https://openreview.net/group?id=NeurIPS.cc/2025/Datasets_and_Benchmarks_Track)
- [ ] OpenReview Account vorhanden
  - [ ] Kevin
  - [ ] Jonathan
  - [ ] Martin
  - [ ] Sercan
  - [ ] Gerome?
- [ ] Alle Autoren haben ein vollständiges OpenReview-Profil
  - [ ] Kevin
  - [ ] Jonathan
  - [ ] Martin
  - [ ] Sercan
  - [ ] Gerome?
- [ ] Richtiger Track ausgewählt (Datasets & Benchmarks, nicht Main Track)

---

## 4. Track-Anforderungen & Paper-Fokus

Der Datasets & Benchmarks Track folgt dem Main Track in Bezug auf wissenschaftliche Qualität, hat jedoch spezifische Anforderungen für daten-zentrierte Arbeiten.

### Grundprinzip
Das Paper muss klar als **data-centric contribution** positioniert sein.  
Nicht Modell-SOTA, sondern:

- Datensatz-Design
- Datengenerierung
- Annotation / Review-Prozess
- Bias-Analyse
- Benchmark-Methodologie
- Robustheit & Evaluation-Design

### Wichtige Punkte, die direkt im Paper adressiert werden müssen

- **Datenherkunft und Generierungspipeline klar dokumentieren**
- **Annotation / Bewertungsprozess transparent beschreiben**
- **Mögliche Bias-Quellen explizit diskutieren**
- **Limitations & Risiken klar benennen**
- **Reproduzierbarkeit sicherstellen**
- **Benchmark-Setup klar definieren (Splits, Metriken, Protokoll)**

Submission kann single-blind erfolgen (vollständige Anonymisierung nicht zwingend), dennoch wissenschaftlich sauber und nachvollziehbar.

---

## 5. Veröffentlichungspflichten

### 5.1 Technische Zugänglichkeit (Submission Pflicht)
- [ ] Dataset öffentlich zugänglich
- [ ] Code öffentlich & ausführbar
- [ ] Keine Zugangsbeschränkung
- [ ] Croissant Metadata vorhanden [https://github.com/Sonne1996/Bachelor-Thesis/blob/main/asag2026/metadata/croissant_metadata.json](https://github.com/Sonne1996/Bachelor-Thesis/blob/main/asag2026/metadata/croissant_metadata.json)

### 5.2 Dokumentation (Submission Pflicht)
- [ ] Data Card vorhanden [https://github.com/Sonne1996/Bachelor-Thesis/blob/main/asag2026/metadata/data_card.md](https://github.com/Sonne1996/Bachelor-Thesis/blob/main/asag2026/metadata/data_card.md)
- [ ] Datengenerierung transparent beschrieben
- [ ] Bewertungs-/Annotationsprozess dokumentiert
- [ ] Bias-Quellen diskutiert
- [ ] Limitations klar benannt
- [ ] Lizenz definiert [https://github.com/Sonne1996/Bachelor-Thesis/blob/main/asag2026/LICENSE](https://github.com/Sonne1996/Bachelor-Thesis/blob/main/asag2026/LICENSE)

### 5.3 Nach Acceptance
- [ ] Dauerhafte Hosting-Garantie
- [ ] Klare Versionierung (z. B. v1.0, v1.1) [https://github.com/Sonne1996/Bachelor-Thesis/blob/main/asag2026/CHANGELOG.md](https://github.com/Sonne1996/Bachelor-Thesis/blob/main/asag2026/CHANGELOG.md)
- [ ] Reproduzierbares Benchmark-Protokoll

⚠️ Nicht-Einhaltung der Zugänglichkeitsanforderungen kann zu Desk Reject führen.

---

## 6. Offizieller Call

NeurIPS 2025 Datasets & Benchmarks Track Call for Papers:  
[https://neurips.cc/Conferences/2025/CallForDatasetsBenchmarks](https://neurips.cc/Conferences/2025/CallForDatasetsBenchmarks)
Use Control + Shift + m to toggle the tab key moving focus. Alternatively, use esc then tab to move to the next interactive element on the page.
Attach files by dragging & dropping, selecting or pasting them.

## 7. Additional Main Track Requirements

- Reproducibility Checklist must be completed during submission.
- Ethical considerations and potential biases must be explicitly discussed.
- Hardware and compute details should be reported if models are trained.
- All external resources must be publicly accessible without login.
- Formatting must strictly follow the official NeurIPS template.
 
