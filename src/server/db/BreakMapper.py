from server.db import Mapper
from server.bo import BreakBO

"""
@author Ha Mi Duong (https://github.com/HamiDuong)

Mapper für BreakBO - Schnittstelle zur Datenbank
Attribute               
id (PK)                     eindeutige Identifikationsnummer                      
dateOfLastChange            Zeitpunkt der letzten Änderung
start                       Startzeitpunkt der Pause
end                         Endzeitpunkt der Pause
timeintervalBookingId (FK)  Zuordnung zu TimeIntervalBooking   
"""
class BreakMapper(Mapper):

    def __init__(self):
        super().__init__()

    """
    Gibt alle BreakBO aus der Datenbank zurück
    return: Liste mit BreakBO (list) - alle BreakBO in der Datenbank
    """    
    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * from break")
        tuples = cursor.fetchall()

        for (id, dateOfLastChange, start, end, timeIntervalBookingId) in tuples:
            breakobj = BreakBO()
            breakobj.set_id(id)
            breakobj.set_date_of_last_change(dateOfLastChange)
            breakobj.set_start(start)
            breakobj.set_end(end)
            breakobj.set_time_interval_booking_id(timeIntervalBookingId)
            result.append(breakobj)

        self._cnx.commit()
        return result

    """
    Gibt das BreakBO mit den gegebener Id zurück
    param: key (int) - Id vom gesuchtem BreakBO
    return: BreakBO mit der Id = key
    """    
    def find_by_key(self, key):
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, dateOfLastChange, start, end, timeIntervalBookingId FROM break WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            (id, dateOfLastChange, start, end, timeIntervalBookingId) = tuples[0]
            breakobj = BreakBO()
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
    Fügt ein BreakBO in die Datenbank ein
    param: break_obj (BreakBO) - BreakBO welches eingefügt werden soll
    return: break_obj
    """
    def insert (self, break_obj):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM break")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            break_obj.set_id(maxid[0]+1)

        command = "INSET INTO break (id, dateOfLastChange, start, end, timeIntervalBookingId) VALUES (%s, %s, %s, %s, %s)"
        data = (break_obj.get_id(), break_obj.get_date_of_last_change(), break_obj.get_start(), break_obj. get_end(), break_obj.get_timeinterval_booking_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return break_obj

    """
    Ändert die Attribute eines BreakBO welches bereits in der Datenbank ist
    param: break_obj (BreakBO) - BreakBO mit aktualisierten Daten
    return: None 
    """
    def update (self, break_obj):
        cursor = self._cnx.cursor()

        command = "UPDATE break " + "SET start=%s, end=%s WHERE id=%s"
        data = (break_obj.get_start(), break_obj.get_end(), break_obj.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    """
    Löscht ein BreakBO aus der Datenbank
    param: break_obj (BreakBO) - BreakBO welches aus der Datenbank gelöscht werden soll
    return: None
    """
    def delete(self, break_obj):
        cursor = self._cnx.cursor()

        command = "DELETE FROM break WHERE id={}".format(break_obj.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()   