from flask import Flask, render_template, redirect
import sql

app = Flask(__name__)


@app.route("/")
def first_page():
    dictionary_of_requirements = {
        "first_requirements": "1. Mentors and schools page",
        "second_requirements": "2. All school page",
        "third_requirements": "3. Contacts page",
        "fourth_requirements": "4. Contacts of the school",
        "fifth_requirements": "5. Applicants page",
        "sixth_requirements": "6. Applicants and mentors page",
    }
    list_of_requirements = [
        "first_requirements",
        "second_requirements",
        "third_requirements",
        "fourth_requirements",
        "fifth_requirements",
        "sixth_requirements"
    ]
    dictionary_of_function = {
        "first_requirements": "/mentors",
        "second_requirements": "/all-school",
        "third_requirements": "/mentors-by-country",
        "fourth_requirements": "/contacts",
        "fifth_requirements": "/applicants",
        "sixth_requirements": "/applicants-and-mentors",
    }

    return render_template(
        "list.html",
        dictionary_of_requirements=dictionary_of_requirements,
        dictionary_of_function=dictionary_of_function,
        list_of_requirements=list_of_requirements
    )


@app.route("/mentors")
def display_a_mentors():
    data = sql.display_a_mentors()
    list_of_key = ["name_of_mentor", "name_of_school", "country"]
    return render_template("display_a_requirement.html",
                           list_of_key=list_of_key,
                           data=data)


@app.route("/all-school")
def all_school():
    data = sql.all_school()
    list_of_key = ["name_of_mentor", "name_of_school", "country"]
    return render_template("display_a_requirement.html",
                           list_of_key=list_of_key,
                           data=data)


@app.route("/mentors-by-country")
def mentors_by_country():
    data = sql.mentors_by_country()
    list_of_key = ["city", "count"]
    return render_template("display_a_requirement.html",
                           list_of_key=list_of_key,
                           data=data)


@app.route("/contacts")
def contacts():
    data = sql.contacts()
    list_of_key = ["name_of_contact_person", "school_name"]
    return render_template("display_a_requirement.html",
                           list_of_key=list_of_key,
                           data=data)


@app.route("/applicants")
def applicants():
    data = sql.applicants()
    list_of_key = ["name_of_mentors", "applicants_date"]
    return render_template("display_a_requirement.html",
                           list_of_key=list_of_key,
                           data=data)


@app.route("/applicants-and-mentors")
def applicants_and_mentors():
    data = sql.applicants_and_mentors()
    list_of_key = ["name", "applicantion_code", "first_name", "last_name"]
    return render_template("display_a_requirement.html",
                           list_of_key=list_of_key,
                           data=data)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
