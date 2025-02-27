from Projects.src.Person.Speaker.report import Report
from Projects.src.Person.person import *

class Request:
    def __init__(self, applicant, report, status="рассматривается"):
        self._applicant = applicant
        self._report = report
        self._status = status

    @property
    def applicant(self):
        return self._applicant

    @applicant.setter
    def applicant(self, value):
        if isinstance(value, Person):
            self._applicant = value
        else:
            raise ValueError("Заявитель должен быть объектом Person")

    @property
    def report(self):
        return self._report

    @report.setter
    def report(self, value):
        if isinstance(value, Report):
            self._report = value
        else:
            raise ValueError("Доклад должен быть объектом Report")

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        valid_statuses = {"рассматривается", "принята", "отклонена"}
        if value in valid_statuses:
            self._status = value
        else:
            raise ValueError("Некорректный статус заявки")

    def change_status(self, new_status):
        self.status = new_status

    def __str__(self):
        return (f"Заявка от: {self.applicant.first_name} {self.applicant.second_name}\n"
                f"Доклад: {self.report.name_of_report}\n" 
                f"Статус: {self.status}")
