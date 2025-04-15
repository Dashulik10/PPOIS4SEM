from datetime import datetime, timedelta

from flask import Flask, render_template, request, redirect, url_for, flash
from Projects.src.Organization.Committee.Program_committee.program_committee import ProgramCommittee
from Projects.src.Organization.Committee.Organizing_committee.organizing_committee import OrganizingCommittee
from Projects.src.Person.Organizer.organizer import Organizer
from Projects.src.Person.Speaker.report import Report
from Projects.src.Person.Speaker.speaker import Speaker
from Projects.src.Person.person import Person
from Projects.src.Organization.Committee.Organizing_committee.venue import Venue
from Projects.src.Organization.Committee.Program_committee.request import Request
import json
'''
    - render_template: Для рендеринга HTML-шаблонов.
    - request: Позволяет извлекать данные из HTTP-запросов (например, данные из формы).
    - redirect: Для перенаправления пользователя на другой маршрут.
    - url_for: Функция для генерации URL по имени маршрута. Вместо жесткой прописки строк типа `"/success"` используем имя функции маршрута. Это удобно для рефакторинга.
    - flash: Позволяет добавлять временные сообщения, которые отображаются пользователю.
    
    Когда браузер "разговаривает" с сервером, он использует протокол HTTP. 
    Этот протокол предоставляет методы для разных запросов.
    - GET: Используется, когда браузер хочет получить информацию с сервера.
    - POST: Используется, когда браузер хочет отправить данные на сервер.
'''

app = Flask(__name__) # Создаем веб-приложение
app.secret_key = "some_secret_key" # Ключ для подписи данных. Уникальный для защиты.


# Глобальные переменные для отслеживания состояния
program_committee = None
organizing_committee = None
base_created = False  # Флаг, указывающий, был ли создан базовый набор.

@app.route("/", methods=["GET", "POST"])
# Декоратор для связывания URL с функцией index(), функция поддерживает GET, POST
def index():
    # Обновляем глобальные функции для передачи между запросами
    global program_committee, organizing_committee, base_created

    # Инициализация доступных областей. Словарик.
    fields = {
        1: ("Биология", ProgramCommittee.FIELD_OF_BIOLOGY),
        2: ("Физика", ProgramCommittee.FIELD_OF_PHYSICS),
        3: ("Литература", ProgramCommittee.FIELD_OF_LITERATURE),
    }

    if request.method == "POST":
        try:
            org_first_name = request.form["org_first_name"]
            org_second_name = request.form["org_second_name"]
            org_age = int(request.form["org_age"])
            org_email = request.form["org_email"]
            org_chairman = Person(
                first_name=org_first_name,
                second_name=org_second_name,
                age=org_age,
                email=org_email
            )

            prog_first_name = request.form["prog_first_name"]
            prog_second_name = request.form["prog_second_name"]
            prog_age = int(request.form["prog_age"])
            prog_email = request.form["prog_email"]
            prog_chairman = Person(
                first_name=prog_first_name,
                second_name=prog_second_name,
                age=prog_age,
                email=prog_email
            )

            selected_field = int(request.form["field"])
            if selected_field not in fields:
                raise ValueError("Выбрана некорректная область.")

            _, selected_topics = fields[selected_field]

            venue_name = request.form["venue_name"]
            venue_address = request.form["venue_address"]
            venue_capacity = int(request.form["venue_capacity"])
            venue = Venue(
                name=venue_name,
                address=venue_address,
                capacity=venue_capacity
            )

            # Формирование комитетов
            program_committee = ProgramCommittee(
                name="Программный комитет",
                email="program_committee@example.com",
                members=set(),
                chairman=prog_chairman,
                topics=selected_topics
            )

            organizing_committee = OrganizingCommittee(
                name="Организационный комитет",
                email="organizing_committee@example.com",
                members=set(),
                chairman=org_chairman,
                venue=venue
            )

            base_created = True

            flash("Базовый набор успешно создан!")
            return redirect(url_for("index"))

        except Exception as e:
            flash(f"Ошибка: {str(e)}")

    return render_template("index.html", fields=fields, base_created=base_created)



