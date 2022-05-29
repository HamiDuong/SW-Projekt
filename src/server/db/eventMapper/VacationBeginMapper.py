from server.db.Mapper import Mapper
from server.bo.eventBOs.VacationBeginBO import VacationBeginBO
from datetime import datetime


class VacationBeginMapper(Mapper):
    def __init__(self):
        super().__init__()

    def insert(self, vacation_begin):
        timestamp = datetime.today()
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM worktimeapp.vacationbegin ")
        tuples = cursor.fetchall()
        vacation_begin.set_date_of_last_change(timestamp)

        for (maxid) in tuples:
            if maxid[0] is not None:
                vacation_begin.set_id(maxid[0] + 1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                vacation_begin.set_id(1)

        command = "INSERT INTO worktimeapp.VacationBegin (id, date_of_last_change, date, type) VALUES (%s, %s, %s, %s)"
        data = (
            vacation_begin.get_id(),
            vacation_begin.get_date_of_last_change(),
            vacation_begin.get_time(),
            vacation_begin.get_type()
        )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return vacation_begin

    def find_all(self):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, date_of_last_change, date, type FROM worktimeapp.vacationbegin"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, dateoflastchange, date, type) in tuples:
            vacation_begin = VacationBeginBO()
            vacation_begin.set_id(id)
            vacation_begin.set_date_of_last_change(dateoflastchange)
            vacation_begin.set_time(date)
            vacation_begin.set_type(type)
            result.append(vacation_begin)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, date_of_last_change, date, type FROM worktimeapp.vacationbegin WHERE id={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, dateoflastchange, date, type) = tuples[0]
            vacation_begin = VacationBeginBO()
            vacation_begin.set_id(id)
            vacation_begin.set_date_of_last_change(dateoflastchange)
            vacation_begin.set_time(date)
            vacation_begin.set_type(type)
            result = vacation_begin
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
        command = "SELECT id, date_of_last_change, date, type FROM worktimeapp.vacationbegin WHERE date={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, dateoflastchange, date, type) in tuples:
            vacation_begin = VacationBeginBO()
            vacation_begin.set_id(id)
            vacation_begin.set_date_of_last_change(dateoflastchange)
            vacation_begin.set_time(date)
            vacation_begin.set_type(type)
            result.append(vacation_begin)

        self._cnx.commit()
        cursor.close()

        return result

    def update(self, vacation_begin):
        datestamp = datetime.today()
        cursor = self._cnx.cursor()
        vacation_begin.set_date_of_last_change(datestamp)

        command = "UPDATE worktimeapp.vacationbegin " + \
            "SET date=%s WHERE id=%s"
        data = (vacation_begin.get_time(),
                vacation_begin.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return vacation_begin

    def delete(self, vacation_begin):
        cursor = self._cnx.cursor()

        command = "DELETE FROM worktimeapp.vacationbegin WHERE id={}".format(
            vacation_begin.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
