from Projects.src.Organization.Committee.Program_committee.basic_program_committee import *
from datetime import datetime, timedelta

class ProgramCommittee(BasicProgramCommittee):
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

    @staticmethod
    def validate_topic(topic: str) -> bool:
        return (any(topic in field for field in
                    ProgramCommittee.LIST_OF_SETS_OF_TOPICS))


    def get_member_count(self) -> int:
        print(f"Количество участников программного комитета: {len(self.members)}")
        return len(self.members)


    def get_member_details(self):
        if not self.members:
            print("В комитете пока нет участников.")
        else:
            print("Информация по всем участникам программного комитета:")
            for idx, member in enumerate(self.members, 1):
                print(f"{idx}. {member}")

    def get_all_topics(self):
        print("Доступные темы заседания программного комитета:")
        for idx, topic_set in enumerate(self.LIST_OF_SETS_OF_TOPICS, 1):
            print(f"\nПоле #{idx}:")
            for topic in topic_set:
                print(f" - {topic}")

    def add_member(self, member):
        if member not in self._members:
            self._members.add(member)

    def __str__(self):
        return (f"Программный комитет:\n"
                f"Председатель:\n {self.chairman}"
                f"Количество членов: {len(self.members)}")


    def program_of_conference(self, start_time="09:00"):
        if not self.members:
            print("Программный комитет пока не содержит участников.")
            return
        current_time = datetime.strptime(start_time, "%H:%M")
        interval = timedelta(minutes=45)
        print("Примерное расписание программы конференции:\n")
        for idx, member in enumerate(self.members, 1):
            print(f"{current_time.strftime('%H:%M')} - {member}")
            current_time += interval
        print("\nРасписание завершено.")
    def print_chairman_info(self):
        if self.chairman:
            print("Председатель организационного комитета: ")
            print(self.chairman)



