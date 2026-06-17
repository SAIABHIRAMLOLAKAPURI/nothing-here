import PyInstaller.__main__
import os
import shutil

def build():
    print("Building Tejodaya Executable...")

    # Define parameters for PyInstaller
    sep = ';' if os.name == 'nt' else ':'
    params = [
        'app.py',
        '--onefile',
        '--name=Tejodaya',
        f'--add-data=tejodaya{sep}tejodaya',
        '--collect-all=sklearn',
        '--collect-all=pandas',
        '--collect-all=flask',
        '--collect-all=webview',
        '--hidden-import=clr', # Common for pywebview on windows
    ]

    PyInstaller.__main__.run(params)

    print("\nBuild complete. The executable can be found in the 'dist' folder.")
    print("Note: To create a Windows .exe, this script must be run on a Windows machine.")

if __name__ == "__main__":
    build()
