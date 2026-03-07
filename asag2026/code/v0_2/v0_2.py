import pandas as pd
import sys
from pathlib import Path
import datetime
import json

def open_parquet_file(path: Path):

    if(not(path.suffix.lower() == ".parquet")):
        print("You did not input a path for a parquet file.")
        sys.exit()

    if not path.exists():
        print(f"File not found at: {path.absolute()}")
        sys.exit()
        
    df = pd.read_parquet(path)
    return df

def remove_rows_from_parquet(df: pd.DataFrame, row_names):
    df_cleaned = df.drop(row_names, axis='columns', inplace=False)
    return df_cleaned

def save_parquet(file_name: str, df: pd.DataFrame):
    target_file = f"{file_name}.parquet"

    df.to_parquet(target_file, engine='pyarrow', compression='snappy', index=False)
    print("Parquet saved to: " + target_file)

def file_information(df: pd.DataFrame, file_name: str, join_stats=None):
    info_file = f"{file_name}_metadata.txt"
    with open(info_file, 'w', encoding='utf-8') as f:
        f.write(f"REPORT: METADATA FOR {file_name.upper()}\n")
        f.write("="*80 + "\n")
        f.write(f"Created on:       {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total Rows:       {len(df)}\n")
        f.write(f"Total Columns:    {len(df.columns)}\n")
        f.write("-" * 80 + "\n")
        
        # Header für die Tabelle
        header = f"{'Column Name':<30} | {'Type':<12} | {'Missing':<8} | {'Distinct':<8} | {'Unique %':<8}"
        f.write(header + "\n")
        f.write("-" * 80 + "\n")
        
        for col in df.columns:
            # Metriken berechnen
            null_count = df[col].isnull().sum()
            dtype = str(df[col].dtype)
            distinct_count = df[col].nunique()
            
            # Uniqueness % berechnen (wie viel % der nicht-leeren Werte sind einzigartig)
            total_non_null = len(df) - null_count
            uniqueness_pct = (distinct_count / total_non_null * 100) if total_non_null > 0 else 0
            
            # Zeile formatieren
            row = f"{col[:30]:<30} | {dtype:<12} | {null_count:<8} | {distinct_count:<8} | {uniqueness_pct:>7.1f}%"
            f.write(row + "\n")
            
        f.write("-" * 80 + "\n")
        f.write(f"RAM Memory Usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB\n")
        
        if join_stats:
            f.write("="*80 + "\n")
            f.write("ADDITIONAL JOIN STATS:\n")
            for key, value in join_stats.items():
                f.write(f"- {key:<35}: {value}\n")
        
        f.write("="*80 + "\n")
    print(f"Detailed metadata report created: {info_file}")


def extract_answer(df: pd.DataFrame, column_name: str):
    """
    Extrahiert Text aus einer Tiptap-JSON-Struktur und erstellt eine neue Spalte 'cleaned_answer'.
    """
    
    def get_text_recursive(node):
        """Hilfsfunktion, um alle 'text' Felder aus dem Tiptap-JSON zu fischen."""
        if not isinstance(node, dict):
            return ""
        
        text = ""
        # Wenn der Knoten vom Typ 'text' ist, nimm den Inhalt
        if node.get("type") == "text":
            text += node.get("text", "")
        
        # Wenn der Knoten 'content' hat (Liste), geh tiefer
        if "content" in node and isinstance(node["content"], list):
            for child in node["content"]:
                text += get_text_recursive(child)
        
        # Zeilenumbruch für Paragraphs oder ListItems hinzufügen, damit es lesbar bleibt
        if node.get("type") in ["paragraph", "listItem", "heading"]:
            text += "\n"
        elif node.get("type") == "hardBreak":
            text += "\n"
            
        return text

    def process_row(json_str):
        if not json_str or pd.isna(json_str):
            return ""
        try:
            # Falls es bereits ein Dict ist, nicht laden, sonst parsen
            data = json.loads(json_str) if isinstance(json_str, str) else json_str
            # Starte die rekursive Textextraktion
            cleaned = get_text_recursive(data)
            # Entferne doppelte Zeilenumbrüche am Ende
            return cleaned.strip()
        except Exception as e:
            print("something went wrong in extract answer function")
            sys.exit()

    # Neue Spalte erstellen
    df['cleaned_answer'] = df[column_name].apply(process_row)
    return df