@app.route("/registration_organizer", methods=["GET", "POST"])
def register_organizer():
    global organizing_committee

    if request.method == "POST":
        try:
            first_name = request.form["first_name"]
            second_name = request.form["second_name"]
            age = int(request.form["age"])
            email = request.form["email"]
            area_of_expertise = int(request.form["area_of_expertise"])

            new_organizer = Organizer(
                first_name=first_name,
                second_name=second_name,
                age=age,
                email=email,
                area_of_expertise=area_of_expertise,
                experience=0
            )

            if organizing_committee:
                organizing_committee.add_member(new_organizer)
                flash("Организатор успешно добавлен!")
            else:
                flash("Ошибка: Организационный комитет не создан!")
                return redirect(url_for("register_organizer"))
            return redirect(url_for("index"))

        except ValueError as e:
            flash(f"Ошибка валидации данных: {e}")
        except Exception as ex:
            flash(f"Произошла ошибка: {ex}")
            return redirect(url_for("register_organizer"))
    return render_template("register_organizer.html")

@app.route("/organizers", methods=["GET"])
def organizers():
    global organizing_committee

    area_of_expertise_names = {
        1: "Представитель государственной организации",
        2: "Специалист по аппаратуре",
        3: "Ведущий",
        4: "Организатор досуга"
    }

    if organizing_committee:
        members = []
        for member in organizing_committee.members:
            members.append({
                "first_name": member.first_name,
                "second_name": member.second_name,
                "age": member.age,
                "email": member.email,
                "area_of_expertise": area_of_expertise_names.get(
                    member._area_of_expertise, "Неизвестная область"
                )
            })
    else:
        members = []

    return render_template("organizers.html", members=members)

@app.route("/organizing_chairman", methods=["GET"])
def organizing_chairman():
    global organizing_committee

    if organizing_committee is None or organizing_committee.chairman is None:
        flash("Председатель организационного комитета не задан.")
        return redirect(url_for("index"))

    chairman = {
        "first_name": organizing_committee.chairman.first_name,
        "second_name": organizing_committee.chairman.second_name,
        "age": organizing_committee.chairman.age,
        "email": organizing_committee.chairman.email
    }

    return render_template("organizing_chairman.html", chairman=chairman)


@app.route("/programming_chairman", methods=["GET"])
def programming_chairman():
    global program_committee

    if program_committee is None or program_committee.chairman is None:
        flash("Председатель организационного комитета не задан.")
        return redirect(url_for("index"))

    chairman = {
        "first_name": program_committee.chairman.first_name,
        "second_name": program_committee.chairman.second_name,
        "age": program_committee.chairman.age,
        "email": program_committee.chairman.email
    }

    return render_template("program_chairman.html", chairman=chairman)


@app.route("/request_reg", methods=["GET", "POST"])
def request_reg():
    global program_committee
    if request.method == "POST":
        try:
            speaker_first_name = request.form["first_name"]
            speaker_second_name = request.form["second_name"]
            speaker_age = int(request.form["age"])
            speaker_email = request.form["email"]
            selected_topic = request.form["topic"]
            report_name = request.form["report_name"]
            report_date = request.form["report_date"]
            report_annotation = request.form["report_annotation"]

            if not program_committee or selected_topic not in program_committee.topics:
                raise ValueError("Выбрана некорректная тема.")
            report_date_parsed = datetime.strptime(report_date, "%Y-%m-%d")

            report = Report(
                name_of_report=report_name,
                date_of_report=report_date_parsed,
                annotation=report_annotation,
            )
            report.topic_of_report = selected_topic

            speaker = Speaker(
                first_name=speaker_first_name,
                second_name=speaker_second_name,
                age=speaker_age,
                email=speaker_email,
                area_of_expertise=selected_topic,
                report=report,
            )

            new_request = Request(applicant=speaker, report=report)

            program_committee.requests.append(new_request)

            request_id = len(program_committee.requests) - 1
            return redirect(url_for("review_request", request_id=request_id))

        except Exception as e:
            flash(f"Ошибка: {str(e)}")
            return redirect(url_for("request_reg"))

    topics = program_committee.topics if program_committee else []
    return render_template("request_reg.html", topics=topics, request_id=len(program_committee.requests) - 1)



