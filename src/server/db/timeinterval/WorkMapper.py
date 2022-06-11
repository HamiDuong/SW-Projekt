from server.db.timeinterval.TimeIntervalMapper import TimeIntervalMapper
from server.bo.timeinterval.WorkBO import WorkBO
from datetime import datetime

"""
@author Ha Mi Duong (https://github.com/HamiDuong)

Mapper für WorkBO - Schnittstelle zur Datenbank
Attribute               
id (PK)                     eindeutige Identifikationsnummer                      
dateOfLastChange            Zeitpunkt der letzten Änderung
start                       Startzeitpunkt der Pause
end                         Endzeitpunkt der Pause   
startEvent (FK)             Zuordnung zu workBegin
endEvent (FK)               Zuordnung zu workEnd
type                        Art des Intervalls

verworfen
timeIntervalId (FK)         Zuordnung zu TimeInterval  
"""


class WorkMapper(TimeIntervalMapper):

    def __init__(self):
        super().__init__()

    """
    Gibt alle WorkBO aus der Datenbank zurück
    return: Liste mit WorkBO (list) - alle WorkBO in der Datenbank
    """

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute(
            "SELECT id, dateOfLastChange, start, end, startEvent, endEvent, type from worktimeapp.works")
        tuples = cursor.fetchall()

        for (id, dateOfLastChange, start, end, startEvent, endEvent, type) in tuples:
            work = WorkBO()
            work.set_id(id)
            work.set_date_of_last_change(dateOfLastChange)
            work.set_start(start)
            work.set_end(end)
            # work.set_time_interval_id(timeIntervalId)
            work.set_start_event(startEvent)
            work.set_end_event(endEvent)
            work.set_type(type)
            result.append(work)

        self._cnx.commit()
        return result

    """
    Gibt das WorkBO mit den gegebener Id zurück
    param: key (int) - Id vom gesuchtem WorkBO
    return: WorkBO mit der Id = key
    """

    def find_by_key(self, key):
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, dateOfLastChange, start, end, startEvent, endEvent, type from worktimeapp.works WHERE id={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            (id, dateOfLastChange, start, end,
             startEvent, endEvent, type) = tuples[0]
            work = WorkBO()
            work.set_id(id)
            work.set_date_of_last_change(dateOfLastChange)
            work.set_start(start)
            work.set_end(end)
            # work.set_time_interval_id(timeIntervalId)
            work.set_start_event(startEvent)
            work.set_end_event(endEvent)
            work.set_type(type)
            result = work

        self._cnx.commit()
        cursor.close()

        return result

    """
    Fügt ein WorkBO in die Datenbank ein
    param: work (WorkBO) - WorkBO welches eingefügt werden soll
    return: work
    """

    def insert(self, work):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM worktimeapp.works")
        tuples = cursor.fetchall()

        timestamp = datetime.today()
        work.set_date_of_last_change(timestamp)

        for (maxid) in tuples:
            if maxid[0] == None:
                work.set_id(1)
            else:
                work.set_id(maxid[0]+1)

        command = "INSERT INTO worktimeapp.works (id, dateOfLastChange, start, end, startEvent, endEvent, type) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = (work.get_id(), work.get_date_of_last_change(), work.get_start(
        ), work. get_end(), work.get_start_event(), work.get_end_event(), "Work")
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return work

    """
    Ändert die Attribute eines WorkBO welches bereits in der Datenbank ist
    param: work (WorkBO) - WorkBO mit aktualisierten Daten
    return: None 
    """

    def update(self, work):
        cursor = self._cnx.cursor()

        timestamp = datetime.today()
        work.set_date_of_last_change(timestamp)

        command = "UPDATE worktimeapp.works " + \
            "SET dateOfLastChange=%s, start=%s, end=%s WHERE id=%s"
        data = (work.get_date_of_last_change(),
                work.get_start(), work.get_end(), work.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return work

    """
    Löscht ein WorkBO aus der Datenbank
    param: work (WorkBO) - WorkBO welches aus der Datenbank gelöscht werden soll
    return: None
    """

    def delete(self, work):
        cursor = self._cnx.cursor()

        command = "DELETE FROM worktimeapp.works WHERE id={}".format(
            work.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    """
    Gibt alle WorkBO mit dem gegebenen Startdatum zurück
    param: date (datetime) - Id vom gesuchtem WorkBO
    return: Liste von WorkBO mit start = date
    """

    def find_by_date(self, date):
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, dateOfLastChange, start, end, startEvent, endEvent, type FROM worktimeapp.works WHERE start={}".format(
            date)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, dateOfLastChange, start, end, startEvent, endEvent, type) in tuples:
            work = WorkBO()
            work.set_id(id)
            work.set_date_of_last_change(dateOfLastChange)
            work.set_start(start)
            work.set_end(end)
            # work.set_time_interval_id(timeIntervalId)
            work.set_start_event(startEvent)
            work.set_end_event(endEvent)
            work.set_type(type)
            result.append(work)

        self._cnx.commit()
        return result

    """
    Gibt alle WorkBO aus einen angegebenen Zeitraum zurück
    param: start_date (date) - Start des Zeitintervalls
           end_date (date) - Ende des Zeitintervalls
    return: result - alle WorkBO im angegebenen Zeitraum
    """

    def find_by_time_period(self, start_date, end_date):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, dateOfLastChange, start, end, startEvent, endEvent, type FROM worktimeapp.works WHERE start>={} AND end<={}".format(
            start_date, end_date)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, dateOfLastChange, start, end, startEvent, endEvent, type) in tuples:
            work = WorkBO()
            work.set_id(id)
            work.set_date_of_last_change(dateOfLastChange)
            work.set_start(start)
            work.set_end(end)
            # work.set_time_interval_booking_id(timeIntervalId)
            work.set_start_event(startEvent)
            work.set_end_event(endEvent)
            work.set_type(type)
            result.append(work)

        self._cnx.commit()
        return result

    """
    Gibt das WorkBO mit gegebener booking_id zurück
    param: bookingId - Fremdschlüssel von BookingBO
    return: result - WorkBO
    """

    def find_by_time_interval_id(self, bookingId):
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, dateOfLastChange, start, end, startEvent, endEvent, type FROM worktimeapp.works WHERE timeIntervalId={}".format(
            bookingId)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            (id, dateOfLastChange, start, end,
             startEvent, endEvent, type) = tuples[0]
            work = WorkBO()
            work.set_id(id)
            work.set_date_of_last_change(dateOfLastChange)
            work.set_start(start)
            work.set_end(end)
            # work.set_time_interval_id(timeIntervalId)
            work.set_start_event(startEvent)
            work.set_end_event(endEvent)
            work.set_type(type)
            result = work

        self._cnx.commit()
        cursor.close()
        return result
