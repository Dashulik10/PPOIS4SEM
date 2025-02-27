from Projects.src.Person.person import Person

class Organizer(Person):

    def __init__(self, *, first_name, second_name, age, email,
                 area_of_expertise, experience):
        super().__init__(
            first_name=first_name,
            second_name=second_name,
            age=age,
            email=email)

        self._area_of_expertise = area_of_expertise



    @property
    def area_of_expertise(self):
        return self._area_of_expertise

    @area_of_expertise.setter
    def area_of_expertise(self, num):
        areas = {
            1: "Представитель государственной организации",
            2: "Специалист по аппаратуре",
            3: "Ведущий",
            4: "Организатор досуга"
        }
        if num in areas:
            self._area_of_expertise = areas[num]
        else:
            raise ValueError("Некорректный номер области")


    def __str__(self):
        return (f"Имя: {self._first_name}\n"
                f"Фамилия: {self._second_name}\n"
                f"Возраст: {self._age}\n"
                f"Почта для связи: {self._email}\n"
                f"Рабочая область: {self._area_of_expertise}\n"
                )

