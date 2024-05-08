class Person:
    
    def __init__(self, name: str, surname: str, ssn: str, birth_date: str, bitrh_place: str, gender: str) -> None:
        """
        This function inizialize an object of Person with
        input: name: str, surname: str, ssn: str
        return: self._name: str
        """
        self._name: str = name
        self._surname: str = surname
        self._ssn: str = ssn
        self._birth_date: str = birth_date
        self._bitrh_place: str = bitrh_place
        self._gender: str = gender


    def get_name(self) -> str:
        """
        This function return a person's name
        input: None
        return: self._name: str
        """
        return self._name

    def set_name(self, new_name: str) -> None:
        """
        This function set the attribute name
        input: name: str
        return: None
        """
        raise Exception("you cannot modify the name!")
    
    def get_surname(self) -> str:
        """
        This function return a person's surname
        input: None
        return: self._surname: str
        """
        return self._surname
    
    def set_surname(self) -> None:
        """
        this functon set a person's surname
        input: surname: str
        return: None
        """
        raise Exception("you cannot modify the surname!")
    
    def get_snn(self) -> str:
        """
        This function return a person's ssn
        input: None
        return: self._snn: str
        """
        return self._snn
    
    def set_snn(self, new_snn: str) -> None:
        """
        This function set the ssn
        input: new_snn: str
        return: None
        """
        raise Exception("you cannot modify the ssn number!")
    

    def check_ssn(self, ssn: str) -> bool:
        return True
    def compute_ssn(self) -> str:
        ssn: str = ""
        return ssn
    
mese: dict = {
    "01" : "A",
    "02" : "B",
    "03" : "C",
    "04" : "D",
    "05" : "E",
    "06" : "H",
    "07" : "L",
    "08" : "M",
    "09" : "P",
    "10" : "R",
    "11" : "S",
    "12" : "T"
}
   
person_1 = Person("Lorenzo", "Colitto", "LNZCLT")
person_2 = Person("Leonardo", "Brussani", "LNDBRS")
person_3 = Person("Angelo", "Carini", "NGLCRN")
person_4 = Person("Giuseppe", "Rossi", "GSPRSS")
queue: list[Person] = [person_1, person_2, person_3, person_4]

print(str(person_1))
                        
for x in queue:
    print(x.get_name())                        
                        
                        
                        
                        
                        
