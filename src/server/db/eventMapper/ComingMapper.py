from server.db.Mapper import Mapper
from server.bo.eventBOs.ComingBO import ComingBO
from datetime import datetime


class ComingMapper(Mapper):
    def __init__(self):
        super().__init__()

    def insert(self, coming):
        """
        @author Khadidja Kebaili (https://github.com/KhadidjaKebaili)

        Fügt ein ComingBO in die Datenbank ein
        param: coming (ComingBO)
        return: coming
        """
        timestamp = datetime.today()
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM worktimeapp.coming ")
        tuples = cursor.fetchall()
        coming.set_date_of_last_change(timestamp)

        for maxid in tuples:
            if maxid[0] is not None:
                coming.set_id(maxid[0] + 1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                coming.set_id(1)

        command = "INSERT INTO worktimeapp.coming (id, date_of_last_change, date, type) VALUES (%s, %s,%s, %s)"
        data = (
            coming.get_id(),
            coming.get_date_of_last_change(),
            coming.get_time(),
            coming.get_type(),
        )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return coming

    def find_all(self):
        """
        @author Khadidja Kebaili (https://github.com/KhadidjaKebaili)

        Gibt alle ComingBO aus der Datenbank zurück
        return: Liste mit ComingBO (Liste)
        """

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, date, date_of_last_change, type FROM worktimeapp.coming"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, dateoflastchange, date, type) in tuples:
            coming = ComingBO()
            coming.set_id(id)
            coming.set_date_of_last_change(dateoflastchange)
            coming.set_time(date)
            coming.set_type(type)
            result.append(coming)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        """
        @author Khadidja Kebaili (https://github.com/KhadidjaKebaili)

        Gibt das ComingBO mit den gegebener Id zurück
        param: key (int) - Id vom gesuchtem ComingBO
        return: ComingBO mit der eingegebenen Id
        """

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, date_of_last_change, date, type FROM worktimeapp.coming WHERE id={}".format(
            key
        )
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, dateoflastchange, date, type) = tuples[0]
            coming = ComingBO()
            coming.set_id(id)
            coming.set_date_of_last_change(dateoflastchange)
            coming.set_time(date)
            coming.set_type(type)
            result = coming
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

        Gibt das ComingBO mit dem angegebenen Datumzurück
        param: key (int) - Id vom gesuchtem ComingBO
        return: ComingBO mit dem angegebenen Datum
        """

        result = []

        cursor = self._cnx.cursor()
        command = "SELECT id, date_of_last_change, date, type FROM worktimeapp.coming WHERE date={}".format(
            key
        )
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, dateoflastchage, date, type) in tuples:
            coming = ComingBO()
            coming.set_id(id)
            coming.set_date_of_last_change(dateoflastchage)
            coming.set_time(date)
            coming.set_type(type)
            result.append(coming)

        self._cnx.commit()
        cursor.close()

        return result

    def update(self, coming):
        datestamp = datetime.today()
        cursor = self._cnx.cursor()
        coming.set_date_of_last_change(datestamp)

        command = (
            "UPDATE worktimeapp.coming "
            + "SET date_of_last_change=%s, date=%s WHERE id=%s"
        )
        data = (coming.get_date_of_last_change(), coming.get_time(), coming.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return coming

    def delete(self, coming):
        cursor = self._cnx.cursor()

        command = "DELETE FROM worktimeapp.coming WHERE id={}".format(coming.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
