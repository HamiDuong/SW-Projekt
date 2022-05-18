from server.db.timeinterval.TimeIntervalMapper import TimeIntervalMapper
from server.bo.timeinterval.ProjectDurationBO import ProjectDurationBO

"""
@author Ha Mi Duong (https://github.com/HamiDuong)

Mapper für ProjectDurationBO - Schnittstelle zur Datenbank
Datentabellenname: projectDurations
Attribute               
id (PK)                     eindeutige Identifikationsnummer                      
dateOfLastChange            Zeitpunkt der letzten Änderung
start                       Startzeitpunkt der Pause
end                         Endzeitpunkt der Pause
startEvent (FK)             Zuordnung zu ProjectBegin
endEvent (FK)               Zuordnung zu ProjectEnd
type                        Art des Intervalls (siehe Subklassen)
projectId (FK)              Zuordnung zu Project

Verworfen
timeintervalBookingId (FK)  Zuordnung zu TimeIntervalBooking 
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
        cursor.execute("SELECT * from worktimeapp.projectdurations")
        tuples = cursor.fetchall()

        #for (id, dateOfLastChange, start, end, timeIntervalId, startEvent, endEvent, type, projectId) in tuples:
        for (id, dateOfLastChange, start, end, startEvent, endEvent, type, projectId) in tuples:
            projectduration_obj = ProjectDurationBO()
            projectduration_obj.set_id(id)
            projectduration_obj.set_date_of_last_change(dateOfLastChange)
            projectduration_obj.set_start(start)
            projectduration_obj.set_end(end)
            #projectduration_obj.set_time_interval_id(timeIntervalId)
            projectduration_obj.set_start_event(startEvent)
            projectduration_obj.set_end_event(endEvent)
            projectduration_obj.set_type(type)
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
        #command = "SELECT id, dateOfLastChange, start, end, timeIntervalId, projectId FROM projectDurations WHERE id={}".format(key)
        command = "SELECT id, dateOfLastChange, start, end, startEvent, endEvent, type, projectId FROM worktimeapp.projectdurations WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            #(id, dateOfLastChange, start, end, timeIntervalId, startEvent, endEvent, type, projectId) = tuples[0]
            (id, dateOfLastChange, start, end, startEvent, endEvent, type, projectId) = tuples[0]
            projectduration_obj = ProjectDurationBO()
            projectduration_obj.set_id(id)
            projectduration_obj.set_date_of_last_change(dateOfLastChange)
            projectduration_obj.set_start(start)
            projectduration_obj.set_end(end)
            #projectduration_obj.set_time_interval_id(timeIntervalId)
            projectduration_obj.set_start_event(startEvent)
            projectduration_obj.set_end_event(endEvent)
            projectduration_obj.set_type(type)
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
        cursor.execute("SELECT MAX(id) AS maxid FROM worktimeapp.projectdurations")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            projectduration_obj.set_id(maxid[0]+1)

        #command = "INSET INTO projectdurations (id, dateOfLastChange, start, end, timeIntervalId, startEvent, endEvent, type, projectId) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        #data = (projectduration_obj.get_id(), projectduration_obj.get_date_of_last_change(), projectduration_obj.get_start(), projectduration_obj.get_end(), projectduration_obj.get_timeinterval_id(), projectduration_obj.get_start_event() ,projectduration_obj.get_project_id())
        command = "INSET INTO worktimeapp.projectdurations (id, dateOfLastChange, start, end, startEvent, endEvent, type, projectId) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        data = (projectduration_obj.get_id(), projectduration_obj.get_date_of_last_change(), projectduration_obj.get_start(), projectduration_obj.get_end(), projectduration_obj.get_start_event(), projectduration_obj.get_end_event(), projectduration_obj.get_type(), projectduration_obj.get_project_id())
 
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

        command = "UPDATE worktimeapp.projectdurations " + "SET start=%s, end=%s WHERE id=%s"
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

        command = "DELETE FROM worktimeapp.projectdurations WHERE id={}".format(projectduration_obj.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()   

    """
    Gibt das ProjectDurationBO mit dem gegebenen Startdatum zurück
    param: date (datetime) - Id vom gesuchtem ProjectDurationBO
    return: ProjectDurationBO mit start = date
    """
    def find_by_date(self, date):
        result = []
        cursor = self._cnx.cursor()
        #command = "SELECT id, dateOfLastChange, start, end, timeIntervalBookingId, projectId FROM projectDurations WHERE start={}".format(date)
        command = "SELECT id, dateOfLastChange, start, end, startEvent, endEvent, type, projectId FROM worktimeapp.projectdurations WHERE start={}".format(date)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            #for (id, dateOfLastChange, start, end, timeIntervalId, startEvent, endEvent, type, projectId) in tuples:
            for (id, dateOfLastChange, start, end, startEvent, endEvent, type, projectId) in tuples:
                projectduration_obj = ProjectDurationBO()
                projectduration_obj.set_id(id)
                projectduration_obj.set_date_of_last_change(dateOfLastChange)
                projectduration_obj.set_start(start)
                projectduration_obj.set_end(end)
                #projectduration_obj.set_time_interval_id(timeIntervalId)
                projectduration_obj.set_start_event(startEvent)
                projectduration_obj.set_end_event(endEvent)
                projectduration_obj.set_type(type)
                projectduration_obj.set_project_id(projectId)
                result.append(projectduration_obj)

        self._cnx.commit()
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
        #cursor.execute("SELECT id, dateOfLastChange, start, end, timeIntervalBookingId, projectId from projectDurations WHERE start={} AND end={}".format(start_date, end_date))
        cursor.execute("SELECT id, dateOfLastChange, start, end, startEvent, endEvent, type, projectId from worktimeapp.projectdurations WHERE start>={} AND end<={}".format(start_date, end_date))
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            #for (id, dateOfLastChange, start, end, timeIntervalId, startEvent, endEvent, type, projectId) in tuples:
            for (id, dateOfLastChange, start, end, startEvent, endEvent, type, projectId) in tuples:
                projectduration_obj = ProjectDurationBO()
                projectduration_obj.set_id(id)
                projectduration_obj.set_date_of_last_change(dateOfLastChange)
                projectduration_obj.set_start(start)
                projectduration_obj.set_end(end)
                #projectduration_obj.set_time_interval_id(timeIntervalId)
                projectduration_obj.set_start_event(startEvent)
                projectduration_obj.set_end_event(endEvent)
                projectduration_obj.set_type(type)
                projectduration_obj.set_project_id(projectId)
                result.append(projectduration_obj)

        self._cnx.commit()
        return result

    """
    Gibt das ProjectDurationBO mit gegebener time_interval_booking_id zurück
    param: bookingId - Fremdschlüssel von BookingBO
    return: result - ProjectDurationBO
    """
    # def find_by_time_intervall_id(self, timeintervalId):
    #     result = None
    #     cursor = self._cnx.cursor()
    #     command = "SELECT id, dateOfLastChange, start, end, timeIntervalId, projectId FROM projectDurations WHERE timeIntervalId={}".format(timeintervalId)
    #     cursor.execute(command)
    #     tuples = cursor.fetchall()

    #     if tuples[0] is not None:
    #         (id, dateOfLastChange, start, end, timeIntervalBookingId, projectId) = tuples[0]
    #         projectduration_obj = ProjectDurationBO()
    #         projectduration_obj.set_id(id)
    #         projectduration_obj.set_date_of_last_change(dateOfLastChange)
    #         projectduration_obj.set_start(start)
    #         projectduration_obj.set_end(end)
    #         projectduration_obj.set_timeinterval_booking_id(timeIntervalBookingId)
    #         projectduration_obj.set_project_id(projectId)
    #         result = projectduration_obj

    #     self._cnx.commit()
    #     cursor.close()

    #     return result

    """
    Gibt das ProjectDurationBO mit gegebener project_id zurück
    param: projectId - Fremdschlüssel von BookingBO
    return: result - ProjectDurationBO
    """
    def find_by_project_id(self, projectId):
        result = None
        cursor = self._cnx.cursor()
        #command = "SELECT id, dateOfLastChange, start, end, timeIntervalBookingId, projectId FROM projectDurations WHERE projectId={}".format(projectId)
        command = "SELECT id, dateOfLastChange, start, end, startEvent, endEvent, type, projectId FROM worktimeapp.projectdurations WHERE projectId={}".format(projectId)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            #(id, dateOfLastChange, start, end, timeIntervalId, startEvent, endEvent, type, projectId) = tuples[0]
            (id, dateOfLastChange, start, end, startEvent, endEvent, type, projectId) = tuples[0]
            projectduration_obj = ProjectDurationBO()
            projectduration_obj.set_id(id)
            projectduration_obj.set_date_of_last_change(dateOfLastChange)
            projectduration_obj.set_start(start)
            projectduration_obj.set_end(end)
            #projectduration_obj.set_time_interval_id(timeIntervalId)
            projectduration_obj.set_start_event(startEvent)
            projectduration_obj.set_end_event(endEvent)
            projectduration_obj.set_type(type)
            projectduration_obj.set_project_id(projectId)
            result = projectduration_obj

        self._cnx.commit()
        cursor.close()

        return result