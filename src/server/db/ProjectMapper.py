from server.db.Mapper import Mapper
from server.bo.ProjectBO import ProjectBO

class ProjectMapper(Mapper):
    def __init__(self):
        super().__init__()

    """
    Gibt alle ProjectBO aus der Datenbank zurück
    return: Liste mit ProjectBO (list) - alle ProjectBO in der Datenbank
    """    
    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * from projects")
        tuples = cursor.fetchall()

        for (id, dateOfLastChange, name, commissioner, user_id) in tuples:
            projectobj = ProjectBO()
            projectobj.set_id(id)
            projectobj.set_date_of_last_change(dateOfLastChange)
            projectobj.set_name(name)
            projectobj.set_commissioner(commissioner)
            projectobj.set_user_id(user_id)
            result.append(projectobj)

        self._cnx.commit()
        return result

    """
    Gibt das ProjectBO mit den gegebener Id zurück
    param: key (int) - Id vom gesuchtem ProjectBO
    return: ProjectBO mit der Id = key
    """    
    def find_by_key(self, key):
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT * FROM projects WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            (id, dateOfLastChange, name, commissioner, user_id) = tuples[0]
            projectobj = ProjectBO()
            projectobj.set_id(id)
            projectobj.set_date_of_last_change(dateOfLastChange)
            projectobj.set_name(name)
            projectobj.set_commissioner(commissioner)
            projectobj.set_user_id(user_id)
            result = projectobj

        self._cnx.commit()
        cursor.close()

        return result

    """
    Fügt ein ProjectBO in die Datenbank ein
    param: project_obj (ProjectBO) - ProjectBO welches eingefügt werden soll
    return: project_obj
    """
    def insert (self, project_obj):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM projects")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            project_obj.set_id(maxid[0]+1)

        command = "INSERT INTO projects (id, dateOfLastChange, name, commissioner, user_id) VALUES (%s, %s, %s, %s, %s)"
        data = (project_obj.get_id(), project_obj.get_date_of_last_change(), project_obj.get_name(), project_obj.get_commissioner(), project_obj.get_user_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return project_obj

    """
    Ändert die Attribute eines ProjectBO welches bereits in der Datenbank ist
    param: project_obj (ProjectBO) - ProjectBO mit aktualisierten Daten
    return: None 
    """
    def update (self, project_obj):
        cursor = self._cnx.cursor()

        command = "UPDATE projects " + "SET name=%s, commissioner=%s WHERE user_id=%s"
        data = (project_obj.get_name(), project_obj.get_commissioner(), project_obj.get_user_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    """
    Löscht ein ProjectBO aus der Datenbank
    param: project_obj (ProjectBO) - ProjectBO welches aus der Datenbank gelöscht werden soll
    return: None
    """
    def delete(self, project_obj):
        cursor = self._cnx.cursor()

        command = "DELETE FROM projects WHERE id={}".format(project_obj.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()   

    """
    Gibt das ProjectBO mit dem gegebenen Startdatum zurück
    param: id (int) - UserId vom gesuchtem ProjectBO
    return: ProjectBO mit user_id = id
    """
    def find_admin_by_user_id(self, id):
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT * FROM projects WHERE user_id={}".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            (id, dateOfLastChange, name, commissioner, user_id) = tuples[0]
            projectobj = ProjectBO()
            projectobj.set_id(id)
            projectobj.set_date_of_last_change(dateOfLastChange)
            projectobj.set_name(name)
            projectobj.set_commissioner(commissioner)
            projectobj.set_user_id(user_id)
            result = projectobj

        self._cnx.commit()
        cursor.close()

        return result
    
    """
    Gibt das ProjectBO mit dem gegebenen Startdatum zurück
    param: name (str) - name vom gesuchtem ProjectBO
    return: ProjectBO mit name = name
    """
    def find_by_project_name(self, name):
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT * FROM projects WHERE name={}".format(name)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            (id, dateOfLastChange, name, commissioner, user_id) = tuples[0]
            projectobj = ProjectBO()
            projectobj.set_id(id)
            projectobj.set_date_of_last_change(dateOfLastChange)
            projectobj.set_name(name)
            projectobj.set_commissioner(commissioner)
            projectobj.set_user_id(user_id)
            result = projectobj

        self._cnx.commit()
        cursor.close()

        return result