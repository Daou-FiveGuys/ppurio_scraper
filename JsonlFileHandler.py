import os
from FAQDataClass import DataClass

class JsonlFileHandler:
    def __init__(self, file_path) -> None:
        self.file_path = file_path
        
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                pass

    def write_data(self, data : list[str]):
        with open(self.file_path, 'a') as f:
            for item in data:
                f.write(f"{item}\n")