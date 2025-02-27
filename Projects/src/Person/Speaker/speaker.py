#from Projects.src.Organization.Committee.Program_committee.program_committee import ProgramCommittee
from Projects.src.Person.person import Person
#from Projects.src.Organization.Committee.Program_committee.basic_program_committee import *

from Projects.src.Person.Speaker.report import *


class Speaker(Person):
    _area_of_expertise: str

    def __init__(self, *, first_name, second_name, age, email,
                 area_of_expertise, report=None):
        super().__init__(first_name=first_name,
                         second_name=second_name,
                         age=age,
                         email=email)

        '''if program_committee:
            if self._is_valid_topic(area_of_expertise, program_committee):
                self._area_of_expertise = area_of_expertise
            else:
                raise ValueError("Неправильная тема.")
        else:
            self._area_of_expertise = area_of_expertise'''

        self._area_of_expertise = area_of_expertise
        self.report = report

    @property
    def area_of_expertise(self):
        return self._area_of_expertise

    @area_of_expertise.setter
    def area_of_expertise(self, topic_of_report):
            self._area_of_expertise = topic_of_report

    '''@staticmethod
    def _is_valid_topic(topic: str, program_committee):
        from Projects.src.Organization.Committee.Program_committee.program_committee import ProgramCommittee
        return any(topic in field for field in program_committee.LIST_OF_SETS_OF_TOPICS)
    def set_topic_and_expertise(self, report: Report, program_committee: ProgramCommittee):
        if self._is_valid_topic(report._topic_of_report, program_committee):
            self._area_of_expertise = report._topic_of_report
        else:
            raise ValueError("тема доклада не соответствует области знаний.")
        self.report = report'''

    def __str__(self):
        report_doc = self.report.__str__()
        return (f"Докладчик: {self.first_name} {self.second_name}\n"
                f"Возраст: {self.age}\n"
                f"Почта: {self.email}\n"
                f"{report_doc}"
                )