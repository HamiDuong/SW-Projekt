from server.db.Mapper import Mapper
from server.bo.UserBO import UserBO

class UserMapper(Mapper):
    def __init__(self):
        super().__init__()

    def insert(self, event):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM users ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:
                event.set_id(maxid[0] + 1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                event.set_id(1)

        command = "INSERT INTO users (id, first_name, last_name, mail_adress, user_name) VALUES (%s, %s, %s, %s, %s)"
        data = (
            event.get_id(),
            event.get_first_name(),
            event.get_last_name(),
            event.get_mail_adress(),
            event.get_user_name
            )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return event

    def find_all(self):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, first_name, last_name, mail_adress, user_name FROM users"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, first_name, last_name, mail_adress, user_name) in tuples:
            event = UserBO()
            event.set_id(id)
            event.set_first_name(first_name)
            event.set_last_name(last_name)
            event.set_mail_adress(mail_adress)
            event.set_user_name(user_name)
            result.append(event)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, first_name, last_name, mail_adress, user_name FROM users WHERE id={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, first_name, last_name, mail_adress, user_name) = tuples[0]
            event = UserBO()
            event.set_id(id)
            event.set_first_name(first_name)
            event.set_last_name(last_name)
            event.set_mail_adress(mail_adress)
            event.set_user_name(user_name)
            result = event
        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_name(self, key):
        result = []

        cursor = self._cnx.cursor()
        command = "SELECT id, first_name, last_name, mail_adress, user_name FROM users WHERE name={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, first_name, last_name, mail_adress, user_name) in tuples:
            event = UserBO()
            event.set_id(id)
            event.set_first_name(first_name)
            event.set_last_name(last_name)
            event.set_mail_adress(mail_adress)
            event.set_user_name(user_name)
            result.append(event)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_googleuserid(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, first_name, last_name, mail_adress, user_name FROM users WHERE googleuserid={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, first_name, last_name, mail_adress, user_name) = tuples[0]
            event = UserBO()
            event.set_id(id)
            event.set_first_name(first_name)
            event.set_last_name(last_name)
            event.set_mail_adress(mail_adress)
            event.set_user_name(user_name)
            result = event
        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_email(self, key):
        result = []

        cursor = self._cnx.cursor()
        command = "SELECT id, first_name, last_name, mail_adress, user_name FROM users WHERE email={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, first_name, last_name, mail_adress, user_name) in tuples:
            event = UserBO()
            event.set_id(id)
            event.set_first_name(first_name)
            event.set_last_name(last_name)
            event.set_mail_adress(mail_adress)
            event.set_user_name(user_name)
            result.append(event)

        self._cnx.commit()
        cursor.close()

        return result

    def update(self, event):
        cursor = self._cnx.cursor()

        command = "UPDATE users " + \
            "SET first_name=%s, last_name=%s, mail_adress=%s, user_name=%s WHERE id=%s"
        data = (event.get_first_name(), event.get_last_name(), event.get_mail_adress(), event.get_user_name(),
                event.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return event

    def delete(self, event):
        cursor = self._cnx.cursor()

        command = "DELETE FROM users WHERE id={}".format(
            event.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()