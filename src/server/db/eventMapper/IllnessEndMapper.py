from server.db.Mapper import Mapper
from server.bo.eventBOs.IllnessEndBO import IllnessEndBO
from datetime import datetime


class IllnessEndMapper(Mapper):
    def __init__(self):
        super().__init__()

    def insert(self, illness_end):
        """
        @author Khadidja Kebaili (https://github.com/KhadidjaKebaili)

        Fügt ein IllnessEndBO in die Datenbank ein
        param: illness_end (IllnessEndBO)
        return: illness_end
        """
        timestamp = datetime.today()
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM worktimeapp.illnessend ")
        tuples = cursor.fetchall()
        illness_end.set_date_of_last_change(timestamp)

        for (maxid) in tuples:
            if maxid[0] is not None:
                illness_end.set_id(maxid[0] + 1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 endnen können."""
                illness_end.set_id(1)

        command = "INSERT INTO worktimeapp.illnessend (id, date_of_last_change, date, type) VALUES (%s, %s,%s, %s)"
        data = (
            illness_end.get_id(),
            illness_end.get_date_of_last_change(),
            illness_end.get_time(),
            illness_end.get_type()
        )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return illness_end

    def find_all(self):
        """
        @author Khadidja Kebaili (https://github.com/KhadidjaKebaili)

        Gibt alle IllnessEndBO aus der Datenbank zurück
        return: Liste mit IllnessEndBO (Liste)
        """

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, date_of_last_change, date, type FROM worktimeapp.illnessend"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, dateoflastchange, date, type) in tuples:
            illness_end = IllnessEndBO()
            illness_end.set_id(id)
            illness_end.set_date_of_last_change(dateoflastchange)
            illness_end.set_time(date)
            illness_end.set_type(type)
            result.append(illness_end)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        """
        @author Khadidja Kebaili (https://github.com/KhadidjaKebaili)

        Gibt das IllnessEndBO mit den gegebener Id zurück
        param: key (int) - Id vom gesuchtem IllnessEndBO
        return: IllnessEndBO mit der eingegebenen Id
        """
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, date_of_last_change, date, type FROM worktimeapp.illnessend WHERE id={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, dateoflastchange, date, type) = tuples[0]
            illness_end = IllnessEndBO()
            illness_end.set_id(id)
            illness_end.set_date_of_last_change(dateoflastchange)
            illness_end.set_time(date)
            illness_end.set_type(type)
            result = illness_end

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

        Gibt das IllnessEndBO mit dem angegebenen Datum zurück
        param: key (int) - Id vom gesuchtem IllnessEndBO
        return: IllnessEndBO mit dem angegebenen Datum Id
        """

        result = []

        cursor = self._cnx.cursor()
        command = "SELECT id, date_of_last_change, date, type FROM worktimeapp.illnessend WHERE date={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, dateoflastchange, date, type) in tuples:
            illness_end = IllnessEndBO()
            illness_end.set_id(id)
            illness_end.set_date_of_last_change(dateoflastchange)
            illness_end.set_time(date)
            illness_end.set_type(type)
            result.append(illness_end)

        self._cnx.commit()
        cursor.close()

        return result

    def update(self, illness_end):
        datestamp = datetime.today()
        cursor = self._cnx.cursor()
        illness_end.set_date_of_last_change(datestamp)

        command = "UPDATE worktimeapp.illnessend " + \
            "SET date_of_last_change=%s, date=%s WHERE id=%s"
        data = (illness_end.get_date_of_last_change(), illness_end.get_time(),
                illness_end.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return illness_end

    def delete(self, illness_end):
        cursor = self._cnx.cursor()

        command = "DELETE FROM worktimeapp.illnessend WHERE id={}".format(
            illness_end.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
