from server.db.Mapper import Mapper
from server.bo.timeinterval.TimeIntervalBO import TimeIntervalBO
from datetime import datetime
from abc import abstractmethod

"""
@author Ha Mi Duong (https://github.com/HamiDuong)

Mapper für TimeIntervalBO - Schnittstelle zur Datenbank
Dient als Superklasse für Break, Illness, ProjectDuration, ProjectWork, Vacation, Work

Attribute               
id (PK)                     eindeutige Identifikationsnummer                      
dateOfLastChange            Zeitpunkt der letzten Änderung
timeintervalBookingId (FK)  Zuordnung zu TimeIntervalBooking
type                        Art des Intervalls (siehe Subklassen)
breakId                     Fremdschlüssel zu Break
illnessId                   Fremdschlüssel zu Illness
projectDurationId           Fremdschlüssel zu ProjectDuration
projectWorkId               Fremdschlüssel zu ProjectWork
vacationId                  Fremdschlüssel zu Vacation
workId                      Fremdschlüssel zu Work
"""
class TimeIntervalMapper(Mapper):

    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def find_by_date(self, date):
        pass

    @abstractmethod
    def find_by_time_period(self, start_date, end_date):
        pass

    # @abstractmethod
    # def find_by_time_intervall_id(self, id):
    #     pass

    """
    Gibt alle TimeIntervalBO aus der Datenbank zurück
    return: Liste mit TimeIntervalBO (list) - alle TimeIntervalBO in der Datenbank
    """    
    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        #cursor.execute("SELECT id, dateOfLastChange, timeIntervalBookingId, type from worktimeapp.timeintervals")
        cursor.execute("SELECT id, dateOfLastChange, type, breakId, illnessId, projectDurationId, projectWorkId, vacationId, workId from worktimeapp.timeintervals")
        tuples = cursor.fetchall()

        for (id, dateOfLastChange, type, breakId, illnessId, projectDurationId, projectWorkId, vacationId, workId) in tuples:
            timeinterval = TimeIntervalBO()
            timeinterval.set_id(id)
            timeinterval.set_date_of_last_change(dateOfLastChange)
            #timeinterval.set_time_interval_booking_id(timeIntervalBookingId)
            timeinterval.set_type(type)
            timeinterval.set_break_id(breakId)
            timeinterval.set_illness_id(illnessId)
            timeinterval.set_project_duration_id(projectDurationId)
            timeinterval.set_project_work_id(projectWorkId)
            timeinterval.set_work_id(workId)
            timeinterval.set_vacation_id(vacationId)
            result.append(timeinterval)

        self._cnx.commit()
        return result

    """
    Gibt das TimeIntervalBO mit den gegebener Id zurück
    param: key (int) - Id vom gesuchtem TimeIntervalBO
    return: TimeIntervalBO mit der Id = key
    """    
    def find_by_key(self, key):
        result = None
        cursor = self._cnx.cursor()
        #command = "SELECT id, dateOfLastChange, timeIntervalBookingId, type, from worktimeapp.timeintervals WHERE id={}".format(key)
        command = "SELECT id, dateOfLastChange, type, breakId, illnessId, projectDurationId, projectWorkId, vacationId, workId from worktimeapp.timeintervals WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            #(id, dateOfLastChange, timeIntervalBookingId, type, breakId, illnessId, projectDurationId, projectWorkId, vacationId, workId) = tuples[0]
            (id, dateOfLastChange, type, breakId, illnessId, projectDurationId, projectWorkId, vacationId, workId) = tuples[0]
            timeinterval = TimeIntervalBO()
            timeinterval.set_id(id)
            timeinterval.set_date_of_last_change(dateOfLastChange)
            #timeinterval.set_time_interval_booking_id(timeIntervalBookingId)
            timeinterval.set_type(type)
            timeinterval.set_break_id(breakId)
            timeinterval.set_illness_id(illnessId)
            timeinterval.set_project_duration_id(projectDurationId)
            timeinterval.set_project_work_id(projectWorkId)
            timeinterval.set_work_id(workId)
            timeinterval.set_vacation_id(vacationId)
            result = timeinterval

        self._cnx.commit()
        cursor.close()

        return result

    """
    Fügt ein TimeIntervalBO in die Datenbank ein
    param: timeinterval (TimeIntervalBO) - TimeIntervalBO welches eingefügt werden soll
    return: timeinterval
    """
    def insert (self, timeinterval):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM worktimeapp.timeintervals")
        tuples = cursor.fetchall()

        timestamp = datetime.today()
        timeinterval.set_date_of_last_change(timestamp)

        for (maxid) in tuples:
            timeinterval.set_id(maxid[0]+1)

        #command = "INSERT INTO worktimeapp.timeintervals (id, dateOfLastChange, timeIntervalBookingId, type) VALUES (%s, %s, %s, %s)"
        #data = (timeinterval.get_id(), timeinterval.get_date_of_last_change(), timeinterval.get_timeinterval_booking_id(), timeinterval.get_type())
        command = "INSERT INTO worktimeapp.timeintervals (id, dateOfLastChange, type, breakId, illnessId, projectDurationId, projectWorkId, vacationId, workId) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data = (timeinterval.get_id(), timeinterval.get_date_of_last_change(), timeinterval.get_type(), timeinterval.get_break_id(), timeinterval.get_illness_id(), timeinterval.get_project_duration(), timeinterval.get_vacation_id(), timeinterval.work_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return timeinterval

    """
    Ändert die Attribute eines TimeIntervalBO welches bereits in der Datenbank ist
    param: timeinterval (TimeIntervalBO) - TimeIntervalBO mit aktualisierten Daten
    return: None 
    """
    def update (self, timeinterval):
        cursor = self._cnx.cursor()

        timestamp = datetime.today()
        timeinterval.set_date_of_last_change(timestamp)

        command = "UPDATE worktimeapp.timeintervals " + "SET dateOfLastChange=%s, type=%s WHERE id=%s"
        data = (timeinterval.get_date_of_last_change(), timeinterval.get_type() ,timeinterval.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    """
    Löscht ein TimeIntervalBO aus der Datenbank
    param: timeinterval (TimeIntervalBO) - TimeIntervalBO welches aus der Datenbank gelöscht werden soll
    return: None
    """
    def delete(self, timeinterval):
        cursor = self._cnx.cursor()

        command = "DELETE FROM worktimeapp.timeintervals WHERE id={}".format(timeinterval.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()  

    """
    Gibt TimeIntervalBOs mit dem gegebenen type zurück
    param: elem (String) - type vom gesuchtem TimeIntervalBO
    return: TimeIntervalBO mit type = elem
    """    
    def find_by_type(self, elem):
        result = []
        cursor = self._cnx.cursor()
        #command = "SELECT id, dateOfLastChange, timeIntervalBookingId, type, from worktimeapp.timeintervals WHERE id={}".format(key)
        command = "SELECT id, dateOfLastChange, type, breakId, illnessId, projectDurationId, projectWorkId, vacationId, workId from worktimeapp.timeintervals WHERE type={}".format(elem)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            for (id, dateOfLastChange, type, breakId, illnessId, projectDurationId, projectWorkId, vacationId, workId) in tuples:
                timeinterval = TimeIntervalBO()
                timeinterval.set_id(id)
                timeinterval.set_date_of_last_change(dateOfLastChange)
                #timeinterval.set_time_interval_booking_id(timeIntervalBookingId)
                timeinterval.set_type(type)
                timeinterval.set_break_id(breakId)
                timeinterval.set_illness_id(illnessId)
                timeinterval.set_project_duration_id(projectDurationId)
                timeinterval.set_project_work_id(projectWorkId)
                timeinterval.set_work_id(workId)
                timeinterval.set_vacation_id(vacationId)
                result.append(timeinterval)

            self._cnx.commit()
        return result