def extract_question_details(df: pd.DataFrame, column_name: str):
    """
    Extrahiert Question, Rubric und Examples aus der komplexen Question-JSON-Struktur.
    Erstellt drei neue Spalten.
    """
    
    def get_text_recursive(node):
        if not isinstance(node, dict):
            return ""
        text = ""
        if node.get("type") == "text":
            text += node.get("text", "")
        if "content" in node and isinstance(node["content"], list):
            for child in node["content"]:
                text += get_text_recursive(child)
        if node.get("type") in ["paragraph", "listItem", "heading"]:
            text += "\n"
        elif node.get("type") == "hardBreak":
            text += "\n"
        return text

    def process_row(json_str):
        # Fallback für leere Zeilen
        res = {"q": "", "r": "", "e": ""}
        if not json_str or pd.isna(json_str):
            return pd.Series(res)
        
        try:
            data = json.loads(json_str) if isinstance(json_str, str) else json_str
            
            # 1. Eigentliche Fragestellung (aus 'content')
            res["q"] = get_text_recursive(data.get("content", {})).strip()
            
            # 2. Rubrik / Bewertungskriterien (aus 'rubric')
            res["r"] = get_text_recursive(data.get("rubric", {})).strip()
            
            # 3. Beispiele (Liste von Objekten mit 'content' und 'accuracy')
            example_list = data.get("examples", [])
            example_texts = []
            for i, ex in enumerate(example_list, 1):
                content_text = get_text_recursive(ex.get("content", {})).strip()
                acc = ex.get("accuracy", "N/A")
                example_texts.append(f"Ex {i} (Acc: {acc}): {content_text}")
            
            res["e"] = "\n---\n".join(example_texts)
            
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            print(error_msg)
            sys.exit()
            
        return pd.Series(res)

    # Wir wenden die Funktion an und expandieren das Ergebnis in 3 Spalten
    new_cols = df[column_name].apply(process_row)
    df['cleaned_question'] = new_cols['q']
    df['cleaned_rubric'] = new_cols['r']
    df['cleaned_examples'] = new_cols['e']
    
    return df

def extract_model_prediction(df: pd.DataFrame, column_name: str):
    """
    Extrahiert Text aus der Tiptap-Struktur der Model-Prediction.
    Erstellt eine neue Spalte 'cleaned_prediction'.
    """
    def get_text_recursive(node):
        if not isinstance(node, dict):
            return ""
        text = ""
        if node.get("type") == "text":
            text += node.get("text", "")
        if "content" in node and isinstance(node["content"], list):
            for child in node["content"]:
                text += get_text_recursive(child)
        if node.get("type") in ["paragraph", "listItem", "heading"]:
            text += "\n"
        elif node.get("type") == "hardBreak":
            text += "\n"
        return text

    def process_row(json_str):
        if not json_str or pd.isna(json_str):
            return ""
        try:
            data = json.loads(json_str) if isinstance(json_str, str) else json_str
            # Da model_prediction direkt das doc-Objekt ist (wie answer):
            cleaned = get_text_recursive(data)
            return cleaned.strip()
        except Exception as e:
            print("something went wrong ub extract model prediction function")
            sys.exit()

    df['cleaned_model_prediction'] = df[column_name].apply(process_row)
    return df

def extract_model_metadata_router(df: pd.DataFrame, column_name: str):
    """Erweiterter Router für Flash, Pro, GPT und Qwen."""
    
    def process_row(json_str):
        if not json_str or pd.isna(json_str):
            return pd.Series([None]*5)
            
        try:
            data = json.loads(json_str) if isinstance(json_str, str) else json_str
            
            # Identifikation über verschiedene Felder
            model_info = str(data.get("response", {}).get("modelId", "")).lower()
            provider = str(data.get("providerMetadata", {}).get("gateway", {}).get("routing", {}).get("finalProvider", "")).lower()
            
            # SWITCH-LOGIK
            if "qwen" in model_info or "cerebras" in provider:
                result = extract_json_qwen(data)
            elif "gpt" in model_info or "openai" in provider:
                result = extract_json_gpt(data)
            elif "pro" in model_info:
                result = extract_json_gemini_pro(data)
            else:
                # Fallback für Flash und alles andere
                result = extract_json_gemini_flash(data)
                
            return pd.Series([
                result["input_tokens"],
                result["inference_duration_ms"],
                result["prompt"],
                result["reasoning"]
            ])
        except Exception:
            return pd.Series([None]*5)

    new_cols = ["input_tokens", "inference_duration_ms", "prompt", "reasoning"]
    df[new_cols] = df[column_name].apply(process_row)
    return df

