from server.db.Mapper import Mapper
from server.bo.eventBOs.ComingBO import ComingBO
from datetime import datetime


class VacationEndMapper(Mapper):
    def __init__(self):
        super().__init__()

    def insert(self, vacationend):
        timestamp = datetime.today()
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM worktimeapp.vacationend ")
        tuples = cursor.fetchall()
        vacationend.set_date_of_last_change(timestamp)

        for (maxid) in tuples:
            if maxid[0] is not None:
                vacationend.set_id(maxid[0] + 1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 endnen können."""
                vacationend.set_id(1)

        command = "INSERT INTO worktimeapp.vacationend (id, date_of_last_change, date, eventid) VALUES (%s, %s,%s,%s)"
        data = (
            vacationend.get_id(),
            vacationend.get_date_of_last_change(),
            vacationend.get_time(),
            vacationend.get_event_id(),
        )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return vacationend

    def find_all(self):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, date, eventid FROM worktimeapp.vacationend"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, date, eventid) in tuples:
            vacationend = ComingBO()
            vacationend.set_id(id)
            vacationend.set_time(date)
            vacationend.set_event_id(eventid)
            result.append(vacationend)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, date, eventid FROM worktimeapp.vacationend WHERE id={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, date, eventid) = tuples[0]
            vacationend = ComingBO()
            vacationend.set_id(id)
            vacationend.set_time(date)
            vacationend.set_event_id(eventid)
            result = vacationend
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
        command = "SELECT id, date, eventid FROM worktimeapp.vacationend WHERE date={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, date, eventid) in tuples:
            vacationend = ComingBO()
            vacationend.set_id(id)
            vacationend.set_time(date)
            vacationend.set_event_id(eventid)
            result.append(vacationend)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_event_booking_id(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, date, eventid FROM worktimeapp.vacationend WHERE chatid={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, date, eventid) = tuples[0]
            vacationend = ComingBO()
            vacationend.set_id(id)
            vacationend.set_time(date)
            vacationend.set_event_id(eventid)
            result = vacationend
        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def update(self, vacationend):
        datestamp = datedate.today()
        cursor = self._cnx.cursor()
        vacationend.set_date_of_last_change(datestamp)

        command = "UPDATE worktimeapp.vacationend " + \
            "SET date=%s, eventid=%s WHERE id=%s"
        data = (vacationend.get_time(), vacationend.get_event_id(),
                vacationend.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return vacationend

    def delete(self, vacationend):
        cursor = self._cnx.cursor()

        command = "DELETE FROM worktimeapp.vacationend WHERE id={}".format(
            vacationend.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
