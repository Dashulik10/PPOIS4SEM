from Projects.src.Organization.Committee.Program_committee.program_committee import *
from Projects.src.Organization.Committee.Organizing_committee.organizing_committee import *

def precreation_program_committee():

    program_committee = ProgramCommittee(
        name="Программный комитет",
        email="program_committee@example.com",
        members=set(),
        chairman=None,
        topics=set()
    )

    fields = {
        1: ("Биология", ProgramCommittee.FIELD_OF_BIOLOGY),
        2: ("Физика", ProgramCommittee.FIELD_OF_PHYSICS),
        3: ("Литература", ProgramCommittee.FIELD_OF_LITERATURE),
    }

    print("Список доступных областей: ")

    for i, (name, _) in fields.items():
        print(f"{i}. {name}")

    try:
        field_choice = int(input("Введите номер области: "))
        if field_choice in fields:
            name, topics = fields[field_choice]
            program_committee.topics = topics
            print(f"Вы выбрали область: {name}")
        else:
            print("Некорректный выбор. Пожалуйста, попробуйте снова.")
            return precreation_program_committee()
    except ValueError:
        print("Ошибка ввода. Ожидался числовой ввод.")
        choice = input("Вы хотите начать заново? Д/Н: ")
        if choice == "Д":
            return precreation_program_committee()
        else:
            exit()

    return program_committee


def precreation_org_committee():

    organizing_committee = OrganizingCommittee(
        name="Организационный комитет",
        email="organizing_committee@example.com",
        members=set(),
        chairman=None,
        venue=None
    )

    try:
        print("\nВведите данные для создания Места Проведения конференции:")
        venue_name = input("Название места проведения: ")
        venue_address = input("Адрес: ")
        venue_capacity = int(input("Вместимость: "))
        venue = Venue(name=venue_name, address=venue_address, capacity=venue_capacity)
        organizing_committee.venue = venue
    except ValueError:
            print(f"Ошибка при создании комитета.")
            choice = input("Вы хотите начать заново? Д/Н: ")
            if choice == "Д":
                return precreation_org_committee()
            else:
                exit()
    return organizing_committee



