from server.db.Mapper import Mapper
from server.bo.eventBOs.ComingBO import ComingBO
from datetime import datetime


class GoingMapper(Mapper):
    def __init__(self):
        super().__init__()

    def insert(self, going):
        timestamp = datetime.today()
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM worktimeapp.going ")
        tuples = cursor.fetchall()
        going.set_date_of_last_change(timestamp)

        for (maxid) in tuples:
            if maxid[0] is not None:
                going.set_id(maxid[0] + 1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                going.set_id(1)

        command = "INSERT INTO worktimeapp.going (id, date_of_last_change, date, eventid) VALUES (%s, %s,%s,%s)"
        data = (
            going.get_id(),
            going.get_date_of_last_change(),
            going.get_time(),
            going.get_event_id(),
        )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return going

    def find_all(self):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, date, eventid FROM worktimeapp.going"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, date, eventid) in tuples:
            going = ComingBO()
            going.set_id(id)
            going.set_time(date)
            going.set_event_id(eventid)
            result.append(going)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, date, eventid FROM worktimeapp.going WHERE id={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, date, eventid) = tuples[0]
            going = ComingBO()
            going.set_id(id)
            going.set_time(date)
            going.set_event_id(eventid)
            result = going
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
        command = "SELECT id, date, eventid FROM worktimeapp.going WHERE date={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, date, eventid) in tuples:
            going = ComingBO()
            going.set_id(id)
            going.set_time(date)
            going.set_event_id(eventid)
            result.append(going)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_event_booking_id(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, date, eventid FROM worktimeapp.going WHERE chatid={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, date, eventid) = tuples[0]
            going = ComingBO()
            going.set_id(id)
            going.set_time(date)
            going.set_event_id(eventid)
            result = going
        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def update(self, going):
        datestamp = datetime.today()
        cursor = self._cnx.cursor()
        going.set_date_of_last_change(datestamp)

        command = "UPDATE worktimeapp.going " + \
            "SET date=%s, eventid=%s WHERE id=%s"
        data = (going.get_time(), going.get_event_id(),
                going.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return going

    def delete(self, going):
        cursor = self._cnx.cursor()

        command = "DELETE FROM worktimeapp.going WHERE id={}".format(
            going.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
