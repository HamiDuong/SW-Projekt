from server.db.Mapper import Mapper
from server.bo.eventBOs.BreakBeginBO import BreakBeginBO
from datetime import datetime


class BreakBeginMapper(Mapper):
    def __init__(self):
        super().__init__()

    def insert(self, break_begin):
        """
        @author Khadidja Kebaili (https://github.com/KhadidjaKebaili)

        Fügt ein BreakBeginBO in die Datenbank ein
        param: break_begin (BreakBeginBO)
        return: break_begin
        """
        timestamp = datetime.today()
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM worktimeapp.breakbegin ")
        tuples = cursor.fetchall()
        break_begin.set_date_of_last_change(timestamp)

        for (maxid) in tuples:
            if maxid[0] is not None:
                break_begin.set_id(maxid[0] + 1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                break_begin.set_id(1)

        command = "INSERT INTO worktimeapp.breakbegin (id, date_of_last_change, date, type) VALUES (%s, %s,%s,%s)"
        data = (
            break_begin.get_id(),
            break_begin.get_date_of_last_change(),
            break_begin.get_time(),
            break_begin.get_type()
        )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return break_begin

    def find_all(self):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, date_of_last_change, date, type FROM worktimeapp.breakbegin"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, dateoflastchange, date, type) in tuples:
            break_begin = BreakBeginBO()
            break_begin.set_id(id)
            break_begin.set_date_of_last_change(dateoflastchange)
            break_begin.set_time(date)
            break_begin.set_type(type)
            result.append(break_begin)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, date_of_last_change, date, type FROM worktimeapp.breakbegin WHERE id={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, dateoflastchange, date, type) = tuples[0]
            break_begin = BreakBeginBO()
            break_begin.set_id(id)
            break_begin.set_date_of_last_change(dateoflastchange)
            break_begin.set_time(date)
            break_begin.set_type(type)
            result = break_begin
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
        command = "SELECT id, date_of_last_change, date, type FROM worktimeapp.breakbegin WHERE date={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, dateoflastchange, date, type) in tuples:
            break_begin = BreakBeginBO()
            break_begin.set_id(id)
            break_begin.set_date_of_last_change(dateoflastchange)
            break_begin.set_time(date)
            break_begin.set_type(type)
            result.appbegin(break_begin)

        self._cnx.commit()
        cursor.close()

        return result

    def update(self, break_begin):
        datestamp = datetime.today()
        cursor = self._cnx.cursor()
        break_begin.set_date_of_last_change(datestamp)

        command = "UPDATE worktimeapp.breakbegin " + \
            "SET date_of_last_change=%s, date=%s WHERE id=%s"
        data = (break_begin.get_date_of_last_change(), break_begin.get_time(),
                break_begin.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return break_begin

    def delete(self, break_begin):
        cursor = self._cnx.cursor()

        command = "DELETE FROM worktimeapp.breakbegin WHERE id={}".format(
            break_begin.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
