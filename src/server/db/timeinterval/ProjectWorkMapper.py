from server.db import TimeIntervalMapper
from server.bo import ProjectWorkBO

"""
@author Ha Mi Duong (https://github.com/HamiDuong)

Mapper für ProjectWorkBO - Schnittstelle zur Datenbank
Datentabellenname: projectWorks
Attribute               
id (PK)                     eindeutige Identifikationsnummer                      
dateOfLastChange            Zeitpunkt der letzten Änderung
start                       Startzeitpunkt der Pause
end                         Endzeitpunkt der Pause
startEvent (FK)             Zuordnung zu ProjectWorkBegin
endEvent (FK)               Zuordnung zu ProjectWorkEnd
type                        Art des Intervalls (siehe Subklassen)                       
activityId (FK)             Zuordnung zu Activity

verworfen
timeintervalBookingId (FK)  Zuordnung zu TimeIntervalBooking   
"""
class ProjectWorkMapper(TimeIntervalMapper):

    def __init__(self):
        super().__init__()

    """
    Gibt alle ProjectWorkBO aus der Datenbank zurück
    return: Liste mit ProjectWorkBO (list) - alle ProjectWorkBO in der Datenbank
    """    
    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * from worktimeapp.projectworks")
        tuples = cursor.fetchall()

        for (id, dateOfLastChange, start, end, startEvent, endEvent, type, activityId) in tuples:
            projectwork_obj = ProjectWorkBO()
            projectwork_obj.set_id(id)
            projectwork_obj.set_date_of_last_change(dateOfLastChange)
            projectwork_obj.set_start(start)
            projectwork_obj.set_end(end)
            projectwork_obj.set_start_event(startEvent)
            projectwork_obj.set_end_event(endEvent)
            projectwork_obj.set_type(type)
            projectwork_obj.set_activity_id(activityId)
            #projectwork_obj.set_time_interval_booking_id(timeIntervalBookingId)
            result.append(projectwork_obj)

        self._cnx.commit()
        return result

    """
    Gibt das ProjectWorkBO mit den gegebener Id zurück
    param: key (int) - Id vom gesuchtem ProjectWorkBO
    return: ProjectWorkBO mit der Id = key
    """    
    def find_by_key(self, key):
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, dateOfLastChange, start, end, startEvent, endEvent, type, activityId FROM worktimeapp.projectworks WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            (id, dateOfLastChange, start, end, startEvent, endEvent, type, activityId) = tuples[0]
            projectwork_obj = ProjectWorkBO()
            projectwork_obj.set_id(id)
            projectwork_obj.set_date_of_last_change(dateOfLastChange)
            projectwork_obj.set_start(start)
            projectwork_obj.set_end(end)
            projectwork_obj.set_start_event(startEvent)
            projectwork_obj.set_end_event(endEvent)
            projectwork_obj.set_type(type)
            projectwork_obj.set_activity_id(activityId)
            #projectwork_obj.set_timeinterval_booking_id(timeIntervalBookingId)
            result = projectwork_obj

        self._cnx.commit()
        cursor.close()

        return result

    """
    Fügt ein ProjectWorkBO in die Datenbank ein
    param: projectwork_obj (ProjectWorkBO) - ProjectWorkBO welches eingefügt werden soll
    return: projectwork_obj
    """
    def insert (self, projectwork_obj):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM worktimeapp.projectworks")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            projectwork_obj.set_id(maxid[0]+1)

        command = "INSET INTO worktimeapp.projectworks (id, dateOfLastChange, start, end, startEvent, endEvent, type, activityId) VALUES (%s, %s, %s, %s, %s, %s, %s, %s )"
        data = (projectwork_obj.get_id(), projectwork_obj.get_date_of_last_change(), projectwork_obj.get_start(), projectwork_obj. get_end(), projectwork_obj.get_start_event(), projectwork_obj.get_end_event(), projectwork_obj.get_type(), projectwork_obj.get_project_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return projectwork_obj

    """
    Ändert die Attribute eines ProjectWorkBO welches bereits in der Datenbank ist
    param: projectwork_obj (ProjectWorkBO) - ProjectWorkBO mit aktualisierten Daten
    return: None 
    """
    def update (self, projectwork_obj):
        cursor = self._cnx.cursor()

        command = "UPDATE worktimeapp.projectworks " + "SET start=%s, end=%s WHERE id=%s"
        data = (projectwork_obj.get_start(), projectwork_obj.get_end(), projectwork_obj.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    """
    Löscht ein ProjectWorkBO aus der Datenbank
    param: projectwork_obj (ProjectWorkBO) - ProjectWorkBO welches aus der Datenbank gelöscht werden soll
    return: None
    """
    def delete(self, projectwork_obj):
        cursor = self._cnx.cursor()

        command = "DELETE FROM worktimeapp.projectworks WHERE id={}".format(projectwork_obj.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()   

    """
    Gibt das ProjectWorkBO mit dem gegebenen Startdatum zurück
    param: date (datetime) - Id vom gesuchtem ProjectWorkBO
    return: ProjectWorkBO mit start = date
    """
    def find_by_date(self, date):
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, dateOfLastChange, start, end, startEvent, endEvent, type, activityId FROM worktimeapp.projectworks WHERE start={}".format(date)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            #for (id, dateOfLastChange, start, end, timeIntervalId, startEvent, endEvent, type, projectId) in tuples:
            for (id, dateOfLastChange, start, end, startEvent, endEvent, type, activityId) in tuples:
                projectwork_obj = ProjectWorkBO()
                projectwork_obj.set_id(id)
                projectwork_obj.set_date_of_last_change(dateOfLastChange)
                projectwork_obj.set_start(start)
                projectwork_obj.set_end(end)
                #projectduration_obj.set_time_interval_id(timeIntervalId)
                projectwork_obj.set_start_event(startEvent)
                projectwork_obj.set_end_event(endEvent)
                projectwork_obj.set_type(type)
                projectwork_obj.set_activity_id(activityId)
                result.append(projectwork_obj)

        self._cnx.commit()
        return result

    """
    Gibt alle ProjectWorkBO aus einen angegebenen Zeitraum zurück
    param: start_date (date) - Start des Zeitintervalls
           end_date (date) - Ende des Zeitintervalls
    return: result - alle ProjectWorkBO im angegebenen Zeitraum
    """
    def find_by_time_period(self, start_date, end_date):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, dateOfLastChange, start, end, startEvent, endEvent, type, activityId FROM worktimeapp.projectworks WHERE start={} AND end={}".format(start_date, end_date)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            #for (id, dateOfLastChange, start, end, timeIntervalId, startEvent, endEvent, type, projectId) in tuples:
            for (id, dateOfLastChange, start, end, startEvent, endEvent, type, activityId) in tuples:
                projectwork_obj = ProjectWorkBO()
                projectwork_obj.set_id(id)
                projectwork_obj.set_date_of_last_change(dateOfLastChange)
                projectwork_obj.set_start(start)
                projectwork_obj.set_end(end)
                #projectduration_obj.set_time_interval_id(timeIntervalId)
                projectwork_obj.set_start_event(startEvent)
                projectwork_obj.set_end_event(endEvent)
                projectwork_obj.set_type(type)
                projectwork_obj.set_activity_id(activityId)
                result.append(projectwork_obj)

        self._cnx.commit()
        return result

    """
    Gibt das ProjectWorkBO mit gegebener booking_id zurück
    param: bookingId - Fremdschlüssel von BookingBO
    return: result - ProjectWorkBO
    """
    # def find_by_time_interval_booking_id(self, bookingId):
    #     result = None
    #     cursor = self._cnx.cursor()
    #     command = "SELECT id, dateOfLastChange, start, end, startEvent, endEvent, type, activityId FROM worktimeapp.projectworks WHERE timeIntervalBookingId={}".format(bookingId)
    #     cursor.execute(command)
    #     tuples = cursor.fetchall()

    #     if tuples[0] is not None:
    #         (id, dateOfLastChange, start, end, startEvent, endEvent, activityId, timeIntervalBookingId) = tuples[0]
    #         projectwork_obj = ProjectWorkBO()
    #         projectwork_obj.set_id(id)
    #         projectwork_obj.set_date_of_last_change(dateOfLastChange)
    #         projectwork_obj.set_start(start)
    #         projectwork_obj.set_end(end)
    #         projectwork_obj.set_start_event(startEvent)
    #         projectwork_obj.set_end_event(endEvent)
    #         projectwork_obj.set_activity_id(activityId)
    #         projectwork_obj.set_timeinterval_booking_id(timeIntervalBookingId)
    #         result = projectwork_obj

    #     self._cnx.commit()
    #     cursor.close()        
    #     return result

    """
    Gibt alle ProjectWorkBO mit gegebener activity_id aus der Datenbank zurück
    param: activityId
    return: Liste mit ProjectWorkBO (list) - alle ProjectWorkBO in der Datenbank
    """    
    def find_all_by_activity_id(self, acId):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * from worktimeapp.projectworks WHERE activityId = {}".format(acId))
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            #for (id, dateOfLastChange, start, end, timeIntervalId, startEvent, endEvent, type, projectId) in tuples:
            for (id, dateOfLastChange, start, end, startEvent, endEvent, type, activityId) in tuples:
                projectwork_obj = ProjectWorkBO()
                projectwork_obj.set_id(id)
                projectwork_obj.set_date_of_last_change(dateOfLastChange)
                projectwork_obj.set_start(start)
                projectwork_obj.set_end(end)
                #projectduration_obj.set_time_interval_id(timeIntervalId)
                projectwork_obj.set_start_event(startEvent)
                projectwork_obj.set_end_event(endEvent)
                projectwork_obj.set_type(type)
                projectwork_obj.set_activity_id(activityId)
                result.append(projectwork_obj)

        self._cnx.commit()
        return result

    