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

        self._area_of_expertise = area_of_expertise
        self.report = report

    @property
    def area_of_expertise(self):
        return self._area_of_expertise

    @area_of_expertise.setter
    def area_of_expertise(self, topic_of_report):
            self._area_of_expertise = topic_of_report

    def __str__(self):
        report_doc = self.report.__str__()
        return (f"Докладчик: {self.first_name} {self.second_name}\n"
                f"Возраст: {self.age}\n"
                f"Почта: {self.email}\n"
                f"{report_doc}"
                )

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "report": self.report.to_dict() if self.report else None,
        })
        return data