def extract_json_gemini_flash(data):
    """Spezialisierte Extraktion für Gemini Flash."""
    res = {"input_tokens": None, "inference_duration_ms": None, "prompt": "", "temperature": None, "reasoning": ""}
    
    # 1. Tokens (Ähnlich wie Pro, aber oft andere Keys)
    usage = data.get("providerMetadata", {}).get("google", {}).get("usageMetadata", {})
    res["input_tokens"] = usage.get("promptTokenCount")
    
    # 2. Zeit
    attempts = data.get("providerMetadata", {}).get("gateway", {}).get("routing", {}).get("attempts", [])
    if attempts:
        res["inference_duration_ms"] = attempts[0].get("endTime", 0) - attempts[0].get("startTime", 0)
        
    # 3. Request
    req_body = data.get("request", {}).get("body", {})
    
    # Prompt
    prompt_list = req_body.get("prompt", [])
    # Flash nutzt oft eine Liste von Objekten mit "text"
    res["prompt"] = " | ".join([str(p.get("content", "")) for p in prompt_list])
    
    # 4. Reasoning
    # Auch Flash kann Reasoning enthalten (siehe dein Beispiel)
    content_list = data.get("response", {}).get("body", {}).get("content", [])
    res["reasoning"] = "\n".join([c.get("text", "") for c in content_list if c.get("type") == "reasoning"]).strip()
    
    return res
                              
def extract_json_gemini_pro(data):
    """Spezialisierte Extraktion für Gemini Pro (Vertex/Gateway)."""
    res = {"input_tokens": None, "inference_duration_ms": None, "prompt": "", "temperature": None, "reasoning": ""}
    
    # 1. Tokens (Liegen tief in usageMetadata)
    google_meta = data.get("providerMetadata", {}).get("google", {})
    usage = google_meta.get("usageMetadata", {})
    # Pro nutzt oft promptTokenCount
    res["input_tokens"] = usage.get("promptTokenCount")

    # 2. Dauer (Berechnung aus Gateway-Logs)
    attempts = data.get("providerMetadata", {}).get("gateway", {}).get("routing", {}).get("attempts", [])       
    if attempts:
        res["inference_duration_ms"] = attempts[0].get("endTime", 0) - attempts[0].get("startTime", 0)

    # 3. Request Details
    req_body = data.get("request", {}).get("body", {})
    
    # Prompt Extraktion (Hole Text aus dem verschachtelten Array)
    prompts = req_body.get("prompt", [])
    if isinstance(prompts, list):
        text_parts = []
        for p in prompts:
            content = p.get("content", "")
            # Manchmal ist content eine Liste von Dicts mit "text"
            if isinstance(content, list):
                text_parts.append(" ".join([c.get("text", "") for c in content if isinstance(c, dict)]))
            else:
                text_parts.append(str(content))
        res["prompt"] = " | ".join(text_parts)

    # 4. Reasoning (Speziell für Gemini Pro / Thought-Modelle)
    # In deinem JSON liegt das Reasoning in response -> body -> content
    content_list = data.get("response", {}).get("body", {}).get("content", [])
    res["reasoning"] = "\n".join([c.get("text", "") for c in content_list if c.get("type") == "reasoning"]).strip()
    
    return res
                              
def extract_json_gpt(data):
    """Spezialisierte Extraktion für OpenAI/GPT Formate über das Gateway."""
    res = {"input_tokens": None, "inference_duration_ms": None, "prompt": "", "temperature": None, "reasoning": ""}
    
    # 1. Tokens (OpenAI Struktur)
    usage = data.get("usage", {})
    res["input_tokens"] = usage.get("inputTokens") or usage.get("prompt_tokens")

    # 2. Dauer (Gateway-Logik bleibt meist gleich)
    attempts = data.get("providerMetadata", {}).get("gateway", {}).get("routing", {}).get("attempts", [])  
    if attempts:
        res["inference_duration_ms"] = attempts[0].get("endTime", 0) - attempts[0].get("startTime", 0)

    # 3. Request Details (Temperature & Prompt)
    request_body = data.get("request", {}).get("body", {})
    
    prompt_data = request_body.get("prompt", [])
    if isinstance(prompt_data, list):
        # Sammelt Texte aus den Rollen (system, user, assistant)
        res["prompt"] = " | ".join([str(m.get("content", "")) for m in prompt_data])

    # 4. Reasoning (Speziell für GPT-5 / o1 Modelle)
    # GPT legt das Reasoning oft in das content-Array der Response
    content_list = data.get("response", {}).get("body", {}).get("content", [])
    reasoning_parts = []
    for item in content_list:
        if item.get("type") == "reasoning":
            # Falls das Feld 'text' vorhanden ist (wie in deinem GPT-JSON)
            reasoning_parts.append(item.get("text", ""))
    
    res["reasoning"] = "\n".join(reasoning_parts).strip()
    
    return res

