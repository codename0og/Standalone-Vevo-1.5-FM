import os
import sys
import subprocess

def vevo_execution_handler():
    print("Vevo-1.5 launcher")
    print("---------------------------------------------------")
    print("  Running FM variant model only (Timbre control, for VC/SVC)")
    print("---------------------------------------------------")

    module_name = "infer_vevosing_fm"

    python_exe = sys.executable 
    script_path = f"models.svc.vevosing.{module_name}"

    command = [
        python_exe,
        '-m',
        script_path
    ]
    print(f"\n Running: {' '.join(command)}")

    try:
        subprocess.run(command, check=True)
    except FileNotFoundError:
        print(f"\n Error: Python executable not found (Unexpected, but caught).")
    except subprocess.CalledProcessError as e:
        print(f"\n Error: Script execution failed with return code {e.returncode}.")
    print()

if __name__ == "__main__":
    vevo_execution_handler()