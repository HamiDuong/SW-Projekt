from server.db.Mapper import Mapper
from server.bo.WorkTimeAccountBO import WorkTimeAccountBO

class WorkTimeAccountMapper(Mapper):
    def __init__(self):
        super().__init__()

    def insert(self, event):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM worktimeaccount ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:
                event.set_id(maxid[0] + 1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                event.set_id(1)

        command = "INSERT INTO worktimeaccount (id, user_id) VALUES (%s, %s,)"
        data = (
            event.get_id(),
            event.get_user_id()
            )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return event

    def find_all(self):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, user_id FROM worktimeaccount"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, user_id) in tuples:
            event = WorkTimeAccountBO()
            event.set_id(id)
            event.set_user_id(user_id)
            result.append(event)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, user_id FROM worktimeaccount WHERE id={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, user_id) = tuples[0]
            event = WorkTimeAccountBO()
            event.set_id(id)
            event.set_user_id(user_id)
            result = event
        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_user_id(self, key):
        result = []

        cursor = self._cnx.cursor()
        command = "SELECT id, user_id FROM worktimeaccount WHERE user_id={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, user_id) in tuples:
            event = WorkTimeAccountBO()
            event.set_id(id)
            event.set_user_id(user_id)
            result.append(event)

        self._cnx.commit()
        cursor.close()

        return result

    def update(self, event):
        cursor = self._cnx.cursor()

        command = "UPDATE worktimeaccount " + \
            "SET user_id=%s WHERE id=%s"
        data = (event.get_user_id(),
                event.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return event

    def delete(self, event):
        cursor = self._cnx.cursor()

        command = "DELETE FROM worktimeaccount WHERE id={}".format(
            event.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()