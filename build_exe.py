import PyInstaller.__main__
import os
import shutil

def build():
    print("Building JARVIS Executable...")

    # Define parameters for PyInstaller
    sep = ';' if os.name == 'nt' else ':'
    params = [
        'app.py',
        '--onefile',
        '--name=JARVIS',
        f'--add-data=jarvis{sep}jarvis',
        '--collect-all=sklearn',
        '--collect-all=pandas',
        '--collect-all=flask',
    ]

    PyInstaller.__main__.run(params)

    print("\nBuild complete. The executable can be found in the 'dist' folder.")
    print("Note: To create a Windows .exe, this script must be run on a Windows machine.")

if __name__ == "__main__":
    build()
