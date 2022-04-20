from server.db import TimeIntervalMapper
from server.bo import ProjectDurationBO

"""
@author Ha Mi Duong (https://github.com/HamiDuong)

Mapper für ProjectDurationBO - Schnittstelle zur Datenbank
Datentabellenname: projectDurations
Attribute               
id (PK)                     eindeutige Identifikationsnummer                      
dateOfLastChange            Zeitpunkt der letzten Änderung
start                       Startzeitpunkt der Pause
end                         Endzeitpunkt der Pause
timeintervalBookingId (FK)  Zuordnung zu TimeIntervalBooking 
projectId (FK)              Zuordnung zu Project  
"""
class ProjectDurationMapper(TimeIntervalMapper):

    def __init__(self):
        super().__init__()

    """
    Gibt alle ProjectDurationBO aus der Datenbank zurück
    return: Liste mit ProjectDurationBO (list) - alle ProjectDurationBO in der Datenbank
    """    
    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * from projectDurations")
        tuples = cursor.fetchall()

        for (id, dateOfLastChange, start, end, timeIntervalBookingId, projectId) in tuples:
            projectduration_obj = ProjectDurationBO()
            projectduration_obj.set_id(id)
            projectduration_obj.set_date_of_last_change(dateOfLastChange)
            projectduration_obj.set_start(start)
            projectduration_obj.set_end(end)
            projectduration_obj.set_time_interval_booking_id(timeIntervalBookingId)
            projectduration_obj.set_project_id(projectId)
            result.append(projectduration_obj)

        self._cnx.commit()
        return result

    """
    Gibt das ProjectDurationBO mit den gegebener Id zurück
    param: key (int) - Id vom gesuchtem ProjectDurationBO
    return: ProjectDurationBO mit der Id = key
    """    
    def find_by_key(self, key):
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, dateOfLastChange, start, end, timeIntervalBookingId, projectId FROM projectDurations WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            (id, dateOfLastChange, start, end, timeIntervalBookingId, projectId) = tuples[0]
            projectduration_obj = ProjectDurationBO()
            projectduration_obj.set_id(id)
            projectduration_obj.set_date_of_last_change(dateOfLastChange)
            projectduration_obj.set_start(start)
            projectduration_obj.set_end(end)
            projectduration_obj.set_timeinterval_booking_id(timeIntervalBookingId)
            projectduration_obj.set_project_id(projectId)
            result = projectduration_obj

        self._cnx.commit()
        cursor.close()

        return result

    """
    Fügt ein ProjectDurationBO in die Datenbank ein
    param: projectwork_obj (ProjectDurationBO) - ProjectDurationBO welches eingefügt werden soll
    return: projectwork_obj
    """
    def insert (self, projectduration_obj):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM projectDurations")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            projectduration_obj.set_id(maxid[0]+1)

        command = "INSET INTO projectDurations (id, dateOfLastChange, start, end, timeIntervalBookingId, projectId) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (projectduration_obj.get_id(), projectduration_obj.get_date_of_last_change(), projectduration_obj.get_start(), projectduration_obj. get_end(), projectduration_obj.get_timeinterval_booking_id(), projectduration_obj.get_project_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return projectduration_obj

    """
    Ändert die Attribute eines ProjectDurationBO welches bereits in der Datenbank ist
    param: projectduration_obj (ProjectDurationBO) - ProjectDurationBO mit aktualisierten Daten
    return: None 
    """
    def update (self, projectduration_obj):
        cursor = self._cnx.cursor()

        command = "UPDATE projectDurations " + "SET start=%s, end=%s WHERE id=%s"
        data = (projectduration_obj.get_start(), projectduration_obj.get_end(), projectduration_obj.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    """
    Löscht ein ProjectDurationBO aus der Datenbank
    param: projectduration_obj (ProjectDurationBO) - ProjectDurationBO welches aus der Datenbank gelöscht werden soll
    return: None
    """
    def delete(self, projectduration_obj):
        cursor = self._cnx.cursor()

        command = "DELETE FROM projectDurations WHERE id={}".format(projectduration_obj.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()   

    """
    Gibt das ProjectDurationBO mit dem gegebenen Startdatum zurück
    param: date (datetime) - Id vom gesuchtem ProjectDurationBO
    return: ProjectDurationBO mit start = date
    """
    def find_by_date(self, date):
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, dateOfLastChange, start, end, timeIntervalBookingId, projectId FROM projectDurations WHERE start={}".format(date)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            (id, dateOfLastChange, start, end, timeIntervalBookingId, projectId) = tuples[0]
            projectduration_obj = ProjectDurationBO()
            projectduration_obj.set_id(id)
            projectduration_obj.set_date_of_last_change(dateOfLastChange)
            projectduration_obj.set_start(start)
            projectduration_obj.set_end(end)
            projectduration_obj.set_timeinterval_booking_id(timeIntervalBookingId)
            projectduration_obj.set_project_id(projectId)
            result = projectduration_obj

        self._cnx.commit()
        cursor.close()

        return result

    """
    Gibt alle ProjectDurationBO aus einen angegebenen Zeitraum zurück
    param: start_date (date) - Start des Zeitintervalls
           end_date (date) - Ende des Zeitintervalls
    return: result - alle ProjectDurationBO im angegebenen Zeitraum
    """
    def find_by_time_period(self, start_date, end_date):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT id, dateOfLastChange, start, end, timeIntervalBookingId, projectId from projectDurations WHERE start={} AND end={}".format(start_date, end_date))
        tuples = cursor.fetchall()

        for (id, dateOfLastChange, start, end, timeIntervalBookingId, projectId) in tuples:
            projectduration_obj = ProjectDurationBO()
            projectduration_obj.set_id(id)
            projectduration_obj.set_date_of_last_change(dateOfLastChange)
            projectduration_obj.set_start(start)
            projectduration_obj.set_end(end)
            projectduration_obj.set_time_interval_booking_id(timeIntervalBookingId)
            projectduration_obj.set_project_id(projectId)
            result.append(projectduration_obj)

        self._cnx.commit()
        return result

    """
    Gibt das ProjectDurationBO mit gegebener time_interval_booking_id zurück
    param: bookingId - Fremdschlüssel von BookingBO
    return: result - ProjectDurationBO
    """
    def find_by_time_intervall_booking_id(self, bookingId):
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, dateOfLastChange, start, end, timeIntervalBookingId, projectId FROM projectDurations WHERE timeIntervalBookingId={}".format(bookingId)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            (id, dateOfLastChange, start, end, timeIntervalBookingId, projectId) = tuples[0]
            projectduration_obj = ProjectDurationBO()
            projectduration_obj.set_id(id)
            projectduration_obj.set_date_of_last_change(dateOfLastChange)
            projectduration_obj.set_start(start)
            projectduration_obj.set_end(end)
            projectduration_obj.set_timeinterval_booking_id(timeIntervalBookingId)
            projectduration_obj.set_project_id(projectId)
            result = projectduration_obj

        self._cnx.commit()
        cursor.close()

        return result

    """
    Gibt das ProjectDurationBO mit gegebener project_id zurück
    param: projectId - Fremdschlüssel von BookingBO
    return: result - ProjectDurationBO
    """
    def find_by_project_id(self, projectId):
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, dateOfLastChange, start, end, timeIntervalBookingId, projectId FROM projectDurations WHERE projectId={}".format(projectId)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            (id, dateOfLastChange, start, end, timeIntervalBookingId, projectId) = tuples[0]
            projectduration_obj = ProjectDurationBO()
            projectduration_obj.set_id(id)
            projectduration_obj.set_date_of_last_change(dateOfLastChange)
            projectduration_obj.set_start(start)
            projectduration_obj.set_end(end)
            projectduration_obj.set_timeinterval_booking_id(timeIntervalBookingId)
            projectduration_obj.set_project_id(projectId)
            result = projectduration_obj

        self._cnx.commit()
        cursor.close()

        return result