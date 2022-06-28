from server.bo.TimeIntervalBookingBO import TimeIntervalBookingBO
from server.db.Mapper import Mapper
from datetime import datetime

'''@author Mihriban Dogan (https://github.com/mihriban-dogan)'''


class TimeIntervalBookingMapper (Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        """Auslesen aller Timeinterval Bookings.
        """
        result = []
        cursor = self._cnx.cursor()
        cursor.execute(
            "SELECT id, dateOfLastChange, timeintervalId from timeintervalbookings")
        tuples = cursor.fetchall()

        for (id, date_of_last_change, time_interval_id) in tuples:
            time_interval_booking = TimeIntervalBookingBO()
            time_interval_booking.set_id(id)
            time_interval_booking.set_timeinterval_id(time_interval_id)
            time_interval_booking.set_date_of_last_change(date_of_last_change)

            result.append(time_interval_booking)

        self._cnx.commit()
        cursor.close()

        return result

    def find_last_entry(self):
        """Auslesen des letzten Eintrags in der TimeintervalBooking Tabelle.
        """
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT * FROM timeintervalbookings ORDER BY id DESC LIMIT 1"
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, date_of_last_change, time_interval_id) = tuples[0]
            time_interval_booking = TimeIntervalBookingBO()
            time_interval_booking.set_id(id)
            time_interval_booking.set_date_of_last_change(date_of_last_change)
            time_interval_booking.set_timeinterval_id(time_interval_id)
            result = time_interval_booking
        except IndexError:
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, time_interval_booking):
        """Einfügen eines Timeintervalbooking-Objekts in die Datenbank.
        """
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM timeintervalbookings")
        tuples = cursor.fetchall()
        time_stamp = datetime.today()
        time_interval_booking.set_date_of_last_change(time_stamp)

        for (maxid) in tuples:
            if maxid[0] == None:
                time_interval_booking.set_id(1)
            else:
                time_interval_booking.set_id(maxid[0]+1)

        command = "INSERT INTO timeintervalbookings (id, dateOfLastChange, timeintervalId) VALUES (%s,%s,%s)"
        data = (time_interval_booking.get_id(), time_interval_booking.get_date_of_last_change(
        ), time_interval_booking.get_timeinterval_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return time_interval_booking

    def update(self, time_interval_booking):
        """Wiederholtes Schreiben eines TimeintervalBooking Objekts in die Datenbank.
        """
        time_stamp = datetime.today()
        time_interval_booking.set_date_of_last_change(time_stamp)
        cursor = self._cnx.cursor()

        command = "UPDATE timeintervalbookings " + \
            "SET dateOfLastChange=%s WHERE id=%s"
        data = (time_interval_booking.get_date_of_last_change(),
                time_interval_booking.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, time_interval_booking):
        """Löschen der Daten eines TimeintervalBooking-Objekts aus der Datenbank.
        """

        cursor = self._cnx.cursor()

        command = "DELETE FROM timeintervalbookings WHERE id={}".format(
            time_interval_booking.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def find_by_key(self, key):
        """Suchen eines TimeIntervalBooking Objekts nach der ID.
        """
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, dateOfLastChange, timeintervalId from timeintervalbookings WHERE id={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, date_of_last_change, time_interval_id) = tuples[0]
            time_interval_booking = TimeIntervalBookingBO()
            time_interval_booking.set_id(id)
            time_interval_booking.set_date_of_last_change(date_of_last_change)
            time_interval_booking.set_timeinterval_id(time_interval_id)
            result = time_interval_booking
        except IndexError:
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_timeinterval_id(self, key):
        """Auslesen eines TimeIntervalBooking Objekts nach der TimeintervalId"""
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, dateOfLastChange, timeintervalId from timeintervalbookings WHERE timeIntervalId={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, date_of_last_change, time_interval_id) = tuples[0]
            time_interval_booking = TimeIntervalBookingBO()
            time_interval_booking.set_id(id)
            time_interval_booking.set_date_of_last_change(date_of_last_change)
            time_interval_booking.set_timeinterval_id(time_interval_id)
            result = time_interval_booking
        except IndexError:
            result = None

        self._cnx.commit()
        cursor.close()

        return result


if (__name__ == "__main__"):
    with TimeIntervalBookingMapper() as mapper:
        result = mapper.find_all()
        for p in result:
            print(p)