@app.route("/review_request/<int:request_id>", methods=["GET", "POST"])
def review_request(request_id):
    global program_committee

    try:
        selected_request = program_committee.requests[request_id]

        if request.method == "POST":
            action = request.form.get("action")
            if action == "approve":
                program_committee.add_member(selected_request.applicant)
                selected_request.status = "принята"
                flash(f"Заявка от {selected_request.applicant.first_name} успешно одобрена.")
            elif action == "reject":
                selected_request.status = "отклонена"
                flash(f"Заявка от {selected_request.applicant.first_name} была отклонена.")

            return redirect(url_for("index"))

        return render_template("review_request.html", request=selected_request, request_id=request_id)

    except IndexError:
        flash("Заявка не найдена.")
        return redirect(url_for("index"))

@app.route("/program_committee_members", methods=["GET"])
def program_committee_members():
    global program_committee

    if program_committee is None or not program_committee.members:
        flash("В программном комитете пока нет участников.")
        return redirect(url_for("index"))

    members = []
    for member in program_committee.members:
        members.append({
            "first_name": member.first_name,
            "second_name": member.second_name,
            "age": member.age,
            "email": member.email,
            "report": {
                "name": member.report.name_of_report,
                "topic": member.report.topic_of_report,
                "date": member.report.date_of_report.strftime("%Y-%m-%d"),
                "annotation": member.report.annotation
            } if member.report else None
        })

    return render_template("program_committee_members.html", members=members)

def save_committees_to_json(program_committee, organizing_committee, program_filename, organizing_filename):

    try:
        program_members = [
            {
                "first_name": member.first_name,
                "second_name": member.second_name,
                "age": member.age,
                "email": member.email,
                "report": {
                    "name": member.report.name_of_report,
                    "topic": member.report.topic_of_report,
                    "date": member.report.date_of_report.strftime("%Y-%m-%d"),
                    "annotation": member.report.annotation
                } if member.report else None
            }
            for member in program_committee.members
        ]

        with open(program_filename, 'w', encoding='utf-8') as file:
            json.dump(program_members, file, ensure_ascii=False, indent=4)

        organizing_members = [
            {
                "first_name": member.first_name,
                "second_name": member.second_name,
                "age": member.age,
                "email": member.email,
                "area_of_expertise": member.area_of_expertise
            }
            for member in organizing_committee.members
        ]

        with open(organizing_filename, 'w', encoding='utf-8') as file:
            json.dump(organizing_members, file, ensure_ascii=False, indent=4)

        print(f"Данные успешно сохранены в файлы: {program_filename} и {organizing_filename}")
    except Exception as e:
        print(f"Произошла ошибка при сохранении данных: {e}")


@app.route("/save_committees", methods=["GET", "POST"])
def save_committees():
    global program_committee
    global organizing_committee

    if program_committee is None or organizing_committee is None:
        flash("Комитеты ещё не созданы!")
        return redirect(url_for("index"))

    try:
        save_committees_to_json(
            program_committee,
            organizing_committee,
            "program_committee_members.json",
            "organizing_committee_members.json"
        )
        flash("Участники успешно сохранены в JSON файлы!")
    except Exception as e:
        flash(f"Произошла ошибка при сохранении: {str(e)}")

    return render_template("save_committees.html")



if __name__ == "__main__":
    app.run(debug=True)
