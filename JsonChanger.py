import json
from FAQDataClass import DataClass

class JsonChanger:
    def __init__(self) -> None:
        pass

    # DataClass 타입을 dict로 변경 후, json으로 변경 
    def to_json(self, datas : list[DataClass]) -> list[str]:
        json_list = []
        for data in datas :
            json_list.append(json.dumps(data.to_dict()))
        return json_list