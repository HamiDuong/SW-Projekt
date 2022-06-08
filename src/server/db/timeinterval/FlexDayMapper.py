from server.db.timeinterval.TimeIntervalMapper import TimeIntervalMapper
from server.bo.timeinterval.FlexDayBO import FlexDayBO
from datetime import datetime

"""
@author Ha Mi Duong (https://github.com/HamiDuong)

Mapper für FlexDayBO - Schnittstelle zur Datenbank
Attribute               
id (PK)                     eindeutige Identifikationsnummer                      
dateOfLastChange            Zeitpunkt der letzten Änderung
start                       Startzeitpunkt der Pause
end                         Endzeitpunkt der Pause    
startEvent (FK)             Zuordnung zu FlexDayBegin
endEvent (FK)               Zuordnung zu FlexDayEnd
type                        Art des Intervalls

Verworfen
timeIntervalId (FK)         Zuordnung zu TimeInterval 
"""


class FlexDayMapper(TimeIntervalMapper):

    def __init__(self):
        super().__init__()

    """
    Gibt alle FlexDayBO aus der Datenbank zurück
    return: Liste mit FlexDayBO (list) - alle FlexDayBO in der Datenbank
    """

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute(
            "SELECT id, dateOfLastChange, start, end, startEvent, endEvent, type from worktimeapp.flexdays")
        tuples = cursor.fetchall()

        for (id, dateOfLastChange, start, end, startEvent, endEvent, type) in tuples:
            flexday = FlexDayBO()
            flexday.set_id(id)
            flexday.set_date_of_last_change(dateOfLastChange)
            flexday.set_start(start)
            flexday.set_end(end)
            flexday.set_start_event(startEvent)
            flexday.set_end_event(endEvent)
            flexday.set_type(type)
            result.append(flexday)

        self._cnx.commit()
        return result

    """
    Gibt das FlexDayBO mit den gegebener Id zurück
    param: key (int) - Id vom gesuchtem FlexDayBO
    return: FlexDayBO mit der Id = key
    """

    def find_by_key(self, key):
        result = None
        cursor = self._cnx.cursor()
        #command = "SELECT id, dateOfLastChange, start, end, timeIntervalId, startEvent, endEvent, type from worktimeapp.illnesses WHERE id={}".format(key)
        command = "SELECT id, dateOfLastChange, start, end, startEvent, endEvent, type from worktimeapp.flexdays WHERE id={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            #(id, dateOfLastChange, start, end, timeIntervalId, startEvent, endEvent, type) = tuples[0]
            (id, dateOfLastChange, start, end,
             startEvent, endEvent, type) = tuples[0]
            flexday = FlexDayBO()
            flexday.set_id(id)
            flexday.set_date_of_last_change(dateOfLastChange)
            flexday.set_start(start)
            flexday.set_end(end)
            # illness.set_time_interval_id(timeIntervalId)
            flexday.set_start_event(startEvent)
            flexday.set_end_event(endEvent)
            flexday.set_type(type)
            result = flexday

        self._cnx.commit()
        cursor.close()

        return result

    """
    Fügt ein FlexDayBO in die Datenbank ein
    param: flexday (FlexDayBO) - FlexDayBO welches eingefügt werden soll
    return: flexday
    """

    def insert(self, flexday):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM worktimeapp.flexdays")
        tuples = cursor.fetchall()

        timestamp = datetime.today()
        flexday.set_date_of_last_change(timestamp)

        for (maxid) in tuples:
            if maxid[0] == None:
                flexday.set_id(1)
            else:
                flexday.set_id(maxid[0]+1)

        #command = "INSERT INTO worktimeapp.illnesses (id, dateOfLastChange, start, end, timeIntervalId, startEvent, endEvent, type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        #data = (illness.get_id(), illness.get_date_of_last_change(), illness.get_start(), illness. get_end(), illness.get_timeinterval_id(), illness.get_start_event(), illness.get_end_event(), "Illness")
        command = "INSERT INTO worktimeapp.flexdays (id, dateOfLastChange, start, end, startEvent, endEvent, type) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = (flexday.get_id(), flexday.get_date_of_last_change(), flexday.get_start(
        ), flexday. get_end(), flexday.get_start_event(), flexday.get_end_event(), "Flex Day")

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return flexday

    """
    Ändert die Attribute eines FlexDayBO welches bereits in der Datenbank ist
    param: flexday (FlexDayBO) - FlexDayBO mit aktualisierten Daten
    return: None 
    """

    def update(self, flexday):
        cursor = self._cnx.cursor()

        timestamp = datetime.today()
        flexday.set_date_of_last_change(timestamp)

        command = "UPDATE worktimeapp.flexdays " + \
            "SET dateOfLastChange=%s, start=%s, end=%s WHERE id=%s"
        data = (flexday.get_date_of_last_change(), flexday.get_start(),
                flexday.get_end(), flexday.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    """
    Löscht ein FlexDayBO aus der Datenbank
    param: flexday (FlexDayBO) - FlexDayBO welches aus der Datenbank gelöscht werden soll
    return: None
    """

    def delete(self, flexday):
        cursor = self._cnx.cursor()

        command = "DELETE FROM worktimeapp.flexdays WHERE id={}".format(
            flexday.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    """
    Gibt alle FlexDayBO mit dem gegebenen Startdatum zurück
    param: date (datetime) - Id vom gesuchtem FlexDayBO
    return: Liste von FlexDayBO mit start = date
    """

    def find_by_date(self, date):
        result = None
        cursor = self._cnx.cursor()
        #command = "SELECT id, dateOfLastChange, start, end, timeIntervalId, startEvent, endEvent, type FROM worktimeapp.illnesses WHERE start={}".format(date)
        command = "SELECT id, dateOfLastChange, start, end, startEvent, endEvent, type FROM worktimeapp.flexdays WHERE start={}".format(
            date)
        cursor.execute(command)
        tuples = cursor.fetchall()

        # for (id, dateOfLastChange, start, end, timeIntervalId, startEvent, endEvent, type) in tuples:
        for (id, dateOfLastChange, start, end, startEvent, endEvent, type) in tuples:
            flexday = FlexDayBO()
            flexday.set_id(id)
            flexday.set_date_of_last_change(dateOfLastChange)
            flexday.set_start(start)
            flexday.set_end(end)
            # illness.set_time_interval_id(timeIntervalId)
            flexday.set_start_event(startEvent)
            flexday.set_end_event(endEvent)
            flexday.set_type(type)
            result.append(flexday)

        self._cnx.commit()
        return result

    """
    Gibt alle FlexDayBO aus einen angegebenen Zeitraum zurück
    param: start_date (date) - Start des Zeitintervalls
           end_date (date) - Ende des Zeitintervalls
    return: result - alle FlexDayBOs im angegebenen Zeitraum
    """

    def find_by_time_period(self, start_date, end_date):
        result = []
        cursor = self._cnx.cursor()
        #command = "SELECT id, dateOfLastChange, start, end, timeIntervalId, startEvent, endEvent, type FROM worktimeapp.illnesses WHERE start>={} AND end<={}".format(start_date, end_date)
        command = "SELECT id, dateOfLastChange, start, end, startEvent, endEvent, type FROM worktimeapp.flexdays WHERE start>={} AND end<={}".format(
            start_date, end_date)
        cursor.execute(command)
        tuples = cursor.fetchall()

        # for (id, dateOfLastChange, start, end, timeIntervalId, startEvent, endEvent, type) in tuples:
        for (id, dateOfLastChange, start, end, startEvent, endEvent, type) in tuples:
            flexday = FlexDayBO()
            flexday.set_id(id)
            flexday.set_date_of_last_change(dateOfLastChange)
            flexday.set_start(start)
            flexday.set_end(end)
            # illness.set_time_interval_booking_id(timeIntervalId)
            flexday.set_start_event(startEvent)
            flexday.set_end_event(endEvent)
            flexday.set_type(type)
            result.append(flexday)

        self._cnx.commit()
        return result

    """
    Gibt das FlexDayBO mit gegebener booking_id zurück
    param: bookingId - Fremdschlüssel von BookingBO
    return: result - FlexDayBO
    """
    # def find_by_time_interval_id(self, bookingId):
    #     result = None
    #     cursor = self._cnx.cursor()
    #     command = "SELECT id, dateOfLastChange, start, end, timeIntervalId, startEvent, endEvent, type FROM worktimeapp.illnesses WHERE timeIntervalId={}".format(bookingId)
    #     cursor.execute(command)
    #     tuples = cursor.fetchall()

    #     if tuples[0] is not None:
    #         (id, dateOfLastChange, start, end, timeIntervalId, startEvent, endEvent, type) = tuples[0]
    #         illness = IllnessBO()
    #         illness.set_id(id)
    #         illness.set_date_of_last_change(dateOfLastChange)
    #         illness.set_start(start)
    #         illness.set_end(end)
    #         illness.set_time_interval_id(timeIntervalId)
    #         illness.set_start_event(startEvent)
    #         illness.set_end_event(endEvent)
    #         illness.set_type(type)
    #         result = illness

    #     self._cnx.commit()
    #     cursor.close()
    #     return result
