import sys
from datetime import date
from io import StringIO

from Projects.src.Organization import Request
from Projects.src.Organization.Committee.Organizing_committee.venue import Venue
from Projects.src.Organization.Committee.Organizing_committee.organizing_committee import OrganizingCommittee
import unittest

from Projects.src.Organization.Committee.Program_committee.program_committee import ProgramCommittee
from Projects.src.Person.Speaker.report import Report
from Projects.src.Person.person import Person


class TestCommitteee(unittest.TestCase):
    def test_orgCommittee(self):
        venue = Venue(
            name="Hall",
            address="123 Main Street",
            capacity=100
        )

        person = Person(
            first_name="John",
            second_name="Doe",
            age=30,
            email="@"
        )

        orgCommittee = OrganizingCommittee(
            name="OrgCommittee",
            email="<EMAIL>",
            members=set(),
            chairman=None,
            venue=venue
        )

        orgCommittee.name = "OrgCommittee"
        orgCommittee.email = "@ye"
        orgCommittee.members = set()
        orgCommittee.chairman = person
        orgCommittee.venue = venue

        self.assertEqual(orgCommittee.name, "OrgCommittee")
        self.assertEqual(orgCommittee.email, "@ye")
        self.assertEqual(orgCommittee.chairman, person)
        self.assertEqual(orgCommittee.venue, venue)

class TestCommittee(unittest.TestCase):
    def test_org(self):
        venue = Venue(
            name="Hall",
            address="123 Main Street",
            capacity=100
        )
        person1 = Person(
            first_name="John",
            second_name="Doe",
            age=30,
            email="john.doe@example.com"
        )
        person2 = Person(
            first_name="Jane",
            second_name="Smith",
            age=40,
            email="jane.smith@example.com"
        )

        orgCommittee = OrganizingCommittee(
            name="OrgCommittee",
            email="org@example.com",
            members=set(),
            chairman=None,
            venue=venue
        )

        orgCommittee.chairman = person1

        orgCommittee.add_member(person2)
        self.assertEqual(len(orgCommittee.members), 2)

class TestProgr(unittest.TestCase):
    def test_progr(self):
        FIELD_OF_BIOLOGY = {
            "Основы биологии",
            "Генетика и наследственность",
            "Эволюция и происхождение жизни",
            "Зоология (наука о животных)",
            "Ботаника (наука о растениях)",
            "Микробиология",
            "Анатомия и физиология человека",
            "Экология",
            "Биотехнологии и генная инженерия",
            "Биофизика и биохимия"
        }

        FIELD_OF_PHYSICS = {
            "Механика",
            "Молекулярная физика и термодинамика",
            "Электродинамика",
            "Оптика",
            "Квантовая физика",
            "Атомная и ядерная физика",
            "Теория относительности",
            "Физика твердого тела"
        }

        FIELD_OF_LITERATURE = {
            "Теория литературы",
            "Античная литература",
            "Средневековая литература",
            "Эпоха Возрождения",
            "Классицизм, Просвещение",
            "Романтизм",
            "Реализм",
            "Модернизм и авангард",
        }

        LIST_OF_SETS_OF_TOPICS = [FIELD_OF_BIOLOGY, FIELD_OF_PHYSICS, FIELD_OF_LITERATURE]

        self.person = Person(
            first_name="Иван",
            second_name="Иванов",
            age=50,
            email="ivan.ivanov@example.com"
        )

        self.programCommittee = ProgramCommittee(
            name="ProgramCommittee",
            email="program@example.com",
            members=set(),
            chairman=None,
            topics=set()
        )

        self.programCommittee.chairman = self.person

        expected_output = (
            "Программный комитет:\n"
            "Председатель:\n"
            " Имя: Иван\n"
            "Фамилия: Иванов\n"
            "Возраст: 50\n"
            "Почта для связи: ivan.ivanov@example.com\n"
            "Количество членов: 1"
        )
        self.assertEqual(str(self.programCommittee), expected_output)

        self.person1 = Person(
            first_name="Иван",
            second_name="Иванов",
            age=50,
            email="ivan.ivanov@example.com"
        )


        self.programCommittee.add_member(self.person1)
        self.assertEqual(len(self.programCommittee.members), 2)



