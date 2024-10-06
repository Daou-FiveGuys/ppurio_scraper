class DataClass():
    def __init__(self) -> None:
        self.__title : str
        self.__type : str
        self.__answer : str 
        self.__link : str
    
    #getter
    @property 
    def title(self) -> str:
        return self.__title
    
    #setter
    @title.setter 
    def title(self, title):
        self.__title = title

    #getter
    @property 
    def type(self) -> str:
        return self.__type
    
    #setter
    @type.setter 
    def type(self, type):
        self.__type = type
    
    #getter
    @property   
    def answer(self) -> str:
        return self.__answer
    
    #setter
    @answer.setter 
    def answer(self, answer):
        self.__answer = answer
    
    #getter
    @property 
    def link(self) -> str:
        return self.__link
    
    #setter
    @link.setter 
    def link(self, link):
        self.__link = link

    # method to return the object as a dictionary
    def to_dict(self) -> dict:
        return {
            "title": self.__title,
            "type": self.__type,
            "answer": self.__answer,
            "link": self.__link
        }