from person import People
from datetime import datetime as dt
birthday_objects = []
current_month = []


def get_people_details():
    """
    This function reads the birthday file and returns the details
     of every entry as a list
    """
    with open("birthday.csv", 'r') as file:
        people_data = file.readlines()

    for person in people_data:
        person = person.split(",")
        friend = People(person[0], person[1],  person[2], person[3])
        birthday_objects.append(friend)


def return_current_month():
    """
    returns the current month and day of the month
    """
    p_month = str(dt.today()).split(" ")[0].split("-")[1]
    p_day = str(dt.today()).split(" ")[0].split("-")[2]
    return p_month, p_day


def send_message(month):
    """
    The function loops through the birthday objects and returns a list of objects
    whose birth month tallies with the current month
    """
    for object_ in birthday_objects:
        if object_.month == month:
            current_month.append(object_)


def check_date(today):
    for object_ in current_month:
        today = int(today)
        object_.day = int(object_.day)
        if today == object_.day:
            print(f" name = {object_.name}")
            print(f" email = {object_.email}")
            print(f" month = {object_.month}")
            print(f" day = {object_.day}")


get_people_details()
T_month, T_day = return_current_month()
send_message(T_month)
check_date(T_day)
