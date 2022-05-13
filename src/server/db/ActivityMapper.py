from unicodedata import name
from server.db.Mapper import Mapper
from server.bo.ActivityBO import ActivityBO

class ActivityMapper(Mapper):
    def __init__(self):
        super().__init__()

    """
    Gibt alle ActivityBO aus der Datenbank zurück
    return: Liste mit ActivityBO (list) - alle ActivityBO in der Datenbank
    """    
    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * from activities")
        tuples = cursor.fetchall()

        for (id, dateOfLastChange, name, capacity, project_id, duration) in tuples:
            activityobj = ActivityBO()
            activityobj.set_id(id)
            activityobj.set_date_of_last_change(dateOfLastChange)
            activityobj.set_name(name)
            activityobj.set_capacity(capacity)
            activityobj.set_project_id(project_id)
            activityobj.set_duration(duration)
            result.append(activityobj)

        self._cnx.commit()
        return result

    """
    Gibt das ActivityBO mit den gegebener Id zurück
    param: key (int) - Id vom gesuchtem ActivityBO
    return: ActivityBO mit der Id = key
    """    
    def find_by_key(self, key):
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT * FROM activities WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            (id, dateOfLastChange, name, capacity, project_id, duration) = tuples[0]
            activityobj = ActivityBO()
            activityobj.set_id(id)
            activityobj.set_date_of_last_change(dateOfLastChange)
            activityobj.set_name(name)
            activityobj.set_capacity(capacity)
            activityobj.set_project_id(project_id)
            activityobj.set_duration(duration)
            result = activityobj

        self._cnx.commit()
        cursor.close()

        return result

    """
    Fügt ein ActivityBO in die Datenbank ein
    param: activity_obj (ActivityBO) - ActivityBO welches eingefügt werden soll
    return: activity_obj
    """
    def insert (self, activity_obj):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM activities")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            activity_obj.set_id(maxid[0]+1)

        command = "INSERT INTO activities (id, dateOfLastChange, name, capacity, project_id, duration) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (activity_obj.get_id(), activity_obj.get_date_of_last_change(), activity_obj.get_name(), activity_obj.get_capacity(), activity_obj.get_project_id(), activity_obj.get_duration())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return activity_obj

    """
    Ändert die Attribute eines ActivityBO welches bereits in der Datenbank ist
    param: activity_obj (ActivityBO) - ActivityBO mit aktualisierten Daten
    return: None 
    """
    def update (self, activity_obj):
        cursor = self._cnx.cursor()

        command = "UPDATE activities " + "SET name=%s, capacity=%s, duration=%s WHERE id=%s"
        data = (activity_obj.get_name(), activity_obj.get_capacity(), activity_obj.get_duration, activity_obj.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    """
    Löscht ein ActivityBO aus der Datenbank
    param: activity_obj (ActivityBO) - ActivityBO welches aus der Datenbank gelöscht werden soll
    return: None
    """
    def delete(self, activity_obj):
        cursor = self._cnx.cursor()

        command = "DELETE FROM activities WHERE id={}".format(activity_obj.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()   

    """
    Gibt das ActivityBO mit dem gegebenen Startdatum zurück
    param: name (str) - UserId vom gesuchtem ActivityBO
    return: ActivityBO mit user_id = id
    """
    def find_by_name(self, name):
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT * FROM activities WHERE name={}".format(name)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            (id, dateOfLastChange, name, capacity, project_id, duration) = tuples[0]
            activityobj = ActivityBO()
            activityobj.set_id(id)
            activityobj.set_date_of_last_change(dateOfLastChange)
            activityobj.set_name(name)
            activityobj.set_capacity(capacity)
            activityobj.set_project_id(project_id)
            activityobj.set_duration(duration)
            result = activityobj

        self._cnx.commit()
        cursor.close()

        return result

    """
    Gibt das ActivityBO mit dem gegebenen Startdatum zurück
    param: project_id (int) - ProjectId vom gesuchtem ActivityBO
    return: ActivityBO mit project_id = project_id
    """
    def find_all_by_project_id(self, project_id):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * from activities WHERE project_id={}".format(project_id))
        tuples = cursor.fetchall()

        for (id, dateOfLastChange, name, capacity, project_id, duration) in tuples:
            activityobj = ActivityBO()
            activityobj.set_id(id)
            activityobj.set_date_of_last_change(dateOfLastChange)
            activityobj.set_name(name)
            activityobj.set_capacity(capacity)
            activityobj.set_project_id(project_id)
            activityobj.set_duration(duration)
            result.append(activityobj)

        self._cnx.commit()
        return result