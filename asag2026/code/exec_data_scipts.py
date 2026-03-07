import subprocess
import sys
import time
from pathlib import Path

scripts = [
    "v0_1/v0_1.py",
    "v0_2/v0_2.py",
]

def run_pipeline():
    start_total = time.time()
    
    for script_path in scripts:
        script = Path(script_path)
        
        if not script.exists():
            print(f"File not found: {script.absolute()}")
            sys.exit(1)

        print(f"\nStarts: {script.name}...")
        start_script = time.time()
        
        result = subprocess.run(
            [sys.executable, script.name],
            cwd=script.parent
        )
        
        duration = time.time() - start_script

        if result.returncode == 0:
            print(f"{script.name} finished in {duration:.2f}s")
        else:
            print(f"Error in {script.name} (Exit Code: {result.returncode})")
            sys.exit(1)

    total_duration = time.time() - start_total
    print(f"\nPipeline succesfull in {total_duration:.2f}s")

if __name__ == "__main__":
    run_pipeline()