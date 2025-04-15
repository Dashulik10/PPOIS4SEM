class Person:

    MIN_AGE = 18
    MAX_AGE = 100
    _first_name: str
    _second_name: str
    _age: int
    _email: str

    def __init__(self,*, first_name, second_name, age, email):
        self._first_name = first_name
        self._second_name = second_name
        self._age = age
        self._email = email

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        if len(first_name) <= 15:
            self._first_name = first_name
        else:
            raise ValueError("Имя слишком длинное.")

    @property
    def second_name(self):
        return self._second_name

    @second_name.setter
    def second_name(self, second_name: str):
        if len(second_name) <= 15:
            self._second_name = second_name
        else:
            raise ValueError("Фамилия слишком длинная.")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        if Person.MIN_AGE <= age <= Person.MAX_AGE:
            self._age = age
        else :
            raise ValueError("Неверный формат возраста.")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email: str) -> None:
        if "@" in email:
            self._email = email
        else:
            raise ValueError("Неверный формат email.")

    def __str__(self):
        return (f"Имя: {self._first_name}\n"
                f"Фамилия: {self._second_name}\n"
                f"Возраст: {self._age}\n"
                f"Почта для связи: {self._email}\n")

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "second_name": self.second_name,
            "age": self.age,
            "email": self.email,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            first_name=data["first_name"],
            second_name=data["second_name"],
            age=data["age"],
            email=data["email"],
        )
