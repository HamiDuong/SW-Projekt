from server.bo.TimeIntervalBookingBO import TimeIntervalBookingBO
from server.db.Mapper import Mapper
from datetime import datetime


class TimeIntervalBookingMapper (Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        """Auslesen aller Event Bookings.
        """
        result = []
        cursor = self._cnx.cursor()
        cursor.execute(
            "SELECT id, dateOfLastChange, bookingId, timeintervalId from timeintervalbookings")
        tuples = cursor.fetchall()

        for (id, dateOfLastChange, bookingId, timeintervalId) in tuples:
            timeintervalbooking = TimeIntervalBookingBO()
            timeintervalbooking.set_id(id)
            timeintervalbooking.set_booking_id(dateOfLastChange)
            timeintervalbooking.set_timeinterval_id(timeintervalId)
            timeintervalbooking.set_date_of_last_change(bookingId)

            result.append(timeintervalbooking)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_booking_id(self, bookingId):
        """Auslesen aller Event Bookings eines bestimmten Zeitkontos.
        """
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, dateOfLastChange, bookingId, timeintervalId from timeintervalbookings WHERE bookingId={} ORDER BY id".format(
            bookingId)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, dateOfLastChange, bookingId, timeintervalId) in tuples:
            timeintervalbooking = TimeIntervalBookingBO()
            timeintervalbooking.set_id(id)
            timeintervalbooking.set_booking_id(dateOfLastChange)
            timeintervalbooking.set_timeinterval_id(timeintervalId)
            timeintervalbooking.set_date_of_last_change(bookingId)

            result.append(timeintervalbooking)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_timeinterval_id(self, timeintervalId):
        """ Auslesen aller Bookings nach eventsIds. 
        """
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, dateOfLastChange, bookingId, timeintervalId from timeintervalbookings WHERE timeintervalId={} ORDER BY id".format(
            timeintervalId)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, dateOfLastChange, bookingId, timeintervalId) in tuples:
            timeintervalbooking = TimeIntervalBookingBO()
            timeintervalbooking.set_id(id)
            timeintervalbooking.set_booking_id(dateOfLastChange)
            timeintervalbooking.set_timeinterval_id(timeintervalId)
            timeintervalbooking.set_date_of_last_change(bookingId)

            result.append(timeintervalbooking)

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, timeintervalbooking):
        """Einfügen eines timeintervalbooking-Objekts in die Datenbank.
        """
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM timeintervalbookings")
        tuples = cursor.fetchall()
        timestamp = datetime.today()
        timeintervalbooking.set_date_of_last_change(timestamp)

        for (maxid) in tuples:
            if maxid[0] == None:
                timeintervalbooking.set_id(1)
            else:
                timeintervalbooking.set_id(maxid[0]+1)

        command = "INSERT INTO timeintervalbookings (id, dateOfLastChange, bookingId, timeintervalId) VALUES (%s,%s,%s,%s)"
        data = (timeintervalbooking.get_id(), timeintervalbooking.get_date_of_last_change(
        ), timeintervalbooking.get_booking_id(), timeintervalbooking.get_timeinterval_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return timeintervalbooking

    def update(self, timeintervalbooking):
        """Wiederholtes Schreiben eines Objekts in die Datenbank.
        """
        timestamp = datetime.today()
        timeintervalbooking.set_date_of_last_change(timestamp)
        cursor = self._cnx.cursor()

        command = "UPDATE timeintervalbookings " + \
            "SET dateOfLastChange=%s WHERE bookingId=%s"
        data = (timeintervalbooking.get_date_of_last_change(),
                timeintervalbooking.get_booking_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, timeintervalbooking):
        """Löschen der Daten eines Booking-Objekts aus der Datenbank.
        """

        cursor = self._cnx.cursor()

        command = "DELETE FROM timeintervalbookings WHERE bookingId={}".format(
            timeintervalbooking.get_booking_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def find_by_key(self, key):

        result = None

        cursor = self._cnx.cursor()
        command = "id, dateOfLastChange, bookingId, timeintervalId from timeintervalbookings WHERE id={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, dateOfLastChange, bookingId, timeintervalId) = tuples[0]
            timeintervalbooking = TimeIntervalBookingBO()
            timeintervalbooking.set_id(id)
            timeintervalbooking.set_date_of_last_change(dateOfLastChange)
            timeintervalbooking.set_booking_id(bookingId)
            timeintervalbooking.set_timeinterval_id(timeintervalId)
            result = timeintervalbooking
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
