from server.db.Mapper import Mapper
from server.bo.ProjectUserBO import ProjectUserBO

class ProjectUserMapper(Mapper):
    def __init__(self):
        super().__init__()

    """
    Gibt alle ProjectUserBO aus der Datenbank zurück
    return: Liste mit ProjectUserBO (list) - alle ProjectUserBO in der Datenbank
    """    
    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * from projectusers")
        tuples = cursor.fetchall()

        for (id, dateOfLastChange, project_id, user_id, capacity) in tuples:
            projectuserobj = ProjectUserBO()
            projectuserobj.set_id(id)
            projectuserobj.set_date_of_last_change(dateOfLastChange)
            projectuserobj.set_project_id(project_id)
            projectuserobj.set_user_id(user_id)
            projectuserobj.set_capacity(capacity)

            result.append(projectuserobj)

        self._cnx.commit()
        return result

    """
    Gibt das ProjectUserBO mit den gegebener Id zurück
    param: key (int) - Id vom gesuchtem ProjectUserBO
    return: ProjectUserBO mit der Id = key
    """    
    def find_by_key(self, key):
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT * FROM projectusers WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            (id, dateOfLastChange, project_id, user_id, capacity) = tuples[0]
            projectuserobj = ProjectUserBO()
            projectuserobj.set_id(id)
            projectuserobj.set_date_of_last_change(dateOfLastChange)
            projectuserobj.set_project_id(project_id)
            projectuserobj.set_user_id(user_id)
            projectuserobj.set_capacity(capacity)
            result = projectuserobj

        self._cnx.commit()
        cursor.close()

        return result

    """
    Fügt ein ProjectUserBO in die Datenbank ein
    param: projectuser_obj (ProjectUserBO) - ProjectUserBO welches eingefügt werden soll
    return: projectuser_obj
    """
    def insert (self, projectuser_obj):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM projectusers")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            projectuser_obj.set_id(maxid[0]+1)

        command = "INSERT INTO projectusers (id, dateOfLastChange, project_id, user_id, capacity) VALUES (%s, %s, %s, %s, %s)"
        data = (projectuser_obj.get_id(), projectuser_obj.get_date_of_last_change(), projectuser_obj.get_project_id(), projectuser_obj.get_user_id(), projectuser_obj.get_capacity())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return projectuser_obj

    """
    Ändert die Attribute eines ProjectUserBO welches bereits in der Datenbank ist
    param: projectuser_obj (ProjectUserBO) - ProjectUserBO mit aktualisierten Daten
    return: None 
    """
    def update (self, projectuser_obj):
        cursor = self._cnx.cursor()

        command = "UPDATE projectusers " + "SET project_id=%s, user_id=%s WHERE capacity=%s"
        data = (projectuser_obj.get_(), projectuser_obj.get_user_id(), projectuser_obj.get_capacity())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    """
    Löscht ein ProjectUserBO aus der Datenbank
    param: projectuser_obj (ProjectUserBO) - ProjectUserBO welches aus der Datenbank gelöscht werden soll
    return: None
    """
    def delete(self, projectuser_obj):
        cursor = self._cnx.cursor()

        command = "DELETE FROM projectusers WHERE id={}".format(projectuser_obj.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()   

    """
    Gibt das ProjectUserBO mit dem gegebenen Startdatum zurück
    param: id (int) - UserId vom gesuchtem ProjectUserBO
    return: ProjectUserBO mit user_id = id
    """
    def find_all_project_members(self, project_id):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * from projectusers WHERE project_id = {}",format(project_id) )
        tuples = cursor.fetchall()

        for (id, dateOfLastChange, project_id, user_id, capacity) in tuples:
            projectuserobj = ProjectUserBO()
            projectuserobj.set_id(id)
            projectuserobj.set_date_of_last_change(dateOfLastChange)
            projectuserobj.set_project_id(project_id)
            projectuserobj.set_user_id(user_id)
            projectuserobj.set_capacity(capacity)

            result.append(projectuserobj)

        self._cnx.commit()
        return result