class TestProgramCommittee(unittest.TestCase):
    def setUp(self):
        self.person1 = Person(
            first_name="John",
            second_name="Doe",
            age=30,
            email="john.doe@example.com"
        )
        self.person2 = Person(
            first_name="Jane",
            second_name="Smith",
            age=35,
            email="jane.smith@example.com"
        )
        self.programCommittee = ProgramCommittee(
            name="ProgramCommittee",
            email="program@example.com",
            members=set(),
            chairman=None,
            topics={"Основы биологии", "Механика"},
        )

    def test_validate_topic(self):
        valid_topic = "Основы биологии"
        invalid_topic = "Некорректная тема"
        self.assertTrue(ProgramCommittee.validate_topic(valid_topic))
        self.assertFalse(ProgramCommittee.validate_topic(invalid_topic))

    def test_get_member_details_no_members(self):
        captured_output = StringIO()
        original_stdout = sys.stdout
        try:
            sys.stdout = captured_output
            self.programCommittee.get_member_details()
        finally:
            sys.stdout = original_stdout

        expected_output = (
            "Информация по всем участникам программного комитета:\n"
            "1. Имя: Иван\n"
            "Фамилия: Иванов\n"
            "Возраст: 50\n"
            "Почта для связи: ivan.ivanov@example.com\n\n"
            "2. Имя: Иван\n"
            "Фамилия: Иванов\n"
            "Возраст: 50\n"
            "Почта для связи: ivan.ivanov@example.com"
        )
        self.assertEqual(captured_output.getvalue().strip(), expected_output)

class TestRequest(unittest.TestCase):
    def test_request(self):
        person = Person(
            first_name="John",
            second_name="Doe",
            age=30,
            email="@"
        )

        report = Report(
            name_of_report="ыолплокпу",
            date_of_report=date(2021, 12, 12),
            annotation="bla bla bla"
        )

        request = Request(
            applicant=person,
            report=report
        )

        request.applicant = person
        request.report = report
        self.assertEqual(request.applicant, person)
        self.assertEqual(request.report, report)

    def test_status_property(self):
        person = Person(
            first_name="Jane",
            second_name="Smith",
            age=35,
            email="jane.smith@example.com"
        )

        report = Report(
            name_of_report="Доклад об экологии",
            date_of_report=date(2023, 11, 18),
            annotation="Влияние человеческой деятельности."
        )

        request = Request(
            applicant=person,
            report=report
        )

        self.assertEqual(request.status, "рассматривается")

        request.status = "принята"
        self.assertEqual(request.status, "принята")

        with self.assertRaises(ValueError):
            request.status = "неизвестно"

    def test_change_status_method(self):
        person = Person(
            first_name="John",
            second_name="Doe",
            age=30,
            email="john.doe@example.com"
        )

        report = Report(
            name_of_report="ИИ и будущее",
            date_of_report=date(2023, 10, 22),
            annotation="Доклад на тему будущего технологий."
        )

        request = Request(
            applicant=person,
            report=report
        )

        request.change_status("принята")
        self.assertEqual(request.status, "принята")

        with self.assertRaises(ValueError):
            request.change_status("неверный статус")

    def test_str_method(self):
        person = Person(
            first_name="Alex",
            second_name="Johnson",
            age=29,
            email="alex.johnson@example.com"
        )

        report = Report(
            name_of_report="Технологии будущего",
            date_of_report=date(2023, 9, 15),
            annotation="Описание грядущих инноваций."
        )

        request = Request(
            applicant=person,
            report=report
        )

        expected_output = (
            "Заявка от: Alex Johnson\n"
            "Доклад: Технологии будущего\n"
            "Статус: рассматривается"
        )
        self.assertEqual(str(request), expected_output)

        request.status = "принята"
        expected_output_after_status_change = (
            "Заявка от: Alex Johnson\n"
            "Доклад: Технологии будущего\n"
            "Статус: принята"
        )
        self.assertEqual(str(request), expected_output_after_status_change)


if __name__ == "__main__":
    unittest.main()