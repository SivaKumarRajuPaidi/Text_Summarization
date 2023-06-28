import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "textsummarizer"

list_of_files = [
    ".github.com/workflows/gitkeep",
    f"scr/{project_name}/__init__.py",
    f"scr/{project_name}/components/__init__.py",
    f"scr/{project_name}/utils/__init__.py",
    f"scr/{project_name}/utils/common.py",
    f"scr/{project_name}/logging/__init__.py",
    f"scr/{project_name}/config/__init__.py",
    f"scr/{project_name}/config/configuration.py",
    f"scr/{project_name}/pipeline/__init__.py",
    f"scr/{project_name}/entity/__init__.py",
    f"scr/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "parms.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
]

for filepath in list_of_files:
    file_path = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for file: {filename}")

    if (not file_path.exists()) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Created empty file: {filepath}")

    else:
            logging.info(f"File already exists: {filepath}")