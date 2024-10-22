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
flexDayId                   Fremdschlüssel zu FlexDay
"""
class TimeIntervalMapper(Mapper):

    def __init__(self):
        super().__init__()

    """
    Gibt alle TimeIntervalBO aus der Datenbank zurück
    return: Liste mit TimeIntervalBO (list) - alle TimeIntervalBO in der Datenbank
    """
    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute(
            "SELECT id, dateOfLastChange, type, breakId, illnessId, projectDurationId, projectWorkId, vacationId, workId, flexDayId from worktimeapp.timeintervals")
        tuples = cursor.fetchall()

        for (id, dateOfLastChange, type, breakId, illnessId, projectDurationId, projectWorkId, vacationId, workId, flexDayId) in tuples:
            timeinterval = TimeIntervalBO()
            timeinterval.set_id(id)
            timeinterval.set_date_of_last_change(dateOfLastChange)
            timeinterval.set_type(type)
            timeinterval.set_break_id(breakId)
            timeinterval.set_illness_id(illnessId)
            timeinterval.set_project_duration_id(projectDurationId)
            timeinterval.set_project_work_id(projectWorkId)
            timeinterval.set_work_id(workId)
            timeinterval.set_vacation_id(vacationId)
            timeinterval.set_flex_day_id(flexDayId)
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
        command = "SELECT id, dateOfLastChange, type, breakId, illnessId, projectDurationId, projectWorkId, vacationId, workId, flexDayId from worktimeapp.timeintervals WHERE id={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            (id, dateOfLastChange, type, breakId, illnessId, projectDurationId,
             projectWorkId, vacationId, workId, flexDayId) = tuples[0]
            timeinterval = TimeIntervalBO()
            timeinterval.set_id(id)
            timeinterval.set_date_of_last_change(dateOfLastChange)
            timeinterval.set_type(type)
            timeinterval.set_break_id(breakId)
            timeinterval.set_illness_id(illnessId)
            timeinterval.set_project_duration_id(projectDurationId)
            timeinterval.set_project_work_id(projectWorkId)
            timeinterval.set_work_id(workId)
            timeinterval.set_vacation_id(vacationId)
            timeinterval.set_flex_day_id(flexDayId)
            result = timeinterval

        self._cnx.commit()
        cursor.close()

        return result

    """
    Gibt das TimeIntervalBO mit den gegebenen key und type zurück
    param: foreign_key (Integer), type (String)
    """
    def find_by_foreign_key_and_type(self, foreign_key, key, type):
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, dateOfLastChange, type, breakId, illnessId, projectDurationId, projectWorkId, vacationId, workId, flexDayId from worktimeapp.timeintervals WHERE {}={} AND type='{}'".format(
            foreign_key, key, type)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            (id, dateOfLastChange, type, breakId, illnessId, projectDurationId,
             projectWorkId, vacationId, workId, flexDayId) = tuples[0]
            timeinterval = TimeIntervalBO()
            timeinterval.set_id(id)
            timeinterval.set_date_of_last_change(dateOfLastChange)
            timeinterval.set_type(type)
            timeinterval.set_break_id(breakId)
            timeinterval.set_illness_id(illnessId)
            timeinterval.set_project_duration_id(projectDurationId)
            timeinterval.set_project_work_id(projectWorkId)
            timeinterval.set_work_id(workId)
            timeinterval.set_vacation_id(vacationId)
            timeinterval.set_flex_day_id(flexDayId)
            result = timeinterval

        self._cnx.commit()
        cursor.close()

        return result

    """
    Fügt ein TimeIntervalBO in die Datenbank ein
    param: timeinterval (TimeIntervalBO) - TimeIntervalBO welches eingefügt werden soll
    return: timeinterval
    """
    def insert(self, timeinterval):
        cursor = self._cnx.cursor()
        cursor.execute(
            "SELECT MAX(id) AS maxid FROM worktimeapp.timeintervals")
        tuples = cursor.fetchall()

        timestamp = datetime.today()
        timeinterval.set_date_of_last_change(timestamp)

        for (maxid) in tuples:
            if maxid[0] == None:
                timeinterval.set_id(1)
            else:
                timeinterval.set_id(maxid[0]+1)

        command = "INSERT INTO worktimeapp.timeintervals (id, dateOfLastChange, type, breakId, illnessId, projectDurationId, projectWorkId, vacationId, workId, flexDayId) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data = (timeinterval.get_id(), timeinterval.get_date_of_last_change(), timeinterval.get_type(), timeinterval.get_break_id(), timeinterval.get_illness_id(
        ), timeinterval.get_project_duration_id(), timeinterval.get_project_work_id(), timeinterval.get_vacation_id(), timeinterval.get_work_id(), timeinterval.get_flex_day_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return timeinterval

    """
    Ändert die Attribute eines TimeIntervalBO welches bereits in der Datenbank ist
    param: timeinterval (TimeIntervalBO) - TimeIntervalBO mit aktualisierten Daten
    return: None 
    """
    def update(self, timeinterval):
        cursor = self._cnx.cursor()

        timestamp = datetime.today()
        timeinterval.set_date_of_last_change(timestamp)

        command = "UPDATE worktimeapp.timeintervals " + \
            "SET dateOfLastChange=%s, type=%s WHERE id=%s"
        data = (timeinterval.get_date_of_last_change(),
                timeinterval.get_type(), timeinterval.get_id())
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

        command = "DELETE FROM worktimeapp.timeintervals WHERE id={}".format(
            timeinterval.get_id())
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
        command = "SELECT id, dateOfLastChange, type, breakId, illnessId, projectDurationId, projectWorkId, vacationId, workId, flexDayId from worktimeapp.timeintervals WHERE type={}".format(
            elem)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            for (id, dateOfLastChange, type, breakId, illnessId, projectDurationId, projectWorkId, vacationId, workId, flexDayId) in tuples:
                timeinterval = TimeIntervalBO()
                timeinterval.set_id(id)
                timeinterval.set_date_of_last_change(dateOfLastChange)
                timeinterval.set_type(type)
                timeinterval.set_break_id(breakId)
                timeinterval.set_illness_id(illnessId)
                timeinterval.set_project_duration_id(projectDurationId)
                timeinterval.set_project_work_id(projectWorkId)
                timeinterval.set_work_id(workId)
                timeinterval.set_vacation_id(vacationId)
                timeinterval.set_flex_day_id(flexDayId)
                result.append(timeinterval)

        self._cnx.commit()
        return result
