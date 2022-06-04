from server.db.Mapper import Mapper
from server.bo.eventBOs.BreakEndBO import BreakEndBO
from datetime import datetime


class BreakEndMapper(Mapper):
    def __init__(self):
        super().__init__()

    def insert(self, break_end):
        timestamp = datetime.today()
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM worktimeapp.breakend ")
        tuples = cursor.fetchall()
        break_end.set_date_of_last_change(timestamp)

        for (maxid) in tuples:
            if maxid[0] is not None:
                break_end.set_id(maxid[0] + 1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                break_end.set_id(1)

        command = "INSERT INTO worktimeapp.breakend (id, date_of_last_change, date, type) VALUES (%s, %s,%s,%s)"
        data = (
            break_end.get_id(),
            break_end.get_date_of_last_change(),
            break_end.get_time(),
            break_end.get_type()
        )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return break_end

    def find_all(self):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, date_of_last_change, date, type FROM worktimeapp.breakend"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, dateoflastchange, date, type) in tuples:
            break_end = BreakEndBO()
            break_end.set_id(id)
            break_end.set_date_of_last_change(dateoflastchange)
            break_end.set_time(date)
            break_end.set_type(type)
            result.append(break_end)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, date_of_last_change, date, type FROM worktimeapp.breakend WHERE id={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, dateoflastchange, date, type) = tuples[0]
            break_end = BreakEndBO()
            break_end.set_id(id)
            break_end.set_date_of_last_change(dateoflastchange)
            break_end.set_time(date)
            break_end.set_type(type)
            result = break_end
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
        command = "SELECT id, date_of_last_change, date, type FROM worktimeapp.breakend WHERE date={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, dateoflastchage, date, type) in tuples:
            break_end = BreakEndBO()
            break_end.set_id(id)
            break_end.set_date_of_last_change(dateoflastchage)
            break_end.set_time(date)
            break_end.set_type(type)
            result.append(break_end)

        self._cnx.commit()
        cursor.close()

        return result

    def update(self, break_end):
        datestamp = datetime.today()
        cursor = self._cnx.cursor()
        break_end.set_date_of_last_change(datestamp)

        command = "UPDATE worktimeapp.breakend " + \
            "SET date=%s WHERE id=%s"
        data = (break_end.get_time(),
                break_end.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return break_end

    def delete(self, break_end):
        cursor = self._cnx.cursor()

        command = "DELETE FROM worktimeapp.breakend WHERE id={}".format(
            break_end.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
