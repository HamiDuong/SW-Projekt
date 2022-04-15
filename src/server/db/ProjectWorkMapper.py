from server.db import Mapper
from server.bo import ProjectWorkBO

"""
@author Ha Mi Duong (https://github.com/HamiDuong)

Mapper für ProjectWorkBO - Schnittstelle zur Datenbank
Attribute               
id (PK)                     eindeutige Identifikationsnummer                      
dateOfLastChange            Zeitpunkt der letzten Änderung
start                       Startzeitpunkt der Pause
end                         Endzeitpunkt der Pause
startEvent                  Wenn True: start ist ein Event
endEvent?                   Wenn True: end ist ein Event
timeintervalBookingId (FK)  Zuordnung zu TimeIntervalBooking   
"""
class ProjectWorkMapper(Mapper):

    def __init__(self):
        super().__init__()

    """
    Gibt alle ProjectWorkBO aus der Datenbank zurück
    return: Liste mit ProjectWorkBO (list) - alle ProjectWorkBO in der Datenbank
    """    
    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * from projectWork")
        tuples = cursor.fetchall()

        for (id, dateOfLastChange, start, end, startEvent, endEvent, timeIntervalBookingId) in tuples:
            projectwork_obj = ProjectWorkBO()
            projectwork_obj.set_id(id)
            projectwork_obj.set_date_of_last_change(dateOfLastChange)
            projectwork_obj.set_start(start)
            projectwork_obj.set_end(end)
            projectwork_obj.set_start_event(startEvent)
            projectwork_obj.set_end_event(endEvent)
            projectwork_obj.set_time_interval_booking_id(timeIntervalBookingId)
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
        command = "SELECT id, dateOfLastChange, start, end, startEvent, endEvent, timeIntervalBookingId FROM projectWork WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            (id, dateOfLastChange, start, end, startEvent, endEvent, timeIntervalBookingId) = tuples[0]
            projectwork_obj = ProjectWorkBO()
            projectwork_obj.set_id(id)
            projectwork_obj.set_date_of_last_change(dateOfLastChange)
            projectwork_obj.set_start(start)
            projectwork_obj.set_end(end)
            projectwork_obj.set_start_event(startEvent)
            projectwork_obj.set_end_event(endEvent)
            projectwork_obj.set_timeinterval_booking_id(timeIntervalBookingId)
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
        cursor.execute("SELECT MAX(id) AS maxid FROM projectWork")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            projectwork_obj.set_id(maxid[0]+1)

        command = "INSET INTO break (id, dateOfLastChange, start, end, startEvent, endEvent, timeIntervalBookingId) VALUES (%s, %s, %s, %s, %s)"
        data = (projectwork_obj.get_id(), projectwork_obj.get_date_of_last_change(), projectwork_obj.get_start(), projectwork_obj. get_end(), projectwork_obj.get_start_event(), projectwork_obj.get_end_event(), projectwork_obj.get_timeinterval_booking_id())
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

        command = "UPDATE break " + "SET start=%s, end=%s , startEvent=%s, endEvent=%s WHERE id=%s"
        data = (projectwork_obj.get_start(), projectwork_obj.get_end(), projectwork_obj. get_start_event(), projectwork_obj.get_end_event(), projectwork_obj.get_id())
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

        command = "DELETE FROM projectWork WHERE id={}".format(projectwork_obj.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()   