from server.db.Mapper import Mapper
from server.bo.eventBOs.ComingBO import ComingBO
from datetime import datetime


class ComingMapper(Mapper):
    def __init__(self):
        super().__init__()

    def insert(self, coming):
        timestamp = datetime.today()
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM worktimeapp.coming ")
        tuples = cursor.fetchall()
        coming.set_date_of_last_change(timestamp)

        for (maxid) in tuples:
            if maxid[0] is not None:
                coming.set_id(maxid[0] + 1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                coming.set_id(1)

        command = "INSERT INTO worktimeapp.coming (id, date_of_last_change, date, eventid) VALUES (%s, %s,%s,%s)"
        data = (
            coming.get_id(),
            coming.get_date_of_last_change(),
            coming.get_time(),
            coming.get_event_id(),
        )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return coming

    def find_all(self):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, date, eventid FROM worktimeapp.coming"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, date, eventid) in tuples:
            coming = ComingBO()
            coming.set_id(id)
            coming.set_time(date)
            coming.set_event_id(eventid)
            result.append(coming)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, date, eventid FROM worktimeapp.coming WHERE id={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, date, eventid) = tuples[0]
            coming = ComingBO()
            coming.set_id(id)
            coming.set_time(date)
            coming.set_event_id(eventid)
            result = coming
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
        command = "SELECT id, date, eventid FROM worktimeapp.coming WHERE date={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, date, eventid) in tuples:
            coming = ComingBO()
            coming.set_id(id)
            coming.set_time(date)
            coming.set_event_id(eventid)
            result.append(coming)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_event_booking_id(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, date, eventid FROM worktimeapp.coming WHERE chatid={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, date, eventid) = tuples[0]
            coming = ComingBO()
            coming.set_id(id)
            coming.set_time(date)
            coming.set_event_id(eventid)
            result = coming
        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def update(self, coming):
        datestamp = datedate.today()
        cursor = self._cnx.cursor()
        coming.set_date_of_last_change(datestamp)

        command = "UPDATE worktimeapp.coming " + \
            "SET date=%s, eventid=%s WHERE id=%s"
        data = (coming.get_time(), coming.get_event_id(),
                coming.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return coming

    def delete(self, coming):
        cursor = self._cnx.cursor()

        command = "DELETE FROM worktimeapp.coming WHERE id={}".format(
            coming.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