def extract_json_qwen(data):
    """Spezialisierte Extraktion für Alibaba Qwen Modelle via Cerebras/Gateway."""
    res = {"input_tokens": None, "inference_duration_ms": None, "prompt": "", "temperature": None, "reasoning": ""}
    
    # 1. Tokens (Cerebras/Gateway Struktur)
    usage = data.get("usage", {})
    res["input_tokens"] = usage.get("inputTokens")

    # 2. Dauer (Berechnung aus startTime/endTime des Cerebras-Attempts)
    attempts = data.get("providerMetadata", {}).get("gateway", {}).get("routing", {}).get("attempts", [])  
    if attempts:
        # Die Zeitangaben bei Cerebras sind oft sehr präzise Floats
        res["inference_duration_ms"] = attempts[0].get("endTime", 0) - attempts[0].get("startTime", 0)

    request_body = data.get("request", {}).get("body", {})
    
    # Prompt-Extraktion aus dem Message-Array
    prompt_data = request_body.get("prompt", [])
    if isinstance(prompt_data, list):
        res["prompt"] = " | ".join([str(m.get("content", "")) for m in prompt_data])

    # 4. Reasoning
    # Qwen-Modelle (außer spezielle Coder/Math-Varianten) liefern oft reinen Text.
    # Wir prüfen trotzdem, ob das Gateway 'reasoning' Inhalte mitgeliefert hat.
    content_list = data.get("response", {}).get("body", {}).get("content", [])
    reasoning_text = ""
    for item in content_list:
        if item.get("type") == "reasoning":
            reasoning_text += item.get("text", "")
    
    res["reasoning"] = reasoning_text.strip()
    
    return res
                              
def version_0_2():
    path = Path("v0.16.parquet")

    #drop json tables of answers, questions, model_prediciton 
    df = open_parquet_file(path)

    row_names = ["answer", "question", "model_prediction", "model_response_with_metadata"]

    df = remove_rows_from_parquet(df, row_names)

    #reorder columns
    new_order = ['cleaned_question', 'cleaned_rubric', 'cleaned_examples', 'used_rubric', 'used_examples', 'cleaned_answer', 'accuracy', 'cleaned_model_prediction', 'used_model', 
                 'input_tokens', 'inference_duration_ms', 'prompt', 'reasoning']

    df = df[new_order]

    #rename columns
    df = df.rename(columns={
        'cleaned_question': 'question',
        'cleaned_rubric': 'rubric',
        'cleaned_examples': 'examples',
        'cleaned_answer': 'answer',
        'cleaned_model_prediction': 'feedback'
    })

    save_path = Path("v0.2")

    save_parquet(save_path, df)

    file_information(df, "v0.2")

def version_0_16():
    path = Path("v0.15.parquet")

    df = open_parquet_file(path)

    df = extract_model_metadata_router(df, "model_response_with_metadata")

    save_path = Path("v0.16")

    save_parquet(save_path, df)

    file_information(df, "v0.16")

def version_0_15():
    path = Path("v0.14.parquet")

    df = open_parquet_file(path)

    row_names = ["rating", "comment"]

    df = remove_rows_from_parquet(df, row_names)

    save_path = Path("v0.15")

    save_parquet(save_path, df)

    file_information(df, "v0.15")

def version_0_14():
    path = Path("v0.13.parquet")

    df = open_parquet_file(path)

    extract_model_prediction(df, "model_prediction")

    save_path = Path("v0.14")

    save_parquet(save_path, df)

    file_information(df, "v0.14")

def version_0_13():
    path = Path("v0.12.parquet")

    df = open_parquet_file(path)

    extract_question_details(df, "question")

    save_path = Path("v0.13")

    save_parquet(save_path, df)

    file_information(df, "v0.13")

def version_0_12():
    path = Path("v0.11.parquet")

    df = open_parquet_file(path)

    extract_answer(df, "answer")

    save_path = Path("v0.12")

    save_parquet(save_path, df)

    file_information(df, "v0.12")

def version_0_11():
    BASE_DIR = Path(__file__).resolve().parent

    path = BASE_DIR / ".." / "v0_1" / "v0.1_stable.parquet"

    df = open_parquet_file(path)

    row_names = ["member_id", "subject_id", "answer_id", "question_id", "grading_id"]

    df = remove_rows_from_parquet(df, row_names)

    save_path = Path("v0.11")

    save_parquet(save_path, df)

    file_information(df, "v0.11")

def main():
    #version 0.11 - drop unecessary tables
    version_0_11()

    #version 0.12 - extract answers out from json
    version_0_12()

    #version 0.13 - extract question out from json
    version_0_13()

    #version 0.14 - extract model prediction from json
    version_0_14()

    #version 0.15 - drop rating and comment
    version_0_15()

    #version 0.16 - extract for each model the api meta data and save them in tables
    version_0_16()

    #version 0.2 - reodering, renaming, dropping columns, etc.
    version_0_2()

main()
