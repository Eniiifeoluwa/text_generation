import os
from pathlib import Path
project_name = "text_generation"

lists_of_files = [
#f"{project_name}/components", 
f"{project_name}/__init__.py",
f"{project_name}/components/__init__.py",
f"{project_name}/components/model_evaluation.py",
f"{project_name}/components/model_trainer.py",
f"{project_name}/components/data_ingestion.py",
f"{project_name}/pipeline/training_pipeline.py",
f"{project_name}/pipeline/prediction_pipeline.py",
'Dockerfile',
'app.py',
'demo.py',
'requirements.txt'


]


for filepath in lists_of_files:
    filepath = Path(filepath)
    file_dir, filename = os.path.split(filepath)
    if file_dir != '':
        os.makedirs(file_dir, exist_ok= True)
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) ==0):
        with open(filepath, 'w') as r:
            pass
    else:
        print(f'The file already exists at .{filepath}')
