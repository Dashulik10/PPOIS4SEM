from Projects.src.Person.person import Person
from Projects.src.Person.Organizer.organizer import Organizer
from Projects.src.Person.Speaker.speaker import Speaker
from Projects.src.Person.Speaker.report import Report
import unittest
import datetime

class TestPerson(unittest.TestCase):

    def test_constructor_invalid_data(self):
        with self.assertRaises(ValueError):
            person = Person(first_name="VeryLongFirstNameExceeding15Chars", second_name="Ivanov", age=25, email="test@test.com")
            person.first_name = "VeryLongFirstNameExceeding15Chars"

        with self.assertRaises(ValueError):
            person = Person(first_name="VeryLongFirstNameExceeding15Chars", second_name="Ivanov", age=25, email="test@test.com")
            person.second_name = "VeryLongFirstNameExceeding15Chars"

        with self.assertRaises(ValueError):
            person = Person(first_name="Victor", second_name="Ivanov", age=12, email="test@test.com")
            person.age = 120

        with self.assertRaises(ValueError):
            person = Person(first_name="Victor", second_name="Ivanov", age=25, email="invalid-email")
            person.email = "invalid-email"

    def test_str_method(self):
        person = Person(
            first_name="Victor",
            second_name="Ivanov",
            age=30,
            email="victor.ivanov@gmail.com"
        )

        expected_output = (
            "Имя: Victor\n"
            "Фамилия: Ivanov\n"
            "Возраст: 30\n"
            "Почта для связи: victor.ivanov@gmail.com\n"
        )

        self.assertEqual(str(person), expected_output)

    def test_age_getter_setter(self):
        person = Person(
            first_name="Victor",
            second_name="Ivanov",
            age=20,
            email="victor.ivanov@gmail.com"
        )

        self.assertEqual(person.age, 20)

        person.age = 30
        self.assertEqual(person.age, 30)

        with self.assertRaises(ValueError):
            person.age = 5

        with self.assertRaises(ValueError):
            person.age = 150

class TestOrganizer(unittest.TestCase):
    def test_constructor(self):
        organizer = Organizer(
            first_name="Victor",
            second_name="Ivanov",
            age=25,
            email="victor.ivanov@gmail.com",
            area_of_expertise=1,
            experience=2
        )

        organizer.area_of_expertise = 1
        organizer.experience = 2

        self.assertEqual(organizer.first_name, "Victor")
        self.assertEqual(organizer.second_name, "Ivanov")
        self.assertEqual(organizer.age, 25)
        self.assertEqual(organizer.email, "victor.ivanov@gmail.com")
        self.assertEqual(organizer.experience, 2)
        self.assertEqual(organizer.area_of_expertise, "Представитель государственной организации")

    def test_str_method(self):
        organizer = Organizer(
            first_name="Victor",
            second_name="Ivanov",
            age=30,
            email="victor.ivanov@gmail.com",
            area_of_expertise=1,
            experience=2
        )

        expected_output = (
            "Имя: Victor\n"
            "Фамилия: Ivanov\n"
            "Возраст: 30\n"
            "Почта для связи: victor.ivanov@gmail.com\n"
            "Рабочая область: 1\n"
        )

        self.assertEqual(str(organizer), expected_output)

class TestSpeaker(unittest.TestCase):
    def test_constructor(self):
        report = Report(
            name_of_report="ыолплокпу",
            date_of_report=2021 - 12 - 12,
            annotation="bla bla bla"
        )

        report.name_of_report="ыолплокпу"
        date_of_report = 2021 - 12 - 12,
        report.annotation="bla bla bla"

        expected_output = (
            "Название доклада: ыолплокпу\n"
            "Тема доклада: Тема не указана\n"
            "Дата публикации: 1997\n"
            "Аннотация:\nbla bla bla\n"
        )

        # Проверяем корректность метода __str__
        self.assertEqual(str(report), expected_output)

        speaker = Speaker(
            first_name="Victor",
            second_name="Ivanov",
            age=25,
            email="victor.ivanov@gmail.com",
            area_of_expertise=1,
            report=report
        )


        speaker.area_of_expertise = 1


        self.assertEqual(speaker.first_name, "Victor")
        self.assertEqual(speaker.second_name, "Ivanov")
        self.assertEqual(speaker.age, 25)
        self.assertEqual(speaker.email, "victor.ivanov@gmail.com")
        self.assertEqual(speaker.area_of_expertise, 1)
        self.assertEqual(speaker.report, report)

    def test_str_method(self):
        speaker = Speaker(
            first_name="Victor",
            second_name="Ivanov",
            age=25,
            email="victor.ivanov@gmail.com",
            area_of_expertise=1,
            report=None
        )


        expected_output = (
            "Докладчик: Victor Ivanov\n"
            "Возраст: 25\n"
            "Почта: victor.ivanov@gmail.com\n"
            "None"
        )

        self.assertEqual(str(speaker), expected_output)



if __name__ == "__main__":
    unittest.main()
