# ASAG2026 Changelog

## v0.01 – 25.02.2026
- Initial export from SQLite database
- Joined core tables (members, questions)

## v0.02 - 25.02.2026
- Joined previous dataset v0.01 with core tables (answers)

## v0.1_stable - 25.02.2026
- Joined previous dataset v0.02 with core tables (gradings)

## v0.11 - 27.02.2026
- Dropped columns member_id, subject_id, answer_id, question_id, grading_id

## v0.12 - 27.02.2026
- Extracted json content from column answer into a non-json format
- New columns:
    - cleaned_answer

## v0.13 - 27.02.2026
- Extracted json content from column question into a non-json format
- New columns:
    - cleaned_question

## v0.14 - 27.02.2026
- Extracted json content from column model_prediction into a non-json format
- New columns:
    - cleaned_model_prediction

## v0.15 - 27.02.2026
- Dropped columns rating and comment

## v0.16 - 27.02.2026
- Extracted for each model the api meta data and saved them in tables
- New columns are: 
    - input_tokens
    - inference_duration_ms
    - prompt
    - temperature
    - reasoning

## v0.20 - 27.02.2026
- Dropped columns answer, question and model_prediction, model_response_with_metadata
- Reordered columns
- Renamed columns like this:
    - cleaned_question -> question
    - cleaned_rubric -> rubric
    - cleaned_examples -> examples
    - cleaned_answer -> answer
    - cleaned_model_prediction -> feedback

## v0.30 - 

## v1.0_stable - 
