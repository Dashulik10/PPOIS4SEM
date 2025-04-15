from datetime import date
import time

from Projects.src.Organization.Committee.Program_committee.request import Request
from Projects.src.Organization.Precreation.precreation_chairmans import set_org_chairman, set_program_chairman
from Projects.src.Organization.Precreation.precreation_committee import precreation_program_committee, \
    precreation_org_committee
from Projects.src.Person.Organizer.organizer import Organizer
from Projects.src.Person.Speaker.speaker import Speaker
from Projects.src.Person.Speaker.report import Report
import json


def save_members_to_json(members, filename):
    """Сохранение списка участников в JSON-файл."""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            members_as_dicts = [member.__dict__ for member in members]
            json.dump(members_as_dicts, file, ensure_ascii=False, indent=4)
        print(f"Список участников успешно сохранен в файл {filename}.")
    except Exception as e:
        print(f"Ошибка при сохранении файла {filename}: {e}")

def start():
    while True:
        choice = input("Вы хотите начать создание? д/н ")
        if choice == "д":


            print("Сначала давайте назначим председателя организационного комитета: ")
            org_chairman = set_org_chairman()
            print("Далее назначим председателя программного комитета: ")
            program_chairman = set_program_chairman()


            print("Теперь можно формировать программный комитет: ")
            program_committeee = precreation_program_committee()
            program_committeee.chairman = program_chairman


            print("\nИ заключительная часть первого этапа - создание организационного комитета.")
            org_committee = precreation_org_committee()
            org_committee.chairman = org_chairman

            return program_committeee, org_committee
        elif choice == "н":
            exit()
        else:
            print("Неверное значение. Повторите попытку.")


def show_menu():
    print("Добро пожаловать! Пожалуйста, выберите пункт из меню:")
    print("1. Регистрация организатора.") # done
    print("2. Подать заявку на участие.") # done
    print("3. Вывод всех участников программного коммитета.") # done
    print("4. Вывод всех организаторов.") # done
    print("5. Вывод председателя программного коммитета.") # done
    print("6. Вывод председателя организационного коммитета.") # done
    print("7. Вывод информации о программном комитете.") # done
    print("8. Вывод информации о организационном комитете.") # done
    print("9. Вывод программы конференции.") # done
    print("10. Старт.")
    print("11. Досрочное завершение.")
    print("12. Сохранить списки участников в файлы JSON.")


def main():
    print("Добро пожаловать!")
    program_committee, org_committee = start()
    while True:
        try:
            show_menu()
            choice  = int(input("Выберите пункт: "))

            if choice == 1:
                first_name = input("Введите имя организатора: ")
                second_name = input("Введите фамилию организатора: ")
                age = int(input("Введите возраст организатора: "))
                email = input("Введите рабочую почту организатора: ")


                print("Области организации:")
                print("1. Представитель государственной организации.")
                print("2. Специалист по аппаратуре.")
                print("3. Ведущий.")
                print("4. Организатор досуга.")
                area_num = int(input("Введите номер области: "))

                organizer = Organizer(
                    first_name=first_name,
                    second_name=second_name,
                    age=age,
                    email=email,
                    area_of_expertise=area_num,
                    experience=0
                )

                org_committee.add_member(organizer)
                print("\nОрганизатор успешно добавлен!")
                print(organizer)

            elif choice == 2:
                print("Создание спикера:")

                speaker_first_name = input("Введите имя спикера: ")
                speaker_second_name = input("Введите фамилию спикера: ")
                speaker_age = int(input("Введите возраст спикера: "))
                speaker_email = input("Введите рабочую почту спикера: ")
                speaker_area_of_expertise = input("Введите научную область спикера: ")

                print("\nСоздание доклада:")
                report_name = input("Введите название доклада: ")
                report_annotation = input("Введите аннотацию доклада: ")
                report_date = input("Введите дату публикации (в формате ГГГГ-ММ-ДД): ")

                try:
                    report_date_parsed = date.fromisoformat(report_date)
                except ValueError:
                    print("Неверный формат даты! Попробуйте ещё раз.")
                    continue

                report = Report(
                    name_of_report=report_name,
                    date_of_report=report_date_parsed,
                    annotation=report_annotation
                )
                report.topic_of_report = speaker_area_of_expertise

                speaker = Speaker(
                    first_name=speaker_first_name,
                    second_name=speaker_second_name,
                    age=speaker_age,
                    email=speaker_email,
                    area_of_expertise=speaker_area_of_expertise,
                    report=report,
                )

                request = Request(
                    applicant=speaker,
                    report=report,
                )

                print("\nЗаявка создана:")
                print(request)

                while True:
                    print("\nЧто вы хотите сделать с заявкой?")
                    print("1. Принять заявку.")
                    print("2. Удалить заявку.")
                    print("3. Отменить действие.")
                    action = int(input("Выберите действие: "))

                    if action == 1:
                        request.status = "принята"
                        print(f"\nЗаявка от спикера {speaker.first_name} {speaker.second_name} принята.")
                        program_committee.add_member(speaker)
                        print(f"Спикер добавлен в программный комитет.")
                        break
                    elif action == 2:
                        request.status = "отклонена"
                        print(f"\nЗаявка от спикера {speaker.first_name} {speaker.second_name} отклонена.")
                        break
                    elif action == 3:
                        print("\nДействие отменено.")
                        break
                    else:
                        print("Некорректный выбор. Попробуйте снова.")

            elif choice == 3:
                print(program_committee.get_member_details())

            elif choice == 4:
                print(org_committee.get_member_details())

            elif choice == 5:
                print(program_committee.print_chairman_info())

            elif choice == 6:
                print(org_committee.print_chairman_info())

            elif choice == 7:
                print(program_committee)

            elif choice == 8:
                print(org_committee)

            elif choice == 9:
                program_committee.program_of_conference()

            elif choice == 10:
                print("Слушаем речь председателя ...")
                time.sleep(3)
                print("Программа: ")
                program_committee.program_of_conference()
                time.sleep(4)
                print("Слушаем спикеров ...")
                time.sleep(4)
                print("Слушаем речь председателя ...")
                print("Конференция закрыта. Вопросы можно задать на научсобрании после обеда ...")
                exit()

            elif choice == 11:
                exit()

            elif choice == 12:
                save_members_to_json(list(program_committee.members), 'program_committee_members.json')
                save_members_to_json(list(org_committee.members), 'organizational_committee_members.json')

            else:
                print("Некорректный выбор. Попробуйте ещё раз.")


        except ValueError:
            print("Ошибка: ожидался числовой ввод. Попробуйте снова.")

        except AttributeError as ae:
            print(f"Сбой в программе: {ae}. Проверьте корректность операций.")
        except Exception as e:
            print(f"Произошла ошибка: {e}. Выполнение программы продолжается.")


if __name__ == "__main__":
    main()


