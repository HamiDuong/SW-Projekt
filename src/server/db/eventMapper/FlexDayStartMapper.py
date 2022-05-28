from server.db.Mapper import Mapper
from server.bo.eventBOs.FlexDayStart import FlexDayStartBO
from datetime import datetime


class FlexDayStartMapper(Mapper):
    def __init__(self):
        super().__init__()

    def insert(self, flex_day_start):
        timestamp = datetime.today()
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM worktimeapp.flexdaystart ")
        tuples = cursor.fetchall()
        flex_day_start.set_date_of_last_change(timestamp)

        for (maxid) in tuples:
            if maxid[0] is not None:
                flex_day_start.set_id(maxid[0] + 1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                flex_day_start.set_id(1)

        command = "INSERT INTO worktimeapp.flexdaystart (id, date_of_last_change, date, type) VALUES (%s, %s,%s, %s)"
        data = (
            flex_day_start.get_id(),
            flex_day_start.get_date_of_last_change(),
            flex_day_start.get_time(),
            flex_day_start.get_type()
        )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return flex_day_start

    def find_all(self):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, date_of_last_change, date, type FROM worktimeapp.flexdaystart"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, dateoflastchange, date, type) in tuples:
            flex_day_start = FlexDayStartBO()
            flex_day_start.set_id(id)
            flex_day_start.set_date_of_last_change(dateoflastchange)
            flex_day_start.set_time(date)
            flex_day_start.set_type(type)
            result.append(flex_day_start)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, date_of_last_change, date FROM worktimeapp.flexdaystart WHERE id={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, dateoflastchange, date, type) = tuples[0]
            flex_day_start = FlexDayStartBO()
            flex_day_start.set_id(id)
            flex_day_start.set_date_of_last_change(dateoflastchange)
            flex_day_start.set_time(date)
            flex_day_start.set_type(type)
            result = flex_day_start

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
        command = "SELECT id, date_of_last_change, date FROM worktimeapp.flexdaystart WHERE date={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, dateoflastchange, date, type) in tuples:
            flex_day_start = FlexDayStartBO()
            flex_day_start.set_id(id)
            flex_day_start.set_date_of_last_change(dateoflastchange)
            flex_day_start.set_time(date)
            flex_day_start.set_type(type)
            result.append(flex_day_start)

        self._cnx.commit()
        cursor.close()

        return result


    def update(self, flex_day_start):
        datestamp = datetime.today()
        cursor = self._cnx.cursor()
        flex_day_start.set_date_of_last_change(datestamp)

        command = "UPDATE worktimeapp.flexdaystart " + \
                  "SET date=%s WHERE id=%s"
        data = (flex_day_start.get_time(),
                flex_day_start.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return flex_day_start

    def delete(self, flex_day_start):
        cursor = self._cnx.cursor()

        command = "DELETE FROM worktimeapp.flexdaystart WHERE id={}".format(
            flex_day_start.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
