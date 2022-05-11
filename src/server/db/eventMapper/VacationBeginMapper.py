from server.db.Mapper import Mapper
from server.bo.eventBOs.ComingBO import ComingBO
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

        command = "INSERT INTO worktimeapp.vacationbegin (id, date_of_last_change, date, eventid) VALUES (%s, %s,%s,%s)"
        data = (
            vacationbegin.get_id(),
            vacationbegin.get_date_of_last_change(),
            vacationbegin.get_time(),
            vacationbegin.get_event_id(),
        )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return vacationbegin

    def find_all(self):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, date, eventid FROM worktimeapp.vacationbegin"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, date, eventid) in tuples:
            vacationbegin = ComingBO()
            vacationbegin.set_id(id)
            vacationbegin.set_time(date)
            vacationbegin.set_event_id(eventid)
            result.append(vacationbegin)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, date, eventid FROM worktimeapp.vacationbegin WHERE id={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, date, eventid) = tuples[0]
            vacationbegin = ComingBO()
            vacationbegin.set_id(id)
            vacationbegin.set_time(date)
            vacationbegin.set_event_id(eventid)
            result = vacationbegin
        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_date(self, key):
        result = []

        cursor = self._cnx.cursor()
        command = "SELECT id, date, eventid FROM worktimeapp.vacationbegin WHERE date={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, date, eventid) in tuples:
            vacationbegin = ComingBO()
            vacationbegin.set_id(id)
            vacationbegin.set_time(date)
            vacationbegin.set_event_id(eventid)
            result.append(vacationbegin)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_event_booking_id(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, date, eventid FROM worktimeapp.vacationbegin WHERE chatid={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, date, eventid) = tuples[0]
            vacationbegin = ComingBO()
            vacationbegin.set_id(id)
            vacationbegin.set_time(date)
            vacationbegin.set_event_id(eventid)
            result = vacationbegin
        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def update(self, vacationbegin):
        datestamp = datedate.today()
        cursor = self._cnx.cursor()
        vacationbegin.set_date_of_last_change(datestamp)

        command = "UPDATE worktimeapp.vacationbegin " + \
            "SET date=%s, eventid=%s WHERE id=%s"
        data = (vacationbegin.get_time(), vacationbegin.get_event_id(),
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
