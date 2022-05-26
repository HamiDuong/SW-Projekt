from server.db.Mapper import Mapper
from server.bo.eventBOs.ProjectWorkBegin import ProjectWorkBeginBO
from datetime import datetime


class ProjectWorkBeginMapper(Mapper):
    def __init__(self):
        super().__init__()

    def insert(self, project_work_begin):
        timestamp = datetime.today()
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM worktimeapp.ProjectWorkBegin ")
        tuples = cursor.fetchall()
        project_work_begin.set_date_of_last_change(timestamp)

        for (maxid) in tuples:
            if maxid[0] is not None:
                project_work_begin.set_id(maxid[0] + 1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                project_work_begin.set_id(1)

        command = "INSERT INTO worktimeapp.ProjectWorkBegin (id, date_of_last_change, date) VALUES (%s, %s,%s)"
        data = (
            project_work_begin.get_id(),
            project_work_begin.get_date_of_last_change(),
            project_work_begin.get_time(),
        )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return project_work_begin

    def find_all(self):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, date FROM worktimeapp.ProjectWorkBegin"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, date) in tuples:
            project_work_begin = ProjectWorkBeginBO()
            project_work_begin.set_id(id)
            project_work_begin.set_time(date)
            result.append(project_work_begin)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, date FROM worktimeapp.ProjectWorkBegin WHERE id={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, date) = tuples[0]
            project_work_begin = ProjectWorkBeginBO()
            project_work_begin.set_id(id)
            project_work_begin.set_time(date)
            result = project_work_begin
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
        command = "SELECT id, date FROM worktimeapp.ProjectWorkBegin WHERE date={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, date) in tuples:
            project_work_begin = ProjectWorkBeginBO()
            project_work_begin.set_id(id)
            project_work_begin.set_time(date)
            result.append(project_work_begin)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_event_booking_id(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, date FROM worktimeapp.ProjectWorkBegin WHERE chatid={}".format(
            key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, date) = tuples[0]
            project_work_begin = ProjectWorkBeginBO()
            project_work_begin.set_id(id)
            project_work_begin.set_time(date)
            result = project_work_begin
        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def update(self, project_work_begin):
        datestamp = datetime.today()
        cursor = self._cnx.cursor()
        project_work_begin.set_date_of_last_change(datestamp)

        command = "UPDATE worktimeapp.ProjectWorkBegin " + \
            "SET date=%s WHERE id=%s"
        data = (project_work_begin.get_time(),
                project_work_begin.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return project_work_begin

    def delete(self, project_work_begin):
        cursor = self._cnx.cursor()

        command = "DELETE FROM worktimeapp.ProjectWorkBegin WHERE id={}".format(
            project_work_begin.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
