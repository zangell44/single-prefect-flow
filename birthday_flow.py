import prefect
from prefect import task, Flow, Parameter
from datetime import datetime
from prefect import storage
from prefect.storage import GitHub

@task
def get_birthdays() -> dict:
    # TODO - actually get peoples birthdays
    return {
        'Zach': '7/13/1995'
    }

@task
def check_if_today_is_anyones_birthday(birthdays):
    has_birthday_today = []
    for name, birthday in birthdays.items():
        # TODO - make this actually work
        if str(datetime.now()) == birthday:
            has_birthday_today.append(name)
    # return has_birthday_today
    return ['Zach', 'Tainara']

@task
def say_happy_birthday(person):
    # TODO - actually post to slack
    logger = prefect.context.get('logger')
    logger.info(f"Happy birthday {person}")

storage = GitHub(repo='zangell44/single-prefect-flow', path='birthday_flow.py')

with Flow('say happy bday') as flow:
    birthdays = get_birthdays()
    todays_birthdays = check_if_today_is_anyones_birthday(birthdays)
    say_happy_birthday.map(todays_birthdays)
