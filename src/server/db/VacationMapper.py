from server.db import TimeIntervalMapper
from server.bo import VacationBO

"""
@author Ha Mi Duong (https://github.com/HamiDuong)

Mapper für VacationBO - Schnittstelle zur Datenbank
Attribute               
id (PK)                     eindeutige Identifikationsnummer                      
dateOfLastChange            Zeitpunkt der letzten Änderung
start                       Startzeitpunkt der Pause
end                         Endzeitpunkt der Pause
timeintervalBookingId (FK)  Zuordnung zu TimeIntervalBooking   
"""
class VacationMapper(TimeIntervalMapper):

    def __init__(self):
        super().__init__()

    """
    Gibt alle VacationBO aus der Datenbank zurück
    return: Liste mit VacationBO (list) - alle Vacation in der Datenbank
    """    
    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * from vacation")
        tuples = cursor.fetchall()

        for (id, dateOfLastChange, start, end, timeIntervalBookingId) in tuples:
            vacation_obj = VacationBO()
            vacation_obj.set_id(id)
            vacation_obj.set_date_of_last_change(dateOfLastChange)
            vacation_obj.set_start(start)
            vacation_obj.set_end(end)
            vacation_obj.set_time_interval_booking_id(timeIntervalBookingId)
            result.append(vacation_obj)

        self._cnx.commit()
        return result

    """
    Gibt das VacationBO mit den gegebener Id zurück
    param: key (int) - Id vom gesuchtem VacationBO
    return: VacationBO mit der Id = key
    """    
    def find_by_key(self, key):
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, dateOfLastChange, start, end, timeIntervalBookingId FROM break WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            (id, dateOfLastChange, start, end, timeIntervalBookingId) = tuples[0]
            vacation_obj = VacationBO()
            vacation_obj.set_id(id)
            vacation_obj.set_date_of_last_change(dateOfLastChange)
            vacation_obj.set_start(start)
            vacation_obj.set_end(end)
            vacation_obj.set_timeinterval_booking_id(timeIntervalBookingId)
            result = vacation_obj

        self._cnx.commit()
        cursor.close()

        return result

    """
    Fügt ein VacationBO in die Datenbank ein
    param: vacation_obj (VacationBO) - VacationBO welches eingefügt werden soll
    return: vacation_obj
    """
    def insert (self, vacation_obj):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM break")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            vacation_obj.set_id(maxid[0]+1)

        command = "INSET INTO break (id, dateOfLastChange, start, end, timeIntervalBookingId) VALUES (%s, %s, %s, %s, %s)"
        data = (vacation_obj.get_id(), vacation_obj.get_date_of_last_change(), vacation_obj.get_start(), vacation_obj. get_end(), vacation_obj.get_timeinterval_booking_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return vacation_obj

    """
    Ändert die Attribute eines VacationBO welches bereits in der Datenbank ist
    param: vacation_obj (VacationBO) - VacationBO mit aktualisierten Daten
    return: None 
    """
    def update (self, vacation_obj):
        cursor = self._cnx.cursor()

        command = "UPDATE break " + "SET start=%s, end=%s WHERE id=%s"
        data = (vacation_obj.get_start(), vacation_obj.get_end(), vacation_obj.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    """
    Löscht ein VacationBO aus der Datenbank
    param: vacation_obj (VacationBO) - VacationBO welches aus der Datenbank gelöscht werden soll
    return: None
    """
    def delete(self, vacation_obj):
        cursor = self._cnx.cursor()

        command = "DELETE FROM break WHERE id={}".format(vacation_obj.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()   
    
    """
    Gibt das VacationBO mit dem gegebenen Startdatum zurück
    param: date (datetime) - Id vom gesuchtem VacationBO
    return: VacationBO mit start = date
    """
    def find_by_date(self, date):
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, dateOfLastChange, start, end, timeIntervalBookingId FROM vacations WHERE start={}".format(date)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            (id, dateOfLastChange, start, end, timeIntervalBookingId) = tuples[0]
            breakobj = VacationBO()
            breakobj.set_id(id)
            breakobj.set_date_of_last_change(dateOfLastChange)
            breakobj.set_start(start)
            breakobj.set_end(end)
            breakobj.set_timeinterval_booking_id(timeIntervalBookingId)
            result = breakobj

        self._cnx.commit()
        cursor.close()
        return result

    """
    Gibt alle VacationBO aus einen angegebenen Zeitraum zurück
    param: start_date (date) - Start des Zeitintervalls
           end_date (date) - Ende des Zeitintervalls
    return: result - alle VacationBO im angegebenen Zeitraum
    """
    def find_by_time_period(self, start_date, end_date):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, dateOfLastChange, start, end, timeIntervalBookingId FROM vacations WHERE start={} AND end={}".format(start_date, end_date)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, dateOfLastChange, start, end, timeIntervalBookingId) in tuples:
            breakobj = VacationBO()
            breakobj.set_id(id)
            breakobj.set_date_of_last_change(dateOfLastChange)
            breakobj.set_start(start)
            breakobj.set_end(end)
            breakobj.set_time_interval_booking_id(timeIntervalBookingId)
            result.append(breakobj)

        self._cnx.commit()
        return result

    """
    Gibt das VacationBO mit gegebener booking_id zurück
    param: bookingId - Fremdschlüssel von BookingBO
    return: result - VacationBO
    """
    def find_by_time_interval_booking_id(self, bookingId):
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, dateOfLastChange, start, end, timeIntervalBookingId FROM vacations WHERE timeIntervallBookingId={}".format(bookingId)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            (id, dateOfLastChange, start, end, timeIntervalBookingId) = tuples[0]
            breakobj = VacationBO()
            breakobj.set_id(id)
            breakobj.set_date_of_last_change(dateOfLastChange)
            breakobj.set_start(start)
            breakobj.set_end(end)
            breakobj.set_timeinterval_booking_id(timeIntervalBookingId)
            result = breakobj

        self._cnx.commit()
        cursor.close()        
        return result