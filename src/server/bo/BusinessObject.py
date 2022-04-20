from abc import ABC, abstractmethod


class BusinessObject(ABC):
    """Gemeinsame Basisklasse aller in diesem Projekt für die Umsetzung des Fachkonzepts relevanten Klassen.

    Zentrales Merkmal ist, dass jedes BusinessObject eine Nummer besitzt, die man in
    einer relationalen Datenbank auch als Primärschlüssel bezeichnen würde.
    """
    def __init__(self):
        self._id = 0   # Die eindeutige Identifikationsnummer einer Instanz dieser Klasse.
        self._date_of_last_change = None

    def get_id(self):
        """Auslesen der ID."""
        return self._id

    def set_id(self,value):
        """Setzen der ID."""
        self._id = value
    
    def get_date_of_last_change(self):
        """Auslesen des Datums der letzten Änderung."""
        return self._date_of_last_change

    def set_date_of_last_change(self,date):
        """Setzen des Datums der letzten Änderung."""
        self._date_of_last_change = date

