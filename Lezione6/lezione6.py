import string

class Person:

    def __init__(self, name: str, surname: str, birth_date: str, bitrh_place: str, gender: str) -> None:
        """
        This function inizialize an object of Person with
        input: name: str, surname: str, ssn: str
        return: self._name: str
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
        con = "BCDFGHJKLMNPQRSTUVWXYZ"
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
        else:
            ssn += self._surname
            while len(ssn) < 3:
                ssn += "X"
        ssn += cons
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
        else:
            ssn += self._name
            while len(ssn) < 6:
                ssn += "X"
        ssn += cons
        if self._gender == "M":
            ssn += self._birth_date[:2]
        else:
            x = int(self._birth_date[:2])+40
            ssn += str(x)
        ssn += mese[self._birth_date[3:5]]
        ssn += self._birth_date[-2:]
        ssn += codici_catastali_capoluoghi[self._bitrh_place.capitalize()]
        pari_n = dispari_n = 0
        print(ssn)
        for x in range(len(ssn)):
            print(ssn[x])
            print(f"{pari_n}---somma")
            if x % 2 == 0:
                print(f"{caratteri_alfanumerici_pari[ssn[x]]}----pari")
                pari_n += caratteri_alfanumerici_pari[ssn[x]]
            else:
                print(f"{caratteri_alfanumerici_dispar[ssn[x]]}----dispari")
                pari_n += caratteri_alfanumerici_dispar[ssn[x]]
        pari_n = pari_n % 26
        print(pari_n)
        ssn += resto_lettera[pari_n]
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
codici_catastali_capoluoghi = {
    "Agrigento": "A091",
    "Alessandria": "A182",
    "Ancona": "A282",
    "Aosta": "A326",
    "L'Aquila": "A345",
    "Arezzo": "A390",
    "Ascoli Piceno": "A462",
    "Asti": "A479",
    "Avellino": "A509",
    "Bari": "A662",
    "Barletta": "B693",
    "Andria": "A285",
    "Trani": "L331",
    "Belluno": "A757",
    "Benevento": "A783",
    "Bergamo": "A794",
    "Biella": "A861",
    "Bologna": "A944",
    "Bolzano": "A952",
    "Brescia": "B157",
    "Brindisi": "B180",
    "Cagliari": "B354",
    "Caltanissetta": "B426",
    "Campobasso": "B519",
    "Carbonia": "B743",
    "Iglesias": "E281",
    "Caserta": "B963",
    "Catania": "C351",
    "Catanzaro": "C351",
    "Chieti": "C632",
    "Como": "C933",
    "Cosenza": "D086",
    "Cremona": "D150",
    "Crotone": "D189",
    "Cuneo": "D205",
    "Enna": "D406",
    "Fermo": "D540",
    "Ferrara": "D548",
    "Firenze": "D612",
    "Foggia": "D643",
    "Forlì": "D704",
    "Cesena": "C573",
    "Frosinone": "D813",
    "Genova": "D969",
    "Gorizia": "E101",
    "Grosseto": "E199",
    "Imperia": "E293",
    "Isernia": "E338",
    "La Spezia": "E463",
    "Latina": "E472",
    "Lecce": "E506",
    "Lecco": "E509",
    "Livorno": "E625",
    "Lodi": "E644",
    "Lucca": "E717",
    "Macerata": "E783",
    "Mantova": "E899",
    "Massa": "F023",
    "Matera": "F052",
    "Messina": "F158",
    "Milano": "F205",
    "Modena": "F207",
    "Monza": "F704",
    "Napoli": "F839",
    "Novara": "F952",
    "Nuoro": "F979",
    "Oristano": "G113",
    "Padova": "G224",
    "Palermo": "G273",
    "Parma": "G337",
    "Pavia": "G388",
    "Perugia": "G478",
    "Pesaro": "G479",
    "Urbino": "G507",
    "Pescara": "G488",
    "Piacenza": "G563",
    "Pisa": "G702",
    "Pistoia": "G722",
    "Pordenone": "G888",
    "Potenza": "G942",
    "Prato": "G999",
    "Ragusa": "H161",
    "Ravenna": "H199",
    "Reggio Calabria": "H224",
    "Reggio Emilia": "H223",
    "Rieti": "H282",
    "Rimini": "H294",
    "Roma": "H501",
    "Rovigo": "H620",
    "Salerno": "H703",
    "Sassari": "H724",
    "Savona": "H730",
    "Siena": "G741",
    "Siracusa": "I754",
    "Sondrio": "I829",
    "Taranto": "L057",
    "Teramo": "L107",
    "Terni": "L121",
    "Torino": "L219",
    "Trapani": "L331",
    "Trento": "L378",
    "Treviso": "L398",
    "Trieste": "L424",
    "Udine": "L483",
    "Varese": "L682",
    "Venezia": "L736",
    "Verbania": "L741",
    "Vercelli": "L749",
    "Verona": "L781",
    "Vibo Valentia": "L840",
    "Vicenza": "L840",
    "Viterbo": "M082"
}
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
