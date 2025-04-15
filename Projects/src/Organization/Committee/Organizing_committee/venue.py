class Venue:
    _name: str
    _address: str
    _capacity: int

    def __init__(self, name, address, capacity):
        self._name = name
        self._address = address
        self._capacity = capacity

    def __str__(self):
        return (f"Место проведения: {self._name}\n"
                f"Адрес: {self._address}\n"
                f"Вместимость: {self._capacity} человек")
