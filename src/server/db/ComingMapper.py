from server.db.Mapper import Mapper
from server.bo.ComingBO import ComingBO


class ComingMapper(Mapper):
    def __init__(self):
        super().__init__()

    def insert(self, coming):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM app.coming ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:
                coming.set_id(maxid[0] + 1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                coming.set_id(1)

        command = "INSERT INTO app.coming (id, time, event_booking_id) VALUES (%s, %s,%s)"
        data = (
            coming.get_id(),
            coming.get_time(),
            coming.get_event_booking_id()
            )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return coming

    def find_all(self):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, time, event_booking_id FROM app.coming"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, time, event_booking_id) in tuples:
            coming = ComingBO()
            coming.set_id(id)
            coming.set_time(time)
            coming.set_event_booking_id(event_booking_id)
            result.append(coming)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, time, event_booking_id FROM app.coming WHERE id={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, time, event_booking_id) = tuples[0]
            coming = ComingBO()
            coming.set_id(id)
            coming.set_time(time)
            coming.set_event_booking_id(event_booking_id)
            result = coming
        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_time(self, key):
        result = []

        cursor = self._cnx.cursor()
        command = "SELECT id, time, event_booking_id FROM app.coming WHERE time={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, time, event_booking_id) in tuples:
            coming = ComingBO()
            coming.set_id(id)
            coming.set_time(time)
            coming.set_event_booking_id(event_booking_id)
            result.append(coming)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_event_booking_id(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, time, event_booking_id FROM app.coming WHERE chatid={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, time, event_booking_id) = tuples[0]
            coming = ComingBO()
            coming.set_id(id)
            coming.set_time(time)
            coming.set_event_booking_id(event_booking_id)
            result = coming
        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def update(self, coming):
        cursor = self._cnx.cursor()

        command = "UPDATE app.coming " + \
            "SET time=%s, event_booking_id=%s WHERE id=%s"
        data = (coming.get_time(), coming.get_event_booking_id(),
                coming.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return coming

    def delete(self, coming):
        cursor = self._cnx.cursor()

        command = "DELETE FROM app.coming WHERE id={}".format(
            coming.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()