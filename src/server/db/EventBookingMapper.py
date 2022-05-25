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

        for (id, dateOfLastChange, eventId) in tuples:
            eventbooking = EventBookingBO()
            eventbooking.set_id(id)
            eventbooking.set_event_id(eventId)
            eventbooking.set_date_of_last_change(dateOfLastChange)

            result.append(eventbooking)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_event_id(self, eventId):
        """ Auslesen aller Bookings nach eventsIds. 
        """
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, dateOfLastChange, eventId from eventbookings WHERE eventId={} ORDER BY id".format(
            eventId)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, dateOfLastChange, eventId) in tuples:
            eventbooking = EventBookingBO()
            eventbooking.set_id(id)
            eventbooking.set_event_id(eventId)
            eventbooking.set_date_of_last_change(dateOfLastChange)

            result.append(eventbooking)

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, eventbooking):
        """Einfügen eines EventBooking-Objekts in die Datenbank.
        """
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM eventbookings")
        tuples = cursor.fetchall()
        timestamp = datetime.today()
        eventbooking.set_date_of_last_change(timestamp)

        for (maxid) in tuples:
            if maxid[0] == None:
                eventbooking.set_id(1)
            else:
                eventbooking.set_id(maxid[0]+1)

        command = "INSERT INTO eventbookings (id, dateOfLastChange, eventId) VALUES (%s,%s,%s)"
        data = (eventbooking.get_id(), eventbooking.get_date_of_last_change(
        ), eventbooking.get_event_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return eventbooking

    def update(self, eventbooking):
        """Wiederholtes Schreiben eines Objekts in die Datenbank.
        """
        timestamp = datetime.today()
        eventbooking.set_date_of_last_change(timestamp)
        cursor = self._cnx.cursor()

        command = "UPDATE eventbookings " + "SET dateOfLastChange=%s WHERE id=%s"
        data = (eventbooking.get_date_of_last_change(),
                eventbooking.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, eventbooking):
        """Löschen der Daten eines Booking-Objekts aus der Datenbank.
        """
        cursor = self._cnx.cursor()

        command = "DELETE FROM eventbookings WHERE id={}".format(
            eventbooking.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def find_by_key(self, key):

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, dateOfLastChange, eventId from eventbookings WHERE id={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, dateOfLastChange, eventId) = tuples[0]
            eventbooking = EventBookingBO()
            eventbooking.set_id(id)
            eventbooking.set_date_of_last_change(dateOfLastChange)
            eventbooking.set_event_id(eventId)
            result = eventbooking
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
