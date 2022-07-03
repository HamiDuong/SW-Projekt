from server.db.Mapper import Mapper
from server.bo.eventBOs.VacationEndBO import VacationEndBO
from datetime import datetime


class VacationEndMapper(Mapper):
    def __init__(self):
        super().__init__()

    def insert(self, vacation_end):
        """
        @author Khadidja Kebaili (https://github.com/KhadidjaKebaili)

        Fügt ein VacationEndBO in die Datenbank ein
        param: vacation_end (VacationEndBO)
        return: vacation_end
        """

        timestamp = datetime.today()
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM worktimeapp.vacationend ")
        tuples = cursor.fetchall()
        vacation_end.set_date_of_last_change(timestamp)

        for maxid in tuples:
            if maxid[0] is not None:
                vacation_end.set_id(maxid[0] + 1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 endnen können."""
                vacation_end.set_id(1)

        command = "INSERT INTO worktimeapp.vacationend (id, date_of_last_change, date, type) VALUES (%s, %s,%s, %s)"
        data = (
            vacation_end.get_id(),
            vacation_end.get_date_of_last_change(),
            vacation_end.get_time(),
            vacation_end.get_type(),
        )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return vacation_end

    def find_all(self):
        """
        @author Khadidja Kebaili (https://github.com/KhadidjaKebaili)

        Gibt alle VacationEndBO aus der Datenbank zurück
        return: Liste mit VacationEndBO (Liste)
        """

        result = []
        cursor = self._cnx.cursor()
        command = (
            "SELECT id, date_of_last_change, date, type FROM worktimeapp.vacationend"
        )
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, dateoflastchange, date, type) in tuples:
            vacation_end = VacationEndBO()
            vacation_end.set_id(id)
            vacation_end.set_date_of_last_change(dateoflastchange)
            vacation_end.set_time(date)
            vacation_end.set_type(type)
            result.append(vacation_end)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        """
        @author Khadidja Kebaili (https://github.com/KhadidjaKebaili)

        Gibt das VacationEndBO mit den gegebener Id zurück
        param: key (int) - Id vom gesuchtem VacationEndBO
        return: VacationEndBO mit der eingegebenen Id
        """

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, date_of_last_change, date, type FROM worktimeapp.vacationend WHERE id={}".format(
            key
        )
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, dateoflastchange, date, type) = tuples[0]
            vacation_end = VacationEndBO()
            vacation_end.set_id(id)
            vacation_end.set_date_of_last_change(dateoflastchange)
            vacation_end.set_time(date)
            vacation_end.set_type(type)
            result = vacation_end

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_date(self, key):
        """
        @author Khadidja Kebaili (https://github.com/KhadidjaKebaili)

        Gibt das VacationEndBO mit den gegebener Id zurück
        param: key (int) - Datum des gesuchten VacationEndBO
        return: VacationEndBO mit dem eingegebenen Datum
        """

        result = []

        cursor = self._cnx.cursor()
        command = "SELECT id, date_of_last_change, date, type FROM worktimeapp.vacationend WHERE date={}".format(
            key
        )
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, dateoflastchange, date, type) in tuples:
            vacation_end = VacationEndBO()
            vacation_end.set_id(id)
            vacation_end.set_date_of_last_change(dateoflastchange)
            vacation_end.set_time(date)
            vacation_end.set_type(type)
            result.append(vacation_end)

        self._cnx.commit()
        cursor.close()

        return result

    def update(self, vacation_end):
        datestamp = datetime.today()
        cursor = self._cnx.cursor()
        vacation_end.set_date_of_last_change(datestamp)

        command = (
            "UPDATE worktimeapp.vacationend "
            + "SET date_of_last_change=%s, date=%s WHERE id=%s"
        )
        data = (
            vacation_end.get_date_of_last_change(),
            vacation_end.get_time(),
            vacation_end.get_id(),
        )
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return vacation_end

    def delete(self, vacation_end):
        cursor = self._cnx.cursor()

        command = "DELETE FROM worktimeapp.vacationend WHERE id={}".format(
            vacation_end.get_id()
        )
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
