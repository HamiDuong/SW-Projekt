from server.db.Mapper import Mapper
from server.bo.eventBOs.ProjectWorkEnd import ProjectWorkEndBO
from datetime import datetime


class ProjectWorkEndMapper(Mapper):
    def __init__(self):
        super().__init__()

    def insert(self, project_work_end):
        timestamp = datetime.today()
        cursor = self._cnx.cursor()
        cursor.execute(
            "SELECT MAX(id) AS maxid FROM worktimeapp.project_work_end ")
        tuples = cursor.fetchall()
        project_work_end.set_date_of_last_change(timestamp)

        for (maxid) in tuples:
            if maxid[0] is not None:
                project_work_end.set_id(maxid[0] + 1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                project_work_end.set_id(1)

        command = "INSERT INTO worktimeapp.project_work_end (id, date_of_last_change, date, eventid) VALUES (%s, %s,%s,%s)"
        data = (
            project_work_end.get_id(),
            project_work_end.get_date_of_last_change(),
            project_work_end.get_time(),
            project_work_end.get_event_id(),
        )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return project_work_end

    def find_all(self):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, date, eventid FROM worktimeapp.project_work_end"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, date, eventid) in tuples:
            project_work_end = ProjectWorkEndBO()
            project_work_end.set_id(id)
            project_work_end.set_time(date)
            project_work_end.set_event_id(eventid)
            result.append(project_work_end)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, date, eventid FROM worktimeapp.project_work_end WHERE id={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, date, eventid) = tuples[0]
            project_work_end = ProjectWorkEndBO()
            project_work_end.set_id(id)
            project_work_end.set_time(date)
            project_work_end.set_event_id(eventid)
            result = project_work_end
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
        command = "SELECT id, date, eventid FROM worktimeapp.project_work_end WHERE date={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, date, eventid) in tuples:
            project_work_end = ProjectWorkEndBO()
            project_work_end.set_id(id)
            project_work_end.set_time(date)
            project_work_end.set_event_id(eventid)
            result.append(project_work_end)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_event_booking_id(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, date, eventid FROM worktimeapp.project_work_end WHERE chatid={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, date, eventid) = tuples[0]
            project_work_end = ProjectWorkEndBO()
            project_work_end.set_id(id)
            project_work_end.set_time(date)
            project_work_end.set_event_id(eventid)
            result = project_work_end
        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def update(self, project_work_end):
        datestamp = datetime.today()
        cursor = self._cnx.cursor()
        project_work_end.set_date_of_last_change(datestamp)

        command = "UPDATE worktimeapp.project_work_end " + \
            "SET date=%s, eventid=%s WHERE id=%s"
        data = (project_work_end.get_time(), project_work_end.get_event_id(),
                project_work_end.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return project_work_end

    def delete(self, project_work_end):
        cursor = self._cnx.cursor()

        command = "DELETE FROM worktimeapp.project_work_end WHERE id={}".format(
            project_work_end.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
