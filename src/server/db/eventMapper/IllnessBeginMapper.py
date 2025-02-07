from server.db.Mapper import Mapper
from server.bo.eventBOs.IllnessBeginBO import IllnessBeginBO
from datetime import datetime


class IllnessBeginMapper(Mapper):
    def __init__(self):
        super().__init__()

    def insert(self, illness_begin):
        """
        @author Khadidja Kebaili (https://github.com/KhadidjaKebaili)

        Fügt ein IllnessBeginBO in die Datenbank ein
        param: illness_begin (IllnessBeginBO)
        return: illness_begin
        """
        timestamp = datetime.today()
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM worktimeapp.illnessbegin ")
        tuples = cursor.fetchall()
        illness_begin.set_date_of_last_change(timestamp)

        for maxid in tuples:
            if maxid[0] is not None:
                illness_begin.set_id(maxid[0] + 1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                illness_begin.set_id(1)

        command = "INSERT INTO worktimeapp.illnessbegin (id, date_of_last_change, date, type) VALUES (%s, %s,%s, %s)"
        data = (
            illness_begin.get_id(),
            illness_begin.get_date_of_last_change(),
            illness_begin.get_time(),
            illness_begin.get_type(),
        )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return illness_begin

    def find_all(self):
        """
        @author Khadidja Kebaili (https://github.com/KhadidjaKebaili)

        Gibt alle IllnessBeginBO aus der Datenbank zurück
        return: Liste mit IllnessBeginBO (Liste)
        """

        result = []
        cursor = self._cnx.cursor()
        command = (
            "SELECT id, date_of_last_change, date, type FROM worktimeapp.illnessbegin"
        )
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, dateoflastchange, date, type) in tuples:
            illness_begin = IllnessBeginBO()
            illness_begin.set_id(id)
            illness_begin.set_date_of_last_change(dateoflastchange)
            illness_begin.set_time(date)
            illness_begin.set_type(type)
            result.append(illness_begin)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        """
        @author Khadidja Kebaili (https://github.com/KhadidjaKebaili)

        Gibt das IllnessBeginBO mit den gegebener Id zurück
        param: key (int) - Id vom gesuchtem IllnessBeginBO
        return: IllnessBeginBO mit der eingegebenen Id
        """

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, date_of_last_change, date, type FROM worktimeapp.illnessbegin WHERE id={}".format(
            key
        )
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, dateoflastchange, date, type) = tuples[0]
            illness_begin = IllnessBeginBO()
            illness_begin.set_id(id)
            illness_begin.set_date_of_last_change(dateoflastchange)
            illness_begin.set_time(date)
            illness_begin.set_type(type)
            result = illness_begin

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

        Gibt das IllnessBeginBO mit dem angegebenen Datum zurück
        param: key (int) - Id vom gesuchtem IllnessBeginBO
        return: IllnessBeginBO mit dem angegebenen Datum Id
        """

        result = []

        cursor = self._cnx.cursor()
        command = "SELECT id, date_of_last_change, date, type FROM worktimeapp.illnessbegin WHERE date={}".format(
            key
        )
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, dateoflastchange, date, type) in tuples:
            illness_begin = IllnessBeginBO()
            illness_begin.set_id(id)
            illness_begin.set_date_of_last_change(dateoflastchange)
            illness_begin.set_time(date)
            illness_begin.set_type(type)
            result.append(illness_begin)

        self._cnx.commit()
        cursor.close()

        return result

    def update(self, illness_begin):
        datestamp = datetime.today()
        cursor = self._cnx.cursor()
        illness_begin.set_date_of_last_change(datestamp)

        command = (
            "UPDATE worktimeapp.illnessbegin "
            + "SET date_of_last_change=%s, date=%s WHERE id=%s"
        )
        data = (
            illness_begin.get_date_of_last_change(),
            illness_begin.get_time(),
            illness_begin.get_id(),
        )
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return illness_begin

    def delete(self, illness_begin):
        cursor = self._cnx.cursor()

        command = "DELETE FROM worktimeapp.illnessbegin WHERE id={}".format(
            illness_begin.get_id()
        )
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
