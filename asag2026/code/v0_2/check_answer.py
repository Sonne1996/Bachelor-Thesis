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


def main():
    path = Path("v0.12.parquet")
    df = open_parquet_file(path)

    columns = df.get("answer")
    hf = {} # Starten mit einem leeren Dict

    for col in columns:
        if col in hf:
            hf[col] = hf[col] + 1
        else:
            hf[col] = 1

    temp = 0
    unique_multi_count = 0

    for k, v in hf.items():
        if v > 1:
            # v - 1 sind die "überflüssigen" Kopien, die den Unique-Count senken
            temp = temp + (v - 1)
            unique_multi_count += 1

    print(f"Anzahl der Kopien (Differenz): {temp}")
    print(f"Anzahl Texte, die mehrfach vorkommen: {unique_multi_count}")

    # Sortiere das Dict nach Häufigkeit (v)
    sorted_hf = sorted(hf.items(), key=lambda item: item[1], reverse=True)

    print("Top 5 Duplikate:")
    for text, count in sorted_hf[:5]:
        # Wir zeigen nur die ersten 50 Zeichen des Textes
        preview = text.replace('\n', ' ')[:50]
        print(f"Häufigkeit: {count} | Text: {preview}...")
            

main()