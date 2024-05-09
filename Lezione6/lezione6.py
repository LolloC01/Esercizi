import string

class Person:

    def __init__(self, name: str, surname: str, birth_date: str, bitrh_place: str, gender: str) -> None:
        """
        This function inizialize an object of Person with
        input: name: str, surname: str, birth_date: str, bitrh_place: str, gender: str (M o F)
        return: None
        """
        self._name: str = name
        self._surname: str = surname
        self._birth_date: str = birth_date
        self._bitrh_place: str = bitrh_place
        self._gender: str = gender
        self._ssn: str = self.compute_ssn()


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
        return self._ssn

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
        con = "BCDFGHJKLMNPQRSTVWXYZ"
        ssn: str = ""
        if len(self._surname) > 3:
            st = self._surname
            cons = ""
            voc = ""
            for x in st.upper():
                if x in con:
                    cons += x
                else:
                    voc += x
            if len(cons) >= 3:
                cons = cons[:3]
            else:
                x = 0
                while len(cons) < 3:
                    cons += voc[x]
                    x += 1
            ssn += cons
        else:
            ssn += self._surname
            while len(ssn) < 3:
                ssn += "X"
        
        if len(self._name) > 3:
            st = self._name
            cons = ""
            voc = ""
            for x in st.upper():
                if x in con:
                    cons += x
                elif x in "AEIOU":
                    voc += x
            if len(cons) >= 4:
                cons = cons[:1] + cons[2:4]
            else:
                x = 0
                while len(cons) < 3:
                    cons += voc[x]
                    x += 1
            ssn += cons
        else:
            ssn += self._name
            while len(ssn) < 6:
                ssn += "X"
        
        ssn += self._birth_date[-2:]
        ssn += mese[self._birth_date[3:5]]
        if self._gender == "M":
            ssn += self._birth_date[:2]
        else:
            x = int(self._birth_date[:2])+40
            ssn += str(x)
        ssn += codici_catastali_capoluoghi[self._bitrh_place.upper()]
        n = n1 = 0
        ssn = ssn.upper()
        for x in range(len(ssn)):
            if x % 2 == 0:
                print(f"{ssn[x]}--------numero dispari")
                print(f"{caratteri_alfanumerici_dispar[ssn[x]]}----dispari")
                n += caratteri_alfanumerici_dispar[ssn[x]]
            else:
                print(f"{ssn[x]}--------numero pari")
                print(f"{caratteri_alfanumerici_pari[ssn[x]]}----pari")
                n += caratteri_alfanumerici_pari[ssn[x]]
        n1 = n % 26
        print(f"{n1}----resto di {n}----{resto_lettera[n1]}")
        ssn += resto_lettera[n1]
        return ssn


import csv
def get_cod_catastale(file: str) -> dict:
    cod_cat: dict = {}
    fields: list = []
    rows: list = []
    # reading csv file
    with open(file, 'r') as csvfile:
    # creating a csv reader object
        csvreader = csv.reader(csvfile)
 
    # extracting field names through first row
        fields = next(csvreader)
        
    # extracting each data row one by one
        for row in csvreader:
            rows.append(row[0].split(";"))
    for x in rows:
        x[1] = x[1].strip('"')
        x[2] = x[2].strip('"')
        cod_cat[x[1]] = x[2]

    return cod_cat

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
caratteri_alfanumerici_pari = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    'K': 10,
    'L': 11,
    'M': 12,
    'N': 13,
    'O': 14,
    'P': 15,
    'Q': 16,
    'R': 17,
    'S': 18,
    'T': 19,
    'U': 20,
    'V': 21,
    'W': 22,
    'X': 23,
    'Y': 24,
    'Z': 25
}
caratteri_alfanumerici_dispar = {
    '0': 1,
    '1': 0,
    '2': 5,
    '3': 7,
    '4': 9,
    '5': 13,
    '6': 15,
    '7': 17,
    '8': 19,
    '9': 21,
    'A': 1,
    'B': 0,
    'C': 5,
    'D': 7,
    'E': 9,
    'F': 13,
    'G': 15,
    'H': 17,
    'I': 19,
    'J': 21,
    'K': 2,
    'L': 4,
    'M': 18,
    'N': 20,
    'O': 11,
    'P': 3,
    'Q': 6,
    'R': 8,
    'S': 12,
    'T': 14,
    'U': 16,
    'V': 10,
    'W': 22,
    'X': 25,
    'Y': 24,
    'Z': 23
}
codici_catastali_capoluoghi = get_cod_catastale("/home/user/VScodeProjects/Esercizi/Lezione6/gi_comuni_nazioni_cf.csv")
resto_lettera = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'E',
    5: 'F',
    6: 'G',
    7: 'H',
    8: 'I',
    9: 'J',
    10: 'K',
    11: 'L',
    12: 'M',
    13: 'N',
    14: 'O',
    15: 'P',
    16: 'Q',
    17: 'R',
    18: 'S',
    19: 'T',
    20: 'U',
    21: 'V',
    22: 'W',
    23: 'X',
    24: 'Y',
    25: 'Z'
}


           