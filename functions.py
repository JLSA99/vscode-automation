#Learning from scratch with Claude

import subprocess
def open_vscode():
    """Open a new VS code window."""
    subprocess.run("code", shell=True)

def open_file_in_vscode(file_path):
    """Open a specific file in VS code"""
    subprocess.run(f'code "{file_path}"',shell=True)

def open_folder_in_vscode(folder_path):
    """Opens a folder in VS Code."""
    subprocess.run(f'code "{folder_path}"', shell=True)

def list_installed_extensions():
    """Prints the extensions installed in VS Code."""
    result = subprocess.run("code --list-extensions", shell=True,
                            capture_output=True, text=True)

    print(result.stdout)