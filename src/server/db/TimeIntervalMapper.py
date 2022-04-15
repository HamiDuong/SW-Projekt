from server.db import Mapper
from server.bo import TimeIntervalBO

"""
Mapper für TimeIntervalBO - Schnittstelle zur Datenbank
"""
class TimeIntervalMapper(Mapper):

    def __init__(self):
        super().__init__()
    
    """
    Gibt alle TimeIntervalBO aus der Datenbank zurück
    return: Liste mit TimeIntervallBO (list) - alle TimeIntervalBO in der Datenbank
    """
    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT id from _")
        tuples = cursor.fetchall()

        for (id) in tuples:
            ti_obj = TimeIntervalBO()
            ti_obj.set_id(id)
            result.append(ti_obj)

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
        command = "SELECT id FROM _ WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            (id, x) = tuples[0]
            ti_obj = TimeIntervalBO()
            ti_obj.set_id(id)
        
        result = ti_obj

        self._cnx.commit()
        cursor.close()

        return result

    """
    Fügt ein TimeIntervalBO in die Datenbank ein
    param: ti_obj (TimeIntervalBO) - TimeIntervalBO welches eingefügt werden soll
    return: ti_obj
    """
    def insert (self, ti_obj):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM _")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            ti_obj.set_id(maxid[0]+1)

        command = "INSET INTO _ () VALUES (%s)"
        data = (ti_obj.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return ti_obj

    """
    Ändert die Attribute eines TimeIntervalBO welches bereits in der Datenbank ist
    param: ti_obj (TimeIntervalBO) - TimeIntervalBO mit aktualisierten Daten
    return: None 
    """
    def update (self, ti_obj):
        cursor = self._cnx.cursor()

        command = "UPDATE _ " + "SET _ WHERE id=%s"
        data = (ti_obj.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    """
    Löscht ein TimeIntervalBO aus der Datenbank
    param: ti_obj (TimeIntervalBO) - TimeIntervalBO welches aus der Datenbank gelöscht werden soll
    return: None
    """
    def delete(self, ti_obj):
        cursor = self._cnx.cursor()

        command = "DELETE FROM _ WHERE id={}".format(ti_obj.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()   