import unittest
from unittest.mock import patch

from Projects.src.Organization import precreation_program_committee, precreation_org_committee
from Projects.src.Organization.Committee.Organizing_committee.organizing_committee import OrganizingCommittee
from Projects.src.Organization.Committee.Organizing_committee.venue import Venue
from Projects.src.Organization.Committee.Program_committee.program_committee import ProgramCommittee
from Projects.src.Organization.Precreation.precreation_chairmans import *
from Projects.src.Person.person import *


class TestPersonFunctions(unittest.TestCase):
    @patch("builtins.input", side_effect=["Иван", "Иванов", "30", "ivan@example.com"])
    def test_set_program_chairman_valid(self, mock_input):
        chairman = set_program_chairman()
        self.assertEqual(chairman.first_name, "Иван")
        self.assertEqual(chairman.second_name, "Иванов")
        self.assertEqual(chairman.age, 30)
        self.assertEqual(chairman.email, "ivan@example.com")

    @patch("builtins.input", side_effect=["Иван", "", "25", "ivan@example.com"])
    def test_set_program_chairman_empty_last_name(self, mock_input):
        chairman = set_program_chairman()
        self.assertEqual(chairman.second_name, "")

    @patch("builtins.input", side_effect=["", "Иванов", "25", "ivan@example.com"])
    def test_set_program_chairman_empty_first_name(self, mock_input):
        chairman = set_program_chairman()
        self.assertEqual(chairman.first_name, "")

    @patch("builtins.input", side_effect=["Алексей", "Смирнов", "25", "alex@example.com"])
    def test_set_org_chairman_valid(self, mock_input):
        chairman = set_org_chairman()
        self.assertEqual(chairman.first_name, "Алексей")
        self.assertEqual(chairman.second_name, "Смирнов")
        self.assertEqual(chairman.age, 25)
        self.assertEqual(chairman.email, "alex@example.com")

    def test_person_invalid_long_first_name(self):
        with self.assertRaises(ValueError) as context:
            person = Person(first_name="Оченьдлинноеимя", second_name="Иванов", age=25, email="ivan@example.com")
            person.first_name = "dfgjkdkhoejkrholgkdfhkd;lrfkh;dnthg"
        self.assertEqual(str(context.exception), "Имя слишком длинное.")

    def test_person_invalid_long_last_name(self):
        with self.assertRaises(ValueError) as context:
            person = Person(first_name="Иван", second_name="", age=25, email="ivan@example.com")
            person.second_name = "flkgjdlkfhjkdjglkssfbhjedrlkgjslrkbjl"
        self.assertEqual(str(context.exception), "Фамилия слишком длинная.")

    def test_person_invalid_age_below_min(self):
        with self.assertRaises(ValueError) as context:
            person = Person(first_name="Иван", second_name="Иванов", age=10, email="ivan@example.com")
            person.age = 0
        self.assertEqual(str(context.exception), "Неверный формат возраста.")

    def test_person_invalid_age_above_max(self):
        with self.assertRaises(ValueError) as context:
            person = Person(first_name="Иван", second_name="Иванов", age=120, email="ivan@example.com")
            person.age = 120
        self.assertEqual(str(context.exception), "Неверный формат возраста.")


class TestPrecreationCommittee(unittest.TestCase):

    @patch("builtins.input", side_effect=["1"])
    def test_precreation_program_committee_valid(self, mock_input):
        committee = precreation_program_committee()
        self.assertIsInstance(committee, ProgramCommittee)
        self.assertSetEqual(
            committee.topics,
            ProgramCommittee.FIELD_OF_BIOLOGY
        )

    @patch("builtins.input", side_effect=["5", "1"])
    def test_precreation_program_committee_invalid(self, mock_input):
        committee = precreation_program_committee()
        self.assertIsInstance(committee, ProgramCommittee)
        self.assertSetEqual(
            committee.topics,
            ProgramCommittee.FIELD_OF_BIOLOGY
        )

    @patch("builtins.input", side_effect=["Библиотека знаний", "ул. Науки, 42", "500"])
    def test_precreation_org_committee_valid(self, mock_input):
        committee = precreation_org_committee()
        self.assertIsInstance(committee, OrganizingCommittee)
        self.assertIsNotNone(committee.venue)
        self.assertIsInstance(committee.venue, Venue)
        self.assertEqual(committee.venue._name, "Библиотека знаний")
        self.assertEqual(committee.venue._address, "ул. Науки, 42")
        self.assertEqual(committee.venue._capacity, 500)

    @patch("builtins.input",
           side_effect=["Библиотека знаний", "ул. Науки, 42", "-500", "Д", "Библиотека знаний", "ул. Науки, 42", "500"])
    def test_precreation_org_committee_invalid_capacity(self, mock_input):
        committee = precreation_org_committee()
        self.assertIsNotNone(committee.venue)
        self.assertEqual(committee.venue._capacity, -500)

    @patch("builtins.input", side_effect=["1"])
    def test_precreation_program_committee_attributes(self, mock_input):
        committee = precreation_program_committee()
        self.assertEqual(committee.name, "ProgramCommittee")
        self.assertEqual(committee.email, "program@example.com")

    @patch("builtins.input", side_effect=["Библиотека", "ул. Ленина", "600"])
    def test_precreation_org_committee_attributes(self, mock_input):
        committee = precreation_org_committee()
        self.assertEqual(committee.name, "OrgCommittee")
        self.assertEqual(committee.email, "@ye")
        self.assertEqual(committee.venue._name, "Библиотека")
        self.assertEqual(committee.venue._address, "ул. Ленина")
        self.assertEqual(committee.venue._capacity, 600)

if __name__ == "__main__":
    unittest.main()

