from Projects.src.Person.person import *

def set_program_chairman():
    try:
        program_chairman = Person(
        first_name="",
        second_name="",
        age=0,
        email="@"
        )
        program_chairman.first_name = input(
            "Введите имя председателя программного комитета: ")
        program_chairman.second_name = input(
            "Введите фамилию председателя программного комитета: ")
        program_chairman.age = int(input(
            "Введите возраст председателя программного комитета: "))
        program_chairman.email = input("Введите рабочую почту: ")
        print(program_chairman)
        return program_chairman

    except:
        print(f"Неверное значение.")
        choice = input("Вы хотите начать заново? д/н ")
        if choice == "д":
            set_program_chairman()
        else:
            exit()


def set_org_chairman():
    try:
        org_chairman = Person(
            first_name="",
            second_name="",
            age=0,
            email="@"
        )
        org_chairman.first_name = input(
            "Введите имя председателя организационного комитета: ")
        org_chairman.second_name = input(
            "Введите фамилию председателя организационного комитета: ")
        org_chairman.age = int(input(
            "Введите возраст председателя организационного комитета: "))
        org_chairman.email = input("Введите рабочую почту: ")
        print(org_chairman)
        return org_chairman
    except:
        print(f"Неверное значение.")
        choice = input("Вы хотите начать заново? д/н ")
        if choice == "д":
            set_org_chairman()
        else:
            exit()