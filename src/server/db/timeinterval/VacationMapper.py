from server.db.timeinterval.TimeIntervalMapper import TimeIntervalMapper
from server.bo.timeinterval.VacationBO import VacationBO
from datetime import datetime

"""
@author Ha Mi Duong (https://github.com/HamiDuong)

Mapper für VacationBO - Schnittstelle zur Datenbank
Attribute               
id (PK)                     eindeutige Identifikationsnummer                      
dateOfLastChange            Zeitpunkt der letzten Änderung
start                       Startzeitpunkt der Pause
end                         Endzeitpunkt der Pause  
startEvent (FK)             Zuordnung zu VacationBegin
endEvent (FK)               Zuordnung zu VacationEnd
type                        Art des Intervalls

verworfen
timeIntervalId (FK)         Zuordnung zu TimeInterval   
"""


class VacationMapper(TimeIntervalMapper):

    def __init__(self):
        super().__init__()

    """
    Gibt alle VacationBO aus der Datenbank zurück
    return: Liste mit VacationBO (list) - alle VacationBO in der Datenbank
    """

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute(
            "SELECT id, dateOfLastChange, start, end, startEvent, endEvent, type from worktimeapp.vacations")
        tuples = cursor.fetchall()

        for (id, dateOfLastChange, start, end, startEvent, endEvent, type) in tuples:
            vacation = VacationBO()
            vacation.set_id(id)
            vacation.set_date_of_last_change(dateOfLastChange)
            vacation.set_start(start)
            vacation.set_end(end)
            # vacation.set_time_interval_id(timeIntervalId)
            vacation.set_start_event(startEvent)
            vacation.set_end_event(endEvent)
            vacation.set_type(type)
            result.append(vacation)

        self._cnx.commit()
        return result

    """
    Gibt das VacationBO mit den gegebener Id zurück
    param: key (int) - Id vom gesuchtem VacationBO
    return: VacationBO mit der Id = key
    """

    def find_by_key(self, key):
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, dateOfLastChange, start, end, startEvent, endEvent, type from worktimeapp.vacations WHERE id={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            (id, dateOfLastChange, start, end,
             startEvent, endEvent, type) = tuples[0]
            illness = VacationBO()
            illness.set_id(id)
            illness.set_date_of_last_change(dateOfLastChange)
            illness.set_start(start)
            illness.set_end(end)
            # illness.set_time_interval_id(timeIntervalId)
            illness.set_start_event(startEvent)
            illness.set_end_event(endEvent)
            illness.set_type(type)
            result = illness

        self._cnx.commit()
        cursor.close()

        return result

    """
    Fügt ein VacationBO in die Datenbank ein
    param: vacation (VacationBO) - VacationBO welches eingefügt werden soll
    return: vacation
    """

    def insert(self, vacation):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM worktimeapp.vacations")
        tuples = cursor.fetchall()

        timestamp = datetime.today()
        vacation.set_date_of_last_change(timestamp)

        for (maxid) in tuples:
            if maxid[0] == None:
                vacation.set_id(1)
            else:
                vacation.set_id(maxid[0]+1)

        command = "INSERT INTO worktimeapp.vacations (id, dateOfLastChange, start, end, startEvent, endEvent, type) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = (vacation.get_id(), vacation.get_date_of_last_change(), vacation.get_start(
        ), vacation. get_end(), vacation.get_start_event(), vacation.get_end_event(), "Vacation")
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return vacation

    """
    Ändert die Attribute eines VacationBO welches bereits in der Datenbank ist
    param: vacation (VacationBO) - VacationBO mit aktualisierten Daten
    return: None 
    """

    def update(self, vacation):
        cursor = self._cnx.cursor()

        timestamp = datetime.today()
        vacation.set_date_of_last_change(timestamp)

        command = "UPDATE worktimeapp.vacations " + "SET start=%s, end=%s WHERE id=%s"
        data = (vacation.get_start(), vacation.get_end(), vacation.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    """
    Löscht ein VacationBO aus der Datenbank
    param: vacation (VacationBO) - VacationBO welches aus der Datenbank gelöscht werden soll
    return: None
    """

    def delete(self, vacation):
        cursor = self._cnx.cursor()

        command = "DELETE FROM worktimeapp.vacations WHERE id={}".format(
            vacation.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    """
    Gibt alle VacationBO mit dem gegebenen Startdatum zurück
    param: date (datetime) - Id vom gesuchtem VacationBO
    return: Liste von VacationBO mit start = date
    """

    def find_by_date(self, date):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, dateOfLastChange, start, end, startEvent, endEvent, type FROM worktimeapp.vacations WHERE start={}".format(
            date)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, dateOfLastChange, start, end, startEvent, endEvent, type) in tuples:
            vacation = VacationBO()
            vacation.set_id(id)
            vacation.set_date_of_last_change(dateOfLastChange)
            vacation.set_start(start)
            vacation.set_end(end)
            # vacation.set_time_interval_id(timeIntervalId)
            vacation.set_start_event(startEvent)
            vacation.set_end_event(endEvent)
            vacation.set_type(type)
            result.append(vacation)

        self._cnx.commit()
        return result

    """
    Gibt alle VacationBO aus einen angegebenen Zeitraum zurück
    param: start_date (date) - Start des Zeitintervalls
           end_date (date) - Ende des Zeitintervalls
    return: result - alle VacationBO im angegebenen Zeitraum
    """

    def find_by_time_period(self, start_date, end_date):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, dateOfLastChange, start, end, startEvent, endEvent, type FROM worktimeapp.vacations WHERE start>={} AND end<={}".format(
            start_date, end_date)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, dateOfLastChange, start, end, startEvent, endEvent, type) in tuples:
            vacation = VacationBO()
            vacation.set_id(id)
            vacation.set_date_of_last_change(dateOfLastChange)
            vacation.set_start(start)
            vacation.set_end(end)
            # vacation.set_time_interval_booking_id(timeIntervalId)
            vacation.set_start_event(startEvent)
            vacation.set_end_event(endEvent)
            vacation.set_type(type)
            result.append(vacation)

        self._cnx.commit()
        return result

    """
    Gibt das VacationBO mit gegebener booking_id zurück
    param: bookingId - Fremdschlüssel von BookingBO
    return: result - VacationBO
    """
    # def find_by_time_interval_id(self, bookingId):
    #     result = None
    #     cursor = self._cnx.cursor()
    #     command = "SELECT id, dateOfLastChange, start, end, startEvent, endEvent, type FROM worktimeapp.vacations WHERE timeIntervalId={}".format(bookingId)
    #     cursor.execute(command)
    #     tuples = cursor.fetchall()

    #     if tuples[0] is not None:
    #         (id, dateOfLastChange, start, end, timeIntervalId, startEvent, endEvent, type) = tuples[0]
    #         vacation = VacationBO()
    #         vacation.set_id(id)
    #         vacation.set_date_of_last_change(dateOfLastChange)
    #         vacation.set_start(start)
    #         vacation.set_end(end)
    #         vacation.set_time_interval_id(timeIntervalId)
    #         vacation.set_start_event(startEvent)
    #         vacation.set_end_event(endEvent)
    #         vacation.set_type(type)
    #         result = vacation

    #     self._cnx.commit()
    #     cursor.close()
    #     return result
