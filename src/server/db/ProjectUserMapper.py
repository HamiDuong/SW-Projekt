from server.db.Mapper import Mapper
from server.bo.ProjectUserBO import ProjectUserBO
from datetime import datetime

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

        for (id, dateOfLastChange, projectId, userId, capacity, currentCapacity) in tuples:
            projectuserobj = ProjectUserBO()
            projectuserobj.set_id(id)
            projectuserobj.set_date_of_last_change(dateOfLastChange)
            projectuserobj.set_project_id(projectId)
            projectuserobj.set_user_id(userId)
            projectuserobj.set_capacity(capacity)
            projectuserobj.set_current_capacity(currentCapacity)

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
            (id, dateOfLastChange, projectId, userId, capacity, currentCapacity) = tuples[0]
            projectuserobj = ProjectUserBO()
            projectuserobj.set_id(id)
            projectuserobj.set_date_of_last_change(dateOfLastChange)
            projectuserobj.set_project_id(projectId)
            projectuserobj.set_user_id(userId)
            projectuserobj.set_capacity(capacity)
            projectuserobj.set_current_capacity(currentCapacity)
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

        timestamp = datetime.today()
        projectuser_obj.set_date_of_last_change(timestamp)    

        for (maxid) in tuples:
            if maxid[0] == None:
                projectuser_obj.set_id(1)
            else:
                projectuser_obj.set_id(maxid[0]+1)

        command = "INSERT INTO projectusers (id, dateOfLastChange, projectId, userId, capacity, currentCapacity) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (projectuser_obj.get_id(), projectuser_obj.get_date_of_last_change(), projectuser_obj.get_project_id(), projectuser_obj.get_user_id(), projectuser_obj.get_capacity(), projectuser_obj.get_current_capacity())
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

        timestamp = datetime.today()
        projectuser_obj.set_date_of_last_change(timestamp)

        command = "UPDATE projectusers " + "SET projectId=%s, userId=%s, capacity=%s, currentCapacity=%s, dateOfLastChange=%s WHERE id=%s"
        data = (projectuser_obj.get_(), projectuser_obj.get_user_id(), projectuser_obj.get_capacity(), projectuser_obj.get_current_capacity(), projectuser_obj.get_date_of_last_change(),projectuser_obj.get_id())
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
    def find_all_project_members(self, projectId):
        result = []
        cursor = self._cnx.cursor()

        command = "SELECT * from projectusers WHERE projectId = {}"
        data = (projectId)
        cursor.execute(command, data)

        #cursor.execute("SELECT * from projectusers WHERE projectId = {}".format(projectId) )
        tuples = cursor.fetchall()

        for (id, dateOfLastChange, projectId, userId, capacity, currentCapacity) in tuples:
            projectuserobj = ProjectUserBO()
            projectuserobj.set_id(id)
            projectuserobj.set_date_of_last_change(dateOfLastChange)
            projectuserobj.set_project_id(projectId)
            projectuserobj.set_user_id(userId)
            projectuserobj.set_capacity(capacity)
            projectuserobj.set_current_capacity(currentCapacity)
            result.append(projectuserobj)

        self._cnx.commit()
        return result