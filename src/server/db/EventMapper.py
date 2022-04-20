from server.db.Mapper import Mapper
from server.bo.EventBO import EventBO


class EventMapper(Mapper):
    def __init__(self):
        super().__init__()

    def insert(self, event):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM app.event ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:
                event.set_id(maxid[0] + 1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                event.set_id(1)

        command = "INSERT INTO app.event (id, eventname, time) VALUES (%s, %s,%s)"
        data = (
            event.get_id(),
            event.get_event_boooking_id(),
            event.get_time()
        )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return event

    def find_all(self):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, eventname, time FROM app.event"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, eventname, time) in tuples:
            event = EventBO()
            event.set_id(id)
            event.set_eventname(eventname)
            event.set_time(time)
            result.append(event)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, eventname, time FROM app.event WHERE id={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, eventname, admin, time) = tuples[0]
            event = EventBO()
            event.set_id(id)
            event.set_eventname(eventname)
            event.set_time(time)
            result = event
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
        command = "SELECT id, eventname, time FROM app.event WHERE time={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, eventname, time) in tuples:
            event = EventBO()
            event.set_id(id)
            event.set_eventname(eventname)
            event.set_time(time)
            result.append(event)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_chatid(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, time FROM app.event WHERE chatid={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, eventname, time) = tuples[0]
            event = EventBO()
            event.set_id(id)
            event.set_eventname(eventname)
            event.set_time(time)
            result = event
        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def update(self, event):
        cursor = self._cnx.cursor()

        command = "UPDATE app.event " + \
            "SET eventname=%s, time=%s WHERE id=%s"
        data = (event.get_eventname(), event.get_time,
                event.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return event

    def delete(self, event):
        cursor = self._cnx.cursor()

        command = "DELETE FROM app.event WHERE id={}".format(
            event.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
