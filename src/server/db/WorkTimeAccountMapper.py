from server.db.Mapper import Mapper
from server.bo.WorkTimeAccountBO import WorkTimeAccountBO
from datetime import datetime

"""
@author Marco
@co-author Ha Mi Duong (https://github.com/HamiDuong)
"""


class WorkTimeAccountMapper(Mapper):
    def __init__(self):
        super().__init__()

    def insert(self, account):
        cursor = self._cnx.cursor()
        cursor.execute(
            "SELECT MAX(id) AS maxid FROM worktimeapp.worktimeaccounts ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:
                account.set_id(maxid[0] + 1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                account.set_id(1)

        timestamp = datetime.today()
        account.set_date_of_last_change(timestamp)

        command = "INSERT INTO worktimeapp.worktimeaccounts (id, dateOfLastChange, userId, contractTime, overTime) VALUES (%s, %s, %s, %s, %s)"
        data = (
            account.get_id(),
            account.get_date_of_last_change(),
            account.get_user_id(),
            account.get_contract_time(),
            account.get_overtime(),
        )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return account

    def find_all(self):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, dateOfLastChange, userId, contractTime, overTime FROM worktimeapp.worktimeaccounts"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, dateOfLastChange, userId, contractTime, overTime) in tuples:
            account = WorkTimeAccountBO()
            account.set_id(id)
            account.set_date_of_last_change(dateOfLastChange)
            account.set_user_id(userId)
            account.set_contract_time(contractTime)
            account.set_overtime(overTime)
            result.append(account)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, dateOfLastChange, userId, contractTime, overTime FROM worktimeapp.worktimeaccounts WHERE id={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, dateOfLastChange, userId, contractTime, overTime) = tuples[0]
            account = WorkTimeAccountBO()
            account.set_id(id)
            account.set_date_of_last_change(dateOfLastChange)
            account.set_user_id(userId)
            account.set_contract_time(contractTime)
            account.set_overtime(overTime)
            result = account
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
        command = "SELECT id, dateOfLastChange, userId, contractTime, overTime FROM worktimeapp.worktimeaccounts WHERE user_id={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, dateOfLastChange, userId, contractTime, overTime) in tuples:
            account = WorkTimeAccountBO()
            account.set_id(id)
            account.set_date_of_last_change(dateOfLastChange)
            account.set_user_id(userId)
            account.set_contract_time(contractTime)
            account.set_overtime(overTime)
            result.append(account)

        self._cnx.commit()
        cursor.close()

        return result

    def update(self, account):
        cursor = self._cnx.cursor()

        timestamp = datetime.today()
        account.set_date_of_last_change(timestamp)

        command = "UPDATE worktimeapp.worktimeaccounts SET dateOfLastChange=%s, contractTime=%s, overTime=%s WHERE id=%s"
        data = (account.get_date_of_last_change(), account.get_contract_time(
        ), account.get_overtime(), account.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return account

    def delete(self, account):
        cursor = self._cnx.cursor()

        command = "DELETE FROM worktimeapp.worktimeaccounts WHERE id={}".format(
            account.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
