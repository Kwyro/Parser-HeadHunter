import requests
import json

class Parser():
    __experience = ["noExperience", "between1And3", "between3And6", "moreThan6"]
    __url = "https://api.hh.ru/vacancies"

    def __init__(self, name: str, exp: int) -> None:
        self.name = name
        self.exp = exp

        self.__responce = requests.get(self.__url, params={"clusters": True,
                                         "per_page": 100,
                                         "text": self.name,
                                         "search_field": "name",
                                         "experience": self.__experience[self.exp],
                                         "only_with_salary": True}).json()
    
    def get_salary(self):
        salary_list = []

        __items = self.__responce["items"]

        for vacancy in __items:
            salary = vacancy["salary"]
            
            if salary["from"] != None and salary["currency"] == "RUR":
                salary_list.append(salary["from"])

            if salary["to"] != None and salary["currency"] == "RUR":
                salary_list.append(salary["to"])

        return salary_list
    
    def get_average_salary(self):
        salary = self.get_salary()

        return sum(salary) // len(salary)
    
UX1 = Parser("Backend разработчик", 2)

print(UX1.get_salary(), UX1.get_average_salary(), sep='\n')
