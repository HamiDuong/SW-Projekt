from server.db.Mapper import Mapper
from server.bo.EventBO import EventBO
from datetime import datetime


class EventMapper(Mapper):
    def __init__(self):
        super().__init__()

    def insert(self, event):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM worktimeapp.event ")
        tuples = cursor.fetchall()
        timestamp = datetime.today()
        '''Wann immer ein neues Objekt in die Datenbank überführt wird, wird ein Zeitstempel erstellt
            und in die Spalte date_of_last_change eingefügt.'''
        event.set_date_of_last_change(timestamp)

        for (maxid) in tuples:
            if maxid[0] is not None:
                event.set_id(maxid[0] + 1)

            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                event.set_id(1)

        command = "INSERT INTO worktimeapp.event (id, dateoflastchange, time) VALUES (%s, %s,%s)"
        data = (
            event.get_id(),
            event.get_date_of_last_change(),
            event.get_time()
        )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return event

    def find_all(self):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, dateoflastchange, time FROM worktimeapp.event"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, dateoflastange, time) in tuples:
            event = EventBO()
            event.set_id(id)
            event.set_date_of_last_change(dateoflastange)
            event.set_time(time)
            result.append(event)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, dateoflastchange, time FROM worktimeapp.event WHERE id={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, dateoflastchange, time) = tuples[0]
            event = EventBO()
            event.set_id(id)
            event.set_date_of_last_change(dateoflastchange)
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
        command = "SELECT id, dateoflastchange, time FROM worktimeapp.event WHERE time={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, dateoflastchange, time) in tuples:
            event = EventBO()
            event.set_id(id)
            event.set_date_of_last_change(dateoflastchange)
            event.set_time(time)
            result.append(event)

        self._cnx.commit()
        cursor.close()

        return result

    def update(self, event):
        cursor = self._cnx.cursor()
        timestamp = datetime.today()
        '''Wann immer ein vorhandenes Objekt in der Datenbank geändert wird, wird ein Zeitstempel erstellt
           und in die Spalte date_of_last_change eingefügt.'''
        event.set_date_of_last_change(timestamp)

        command = "UPDATE worktimeapp.event " + \
            "SET time=%s WHERE id=%s"
        data = (event.get_date_of_last_change, event.get_time,
                event.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return event

    def delete(self, event):
        cursor = self._cnx.cursor()

        command = "DELETE FROM worktimeapp.event WHERE id={}".format(
            event.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
