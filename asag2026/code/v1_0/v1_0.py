import pandas as pd
import sys
from pathlib import Path
import datetime

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

def file_information(df: pd.DataFrame, file_name):
    info_file = f"{file_name}_metadata.txt"

def file_information(df: pd.DataFrame, file_name: str, join_stats=None):
    info_file = f"{file_name}_metadata.txt"
    with open(info_file, 'w', encoding='utf-8') as f:
        f.write(f"REPORT: METADATA FOR {file_name.upper()}\n")
        f.write("="*40 + "\n")
        f.write(f"Created on:      {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Entries in result (Rows): {len(df)}\n")
        f.write(f"Columns (Cols):  {len(df.columns)}\n")
        
        if join_stats:
            f.write("-" * 40 + "\n")
            f.write("TABLE SIZES & JOIN ANALYSIS:\n")
            for key, value in join_stats.items():
                f.write(f"- {key:<35}: {value}\n")
        
        f.write("-" * 40 + "\n")
        f.write("COLUMN DETAILS:\n")
        for col in df.columns:
            null_count = df[col].isnull().sum()
            dtype = df[col].dtype
            f.write(f"- {col:<40} | Type: {str(dtype):<10} | Missing: {null_count}\n")
            
        f.write("-" * 40 + "\n")
        f.write(f"RAM Memory Usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB\n")
        f.write("="*40 + "\n")
    print(f"Metadata report created: {info_file}")


def main():
    path = Path("../v0_1/v0.1_stable.parquet")

    df = open_parquet_file(path)

    row_names = ["member_id", "subject_id", "answer_id", "question_id", "grading_id"]

    df = remove_rows_from_parquet(df, row_names)

    path = Path("v1.0")

    save_parquet(path, df)

    file_information(df, "v1.0_stable")

main()
