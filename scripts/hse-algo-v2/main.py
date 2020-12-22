import datetime
import logging
import sys
import config

from sheets import GoogleSheetsUpdater
from yandex_contest_api import YandexContestAPI


def main(contests):
    gsu = GoogleSheetsUpdater('HSE Algo Seminars 2021', 'Контесты 2 модуль')

    students = gsu.get_students_list()

    gsu.wks.update('A1', str(datetime.datetime.now()))
    logging.info(students)

    for contest_id in contests:
        yandex_contest_api = YandexContestAPI(config.AUTH_KEY, contest_id)
        standings = yandex_contest_api.generate_standings(students)
        gsu.update_sheet(standings)


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    main([21961, 23375, 21895, 22752])