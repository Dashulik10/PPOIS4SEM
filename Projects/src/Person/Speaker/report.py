import datetime


class Report:
    _name_of_report: str
    _topic_of_report: str
    _date_of_report: datetime.date
    _annotation: str

    def __init__(self, name_of_report, date_of_report, annotation, speaker=None):
        self._name_of_report = name_of_report
        self._date_of_report = date_of_report
        self._annotation = annotation

        if speaker and hasattr(speaker, 'area_of_expertise'):
            self._topic_of_report = speaker.area_of_expertise
        else:
            self._topic_of_report = "Тема не указана"

    @property
    def name_of_report(self):
        return self._name_of_report

    @name_of_report.setter
    def name_of_report(self, name_of_report):
        if len(name_of_report) <= 100:
            self._name_of_report = name_of_report
        else:
            raise ValueError("Название доклада слишком длинное")

    @property
    def topic_of_report(self):
        return self._topic_of_report

    @topic_of_report.setter
    def topic_of_report(self, topic_of_report):
        if len(topic_of_report) <= 100:
            self._topic_of_report = topic_of_report
        else:
            raise ValueError("Тема доклада слишком длинная")

    @property
    def date_of_report(self):
        return self._date_of_report

    @date_of_report.setter
    def date_of_report(self, date_of_report):
        if isinstance(date_of_report, datetime.date):
            self._date_of_report = date_of_report
        else:
            raise TypeError("Дата доклада должна быть типа datetime.date")

    @property
    def annotation(self):
        return self._annotation

    @annotation.setter
    def annotation(self, annotation):
        if len(annotation) <= 500:
            self._annotation = annotation
        else:
            raise ValueError("Аннотация слишком длинная")

    def __str__(self):
        return (f"Название доклада: {self.name_of_report}\n"
                f"Тема доклада: {self.topic_of_report}\n"
                f"Дата публикации: {self.date_of_report}\n"
                f"Аннотация:\n{self.annotation}\n")
