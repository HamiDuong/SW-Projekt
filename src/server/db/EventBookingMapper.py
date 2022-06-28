from server.bo.EventBookingBO import EventBookingBO
from server.db.Mapper import Mapper
from datetime import datetime

'''@author Mihriban Dogan (https://github.com/mihriban-dogan)'''


class EventBookingMapper (Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        """Auslesen aller Event Bookings.
        """
        result = []
        cursor = self._cnx.cursor()
        cursor.execute(
            "SELECT id, dateOfLastChange, eventId from eventbookings")
        tuples = cursor.fetchall()

        for (id, date_of_last_change, event_id) in tuples:
            event_booking = EventBookingBO()
            event_booking.set_id(id)
            event_booking.set_event_id(event_id)
            event_booking.set_date_of_last_change(date_of_last_change)

            result.append(event_booking)

        self._cnx.commit()
        cursor.close()

        return result

    def find_last_entry(self):
        """Auslesen des letzten Eintrags in der EventBooking Tabelle.
        """
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT * FROM eventbookings ORDER BY id DESC LIMIT 1"
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, date_of_last_change, event_id) = tuples[0]
            event_booking = EventBookingBO()
            event_booking.set_id(id)
            event_booking.set_date_of_last_change(date_of_last_change)
            event_booking.set_event_id(event_id)
            result = event_booking
        except IndexError:
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, event_booking):
        """Einfügen eines EventBooking-Objekts in die Datenbank.
        """
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM eventbookings")
        tuples = cursor.fetchall()
        time_stamp = datetime.today()
        event_booking.set_date_of_last_change(time_stamp)

        for (maxid) in tuples:
            if maxid[0] == None:
                event_booking.set_id(1)
            else:
                event_booking.set_id(maxid[0]+1)

        command = "INSERT INTO eventbookings (id, dateOfLastChange, eventId) VALUES (%s,%s,%s)"
        data = (event_booking.get_id(), event_booking.get_date_of_last_change(
        ), event_booking.get_event_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return event_booking

    def update(self, event_booking):
        """Wiederholtes Schreiben eines EventBooking Objekts in die Datenbank.
        """
        time_stamp = datetime.today()
        event_booking.set_date_of_last_change(time_stamp)
        cursor = self._cnx.cursor()

        command = "UPDATE eventbookings " + "SET dateOfLastChange=%s WHERE id=%s"
        data = (event_booking.get_date_of_last_change(),
                event_booking.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, event_booking):
        """Löschen der Daten eines EventBooking-Objekts aus der Datenbank.
        """
        cursor = self._cnx.cursor()

        command = "DELETE FROM eventbookings WHERE id={}".format(
            event_booking.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def find_by_key(self, key):
        """Suchen eines EventBooking Objekts nach der ID.
        """
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, dateOfLastChange, eventId from eventbookings WHERE id={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, date_of_last_change, event_id) = tuples[0]
            event_booking = EventBookingBO()
            event_booking.set_id(id)
            event_booking.set_date_of_last_change(date_of_last_change)
            event_booking.set_event_id(event_id)
            result = event_booking
        except IndexError:
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_event_id(self, key):
        """Auslesen eines EventBooking Objekts nach der EventId"""
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, dateOfLastChange, eventId from eventbookings WHERE eventId={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, date_of_last_change, event_id) = tuples[0]
            event_booking = EventBookingBO()
            event_booking.set_id(id)
            event_booking.set_date_of_last_change(date_of_last_change)
            event_booking.set_event_id(event_id)
            result = event_booking
        except IndexError:
            result = None

        self._cnx.commit()
        cursor.close()

        return result


if (__name__ == "__main__"):
    with EventBookingMapper() as mapper:
        result = mapper.find_all()
        for p in result:
            print(p)
