class Animal:
    def __init__(self, name: str, legs: int) -> None:
        self.name: str = name
        self.legs: int = legs
    
    def get_legs(self) -> int:
        return self.legs
    def get_name(self) -> str:
        return self.name
    def set_legs(self, legs) -> None:
        self.legs = legs
    def set_name(self) -> None:
        raise Exception("NON PUOI CAMBIARE NOME")
    
    def print_info(self) -> None:
        print(f"{self.name} ha {self.legs} zampe")