import psycopg2
from private_psql_settings import connectioon_triplets


def run_query(query):
    """
    A single query from the localhost database.
    Arg:
        @query: string - a whole executable psql query
    return:
        - for SELECT: list of tuples
        - in case of error: error message
        - "Done :)" if non SELECT query executed without error
    """
    try:
        dbname, user, password = connectioon_triplets()
        connect_str = "dbname='{}' user='{}' host='localhost' password='{}'".format(dbname, user, password)
        connection = psycopg2.connect(connect_str)
        cursor = connection.cursor()
        connection.autocommit = True
        cursor = connection.cursor()

        cursor.execute(query)

        if query.upper().startswith("SELECT"):
            rows = cursor.fetchall()
        else:
            rows = "Done :)"
        cursor.close()

    except psycopg2.DatabaseError as exception:
        print(exception)
        rows = exception

    finally:
        if connection:
            connection.close()
    return rows


def build_dictionary_of_list(sql_result, list_of_key):
    # select column_name
    # from INFORMATION_SCHEMA.COLUMNS
    # where TABLE_NAME='mentors'
    list_of_dictionary = []
    for row in sql_result:
        build_dict = {}
        for index, name in enumerate(list_of_key):
            build_dict[name] = row[index]
        list_of_dictionary.append(build_dict)
    return list_of_dictionary


def display_a_mentors():
    # mentors.first_name, mentors.last_name, schools.name, schools.country
    query = """SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
               FROM mentors
               LEFT JOIN schools
               ON mentors.city=schools.city ORDER BY mentors.id"""
    sql_result = run_query(query)
    list_of_key = ["name_of_mentor", "name_of_school", "country"]
    result = build_dictionary_of_list(sql_result, list_of_key)

    return result


def all_school():
    query = """SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
               FROM mentors RIGHT JOIN schools ON schools.city=mentors.city
               ORDER BY mentors.id"""
    sql_result = run_query(query)
    list_of_key = ["name_of_mentor", "name_of_school", "country"]
    result = build_dictionary_of_list(sql_result, list_of_key)

    return result


def mentors_by_country():
    query = """SELECT schools.country, COUNT(mentors.id)
                FROM mentors
                RIGHT JOIN schools ON schools.city=mentors.city
                GROUP BY schools.country"""
    sql_result = run_query(query)
    list_of_key = ["city", "count"]
    result = build_dictionary_of_list(sql_result, list_of_key)
    return result


def contacts():
    query = """SELECT schools.name, mentors.first_name, mentors.last_name
                FROM mentors
                RIGHT JOIN schools ON
                mentors.id = schools.contact_person
                ORDER BY schools.name"""
    sql_result = run_query(query)
    list_of_key = ["school_name", "name_of_contact_person"]
    result = build_dictionary_of_list(sql_result, list_of_key)
    return result


def applicants():
    query = """SELECT CONCAT(applicants.Last_name,' ',applicants.First_name), applicants.application_code
               FROM applicants
               LEFT JOIN applicants_mentors
               ON applicants.id = applicants_mentors.applicant_id
               WHERE applicants_mentors.creation_date >= '2016-01-01'
               ORDER BY applicants_mentors.creation_date DESC"""
    sql_result = run_query(query)
    list_of_key = ["name_of_mentors", "applicants_date"]
    result = build_dictionary_of_list(sql_result, list_of_key)
    return result


def applicants_and_mentors():
    query = """SELECT applicants.first_name, applicants.application_code, mentors.first_name, mentors.last_name
               FROM applicants
               LEFT JOIN applicants_mentors
               ON applicants.id = applicants_mentors.applicant_id
               LEFT JOIN mentors
               ON applicants_mentors.mentor_id = mentors.id"""
    sql_result = run_query(query)
    list_of_key = ["name", "applicantion_code", "first_name", "last_name"]
    result = build_dictionary_of_list(sql_result, list_of_key)
    return result


def main():
    pass


if __name__ == '__main__':
    main()
