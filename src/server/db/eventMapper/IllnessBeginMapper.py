from server.db.Mapper import Mapper
from server.bo.eventBOs.ComingBO import ComingBO
from datetime import datetime


class IllnessBeginMapper(Mapper):
    def __init__(self):
        super().__init__()

    def insert(self, illnessbegin):
        timestamp = datetime.today()
        cursor = self._cnx.cursor()
        cursor.execute(
            "SELECT MAX(id) AS maxid FROM worktimeapp.illnessbegin ")
        tuples = cursor.fetchall()
        illnessbegin.set_date_of_last_change(timestamp)

        for (maxid) in tuples:
            if maxid[0] is not None:
                illnessbegin.set_id(maxid[0] + 1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                illnessbegin.set_id(1)

        command = "INSERT INTO worktimeapp.illnessbegin (id, date_of_last_change, date, eventid) VALUES (%s, %s,%s,%s)"
        data = (
            illnessbegin.get_id(),
            illnessbegin.get_date_of_last_change(),
            illnessbegin.get_time(),
            illnessbegin.get_event_id(),
        )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return illnessbegin

    def find_all(self):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, date, eventid FROM worktimeapp.illnessbegin"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, date, eventid) in tuples:
            illnessbegin = ComingBO()
            illnessbegin.set_id(id)
            illnessbegin.set_time(date)
            illnessbegin.set_event_id(eventid)
            result.append(illnessbegin)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, date, eventid FROM worktimeapp.illnessbegin WHERE id={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, date, eventid) = tuples[0]
            illnessbegin = ComingBO()
            illnessbegin.set_id(id)
            illnessbegin.set_time(date)
            illnessbegin.set_event_id(eventid)
            result = illnessbegin
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
        command = "SELECT id, date, eventid FROM worktimeapp.illnessbegin WHERE date={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, date, eventid) in tuples:
            illnessbegin = ComingBO()
            illnessbegin.set_id(id)
            illnessbegin.set_time(date)
            illnessbegin.set_event_id(eventid)
            result.append(illnessbegin)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_event_booking_id(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, date, eventid FROM worktimeapp.illnessbegin WHERE chatid={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, date, eventid) = tuples[0]
            illnessbegin = ComingBO()
            illnessbegin.set_id(id)
            illnessbegin.set_time(date)
            illnessbegin.set_event_id(eventid)
            result = illnessbegin
        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def update(self, illnessbegin):
        datestamp = datetime.today()
        cursor = self._cnx.cursor()
        illnessbegin.set_date_of_last_change(datestamp)

        command = "UPDATE worktimeapp.illnessbegin " + \
            "SET date=%s, eventid=%s WHERE id=%s"
        data = (illnessbegin.get_time(), illnessbegin.get_event_id(),
                illnessbegin.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return illnessbegin

    def delete(self, illnessbegin):
        cursor = self._cnx.cursor()

        command = "DELETE FROM worktimeapp.illnessbegin WHERE id={}".format(
            illnessbegin.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
