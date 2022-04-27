from server.db.Mapper import Mapper
from server.bo.VacationBeginBO import VacationBeginBO
from datetime import datetime


class VacationBeginMapper(Mapper):
    def __init__(self):
        super().__init__()

    def insert(self, vacationbegin):
        timestamp = datetime.today()
        cursor = self._cnx.cursor()
        cursor.execute(
            "SELECT MAX(id) AS maxid FROM worktimeapp.vacationbegin ")
        tuples = cursor.fetchall()
        vacationbegin.set_date_of_last_change(timestamp)

        for (maxid) in tuples:
            if maxid[0] is not None:
                vacationbegin.set_id(maxid[0] + 1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                vacationbegin.set_id(1)

        command = "INSERT INTO worktimeapp.vacationbegin (id, time, event_booking_id) VALUES (%s, %s,%s)"
        data = (
            vacationbegin.get_id(),
            vacationbegin.get_time(),
            vacationbegin.get_event_booking_id()
        )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return vacationbegin

    def find_all(self):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, time, event_booking_id FROM worktimeapp.vacationbegin"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, time, event_booking_id) in tuples:
            vacationbegin = VacationBeginBO()
            vacationbegin.set_id(id)
            vacationbegin.set_time(time)
            vacationbegin.set_event_booking_id(event_booking_id)
            result.append(vacationbegin)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, time, event_booking_id FROM worktimeapp.vacationbegin WHERE id={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, time, event_booking_id) = tuples[0]
            vacationbegin = VacationBeginBO()
            vacationbegin.set_id(id)
            vacationbegin.set_time(time)
            vacationbegin.set_event_booking_id(event_booking_id)
            result = vacationbegin
        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_time(self, key):
        result = []

        cursor = self._cnx.cursor()
        command = "SELECT id, time, event_booking_id FROM worktimeapp.vacationbegin WHERE time={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, time, event_booking_id) in tuples:
            vacationbegin = VacationBeginBO()
            vacationbegin.set_id(id)
            vacationbegin.set_time(time)
            vacationbegin.set_event_booking_id(event_booking_id)
            result.append(vacationbegin)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_event_booking_id(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, time, event_booking_id FROM worktimeapp.vacationbegin WHERE chatid={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, time, event_booking_id) = tuples[0]
            vacationbegin = VacationBeginBO()
            vacationbegin.set_id(id)
            vacationbegin.set_time(time)
            vacationbegin.set_event_booking_id(event_booking_id)
            result = vacationbegin
        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def update(self, vacationbegin):
        timestamp = datetime.today()
        cursor = self._cnx.cursor()
        vacationbegin.set_date_of_last_change(timestamp)

        command = "UPDATE worktimeapp.vacationbegin " + \
            "SET time=%s, event_booking_id=%s WHERE id=%s"
        data = (vacationbegin.get_time(), vacationbegin.get_event_booking_id(),
                vacationbegin.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return vacationbegin

    def delete(self, vacationbegin):
        cursor = self._cnx.cursor()

        command = "DELETE FROM worktimeapp.vacationbegin WHERE id={}".format(
            vacationbegin.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
