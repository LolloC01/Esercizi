class Food:
    def __init__(self, name: str, price: float, description: str) -> None:
        self._name = name
        self._price = price
        self._description = description

        # Getter method for name
    def get_name(self) -> str:
        return self._name

    # Setter method for name
    def set_name(self, name: str) -> None:
        self._name = name

    # Getter method for price
    def get_price(self) -> float:
        return self._price

    # Setter method for price
    def set_price(self, price: float) -> None:
        self._price = price

    # Getter method for description
    def get_description(self) -> str:
        return self._description

    # Setter method for description
    def set_description(self, description: str) -> None:
        self._description = description