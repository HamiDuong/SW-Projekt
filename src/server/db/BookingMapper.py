from server.bo.BookingBO import BookingBO
from server.db.Mapper import Mapper
from datetime import datetime

'''@author Mihriban Dogan (https://github.com/mihriban-dogan)'''


class BookingMapper (Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        """Auslesen aller Bookings.
        """
        result = []
        cursor = self._cnx.cursor()
        cursor.execute(
            "SELECT id, dateOfLastChange, workTimeAccountId, userId, type, eventBookingId, timeIntervalBookingId from bookings")
        tuples = cursor.fetchall()

        for (id, dateOfLastChange, workTimeAccountId, userId, type, eventBookingId, timeIntervalBookingId) in tuples:
            booking = BookingBO()
            booking.set_id(id)
            booking.set_date_of_last_change(dateOfLastChange)
            booking.set_work_time_account_id(workTimeAccountId)
            booking.set_user_id(userId)
            booking.set_type(type)
            booking.set_event_booking_id(eventBookingId)
            booking.set_time_interval_booking_id(timeIntervalBookingId)
            result.append(booking)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_user_id(self, userId):
        """Auslesen aller Bookings eines bestimmten Users.
        """
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, dateOfLastChange, workTimeAccountId, userId, type, eventBookingId, timeIntervalBookingId FROM bookings WHERE userId={} ORDER BY id".format(
            userId)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, dateOfLastChange, workTimeAccountId, userId, type, eventBookingId, timeIntervalBookingId) in tuples:
            booking = BookingBO()
            booking.set_id(id)
            booking.set_date_of_last_change(dateOfLastChange)
            booking.set_work_time_account_id(workTimeAccountId)
            booking.set_user_id(userId)
            booking.set_type(type)
            booking.set_event_booking_id(eventBookingId)
            booking.set_time_interval_booking_id(timeIntervalBookingId)
            result.append(booking)

        self._cnx.commit()
        cursor.close()

        return result

    def find_timeinterval_bookings_by_user_id(self, userId):
        """Auslesen aller Timeinterval Bookings eines bestimmten Users.
        """
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, dateOfLastChange, workTimeAccountId, userId, type, eventBookingId, timeIntervalBookingId FROM bookings WHERE userId={} AND type='T' ORDER BY id".format(
            userId)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, dateOfLastChange, workTimeAccountId, userId, type, eventBookingId, timeIntervalBookingId) in tuples:
            booking = BookingBO()
            booking.set_id(id)
            booking.set_date_of_last_change(dateOfLastChange)
            booking.set_work_time_account_id(workTimeAccountId)
            booking.set_user_id(userId)
            booking.set_type(type)
            booking.set_event_booking_id(eventBookingId)
            booking.set_time_interval_booking_id(timeIntervalBookingId)
            result.append(booking)

        self._cnx.commit()
        cursor.close()

        return result

    def find_event_bookings_by_user_id(self, userId):
        """Auslesen aller Event Bookings eines bestimmten Users.
        """
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, dateOfLastChange, workTimeAccountId, userId, type, eventBookingId, timeIntervalBookingId FROM bookings WHERE userId={} AND type='E' ORDER BY id".format(
            userId)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, dateOfLastChange, workTimeAccountId, userId, type, eventBookingId, timeIntervalBookingId) in tuples:
            booking = BookingBO()
            booking.set_id(id)
            booking.set_date_of_last_change(dateOfLastChange)
            booking.set_work_time_account_id(workTimeAccountId)
            booking.set_user_id(userId)
            booking.set_type(type)
            booking.set_event_booking_id(eventBookingId)
            booking.set_time_interval_booking_id(timeIntervalBookingId)
            result.append(booking)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_type(self, type):
        """ Auslesen aller Bookings mit einem spezifischen Typ. 
        """

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, dateOfLastChange,workTimeAccountId, userId, type, eventBookingId, timeIntervalBookingId FROM bookings WHERE type='{}' ORDER BY id".format(
            type)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, dateOfLastChange, workTimeAccountId, userId, type, eventBookingId, timeIntervalBookingId) in tuples:
            booking = BookingBO()
            booking.set_id(id)
            booking.set_date_of_last_change(dateOfLastChange)
            booking.set_work_time_account_id(workTimeAccountId)
            booking.set_user_id(userId)
            booking.set_type(type)
            booking.set_event_booking_id(eventBookingId)
            booking.set_time_interval_booking_id(timeIntervalBookingId)
            result.append(booking)

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, booking):
        """Einfügen eines Bookings-Objekts in die Datenbank.
        """
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM bookings")
        tuples = cursor.fetchall()
        timestamp = datetime.today()
        booking.set_date_of_last_change(timestamp)

        for (maxid) in tuples:
            # Wenn kein Datensatz vorhanden ist in der Tababelle dann setze die Id = 1 sonst zähle immer eins drauf
            if maxid[0] == None:
                booking.set_id(1)
            else:
                booking.set_id(maxid[0]+1)

        command = "INSERT INTO bookings (id, dateOfLastChange, workTimeAccountId, userId, type, eventBookingId, timeIntervalBookingId) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        data = (booking.get_id(), booking.get_date_of_last_change(
        ), booking.get_work_time_account_id(), booking.get_user_id(), booking.get_type(), booking.get_event_booking_id(), booking.get_time_interval_booking_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return booking

    def update(self, booking):
        """Wiederholtes Schreiben eines Booking Objekts in die Datenbank.
        """
        timestamp = datetime.today()
        booking.set_date_of_last_change(timestamp)
        cursor = self._cnx.cursor()

        command = "UPDATE bookings " + "SET dateOfLastChange=%s WHERE id=%s"
        data = (booking.get_date_of_last_change(), booking.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, booking):
        """Löschen der Daten eines Booking-Objekts aus der Datenbank.
        """
        cursor = self._cnx.cursor()

        command = "DELETE FROM bookings WHERE id={}".format(booking.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def find_by_key(self, key):
        """Suchen eines Booking Objekts nach der ID.
        """
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, dateOfLastChange, workTimeAccountId, userId, type, eventBookingId, timeIntervalBookingId from bookings WHERE id={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, dateOfLastChange, workTimeAccountId, userId, type,
             eventBookingId, timeIntervalBookingId) = tuples[0]
            booking = BookingBO()
            booking.set_id(id)
            booking.set_date_of_last_change(dateOfLastChange)
            booking.set_work_time_account_id(workTimeAccountId)
            booking.set_user_id(userId)
            booking.set_type(type)
            booking.set_event_booking_id(eventBookingId)
            booking.set_time_interval_booking_id(timeIntervalBookingId)
            result = booking
        except IndexError:
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_booking_by_booking_subclass(self, foreignkey, key, type):
        """Suchen eines Bookings nach Typ und Fremdschlüssel.
        """
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, dateOfLastChange, workTimeAccountId, userId, type, eventBookingId, timeIntervalBookingId from bookings WHERE {}={} AND type='{}'".format(
            foreignkey, key, type)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, dateOfLastChange, workTimeAccountId, userId, type,
             eventBookingId, timeIntervalBookingId) = tuples[0]
            booking = BookingBO()
            booking.set_id(id)
            booking.set_date_of_last_change(dateOfLastChange)
            booking.set_work_time_account_id(workTimeAccountId)
            booking.set_user_id(userId)
            booking.set_type(type)
            booking.set_event_booking_id(eventBookingId)
            booking.set_time_interval_booking_id(timeIntervalBookingId)
            result = booking
        except IndexError:
            result = None

        self._cnx.commit()
        cursor.close()

        return result


if (__name__ == "__main__"):
    with BookingMapper() as mapper:
        result = mapper.find_all()
        for p in result:
            print(p)
