# Verwandte Arbeiten – Funktionaler Überblick

## 1. Referenzen zu Benchmark- und Datensatzdesign (Artikel, die uns bei der Gestaltung von Datensatzvergleichstabellen, Datensatzstrukturen und Benchmark-Dimensionen helfen)

### [ASAG2024 – A Combined Benchmark for Short Answer Grading](https://github.com/Sonne1996/Bachelor-Thesis/blob/main/Related%20Works/ASAG2024%20A%20Combined%20Benchmark%20(2024).pdf)
Kombiniert sieben bestehende ASAG-Datensätze in einer einheitlichen Struktur mit normalisierter Bewertungsskala und ermöglicht dadurch datensatzübergreifende Benchmark-Vergleiche. Dient als Referenz für Datensatz-Harmonisierung, Benchmark-Konstruktion und gewichtete Evaluationsmetriken bei unausgeglichenen Notenverteilungen.

### [SM3 – Text-to-Query Benchmark (NeurIPS 2024)](https://github.com/Sonne1996/Bachelor-Thesis/blob/main/Related%20Works/NeurIPS24_SM3_Text_to_Query__Revision_.pdf)
NeurIPS-Datasets-&-Benchmarks-Paper mit klar strukturierter Darstellung von Datensatzaufbau, Benchmark-Design, Evaluationsprotokollen und Reproduzierbarkeitsstandards. Dient als strukturelle und stilistische Vorlage für Aufbau, Tabellenstruktur und Methodikdarstellung unseres eigenen Benchmark-Papers.

### [SAS-Bench – Fine-Grained Benchmark for Short Answer Scoring](https://github.com/Sonne1996/Bachelor-Thesis/blob/main/Related%20Works/SAS-Bench%20(2026)%20%E2%80%93%20Fine-Grained%20Benchmark.pdf)
Feingranularer Benchmark für Kurzantwortbewertung mit schrittweiser Punktevergabe, detaillierten Fehlerkategorien und Expertenannotation zur Analyse von Bewertungsgenauigkeit und Erklärbarkeit automatischer Grading-Systeme. Dient als Referenz für Benchmark-Design, differenzierte Bewertungsdimensionen und Evaluationskriterien über reine Gesamtnoten hinaus.

## 2. Referenzen zu Bewertungs- und Benotungsmethoden (Artikel, die Bewertungsmetriken, Benotungspipelines und Modellvergleiche behandeln)

### [Powergrading – Clustering-Assisted Short Answer Grading (Basu et al., 2013)](https://github.com/Sonne1996/Bachelor-Thesis/blob/main/Related%20Works/Powergrading%20(Basu%20et%20al.%2C%20TACL%202013)%20%E2%80%93%20clusteringassisted%20grading.pdf)
Stellt ein halbautomatisches Bewertungsverfahren vor, bei dem ähnliche Studentenantworten mithilfe von Clustering gruppiert werden, sodass Lehrpersonen ganze Antwortgruppen gemeinsam bewerten und typische Fehlermuster schneller erkennen können. Dient als Referenz für clusterbasierte Bewertungsansätze, Effizienzsteigerung im Korrekturprozess und Analyse von Antwortmustern.

## 3. ASAG-Systeme in der Praxis und Herkunft von Datensätzen (Artikel, die zeigen, wie ASAG-Systeme eingesetzt werden und wie reale Datensätze erstellt werden)

### [Closing the Feedback Loop – LLM-basierte Bewertung im realen Hochschulbetrieb](https://github.com/Sonne1996/Bachelor-Thesis/blob/main/Related%20Works/Closing%20the%20Feedback%20Loop%20-%20A%20Deployment%20of%20LLM-driven%20Question%20Generation%20and%20Automated%20Grading%20in%20a%20Large-Scale%20Undergraduate%20Course.pdf)
Beschreibt den praktischen Einsatz eines geschlossenen LLM-Systems zur automatisierten Fragenerstellung und Kurzantwortbewertung in einem grossen Hochschulkurs und analysiert reale Bewertungsqualität, Studierendenwahrnehmung sowie Nutzungsverhalten. Dient als Referenz für reale Einsatzszenarien, Datensatzentstehung und praktische Herausforderungen automatisierter Bewertung.

## 4. Verwendete Datensets für den Vergleich

