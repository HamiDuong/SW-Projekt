from server.db.Mapper import Mapper
from server.bo.eventBOs.EventBO import EventBO
from datetime import datetime


class EventMapper(Mapper):
    def __init__(self):
        super().__init__()

    def insert(self, event):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM worktimeapp.event ")
        tuples = cursor.fetchall()
        datestamp = datetime.today()
        '''Wann immer ein neues Objekt in die Datenbank überführt wird, wird ein Zeitstempel erstellt
            und in die Spalte date_of_last_change eingefügt.'''
        event.set_date_of_last_change(datestamp)

        for (maxid) in tuples:
            if maxid[0] is not None:
                event.set_id(maxid[0] + 1)

            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                event.set_id(1)

        command = "INSERT INTO worktimeapp.event (id, date_of_last_change, type, coming_id, going_id, break_begin_id, \
                   break_end_id, illness_begin_id, illness_end_id, project_work_begin_id, project_work_end_id, \
                   vacation_begin_id, vacation_end_id, flex_day_start_id, flex_day_end_id )  \
                   VALUES (%s, %s, %s, %s, %s,%s, %s, %s,%s ,%s, %s, %s, %s, %s, %s)"
        data = (
            event.get_id(),
            event.get_date_of_last_change(),
            event.get_type(),
            event.get_coming_id(),
            event.get_going_id(),
            event.get_break_begin_id(),
            event.get_break_end_id(),
            event.get_illness_begin_id(),
            event.get_illness_end_id(),
            event.get_project_work_begin_id(),
            event.get_project_work_end_id(),
            event.get_vacation_begin_id(),
            event.get_vacation_end_id(),
            event.get_flex_day_start_id(),
            event.get_flex_day_end_id()

        )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return event

    def find_all(self):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, date_of_last_change, type, coming_id, going_id, break_begin_id, break_end_id,\
                    illness_begin_id, illness_end_id, project_work_begin_id, project_work_end_id, \
                    vacation_begin_id, vacation_end_id, flex_day_start_id, flex_day_end_id FROM worktimeapp.event"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, dateoflastange,  type, coming_id, going_id, break_begin_id,  break_end_id,
             illness_begin_id, illness_end_id, project_work_begin_id, project_work_end_id,
             vacation_begin_id, vacation_end_id, flex_day_start_id, flex_day_end_id) in tuples:

            event = EventBO()
            event.set_id(id)
            event.set_date_of_last_change(dateoflastange)
            event.set_type(type),
            event.set_coming_id(coming_id), event.set_going_id(going_id),
            event.set_break_begin_id(
                break_begin_id), event.set_break_end_id(break_end_id),
            event.set_illness_begin_id(
                illness_begin_id), event.set_illness_end_id(illness_end_id),
            event.set_project_work_begin_id(
                project_work_begin_id), event.set_project_work_end_id(project_work_end_id),
            event.set_vacation_begin_id(
                vacation_begin_id), event.set_vacation_end_id(vacation_end_id),
            event.set_flex_day_start_id(
                flex_day_start_id), event.set_flex_day_end_id(flex_day_end_id)
            result.append(event)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, date_of_last_change, type, coming_id, going_id, break_begin_id, break_end_id,\
                    illness_begin_id, illness_end_id, project_work_begin_id, project_work_end_id, \
                    vacation_begin_id, vacation_end_id, flex_day_start_id, flex_day_end_id FROM worktimeapp.event WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, date_of_last_change, type, coming_id, going_id, break_begin_id,  break_end_id,
             illness_begin_id, illness_end_id, project_work_begin_id, project_work_end_id,
             vacation_begin_id, vacation_end_id, flex_day_start_id, flex_day_end_id) = tuples[0]
            event = EventBO()
            event.set_id(id)
            event.set_date_of_last_change(date_of_last_change)
            event.set_type(type),
            event.set_coming_id(coming_id), event.set_going_id(going_id),
            event.set_break_begin_id(
                break_begin_id), event.set_break_end_id(break_end_id),
            event.set_illness_begin_id(
                illness_begin_id), event.set_illness_end_id(illness_end_id),
            event.set_project_work_begin_id(
                project_work_begin_id), event.set_project_work_end_id(project_work_end_id),
            event.set_vacation_begin_id(
                vacation_begin_id), event.set_vacation_end_id(vacation_end_id),
            event.set_flex_day_start_id(
                flex_day_start_id), event.set_flex_day_end_id(flex_day_end_id)
            result = event
        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_foreign_key_and_type(self, foreign_key, key, type):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, date_of_last_change, type, coming_id, going_id, break_begin_id, break_end_id,\
                    illness_begin_id, illness_end_id, project_work_begin_id, project_work_end_id, \
                    vacation_begin_id, vacation_end_id, flex_day_start_id, flex_day_end_id FROM worktimeapp.event WHERE {}={} AND type='{}'".format(foreign_key, key, type)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, date_of_last_change, type, coming_id, going_id, break_begin_id,  break_end_id,
             illness_begin_id, illness_end_id, project_work_begin_id, project_work_end_id,
             vacation_begin_id, vacation_end_id, flex_day_start_id, flex_day_end_id) = tuples[0]
            event = EventBO()
            event.set_id(id)
            event.set_date_of_last_change(date_of_last_change)
            event.set_type(type),
            event.set_coming_id(coming_id), event.set_going_id(going_id),
            event.set_break_begin_id(
                break_begin_id), event.set_break_end_id(break_end_id),
            event.set_illness_begin_id(
                illness_begin_id), event.set_illness_end_id(illness_end_id),
            event.set_project_work_begin_id(
                project_work_begin_id), event.set_project_work_end_id(project_work_end_id),
            event.set_vacation_begin_id(
                vacation_begin_id), event.set_vacation_end_id(vacation_end_id),
            event.set_flex_day_start_id(
                flex_day_start_id), event.set_flex_day_end_id(flex_day_end_id)
            result = event
        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_date(self, key):
        result = []

        cursor = self._cnx.cursor()
        command = "SELECT id, date_of_last_change, type, coming_id, going_id, break_begin_id, break_end_id,\
                    illness_begin_id, illness_end_id, project_work_begin_id, project_work_end_id, \
                    vacation_begin_id, vacation_end_id, flex_day_start_id, flex_day_end_id \
                    FROM worktimeapp.event WHERE date={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, date_of_last_change, type, coming_id, going_id, break_begin_id,  break_end_id,
             illness_begin_id, illness_end_id, project_work_begin_id, project_work_end_id,
             vacation_begin_id, vacation_end_id, flex_day_start_id, flex_day_end_id) in tuples:
            event = EventBO()
            event.set_id(id)
            event.set_date_of_last_change(date_of_last_change)
            event.set_type(type),
            event.set_coming_id(coming_id), event.set_going_id(going_id),
            event.set_break_begin_id(
                break_begin_id), event.set_break_end_id(break_end_id),
            event.set_illness_begin_id(
                illness_begin_id), event.set_illness_end_id(illness_end_id),
            event.set_project_work_begin_id(
                project_work_begin_id), event.set_project_work_end_id(project_work_end_id),
            event.set_vacation_begin_id(
                vacation_begin_id), event.set_vacation_end_id(vacation_end_id),
            event.set_flex_day_start_id(
                flex_day_start_id), event.set_flex_day_end_id(flex_day_end_id)
            result.append(event)

        self._cnx.commit()
        cursor.close()

        return result

    def update(self, event):
        print("HIER", event)
        cursor = self._cnx.cursor()
        datestamp = datetime.today()
        '''Wann immer ein vorhandenes Objekt in der Datenbank geändert wird, wird ein Zeitstempel erstellt
           und in die Spalte date_of_last_change eingefügt.'''
        event.set_date_of_last_change(datestamp)

        command = "UPDATE worktimeapp.event " + \
            "SET date_of_last_change=%s WHERE id=%s"
        data = (event.get_date_of_last_change(),
                event.get_id()
                )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return event

    def delete(self, event):
        cursor = self._cnx.cursor()

        command = "DELETE FROM worktimeapp.event WHERE id={}".format(
            event.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
