from server.db.timeinterval.TimeIntervalMapper import TimeIntervalMapper
from server.bo.timeinterval.BreakBO import BreakBO
from datetime import datetime

"""
@author Ha Mi Duong (https://github.com/HamiDuong)

Mapper für BreakBO - Schnittstelle zur Datenbank
Attribute               
id (PK)                     eindeutige Identifikationsnummer                      
dateOfLastChange            Zeitpunkt der letzten Änderung
start                       Startzeitpunkt der Pause
end                         Endzeitpunkt der Pause   
startEvent (FK)             Zuordnung zu BreakBegin
endEvent (FK)               Zuordnung zu BreakEnd
type                        Art des Intervalls

Verworfen
timeIntervalId (FK)         Zuordnung zu TimeInterval  
"""


class BreakMapper(TimeIntervalMapper):

    def __init__(self):
        super().__init__()

    """
    Gibt alle BreakBO aus der Datenbank zurück
    return: Liste mit BreakBO (list) - alle BreakBO in der Datenbank
    """

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        #cursor.execute("SELECT id, dateOfLastChange, start, end, timeIntervalId, startEvent, endEvent, type from worktimeapp.breaks")
        cursor.execute(
            "SELECT id, dateOfLastChange, start, end, startEvent, endEvent, type from worktimeapp.breaks")
        tuples = cursor.fetchall()

        # for (id, dateOfLastChange, start, end, timeIntervalId, startEvent, endEvent, type) in tuples:
        for (id, dateOfLastChange, start, end, startEvent, endEvent, type) in tuples:
            breakobj = BreakBO()
            breakobj.set_id(id)
            breakobj.set_date_of_last_change(dateOfLastChange)
            breakobj.set_start(start)
            breakobj.set_end(end)
            # breakobj.set_time_interval_id(timeIntervalId)
            breakobj.set_start_event(startEvent)
            breakobj.set_end_event(endEvent)
            breakobj.set_type(type)
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
        #command = "SELECT id, dateOfLastChange, start, end, timeIntervalId, startEvent, endEvent, type from worktimeapp.breaks WHERE id={}".format(key)
        command = "SELECT id, dateOfLastChange, start, end, startEvent, endEvent, type from worktimeapp.breaks WHERE id={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            #(id, dateOfLastChange, start, end, timeIntervalId, startEvent, endEvent, type) = tuples[0]
            (id, dateOfLastChange, start, end,
             startEvent, endEvent, type) = tuples[0]
            breakobj = BreakBO()
            breakobj.set_id(id)
            breakobj.set_date_of_last_change(dateOfLastChange)
            breakobj.set_start(start)
            breakobj.set_end(end)
            # breakobj.set_time_interval_id(timeIntervalId)
            breakobj.set_start_event(startEvent)
            breakobj.set_end_event(endEvent)
            breakobj.set_type(type)
            result = breakobj

        self._cnx.commit()
        cursor.close()

        return result

    """
    Fügt ein BreakBO in die Datenbank ein
    param: breakobj (BreakBO) - BreakBO welches eingefügt werden soll
    return: breakobj
    """

    def insert(self, breakobj):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM worktimeapp.breaks")
        tuples = cursor.fetchall()

        timestamp = datetime.today()
        breakobj.set_date_of_last_change(timestamp)

        for (maxid) in tuples:
            if maxid[0] == None:
                breakobj.set_id(1)
            else:
                breakobj.set_id(maxid[0]+1)

        #command = "INSERT INTO worktimeapp.breaks (id, dateOfLastChange, start, end, timeIntervalId, startEvent, endEvent, type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        #data = (breakobj.get_id(), breakobj.get_date_of_last_change(), breakobj.get_start(), breakobj. get_end(), breakobj.get_timeinterval_id(), breakobj.get_start_event(), breakobj.get_end_event(), "Break")
        command = "INSERT INTO worktimeapp.breaks (id, dateOfLastChange, start, end, startEvent, endEvent, type) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = (breakobj.get_id(), breakobj.get_date_of_last_change(), breakobj.get_start(
        ), breakobj. get_end(), breakobj.get_start_event(), breakobj.get_end_event(), "Break")

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return breakobj

    """
    Ändert die Attribute eines BreakBO welches bereits in der Datenbank ist
    param: breakobj (BreakBO) - BreakBO mit aktualisierten Daten
    return: None 
    """

    def update(self, breakobj):
        cursor = self._cnx.cursor()

        timestamp = datetime.today()
        breakobj.set_date_of_last_change(timestamp)

        command = "UPDATE worktimeapp.breaks " + \
            "SET dateOfLastChange=%s, start=%s, end=%s WHERE id=%s"
        data = (breakobj.get_date_of_last_change(),
                breakobj.get_start(), breakobj.get_end(), breakobj.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    """
    Löscht ein BreakBO aus der Datenbank
    param: breakobj (BreakBO) - BreakBO welches aus der Datenbank gelöscht werden soll
    return: None
    """

    def delete(self, breakobj):
        cursor = self._cnx.cursor()

        command = "DELETE FROM worktimeapp.breaks WHERE id={}".format(
            breakobj.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    """
    Gibt alle BreakBO mit dem gegebenen Startdatum zurück
    param: date (datetime) - Id vom gesuchtem BreakBO
    return: Liste von BreakBO mit start = date
    """

    def find_by_date(self, date):
        result = None
        cursor = self._cnx.cursor()
        #command = "SELECT id, dateOfLastChange, start, end, timeIntervalId, startEvent, endEvent, type FROM worktimeapp.breaks WHERE start={}".format(date)
        command = "SELECT id, dateOfLastChange, start, end, startEvent, endEvent, type FROM worktimeapp.breaks WHERE start={}".format(
            date)
        cursor.execute(command)
        tuples = cursor.fetchall()

        # for (id, dateOfLastChange, start, end, timeIntervalId, startEvent, endEvent, type) in tuples:
        for (id, dateOfLastChange, start, end, startEvent, endEvent, type) in tuples:
            breakobj = BreakBO()
            breakobj.set_id(id)
            breakobj.set_date_of_last_change(dateOfLastChange)
            breakobj.set_start(start)
            breakobj.set_end(end)
            # breakobj.set_time_interval_id(timeIntervalId)
            breakobj.set_start_event(startEvent)
            breakobj.set_end_event(endEvent)
            breakobj.set_type(type)
            result.append(breakobj)

        self._cnx.commit()
        return result

    """
    Gibt alle BreakBO aus einen angegebenen Zeitraum zurück
    param: start_date (date) - Start des Zeitintervalls
           end_date (date) - Ende des Zeitintervalls
    return: result - alle BreakBO im angegebenen Zeitraum
    """

    def find_by_time_period(self, start_date, end_date):
        result = []
        cursor = self._cnx.cursor()
        #command = "SELECT id, dateOfLastChange, start, end, timeIntervalId, startEvent, endEvent, type FROM worktimeapp.breaks WHERE start>={} AND end<={}".format(start_date, end_date)
        command = "SELECT id, dateOfLastChange, start, end, startEvent, endEvent, type FROM worktimeapp.breaks WHERE start>={} AND end<={}".format(
            start_date, end_date)
        cursor.execute(command)
        tuples = cursor.fetchall()

        # for (id, dateOfLastChange, start, end, timeIntervalId, startEvent, endEvent, type) in tuples:
        for (id, dateOfLastChange, start, end, startEvent, endEvent, type) in tuples:
            breakobj = BreakBO()
            breakobj.set_id(id)
            breakobj.set_date_of_last_change(dateOfLastChange)
            breakobj.set_start(start)
            breakobj.set_end(end)
            # breakobj.set_time_interval_id(timeIntervalId)
            breakobj.set_start_event(startEvent)
            breakobj.set_end_event(endEvent)
            breakobj.set_type(type)
            result.append(breakobj)

        self._cnx.commit()
        return result

    """
    Gibt das BreakBO mit gegebener booking_id zurück
    param: bookingId - Fremdschlüssel von BookingBO
    return: result - BreakBO
    """
    # def find_by_time_interval_id(self, bookingId):
    #     result = None
    #     cursor = self._cnx.cursor()
    #     command = "SELECT id, dateOfLastChange, start, end, timeIntervalId startEvent, endEvent, type FROM worktimeapp.breaks WHERE timeIntervalId={}".format(bookingId)
    #     cursor.execute(command)
    #     tuples = cursor.fetchall()

    #     if tuples[0] is not None:
    #         (id, dateOfLastChange, start, end, timeIntervalId, startEvent, endEvent, type) = tuples[0]
    #         breakobj = BreakBO()
    #         breakobj.set_id(id)
    #         breakobj.set_date_of_last_change(dateOfLastChange)
    #         breakobj.set_start(start)
    #         breakobj.set_end(end)
    #         breakobj.set_time_interval_id(timeIntervalId)
    #         breakobj.set_start_event(startEvent)
    #         breakobj.set_end_event(endEvent)
    #         breakobj.set_type(type)
    #         result = breakobj

    #     self._cnx.commit()
    #     cursor.close()
    #     return result
