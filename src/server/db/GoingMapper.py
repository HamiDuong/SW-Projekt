from time import time
from server.db.Mapper import Mapper
from server.bo.GoingBO import GoingBO
from datetime import datetime

'''timestamp="NOW()"
insert_data = "INSERT into test (test_date,test1,test2) values (%s,%s,%s)"
cur.execute(insert_data,(test_date,test1,test2,timestamp))'''


class GoingMapper(Mapper):
    def __init__(self):
        super().__init__()

    def insert(self, going):
        timestamp = datetime.today()
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM worktimeapp.going ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:
                going.set_id(maxid[0] + 1)
                going.set_date_of_last_change(timestamp)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                going.set_id(1)
                going.set_date_of_last_change(timestamp)

        command = "INSERT INTO worktimeapp.going (id, dateoflastchange, time, event_booking_id) VALUES ( %s,%s,%s,%s)"
        data = (
            going.get_id(),
            going.get_date_of_last_change(),
            going.get_time(),
            going.get_event_booking_id()
        )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return going

    def find_all(self):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, date_of_last_change, time, event_booking_id FROM worktimeapp.going"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, date_of_last_change, time, event_booking_id) in tuples:
            going = GoingBO()
            going.set_id(id)
            going.set_date_of_last_change(date_of_last_change)
            going.set_time(time)
            going.set_event_booking_id(event_booking_id)
            result.append(going)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, date_of_last_change, time, event_booking_id FROM worktimeapp.going WHERE id={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, date_of_last_change, time, event_booking_id) = tuples[0]
            going = GoingBO()
            going.set_id(id)
            going.set_date_of_last_change(date_of_last_change)
            going.set_time(time)
            going.set_event_booking_id(event_booking_id)
            result = going
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
        command = "SELECT id, time, event_booking_id FROM worktimeapp.going WHERE time={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, date_of_last_change, time, event_booking_id) in tuples:
            going = GoingBO()
            going.set_id(id)
            going.set_date_of_last_change(date_of_last_change)
            going.set_time(time)
            going.set_event_booking_id(event_booking_id)
            result.append(going)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_event_booking_id(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, date_of_last_change, time, event_booking_id FROM worktimeapp.going WHERE chatid={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, date_of_last_change, time, event_booking_id) = tuples[0]
            going = GoingBO()
            going.set_id(id)
            going.set_date_of_last_change(date_of_last_change)
            going.set_time(time)
            going.set_event_booking_id(event_booking_id)
            result = going
        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def update(self, going):
        cursor = self._cnx.cursor()

        command = "UPDATE worktimeapp.going " + \
            "SET date_of_last_change =Current_Time(), time=%s, event_booking_id=%s WHERE id=%s"
        data = (going.get_date_of_last_change(), going.get_time(), going.get_event_booking_id(),
                going.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return going

    def delete(self, going):
        cursor = self._cnx.cursor()

        command = "DELETE FROM worktimeapp.going WHERE id={}".format(
            going.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
