import os
from FAQDataClass import DataClass

class JsonlFileHandler:
    def __init__(self, file_path) -> None:
        self.file_path = file_path
        
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                pass

    def write_data(self, data : list[DataClass]):
        with open(self.file_path, 'a') as f:
            f.write(f"{data}\n")

    def processing_faq_data(faq_data : DataClass) -> dict :
        #TODO FAQDataClass -> Dict로 변환
        pass