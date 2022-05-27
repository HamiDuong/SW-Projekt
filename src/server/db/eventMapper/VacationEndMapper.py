from server.db.Mapper import Mapper
from server.bo.eventBOs.VacationEndBO import VacationEndBO
from datetime import datetime


class VacationEndMapper(Mapper):
    def __init__(self):
        super().__init__()

    def insert(self, vacation_end):
        timestamp = datetime.today()
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM worktimeapp.VacationEnd ")
        tuples = cursor.fetchall()
        vacation_end.set_date_of_last_change(timestamp)

        for (maxid) in tuples:
            if maxid[0] is not None:
                vacation_end.set_id(maxid[0] + 1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 endnen können."""
                vacation_end.set_id(1)

        command = "INSERT INTO worktimeapp.VacationEnd (id, date_of_last_change, date) VALUES (%s, %s,%s)"
        data = (
            vacation_end.get_id(),
            vacation_end.get_date_of_last_change(),
            vacation_end.get_time(),
        )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return vacation_end

    def find_all(self):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, date FROM worktimeapp.VacationEnd"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, date) in tuples:
            vacation_end = VacationEndBO()
            vacation_end.set_id(id)
            vacation_end.set_time(date)
            result.append(vacation_end)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, date FROM worktimeapp.VacationEnd WHERE id={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, date) = tuples[0]
            vacation_end = VacationEndBO()
            vacation_end.set_id(id)
            vacation_end.set_time(date)
            result = vacation_end
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
        command = "SELECT id, date FROM worktimeapp.VacationEnd WHERE date={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, date) in tuples:
            vacation_end = VacationEndBO()
            vacation_end.set_id(id)
            vacation_end.set_time(date)
            result.append(vacation_end)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_event_booking_id(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, date FROM worktimeapp.VacationEnd WHERE chatid={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, date) = tuples[0]
            vacation_end = VacationEndBO()
            vacation_end.set_id(id)
            vacation_end.set_time(date)
            result = vacation_end
        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def update(self, vacation_end):
        datestamp = datetime.today()
        cursor = self._cnx.cursor()
        vacation_end.set_date_of_last_change(datestamp)

        command = "UPDATE worktimeapp.VacationEnd " + \
            "SET date=%s WHERE id=%s"
        data = (vacation_end.get_time(),
                vacation_end.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return vacation_end

    def delete(self, vacation_end):
        cursor = self._cnx.cursor()

        command = "DELETE FROM worktimeapp.VacationEnd WHERE id={}".format(
            vacation_end.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