[ASAG2024](https://github.com/Sonne1996/Bachelor-Thesis/blob/main/Related%20Works/ASAG2024%20A%20Combined%20Benchmark%20(2024).pdf): Mehrere bestehende ASAG-Datensätze vereinheitlicht -> Vorgänger Arbeit

[ASAP-SAS](https://www.kaggle.com/c/asap-sas): Grosser bekannter Public-ASAG-Datensatz -> Wird in Arbeit wiederholt verwendet

[SciEntsBank and Beetle](https://github.com/Sonne1996/Bachelor-Thesis/blob/main/Related%20Works/SciEntsBank%20%20Student%20Response%20Analysis%20(SemEval-2013%20Task%207)%20%E2%80%93%20Original%20Task%20Paper.pdf): Gilt als Standard Benchmark

[SAS-Bench](https://github.com/Sonne1996/Bachelor-Thesis/blob/main/Related%20Works/SAS-Bench%20(2026)%20%E2%80%93%20Fine-Grained%20Benchmark.pdf): moderner (2025) LLM-Benchmark für SAS/ASAG-like scoring

[SAF](https://github.com/Sonne1996/Bachelor-Thesis/blob/main/Related%20Works/Filighera%20et%20al.%20(ACL%202022)%20%E2%80%93%20Short%20Answer%20Feedback%20(SAF).pdf): Feedback-orientierter Spezialbenchmark, der bereits in Folgeararbeiten genutzt wird -> Kann auch ausgebaut verwendet werden, wenn wir uns auf Feedback konzentrieren

## 5. Zusätzliche Hintergrundinformationen und bisherige Arbeiten (Ältere modellbasierte Ansätze, Umfragen und interne Abschlussarbeiten zum Kontext)

### [Focusing on Students, not Machines – Grounded Question Generation and Automated Answer Grading](https://github.com/Sonne1996/Bachelor-Thesis/blob/main/Related%20Works/BA_Thesis_FocusingOnStudentsNotMachines.pdf)
Beschreibt ein LLM-basiertes System zur generierung lernzielbasierter Prüfungsfragen und automatisierten Bewertung von Kurzantworten sowie die Einführung des kombinierten ASAG2024-Benchmarks zur vergleichenden Evaluation verschiedener Grading-Ansätze. Dient als methodische Referenz für Systemarchitektur, Benchmark-Idee und Evaluationsaufbau.

### [BEETLE II – Student Explanation Dataset for Intelligent Tutoring](https://github.com/Sonne1996/Bachelor-Thesis/blob/main/Related%20Works/Beetle%20(BEETLE%20%20BEETLE%20II).pdf)
Datensatz mit studentischen Freitext-Erklärungen aus einem intelligenten Tutorensystem im Bereich Elektrotechnik, ergänzt durch Referenzantworten und Korrektheitsannotation. Dient als etablierter Vergleichsdatensatz für automatische Kurzantwortbewertung und Antwortklassifikation.

### [Burrows et al. (2015) – Automatic Short Answer Grading: A Survey](https://github.com/Sonne1996/Bachelor-Thesis/blob/main/Related%20Works/Burrows%20et%20al.%20(2015)%20%E2%80%93%20Survey.pdf)
Systematische Übersicht früher ASAG-Forschung mit Einordnung von Datensätzen, Bewertungsverfahren und Evaluationsansätzen. Dient als Hintergrundreferenz für historische Entwicklungen und grundlegende Vergleichskriterien im ASAG-Bereich.

### [CREG – Corpus of Reading Comprehension Exercises](https://github.com/Sonne1996/Bachelor-Thesis/blob/main/Related%20Works/CREG%20(Corpus%20of%20Reading%20Comprehension%20Exercises)%20%E2%80%93%20learner%20answers%20%20reading%20comprehension.pdf)
Lernerkorpus mit studentischen Freitextantworten auf Leseverständnisfragen inklusive Referenzantworten und binärer Korrektheitsannotation. Dient als Vergleichsdatensatz für automatische Inhaltsbewertung kurzer Antworten im Bildungskontext.

### [SAF – Short Answer Feedback Dataset (Filighera et al., ACL 2022)](https://github.com/Sonne1996/Bachelor-Thesis/blob/main/Related%20Works/Filighera%20et%20al.%20(ACL%202022)%20%E2%80%93%20Short%20Answer%20Feedback%20(SAF).pdf)
Bilingualer ASAG-Datensatz mit Kurzantworten, Noten und ausführlichem erklärendem Feedback, das Fehler inhaltlich begründet statt nur eine Punktzahl zu vergeben. Dient als Referenz für erklärbares Grading, Feedback-Generierung und erweiterte Bewertungsdimensionen über reine Score-Vergleiche hinaus.

### [Mohler & Mihalcea (2009) – Texas Short Answer Dataset](https://github.com/Sonne1996/Bachelor-Thesis/blob/main/Related%20Works/Mohler%20%26%20Mihalcea%20(2009)%20%E2%80%93%20TexasMohler%20Dataset%20(klassischer%20Datensatz-Paper).pdf)
Früher ASAG-Referenzdatensatz mit studentischen Kurzantworten aus Informatikprüfungen, mehrfach manuell bewertet und zur Evaluation semantischer Ähnlichkeitsverfahren zwischen Referenz- und Studentenlösungen genutzt. Dient als klassischer Vergleichsdatensatz und methodische Grundlage früher automatischer Bewertungsansätze.

### [Mohler et al. (2011) – Learning to Grade Short Answer Questions](https://github.com/Sonne1996/Bachelor-Thesis/blob/main/Related%20Works/Mohler%20et%20al.%202011%20(ACL).pdf)
Früher modellzentrierter ASAG-Ansatz, der semantische Ähnlichkeitsmetriken mit syntaktischer Abhängigkeitsgraph-Ausrichtung kombiniert und maschinelles Lernen zur automatischen Notenvorhersage nutzt. Dient als methodische Referenz für hybride Bewertungsmodelle, die Struktur- und Inhaltsmerkmale gemeinsam berücksichtigen.

### [CREG – Corpus of Reading Comprehension Exercises (Ott et al., 2012)](https://github.com/Sonne1996/Bachelor-Thesis/blob/main/Related%20Works/Ott%20et%20al.%202012.pdf)
Aufgabenbasierter Lernerkorpus mit studentischen Freitextantworten auf Leseverständnisfragen inklusive Zielantworten und detaillierter Bedeutungsannotation zur Bewertung inhaltlicher Korrektheit. Dient als Vergleichsdatensatz für kontextbasierte Kurzantwortbewertung und Meaning-in-Context-Analysen.

### [Riordan et al. (2017) – Neural Architectures for Short Answer Scoring](https://github.com/Sonne1996/Bachelor-Thesis/blob/main/Related%20Works/Riordan%20et%20al.%20(2017).pdf)
Untersucht verschiedene neuronale Architekturen (u.a. CNN und LSTM) zur automatischen Bewertung kurzer Schülertexte und analysiert den Einfluss vortrainierter Wortrepräsentationen auf die Bewertungsqualität. Dient als Referenz für frühe Deep-Learning-Ansätze im ASAG-Bereich und für den Vergleich klassischer neuronaler Modellarchitekturen.

### [SciEntsBank – Student Response Analysis (SemEval-2013 Task 7)](https://github.com/Sonne1996/Bachelor-Thesis/blob/main/Related%20Works/SciEntsBank%20%20Student%20Response%20Analysis%20(SemEval-2013%20Task%207)%20%E2%80%93%20Original%20Task%20Paper.pdf)
Grosser Benchmark-Datensatz mit studentischen Kurzantworten aus verschiedenen naturwissenschaftlichen Themenbereichen, annotiert mit mehrstufigen Korrektheitslabels zur Bewertung semantischer Übereinstimmung mit Referenzantworten. Dient als etablierter Vergleichsdatensatz für kategorielle Kurzantwortbewertung und Benchmark-Evaluation im ASAG-Bereich.

### [Survey on Automated Short Answer Grading with Deep Learning (Haller et al., 2022)](https://github.com/Sonne1996/Bachelor-Thesis/blob/main/Related%20Works/Survey%20on%20Automated%20Short%20Answer%20Grading%20with%20Deep%20Learning.pdf)
Umfassende Übersicht moderner ASAG-Methoden mit Fokus auf Deep-Learning-Ansätze, Benchmark-Datensätze und Evaluationspraktiken sowie einer Taxonomie von Feature-Engineering bis Transformer-Modelle. Dient als Hintergrundreferenz für Forschungsstand, Methodenentwicklung und etablierte Vergleichsdimensionen im ASAG-Bereich.

### [ASAP-SAS – Automated Student Assessment Prize Dataset (Hewlett Foundation, Kaggle 2012)](https://www.kaggle.com/c/asap-sas)
Grosser Benchmark-Datensatz mit studentischen Kurzantworten aus verschiedenen Prüfungsaufgaben, mehrfach manuell bewertet und zur Entwicklung automatischer Bewertungsverfahren im Rahmen eines internationalen Kaggle-Wettbewerbs erstellt. Dient als einer der meistgenutzten Vergleichsdatensätze für ASAG-Benchmarking und Modellvergleich.
