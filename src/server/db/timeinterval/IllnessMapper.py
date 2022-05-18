from server.db.timeinterval.TimeIntervalMapper import TimeIntervalMapper
from server.bo.timeinterval.IllnessBO import IllnessBO
from datetime import datetime

"""
@author Ha Mi Duong (https://github.com/HamiDuong)

Mapper für IllnessBO - Schnittstelle zur Datenbank
Attribute               
id (PK)                     eindeutige Identifikationsnummer                      
dateOfLastChange            Zeitpunkt der letzten Änderung
start                       Startzeitpunkt der Pause
end                         Endzeitpunkt der Pause    
startEvent (FK)             Zuordnung zu IllnessBegin
endEvent (FK)               Zuordnung zu IllnessEnd
type                        Art des Intervalls

Verworfen
timeIntervalId (FK)         Zuordnung zu TimeInterval 
"""
class IllnessMapper(TimeIntervalMapper):

    def __init__(self):
        super().__init__()

    """
    Gibt alle IllnessBO aus der Datenbank zurück
    return: Liste mit IllnessBO (list) - alle IllnessBO in der Datenbank
    """    
    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT id, dateOfLastChange, start, end, startEvent, endEvent, type from worktimeapp.illnesses")
        tuples = cursor.fetchall()

        for (id, dateOfLastChange, start, end, startEvent, endEvent, type) in tuples:
            illness = IllnessBO()
            illness.set_id(id)
            illness.set_date_of_last_change(dateOfLastChange)
            illness.set_start(start)
            illness.set_end(end)
            illness.set_start_event(startEvent)
            illness.set_end_event(endEvent)
            illness.set_type(type)
            result.append(illness)

        self._cnx.commit()
        return result

    """
    Gibt das IllnessBO mit den gegebener Id zurück
    param: key (int) - Id vom gesuchtem IllnessBO
    return: IllnessBO mit der Id = key
    """    
    def find_by_key(self, key):
        result = None
        cursor = self._cnx.cursor()
        #command = "SELECT id, dateOfLastChange, start, end, timeIntervalId, startEvent, endEvent, type from worktimeapp.illnesses WHERE id={}".format(key)
        command = "SELECT id, dateOfLastChange, start, end, startEvent, endEvent, type from worktimeapp.illnesses WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            #(id, dateOfLastChange, start, end, timeIntervalId, startEvent, endEvent, type) = tuples[0]
            (id, dateOfLastChange, start, end, startEvent, endEvent, type) = tuples[0]
            illness = IllnessBO()
            illness.set_id(id)
            illness.set_date_of_last_change(dateOfLastChange)
            illness.set_start(start)
            illness.set_end(end)
            #illness.set_time_interval_id(timeIntervalId)
            illness.set_start_event(startEvent)
            illness.set_end_event(endEvent)
            illness.set_type(type)
            result = illness

        self._cnx.commit()
        cursor.close()

        return result

    """
    Fügt ein IllnessBO in die Datenbank ein
    param: illness (IllnessBO) - IllnessBO welches eingefügt werden soll
    return: illness
    """
    def insert (self, illness):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM worktimeapp.illnesses")
        tuples = cursor.fetchall()

        timestamp = datetime.today()
        illness.set_date_of_last_change(timestamp)

        for (maxid) in tuples:
            illness.set_id(maxid[0]+1)

        #command = "INSERT INTO worktimeapp.illnesses (id, dateOfLastChange, start, end, timeIntervalId, startEvent, endEvent, type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        #data = (illness.get_id(), illness.get_date_of_last_change(), illness.get_start(), illness. get_end(), illness.get_timeinterval_id(), illness.get_start_event(), illness.get_end_event(), "Illness")
        command = "INSERT INTO worktimeapp.illnesses (id, dateOfLastChange, start, end, startEvent, endEvent, type) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = (illness.get_id(), illness.get_date_of_last_change(), illness.get_start(), illness. get_end(), illness.get_start_event(), illness.get_end_event(), "Illness")

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return illness

    """
    Ändert die Attribute eines IllnessBO welches bereits in der Datenbank ist
    param: illness (IllnessBO) - IllnessBO mit aktualisierten Daten
    return: None 
    """
    def update (self, illness):
        cursor = self._cnx.cursor()

        timestamp = datetime.today()
        illness.set_date_of_last_change(timestamp)

        command = "UPDATE worktimeapp.illnesses " + "SET start=%s, end=%s WHERE id=%s"
        data = (illness.get_start(), illness.get_end(), illness.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    """
    Löscht ein IllnessBO aus der Datenbank
    param: illness (IllnessBO) - IllnessBO welches aus der Datenbank gelöscht werden soll
    return: None
    """
    def delete(self, illness):
        cursor = self._cnx.cursor()

        command = "DELETE FROM worktimeapp.illnesses WHERE id={}".format(illness.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()   

    """
    Gibt alle IllnessBO mit dem gegebenen Startdatum zurück
    param: date (datetime) - Id vom gesuchtem IllnessBO
    return: Liste von IllnessBO mit start = date
    """
    def find_by_date(self, date):
        result = None
        cursor = self._cnx.cursor()
        #command = "SELECT id, dateOfLastChange, start, end, timeIntervalId, startEvent, endEvent, type FROM worktimeapp.illnesses WHERE start={}".format(date)
        command = "SELECT id, dateOfLastChange, start, end, startEvent, endEvent, type FROM worktimeapp.illnesses WHERE start={}".format(date)
        cursor.execute(command)
        tuples = cursor.fetchall()

        #for (id, dateOfLastChange, start, end, timeIntervalId, startEvent, endEvent, type) in tuples:
        for (id, dateOfLastChange, start, end, startEvent, endEvent, type) in tuples:
            illness = IllnessBO()
            illness.set_id(id)
            illness.set_date_of_last_change(dateOfLastChange)
            illness.set_start(start)
            illness.set_end(end)
            #illness.set_time_interval_id(timeIntervalId)
            illness.set_start_event(startEvent)
            illness.set_end_event(endEvent)
            illness.set_type(type)
            result.append(illness)

        self._cnx.commit()
        return result

    """
    Gibt alle IllnessBO aus einen angegebenen Zeitraum zurück
    param: start_date (date) - Start des Zeitintervalls
           end_date (date) - Ende des Zeitintervalls
    return: result - alle IllnessBO im angegebenen Zeitraum
    """
    def find_by_time_period(self, start_date, end_date):
        result = []
        cursor = self._cnx.cursor()
        #command = "SELECT id, dateOfLastChange, start, end, timeIntervalId, startEvent, endEvent, type FROM worktimeapp.illnesses WHERE start>={} AND end<={}".format(start_date, end_date)
        command = "SELECT id, dateOfLastChange, start, end, startEvent, endEvent, type FROM worktimeapp.illnesses WHERE start>={} AND end<={}".format(start_date, end_date)
        cursor.execute(command)
        tuples = cursor.fetchall()

        #for (id, dateOfLastChange, start, end, timeIntervalId, startEvent, endEvent, type) in tuples:
        for (id, dateOfLastChange, start, end, startEvent, endEvent, type) in tuples:
            illness = IllnessBO()
            illness.set_id(id)
            illness.set_date_of_last_change(dateOfLastChange)
            illness.set_start(start)
            illness.set_end(end)
            #illness.set_time_interval_booking_id(timeIntervalId)
            illness.set_start_event(startEvent)
            illness.set_end_event(endEvent)
            illness.set_type(type)
            result.append(illness)

        self._cnx.commit()
        return result

    """
    Gibt das IllnessBO mit gegebener booking_id zurück
    param: bookingId - Fremdschlüssel von BookingBO
    return: result - IllnessBO
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