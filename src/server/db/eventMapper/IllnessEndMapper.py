from server.db.Mapper import Mapper
from server.bo.eventBOs.ComingBO import ComingBO
from datetime import datetime


class IllnessEndMapper(Mapper):
    def __init__(self):
        super().__init__()

    def insert(self, illnessend):
        timestamp = datetime.today()
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM worktimeapp.illnessend ")
        tuples = cursor.fetchall()
        illnessend.set_date_of_last_change(timestamp)

        for (maxid) in tuples:
            if maxid[0] is not None:
                illnessend.set_id(maxid[0] + 1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 endnen können."""
                illnessend.set_id(1)

        command = "INSERT INTO worktimeapp.illnessend (id, date_of_last_change, date, eventid) VALUES (%s, %s,%s,%s)"
        data = (
            illnessend.get_id(),
            illnessend.get_date_of_last_change(),
            illnessend.get_time(),
            illnessend.get_event_id(),
        )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return illnessend

    def find_all(self):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, date, eventid FROM worktimeapp.illnessend"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, date, eventid) in tuples:
            illnessend = ComingBO()
            illnessend.set_id(id)
            illnessend.set_time(date)
            illnessend.set_event_id(eventid)
            result.append(illnessend)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, date, eventid FROM worktimeapp.illnessend WHERE id={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, date, eventid) = tuples[0]
            illnessend = ComingBO()
            illnessend.set_id(id)
            illnessend.set_time(date)
            illnessend.set_event_id(eventid)
            result = illnessend
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
        command = "SELECT id, date, eventid FROM worktimeapp.illnessend WHERE date={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, date, eventid) in tuples:
            illnessend = ComingBO()
            illnessend.set_id(id)
            illnessend.set_time(date)
            illnessend.set_event_id(eventid)
            result.append(illnessend)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_event_booking_id(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, date, eventid FROM worktimeapp.illnessend WHERE chatid={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, date, eventid) = tuples[0]
            illnessend = ComingBO()
            illnessend.set_id(id)
            illnessend.set_time(date)
            illnessend.set_event_id(eventid)
            result = illnessend
        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def update(self, illnessend):
        datestamp = datedate.today()
        cursor = self._cnx.cursor()
        illnessend.set_date_of_last_change(datestamp)

        command = "UPDATE worktimeapp.illnessend " + \
            "SET date=%s, eventid=%s WHERE id=%s"
        data = (illnessend.get_time(), illnessend.get_event_id(),
                illnessend.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return illnessend

    def delete(self, illnessend):
        cursor = self._cnx.cursor()

        command = "DELETE FROM worktimeapp.illnessend WHERE id={}".format(
            illnessend.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
