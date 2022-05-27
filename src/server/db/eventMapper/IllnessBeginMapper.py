from server.db.Mapper import Mapper
from server.bo.eventBOs.IllnessBeginBO import IllnessBeginBO
from datetime import datetime


class IllnessBeginMapper(Mapper):
    def __init__(self):
        super().__init__()

    def insert(self, illness_begin):
        timestamp = datetime.today()
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM worktimeapp.illnessbegin ")
        tuples = cursor.fetchall()
        illness_begin.set_date_of_last_change(timestamp)

        for (maxid) in tuples:
            if maxid[0] is not None:
                illness_begin.set_id(maxid[0] + 1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                illness_begin.set_id(1)

        command = "INSERT INTO worktimeapp.illnessbegin (id, date_of_last_change, date) VALUES (%s, %s,%s)"
        data = (
            illness_begin.get_id(),
            illness_begin.get_date_of_last_change(),
            illness_begin.get_time(),
        )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return illness_begin

    def find_all(self):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, date_of_last_change, date FROM worktimeapp.illnessbegin"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, date) in tuples:
            illness_begin = IllnessBeginBO()
            illness_begin.set_id(id)
            illness_begin.set_time(date)
            result.append(illness_begin)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, date_of_last_change, date FROM worktimeapp.illnessbegin WHERE id={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, date) = tuples[0]
            illness_begin = IllnessBeginBO()
            illness_begin.set_id(id)
            illness_begin.set_time(date)
            result = illness_begin
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
        command = "SELECT id, date_of_last_change, date FROM worktimeapp.illnessbegin WHERE date={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, dateoflastchange, date) in tuples:
            illness_begin = IllnessBeginBO()
            illness_begin.set_id(id)
            illness_begin.set_date_of_last_change(dateoflastchange)
            illness_begin.set_time(date)
            result.append(illness_begin)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_event_booking_id(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, date FROM worktimeapp.illnessbegin WHERE id={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, dateoflastchange, date) = tuples[0]
            illness_begin = IllnessBeginBO()
            illness_begin.set_id(id)
            illness_begin.set_date_of_last_change(dateoflastchange)
            illness_begin.set_time(date)
            result = illness_begin
        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def update(self, illness_begin):
        datestamp = datetime.today()
        cursor = self._cnx.cursor()
        illness_begin.set_date_of_last_change(datestamp)

        command = "UPDATE worktimeapp.illnessbegin " + \
            "SET date=%s WHERE id=%s"
        data = (illness_begin.get_time(),
                illness_begin.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return illness_begin

    def delete(self, illness_begin):
        cursor = self._cnx.cursor()

        command = "DELETE FROM worktimeapp.illnessbegin WHERE id={}".format(
            illness_begin.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
