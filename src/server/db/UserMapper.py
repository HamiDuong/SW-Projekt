from server.db.Mapper import Mapper
from server.bo.UserBO import UserBO

"""
@author Marco
@co-author Ha Mi Duong (https://github.com/HamiDuong)
"""
class UserMapper(Mapper):
    def __init__(self):
        super().__init__()

    def insert(self, user):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM worktimeapp.users ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:
                user.set_id(maxid[0] + 1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                user.set_id(1)

        command = "INSERT INTO worktimeapp.users (id, dateOfLastChange, firstName, lastName, mailAdress, googleUserId) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (
            user.get_id(),
            user.get_date_of_last_change(),
            user.get_first_name(),
            user.get_last_name(),
            user.get_mail_adress(),
            user.get_google_user_id()
            )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return user

    def find_all(self):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, dateOfLastChange, firstName, lastName, mailAdress, googleUserId FROM worktimeapp.users"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, dateOfLastChange, firstName, lastName, mailAdress, googleUserId) in tuples:
            user = UserBO()
            user.set_id(id)
            user.set_date_of_last_change(dateOfLastChange)
            user.set_first_name(firstName)
            user.set_last_name(lastName)
            user.set_mail_adress(mailAdress)
            user.set_google_user_id(googleUserId)
            result.append(user)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, dateOfLastChange, firstName, lastName, mailAdress, googleUserId FROM worktimeapp.users WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, dateOfLastChange, firstName, lastName, mailAdress, googleUserId) = tuples[0]
            user = UserBO()
            user.set_id(id)
            user.set_date_of_last_change(dateOfLastChange)
            user.set_first_name(firstName)
            user.set_last_name(lastName)
            user.set_mail_adress(mailAdress)
            user.set_google_user_id(googleUserId)
            result = user
        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    '''    def find_by_name(self, key):
        result = []

        cursor = self._cnx.cursor()
        command = "SELECT id, first_name, last_name, mail_adress, user_name FROM users WHERE name={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, first_name, last_name, mail_adress, user_name) in tuples:
            user = UserBO()
            user.set_id(id)
            user.set_first_name(first_name)
            user.set_last_name(last_name)
            user.set_mail_adress(mail_adress)
            user.set_user_name(user_name)
            result.append(user)

        self._cnx.commit()
        cursor.close()

        return result'''

    def find_by_googleuserid(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT * FROM worktimeapp.users WHERE googleUserId='{}'".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, dateOfLastChange, firstName, lastName, mailAdress, googleUserId) = tuples[0]
            user = UserBO()
            user.set_id(id)
            user.set_date_of_last_change(dateOfLastChange)
            user.set_first_name(firstName)
            user.set_last_name(lastName)
            user.set_mail_adress(mailAdress)
            user.set_google_user_id(googleUserId)
            result = user
        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_mail(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT * FROM worktimeapp.users WHERE mailAdress='{}'".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, dateOfLastChange, firstName, lastName, mailAdress, googleUserId) = tuples[0]
            user = UserBO()
            user.set_id(id)
            user.set_date_of_last_change(dateOfLastChange)
            user.set_first_name(firstName)
            user.set_last_name(lastName)
            user.set_mail_adress(mailAdress)
            user.set_google_user_id(googleUserId)
            result = user
        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    # def find_by_user_name(self, key):
    #     result = []

    #     cursor = self._cnx.cursor()
    #     command = "SELECT id, first_name, last_name, mail_adress, user_name FROM users WHERE user_name={}".format(
    #         key)
    #     cursor.execute(command)
    #     tuples = cursor.fetchall()

    #     for (id, first_name, last_name, mail_adress, user_name) in tuples:
    #         user = UserBO()
    #         user.set_id(id)
    #         user.set_first_name(first_name)
    #         user.set_last_name(last_name)
    #         user.set_mail_adress(mail_adress)
    #         user.set_user_name(user_name)
    #         result.append(user)

    #     self._cnx.commit()
    #     cursor.close()

    #     return result

    def update(self, user):
        cursor = self._cnx.cursor()

        command = "UPDATE worktimeapp.users SET firstName=%s, lastName=%s, mailAdress=%s WHERE id=%s"
        data = (user.get_first_name(), user.get_last_name(), user.get_mail_adress(), user.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return user

    def delete(self, user):
        cursor = self._cnx.cursor()

        command = "DELETE FROM worktimeapp.users WHERE id={}".format(user.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()