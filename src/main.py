"""
A. Allgemeine Hinweise zu diesem Module:
Normalerweise würde man eine Datei dieser Länge bzw. ein Module
dieser Größe in mehrere Dateien bzw. Modules untergliedern. So könnte
man z.B. pro Resource Class ein eigenes Module anlegen. Dadurch
ergäben sich erhebliche Vorteile bzgl. der Wartungsfreundlichkeit
dieses Modules. Es ergäben sich aber auch Nachteile! So haben Sie
etwa mit einer Reihe von Abhängigkeiten z.B. zwischen der API-Definition
und den Decorators zu tun. Außerdem verschlechtert sich aufgrund der Länge
der Datei die Übersichtlichkeit der Inhalte und Strukturen.
Abgesehen von Lehrbüchern und Vorlesungen müssen Sie in realen Projekten
häufig die Vor- und Nachteile von Entscheidungen abwägen und sich dann
bewusst für einen Weg entscheiden. Hier wurde die Entscheidung getroffen,
die Einfachheit und Verständlichkeit des Source Codes höher zu werten als
die Optimierung des Kopplungsgrads und damit die Wartbarkeit des Modules.
B. Konventionen für dieses Module:
    B.1. HTTP response status codes:
        Folgende Codes werden verwendet:
        200 OK           :      bei erfolgreichen requests. Af die Verwendung von
                                weiter differenzierenden Statusmeldungen wie etwa
                                '204 No Content' für erfolgreiche requests, die
                                außer evtl. im Header keine weiteren Daten zurückliefern,
                                wird in dieser Fallstudie auch aus Gründen einer
                                möglichst einfachen Umsetzung verzichtet.
        401 Unauthorized :      falls der User sich nicht gegenüber dem System
                                authentisiert hat und daher keinen Zugriff erhält.
        404 Not Found    :      falls eine angefragte Resource nicht verfügbar ist
        500 Internal Server Error : falls der Server einen Fehler erkennt,
                                diesen aber nicht genauer zu bearbeiten weiß.
    B.2. Name des Moduls:
        Der Name dieses Moduls lautet main.py. Grund hierfür ist, dass Google
        App Engine, diesen Namen bevorzugt und sich dadurch das Deployment
        einfacher gestaltet. Natürlich wären auch andere Namen möglich. Dies
        wäre aber mit zusätzlichem Konfigurationsaufwand in der Datei app.yaml
        verbunden.
"""

# Unser Service basiert auf Flask
# from attr import attributes
from asyncio import events
from flask import Flask
# Auf Flask aufbauend nutzen wir RestX
from flask_restx import Api, Resource, fields
# Wir benutzen noch eine Flask-Erweiterung für Cross-Origin Resource Sharing
from flask_cors import CORS

# Wir greifen natürlich auf unsere Applikationslogik inkl. BusinessObject-Klassen zurück
from server.Businesslogic import Businesslogic
from server.bo.UserBO import UserBO
from server.bo.WorkTimeAccountBO import WorkTimeAccountBO
from server.bo.eventBOs.EventBO import EventBO
from server.bo.eventBOs.GoingBO import GoingBO
from server.bo.eventBOs.ComingBO import ComingBO
from server.bo.eventBOs.ProjectWorkBegin import ProjectWorkBeginBO
from server.bo.eventBOs.ProjectWorkEnd import ProjectWorkEndBO
from server.bo.eventBOs.VacationEndBO import VacationEndBO
from server.bo.eventBOs.VacationBeginBO import VacationBeginBO
from server.bo.eventBOs.BreakBeginBO import BreakBeginBO
from server.bo.eventBOs.BreakEndBO import BreakEndBO
from server.bo.eventBOs.IllnessEndBO import IllnessEndBO
from server.bo.eventBOs.IllnessBeginBO import IllnessBeginBO
from server.bo.eventBOs.FlexDayStart import FlexDayStartBO
from server.bo.eventBOs.FlexDayEndBO import FlexDayEndBO
from server.Businesslogic import Businesslogic
from server.bo.ProjectBO import ProjectBO
from server.bo.ProjectUserBO import ProjectUserBO
from server.bo.ActivityBO import ActivityBO
#from SecurityDecorator import secured

from server.bo.UserBO import UserBO
from server.bo.WorkTimeAccountBO import WorkTimeAccountBO
from server.bo.timeinterval.BreakBO import BreakBO
from server.bo.timeinterval.IllnessBO import IllnessBO
from server.bo.timeinterval.ProjectDurationBO import ProjectDurationBO
from server.bo.timeinterval.ProjectWorkBO import ProjectWorkBO
from server.bo.timeinterval.TimeIntervalBO import TimeIntervalBO
from server.bo.timeinterval.VacationBO import VacationBO
from server.bo.timeinterval.WorkBO import WorkBO
from server.bo.timeinterval.FlexDayBO import FlexDayBO

from server.bo.BookingBO import BookingBO
from server.bo.EventBookingBO import EventBookingBO
from server.bo.TimeIntervalBookingBO import TimeIntervalBookingBO
import time


# Außerdem nutzen wir einen selbstgeschriebenen Decorator, der die Authentifikation übernimmt
# from SecurityDecorator import secured

"""
Instanzieren von Flask. Am Ende dieser Datei erfolgt dann erst der 'Start' von Flask.
"""
app = Flask(__name__)

"""
Alle Ressourcen mit dem Präfix /worktimeapp für **Cross-Origin Resource Sharing** (CORS) freigeben.
Diese eine Zeile setzt die Installation des Package flask-cors voraus.
Sofern Frontend und Backend auf getrennte Domains/Rechnern deployed würden, wäre sogar eine Formulierung
wie etwa diese erforderlich:
CORS(app, resources={r"/worktimeapp/*": {"origins": "*"}})
Allerdings würde dies dann eine Missbrauch Tür und Tor öffnen, so dass es ratsamer wäre, nicht alle
"origins" zuzulassen, sondern diese explizit zu nennen. Weitere Infos siehe Doku zum Package flask-cors.
"""
CORS(app, resources=r'/worktimeapp/*')

"""
In dem folgenden Abschnitt bauen wir ein Modell auf, das die Datenstruktur beschreibt,
auf deren Basis Clients und Server Daten austauschen. Grundlage hierfür ist das Package flask-restx.
"""
api = Api(app, version='1.0', title='WorkTimeApp API',
          description='Eine rudimentäre Zeitwirtschaftsapp realisiert durch Flask')

"""Worktimeapp - Namespace
Namespaces erlauben die Strukturierung von APIs. In diesem Fall fasst dieser Namespace alle
Zeitwirtschaftsrelevanten Operationen unter dem Präfix /worktimeapp zusammen."""

worktimeapp = api.namespace(
    'worktimeapp', description='Funktionen der Worktimeapp')

"""Nachfolgend werden analog zu unseren BusinessObject-Klassen transferierbare Strukturen angelegt.
BusinessObject dient als Basisklasse, auf der die weiteren Strukturen User, Events, Projects, etc. aufsetzen."""
bo = api.model('BusinessObject', {
    'id': fields.Integer(attribute='_id', description='Der Unique Identifier eines Business Object'),
    'dateOfLastChange': fields.String(attribute='_date_of_last_change', description='Zeitpunkt der letzten Änderung')
})

"""Users"""
user = api.inherit('User', bo, {
    'first_name': fields.String(attribute='_first_name', description='Vorname eines Benutzers'),
    'last_name': fields.String(attribute='_last_name', description='Nachname eines Benutzers'),
    'mail_adress': fields.String(attribute='_mail_adress', description='E-Mail-Adresse eines Benutzers'),
    'google_user_id': fields.String(attribute='_google_user_id', description='Google User Id')
})

"""WorkTimeAccount"""
worktimeaccount = api.inherit('Object', bo, {
    'user_id': fields.Integer(attribute='_user_id', description='User ID eines Benutzers'),
    'contract_time': fields.Float(attribute='_contract_time', description='Vertragszeit des Benutzers'),
    'overtime': fields.Float(attribute='_overtime', description='Überstunden des Benutzers')
})

'''Project'''
project = api.inherit('Project', bo, {
    'name': fields.String(attribute='_name', description='Der Name des Projekts'),
    'commissioner': fields.String(attribute='_commissioner', description='Der Name des Projektleiter'),
    'user_id': fields.Integer(attribute='_user_id', description='Die ID eines Benutzer')
})

'''ProjectUser'''
projectuser = api.inherit('ProjectUser', bo, {
    'project_id': fields.Integer(attribute='_project_id', description='Die ID eines Projektmitglieds'),
    'user_id': fields.Integer(attribute='_user_id', description='Die ID eines Benutzer'),
    'capacity': fields.Float(attribute='_capacity', description='Die Kapazität eines Projekts')
})

'''Activity'''
activity = api.inherit('Activity', bo, {
    'name': fields.String(attribute='_name', description='Der Name des Akktivitäts'),
    'capacity': fields.Float(attribute='_capacity', description='Die Kapazität eines Aktivitäts'),
    'project_id': fields.Integer(attribute='_project_id', description='Die ID eines Aktivitäts'),
    'current_capacity':fields.Float(attribute='_current_capacity', description='Die aktuelle Kapazität eines Aktivitäts')

})

'''Event'''
event = api.inherit('Event', bo, {
    'event_id': fields.Integer(attribute='_event_id', description='Die ID des Events'),
    'type': fields.String(attribute='_type', description='Der Typ des Events'),
    'coming_id': fields.Integer(attribute='_event_id', description='Die ID des Coming - Events'),
    'going_id': fields.Integer(attribute='_event_id', description='Die ID des Going - Events'),
    'break_begin_id': fields.Integer(attribute='_event_id', description='Die ID des Pausenbeginn-Events'),
    'break_end_id': fields.Integer(attribute='_event_id', description='Die ID des Pausenende-Events'),
    'illness_begin_id': fields.Integer(attribute='_event_id', description='Die ID des Krankheitsbeginn-Events'),
    'illness_end_id': fields.Integer(attribute='_event_id', description='Die ID des Krankheitsende-Events'),
    'project_work_begin_id': fields.Integer(attribute='_event_id', description='Die ID des Projektarbeitbeginn-Events'),
    'project_work_end_id': fields.Integer(attribute='_event_id', description='Die ID des Projektarbeitende-Events'),
    'vacation_begin_id': fields.Integer(attribute='_event_id', description='Die ID des Urlaubbeginn-Events'),
    'vacation_end_id': fields.Integer(attribute='_event_id', description='Die ID des Urlaubende-Events')

})

event_subclass = api.inherit('event_subclass', bo, {
    'time': fields.String(attribute='_time', description='Zeitpunkt des Events'),
    'type': fields.String(attribute='_type', description='Der Typ des Events'),
})

coming = api.inherit('Coming', bo, {
    'time': fields.String(attribute='_time', description='Zeitpunkt des Events')
})

going = api.inherit('GoingBO', bo, {
    'time': fields.String(attribute='_time', description='Zeitpunkt des Events')
})

break_begin = api.inherit('BreakBegin', bo, {
    'time': fields.String(attribute='_time', description='Zeitpunkt des Events')
})

break_end = api.inherit('BreakEnd', bo, {
    'time': fields.String(attribute='_time', description='Zeitpunkt des Events')
})

illness_end = api.inherit('IllnessEnd', bo, {
    'time': fields.String(attribute='_time', description='Zeitpunkt des Events')
})

illness_begin = api.inherit('IllnessBegin', bo, {
    'time': fields.String(attribute='_time', description='Zeitpunkt des Events')
})

vacation_end = api.inherit('VacationEnd', bo, {
    'time': fields.String(attribute='_time', description='Zeitpunkt des Events')
})

vacation_begin = api.inherit('VacationBegin', bo, {
    'time': fields.String(attribute='_time', description='Zeitpunkt des Events')
})

project_work_end = api.inherit('ProjectWorkEnd', bo, {
    'time': fields.String(attribute='_time', description='Zeitpunkt des Events')
})

project_work_begin = api.inherit('ProjectWorkBegin', bo, {
    'time': fields.String(attribute='_time', description='Zeitpunkt des Events')
})

flex_day_start = api.inherit('FlexDayStart', bo, {
    'time': fields.String(attribute='_time', description='Zeitpunkt des Events')
})

flex_day_end = api.inherit('FlexDayEnd', bo, {
    'time': fields.String(attribute='_time', description='Zeitpunkt des Events')
})

"""
Timeinterval und zugehörige Subklassen
"""
timeinterval = api.inherit('TimeInterval', bo, {
    '_type': fields.String(attribute='_type', description='Art des Intervals'),
    '_break_id': fields.Integer(attribute='_break_id', descriptiong='Fremdschlüssel zu BreakBO'),
    '_illness_id': fields.Integer(attribute='_illness_id', descriptiong='Fremdschlüssel zu IllnessBO'),
    '_project_duration_id': fields.Integer(attribute='_project_duration_id', descriptiong='Fremdschlüssel zu ProjectDurationBO'),
    '_project_work_id': fields.Integer(attribute='_project_work_id', descriptiong='Fremdschlüssel zu ProjectWorkBO'),
    '_vacation_id': fields.Integer(attribute='_vacation_id', descriptiong='Fremdschlüssel zu VacationBO'),
    '_work_id': fields.Integer(attribute='_work_id', descriptiong='Fremdschlüssel zu WorkBO')
})

timeinterval_subclass = api.inherit('TimeInterval_subclass', bo, {
    'start': fields.String(attribute='_start', description='Startpunkt des Intervalls'),
    'end': fields.String(attribute='_end', description='Endpunkt des Intervalls'),
    'start_event': fields.Integer(attribute='_start_event', description='Fremdschlüssel zum Startevent'),
    'end_event': fields.Integer(attribute='_end_event', description='Fremdschlüssel zum Endevent'),
    'type': fields.String(attribute='_type', description='Art des Intervals')
})


breaks = api.inherit('Break', bo, {
    '_start': fields.String(attribute='_start', description='Startpunkt des Intervalls'),
    '_end': fields.String(attribute='_end', description='Endpunkt des Intervalls'),
    '_start_event': fields.Integer(attribute='_start_event', description='Fremdschlüssel zum Startevent'),
    '_end_event': fields.Integer(attribute='_end_event', description='Fremdschlüssel zum Endevent'),
    '_type': fields.String(attribute='_type', description='Art des Intervals')
})

illness = api.inherit('Illness', bo, {
    '_start': fields.String(attribute='_start', description='Startpunkt des Intervalls'),
    '_end': fields.String(attribute='_end', description='Endpunkt des Intervalls'),
    '_time_interval_id': fields.Integer(attribute='_time_interval_id', description='Fremdschlüssel zu Timeintervalbooking'),
    '_start_event': fields.Integer(attribute='_start_event', description='Fremdschlüssel zum Startevent'),
    '_end_event': fields.Integer(attribute='_end_event', description='Fremdschlüssel zum Endevent'),
    '_type': fields.String(attribute='_type', description='Art des Intervals')
})

vacation = api.inherit('Vacation', bo, {
    '_start': fields.String(attribute='_start', description='Startpunkt des Intervalls'),
    '_end': fields.String(attribute='_end', description='Endpunkt des Intervalls'),
    '_start_event': fields.Integer(attribute='_start_event', description='Fremdschlüssel zum Startevent'),
    '_end_event': fields.Integer(attribute='_end_event', description='Fremdschlüssel zum Endevent'),
    '_type': fields.String(attribute='_type', description='Art des Intervals')
})

work = api.inherit('Work', bo, {
    '_start': fields.String(attribute='_start', description='Startpunkt des Intervalls'),
    '_end': fields.String(attribute='_end', description='Endpunkt des Intervalls'),
    '_start_event': fields.Integer(attribute='_start_event', description='Fremdschlüssel zum Startevent'),
    '_end_event': fields.Integer(attribute='_end_event', description='Fremdschlüssel zum Endevent'),
    '_type': fields.String(attribute='_type', description='Art des Intervals')
})

flexday = api.inherit('FlexDay', bo, {
    '_start': fields.String(attribute='_start', description='Startpunkt des Intervalls'),
    '_end': fields.String(attribute='_end', description='Endpunkt des Intervalls'),
    '_start_event': fields.Integer(attribute='_start_event', description='Fremdschlüssel zum Startevent'),
    '_end_event': fields.Integer(attribute='_end_event', description='Fremdschlüssel zum Endevent'),
    '_type': fields.String(attribute='_type', description='Art des Intervals')
})

projectduration = api.inherit('ProjectDuration', bo, {
    '_start': fields.String(attribute='_start', description='Startpunkt des Intervalls'),
    '_end': fields.String(attribute='_end', description='Endpunkt des Intervalls'),
    '_start_event': fields.Integer(attribute='_start_event', description='Fremdschlüssel zum Startevent'),
    '_end_event': fields.Integer(attribute='_end_event', description='Fremdschlüssel zum Endevent'),
    '_type': fields.String(attribute='_type', description='Art des Intervals'),
    '_project_id': fields.Integer(attribute='_project_id', description='Fremschlüssel zum Projekt')
})

projectwork = api.inherit('ProjectWork', bo, {
    '_start': fields.String(attribute='_start', description='Startpunkt des Intervalls'),
    '_end': fields.String(attribute='_end', description='Endpunkt des Intervalls'),
    '_time_interval_id': fields.Integer(attribute='_time_interval_id', description='Fremdschlüssel zu Timeintervalbooking'),
    '_start_event': fields.Integer(attribute='_start_event', description='Fremdschlüssel zum Startevent'),
    '_end_event': fields.Integer(attribute='_end_event', description='Fremdschlüssel zum Endevent'),
    '_type': fields.String(attribute='_type', description='Art des Intervals'),
    '_activity_id': fields.Integer(attribute='_activity_id', description='Fremschlüssel zur Aktivity')
})

'''Booking und zugehörige Subklassen @author Mihriban Dogan (https://github.com/mihriban-dogan)'''
booking = api.inherit("Booking", bo, {
    '_work_time_account_id': fields.Integer(attribute="_work_time_account_id"),
    '_user_id': fields.Integer(attribute="_work_time_account_id"),
    '_type': fields.String(attribute="_type"),
    '_event_booking_id': fields.Integer(attribute="_event_booking_id"),
    '_time_interval_booking_id': fields.Integer(attribute="_time_interval_booking_id")
})

eventbooking = api.inherit("Eventbooking", bo, {
    '_event_id': fields.Integer(attribute="_event_id")
})
timeintervalbooking = api.inherit("Timeintervalbooking", bo, {
    '_time_interval_id': fields.Integer(attribute="_time_interval_id")
})

timeinterval_with_events = api.model("Timeinterval_with_events", {
    "timeintervals": fields.Nested(timeinterval_subclass),
    "events": fields.Nested(event_subclass)
})


# Tatsächliche Funktionen beginnen ab hier.
"""
User Methoden
"""


@worktimeapp.route('/user')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class UserOperations(Resource):
    @worktimeapp.marshal_list_with(user)
    # #@secured
    def get(self):
        """Auslesen aller User-Objekte.
        Sollten keine User-Objekte verfügbar sein, so wird eine leere Sequenz zurückgegeben."""
        adm = Businesslogic()
        user = adm.get_all_users()
        return user

    @worktimeapp.marshal_with(user, code=200)
    @worktimeapp.expect(user)  # Wir erwarten ein User-Objekt von Client-Seite.
    # #@secured
    def post(self):
        """Anlegen eines neuen User-Objekts.
        **ACHTUNG:** Wir fassen die vom Client gesendeten Daten als Vorschlag auf.
        So ist zum Beispiel die Vergabe der ID nicht Aufgabe des Clients.
        Selbst wenn der Client eine ID in dem Proposal vergeben sollte, so
        liegt es an der Businesslogic (Businesslogik), eine korrekte ID
        zu vergeben. *Das korrigierte Objekt wird schließlich zurückgegeben.*
        """
        adm = Businesslogic()
        proposal = UserBO.from_dict(api.payload)

        """RATSCHLAG: Prüfen Sie stets die Referenzen auf valide Werte, bevor Sie diese verwenden!"""
        if proposal is not None:
            """ Wir verwenden lediglich Vor- und Nachnamen des Proposals für die Erzeugung
            eines User-Objekts. Das serverseitig erzeugte Objekt ist das maßgebliche und 
            wird auch dem Client zurückgegeben. 
            """
            c = adm.create_user(
                proposal.get_first_name(),
                proposal.get_last_name(),
                proposal.get_mail_adress(),
                proposal.get_google_user_id())
            return c, 200
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500


@worktimeapp.route('/users/<int:id>')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@worktimeapp.param('id', 'Id des Objekts')
class UserWithIdOperations(Resource):
    @worktimeapp.marshal_with(user)
    # @secured
    def get(self, id):
        """Auslesen eines bestimmten User-Objekts.

        Das auszulesende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        user = adm.get_user_by_id(id)
        return user

    # @secured
    def delete(self, id):
        """Löschen eines bestimmten User-Objekts.

        Das zu löschende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        user = adm.get_user_by_id(id)
        adm.delete_user(user)
        return '', 200

    @worktimeapp.marshal_with(user)
    @worktimeapp.expect(user, validate=True)
    # #@secured
    def put(self, id):
        """Update eines bestimmten User-Objekts.

        **ACHTUNG:** Relevante id ist die id, die mittels URI bereitgestellt und somit als Methodenparameter
        verwendet wird. Dieser Parameter überschreibt das ID-Attribut des im Payload der Anfrage übermittelten
        User-Objekts.
        """
        adm = Businesslogic()
        user = UserBO.from_dict(api.payload)

        if user is not None:
            """Hierdurch wird die id des zu überschreibenden (vgl. Update) User-Objekts gesetzt.
            Siehe Hinweise oben.
            """
            user.set_id(id)
            adm.save_user(user)
            return '', 200
        else:
            return '', 500


# @worktimeapp.route('/users-by-name/<string:user_name>')
# @worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
# @worktimeapp.param('user_name', 'Der User Name des Benutzers')
# class UsersByNameOperations(Resource):
#     @worktimeapp.marshal_with(user)
#     # #@secured
#     def get(self, user_name):
#         """ Auslesen von User-Objekten, die durch den User Name bestimmt werden.

#         Die auszulesenden Objekte werden durch ```user_name``` in dem URI bestimmt.
#         """
#         adm = Businesslogic()
#         cust = adm.get_user_by_user_name(user_name)
#         return cust


@worktimeapp.route('/users-by-name/<string:last_name>')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@worktimeapp.param('last_name', 'Der Nachname des Benutzers')
class UsersByNameOperations(Resource):
    @worktimeapp.marshal_with(user)
    # #@secured
    def get(self, last_name):
        """ Auslesen von User-Objekten, die durch den Nachnamen bestimmt werden.

        Die auszulesenden Objekte werden durch ```last_name``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        cust = adm.get_user_by_last_name(last_name)
        return cust



@worktimeapp.route('/usermail/<string:mail_adress>')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@worktimeapp.param('String', 'Die E-Mail-Adresse eines Benutzers')
class UserWithEmailOperations(Resource):
    @worktimeapp.marshal_with(user)
    # #@secured
    def get(self, mail_adress):
        """Auslesen von User-Objekten, die durch die E-Mail_Adresse bestimmt werden.

        Die auszulesenden Objekte werden durch ```mail_adress``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        user = adm.get_user_by_mail_adress(mail_adress)
        return user


# @worktimeapp.route('/users/<string:user_name>')
# @worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
# @worktimeapp.param('id', 'Die E-Mail-Adresse eines Benutzers')
# class UserRelatedAccountOperations(Resource):
#     @worktimeapp.marshal_with(user)
#     # #@secured
#     def get(self, user_name):
#         """Auslesen von User-Objekten, die durch den User Namen bestimmt werden.

#         Die auszulesenden Objekte werden durch ```user_name``` in dem URI bestimmt.
#         """
#         adm = Businesslogic()
#         cust = adm.get_user_by_user_name(user_name)
#         return cust

@worktimeapp.route('/usergoogle/<string:google_user_id>')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@worktimeapp.param('google_user_id', 'Google Id eines Benutzers')
class UserWithGoogleOperations(Resource):
    @worktimeapp.marshal_with(user)
    # #@secured
    def get(self, googleId):
        """Auslesen von User-Objekten, die durch den User Namen bestimmt werden.

        Die auszulesenden Objekte werden durch ```user_name``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        user = adm.get_user_by_google_user_id(googleId)
        return user

# @worktimeapp.route('/projects')
# @worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
# class UserListOperations(Resource):
#     @worktimeapp.marshal_list_with(user)
#     # #@secured
#     def get(self):
#         """Auslesen aller User-Objekte.

#         Sollten keine User-Objekte verfügbar sein, so wird eine leere Sequenz zurückgegeben."""
#         adm = Businesslogic()
#         users = adm.get_all_users()
#         return users

#     @worktimeapp.marshal_with(user, code=200)
#     @worktimeapp.expect(user)  # Wir erwarten ein User-Objekt von Client-Seite.
#     # #@secured
#     def post(self):
#         """Anlegen eines neuen User-Objekts.

#         **ACHTUNG:** Wir fassen die vom Client gesendeten Daten als Vorschlag auf.
#         So ist zum Beispiel die Vergabe der ID nicht Aufgabe des Clients.
#         Selbst wenn der Client eine ID in dem Proposal vergeben sollte, so
#         liegt es an der Businesslogic (Businesslogik), eine korrekte ID
#         zu vergeben. *Das korrigierte Objekt wird schließlich zurückgegeben.*
#         """
#         adm = Businesslogic()

#         proposal = user.from_dict(api.payload)

#         """RATSCHLAG: Prüfen Sie stets die Referenzen auf valide Werte, bevor Sie diese verwenden!"""
#         if proposal is not None:
#             """ Wir verwenden lediglich Vor- und Nachnamen des Proposals für die Erzeugung
#             eines User-Objekts. Das serverseitig erzeugte Objekt ist das maßgebliche und
#             wird auch dem Client zurückgegeben.
#             """
#             c = adm.create_user(proposal.get_first_name(),
#                                 proposal.get_last_name())
#             return c, 200
#         else:
#             # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
#             return '', 500


# @worktimeapp.route('/users/<int:id>')
# @worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
# @worktimeapp.param('id', 'Die ID des User-Objekts')
# class UserOperations(Resource):
#     @worktimeapp.marshal_with(user)
#     # #@secured
#     def get(self, id):
#         """Auslesen eines bestimmten User-Objekts.

#         Das auszulesende Objekt wird durch die ```id``` in dem URI bestimmt.
#         """
#         adm = Businesslogic()
#         cust = adm.get_user_by_id(id)
#         return cust

#     # #@secured
#     def delete(self, id):
#         """Löschen eines bestimmten User-Objekts.

#         Das zu löschende Objekt wird durch die ```id``` in dem URI bestimmt.
#         """
#         adm = Businesslogic()
#         cust = adm.get_user_by_id(id)
#         adm.delete_user(cust)
#         return '', 200

#     @worktimeapp.marshal_with(user)
#     @worktimeapp.expect(user, validate=True)
#     # #@secured
#     def put(self, id):
#         """Update eines bestimmten User-Objekts.

#         **ACHTUNG:** Relevante id ist die id, die mittels URI bereitgestellt und somit als Methodenparameter
#         verwendet wird. Dieser Parameter überschreibt das ID-Attribut des im Payload der Anfrage übermittelten
#         User-Objekts.
#         """
#         adm = Businesslogic()
#         c = user.from_dict(api.payload)

#         if c is not None:
#             """Hierdurch wird die id des zu überschreibenden (vgl. Update) User-Objekts gesetzt.
#             Siehe Hinweise oben.
#             """
#             c.set_id(id)
#             adm.save_user(c)
#             return '', 200
#         else:
#             return '', 500


# @worktimeapp.route('/users-by-name/<string:lastname>')
# @worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
# @worktimeapp.param('lastname', 'Der Nachname des Kunden')
# class UsersByNameOperations(Resource):
#     @worktimeapp.marshal_with(user)
#     # #@secured
#     def get(self, lastname):
#         """ Auslesen von User-Objekten, die durch den Nachnamen bestimmt werden.

#         Die auszulesenden Objekte werden durch ```lastname``` in dem URI bestimmt.
#         """
#         adm = Businesslogic()
#         cust = adm.get_user_by_name(lastname)
#         return cust


# @worktimeapp.route('/users/<int:id>/accounts')
# @worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
# @worktimeapp.param('id', 'Die ID des User-Objekts')
# class UserRelatedAccountOperations(Resource):
#     @worktimeapp.marshal_with(user)
#     # #@secured
#     def get(self, id):
#         """Auslesen aller Acount-Objekte bzgl. eines bestimmten User-Objekts.

#         Das User-Objekt dessen Accounts wir lesen möchten, wird durch die ```id``` in dem URI bestimmt.
#         """
#         adm = Businesslogic()
#         # Zunächst benötigen wir den durch id gegebenen User.
#         cust = adm.get_user_by_id(id)

#         # Haben wir eine brauchbare Referenz auf ein User-Objekt bekommen?
#         if cust is not None:
#             # Jetzt erst lesen wir die Konten des User aus.
#             account_list = adm.get_accounts_of_user(cust)
#             return account_list
#         else:
#             return "User not found", 500

"""
Worktimeaccount
"""


@worktimeapp.route('/worktimeaccount')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class WorkTimeAccountOperations(Resource):
    @worktimeapp.marshal_list_with(worktimeaccount)
    # #@secured
    def get(self):
        """Auslesen aller WorkTimeAccount-Objekte.

        Sollten keine User-Objekte verfügbar sein, so wird eine leere Sequenz zurückgegeben."""
        adm = Businesslogic()
        worktimeaccounts = adm.get_all_worktimeaccounts()
        return worktimeaccounts

    @worktimeapp.marshal_with(worktimeaccount, code=200)
    # Wir erwarten ein Worktimeaccount-Objekt von Client-Seite.
    @worktimeapp.expect(worktimeaccount)
    # #@secured
    def post(self):
        """Anlegen eines neuen Worktimeaccount-Objekts.

        **ACHTUNG:** Wir fassen die vom Client gesendeten Daten als Vorschlag auf.
        So ist zum Beispiel die Vergabe der ID nicht Aufgabe des Clients.
        Selbst wenn der Client eine ID in dem Proposal vergeben sollte, so
        liegt es an der Businesslogic (Businesslogik), eine korrekte ID
        zu vergeben. *Das korrigierte Objekt wird schließlich zurückgegeben.*
        """
        adm = Businesslogic()

        proposal = WorkTimeAccountBO.from_dict(api.payload)

        """RATSCHLAG: Prüfen Sie stets die Referenzen auf valide Werte, bevor Sie diese verwenden!"""
        if proposal is not None:
            """ Wir verwenden lediglich Vor- und Nachnamen des Proposals für die Erzeugung
            eines Worktimeaccount-Objekts. Das serverseitig erzeugte Objekt ist das maßgebliche und 
            wird auch dem Client zurückgegeben. 
            """
            c = adm.create_worktimeaccount(
                proposal.get_user_id(),
                proposal.get_contract_time(),
                proposal.get_overtime()
            )
            return c, 200
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500


@worktimeapp.route('/worktimeaccount/<int:id>')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@worktimeapp.param('id', 'Id des Accounts')
class WorktimeaccountWithIdOperations(Resource):
    @worktimeapp.marshal_with(worktimeaccount)
    # #@secured
    def get(self, id):
        """Auslesen von User-Objekten, die durch den User Namen bestimmt werden.

        Die auszulesenden Objekte werden durch ```user_id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        worktimeaccount = adm.get_worktimeaccount_by_id(id)
        return worktimeaccount

    @worktimeapp.marshal_with(worktimeaccount)
    # @secured
    def delete(self, id):
        """Löschen eines bestimmten User-Objekts.

        Das zu löschende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        user = adm.get_worktimeaccount_by_id(id)
        adm.delete_worktimeaccount(user)
        return '', 200

    @worktimeapp.marshal_with(worktimeaccount)
    @worktimeapp.expect(worktimeaccount, validate=True)
    # #@secured
    def put(self, id):
        """Update eines bestimmten User-Objekts.

        **ACHTUNG:** Relevante id ist die id, die mittels URI bereitgestellt und somit als Methodenparameter
        verwendet wird. Dieser Parameter überschreibt das ID-Attribut des im Payload der Anfrage übermittelten
        User-Objekts.
        """
        adm = Businesslogic()
        user = UserBO.from_dict(api.payload)

        if user is not None:
            """Hierdurch wird die id des zu überschreibenden (vgl. Update) User-Objekts gesetzt.
            Siehe Hinweise oben.
            """
            user.set_id(id)
            adm.save_worktimeaccount(user)
            return '', 200
        else:
            return '', 500


@worktimeapp.route('/worktimeaccountuser/<int:user_id>')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@worktimeapp.param('user_id', 'User Id des Accounts')
class WorktimeaccountWithUserIdOperations(Resource):
    @worktimeapp.marshal_with(worktimeaccount)
    # #@secured
    def get(self, id):
        """Auslesen von User-Objekten, die durch den User Namen bestimmt werden.

        Die auszulesenden Objekte werden durch ```user_id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        worktimeaccount = adm.get_worktimeaccount_by_user_id(id)
        return worktimeaccount


"""
Project
"""


@worktimeapp.route('/projects')
class ProjectOperations(Resource):
    @worktimeapp.marshal_with(project)
    @worktimeapp.expect(project)
    # @secured
    def post(self):
        adm = Businesslogic()
        proposal = ProjectBO.from_dict(api.payload)
        if proposal is not None:
            p = adm.create_project(
                proposal.get_name(),
                proposal.get_commissioner(),
                proposal.get_user_id(),
            )
            return p

    @worktimeapp.marshal_list_with(project)
    # @secured
    def get(self):
        adm = Businesslogic()
        project = adm.get_all_projects()
        return project


@worktimeapp.route('/project/user/<int:id>')
@worktimeapp.param('id', 'Die ID des Users')
class ProjectWithUserIDOperations(Resource):
    @worktimeapp.marshal_with(project)
    # @secured
    def get(self, id):
        adm = Businesslogic()
        project = adm.get_projects_by_user_id(id)
        return project


@worktimeapp.route('/project/<int:id>')
@worktimeapp.param('id', 'Die ID des Projekts')
class ProjectWithIDOperations(Resource):
    @worktimeapp.marshal_with(project)
    # @secured
    def get(self, id):
        adm = Businesslogic()
        project = adm.get_project_by_id(id)
        return project

    @worktimeapp.marshal_with(project)
    # @secured
    def delete(self, id):
        adm = Businesslogic()
        project = adm.get_project_by_id(id)
        adm.delete_project(project)
        return ''

    @worktimeapp.marshal_with(project)
    @worktimeapp.expect(project, validate=True)
    # @secured
    def put(self, id):
        adm = Businesslogic()
        p = ProjectBO.from_dict(api.payload)

        if p is not None:
            p.set_id(id)
            adm.update_project(p)
            return p, 200
        else:
            return '', 50


@worktimeapp.route('/project/<name>')
@worktimeapp.param('name', 'Der Name des Projekts')
class ProjectWithSTRINGOperations(Resource):
    @worktimeapp.marshal_with(project)
    # @secured
    def get(self, name):
        adm = Businesslogic()
        project = adm.get_project_by_name(project)
        return project


# ProjectUser
@worktimeapp.route('/projectusers')
class ProjectUserOperations(Resource):
    @worktimeapp.marshal_with(projectuser)
    @worktimeapp.expect(projectuser)
    # @secured
    def post(self):
        adm = Businesslogic()
        proposal = ProjectUserBO.from_dict(api.payload)
        if proposal is not None:
            p = adm.create_projectuser(
                proposal.get_project_id(),
                proposal.get_user_id(),
                proposal.get_capacity()
            )
            return p

    @worktimeapp.marshal_list_with(projectuser)
    # @secured
    def get(self):
        adm = Businesslogic()
        projectuser = adm.get_all_projectusers()
        return projectuser


@worktimeapp.route('/projectuser/<int:id>')
@worktimeapp.param('id', 'Die ID des Projekts')
class ProjectWithIDOperations(Resource):
    @worktimeapp.marshal_with(projectuser)
    # @secured
    def get(self, id):
        adm = Businesslogic()
        projectuser = adm.get_projectuser_by_id(id)
        return projectuser

    def get_project_members(self, project_id):
        adm = Businesslogic()
        projectuser = adm.get_all_project_members(project_id)
        return projectuser

    @worktimeapp.marshal_with(projectuser)
    # @secured
    def delete(self, id):
        adm = Businesslogic()
        projectuser = adm.get_projectuser_by_id(id)
        adm.delete_projectuser(projectuser)
        return ''

    @worktimeapp.marshal_with(projectuser)
    @worktimeapp.expect(projectuser, validate=True)
    # @secured
    def put(self, id):
        adm = Businesslogic()
        p = ProjectUserBO.from_dict(api.payload)

        if p is not None:
            p.set_id(id)
            adm.update_projectuser(p)
            return p, 200
        else:
            return '', 500

# Activity


@worktimeapp.route('/activities')
class ActivityOperations(Resource):
    @worktimeapp.marshal_with(activity)
    @worktimeapp.expect(activity)
    # @secured
    def post(self):
        adm = Businesslogic()
        proposal = ActivityBO.from_dict(api.payload)
        if proposal is not None:
            p = adm.create_activity(
                proposal.get_name(),
                proposal.get_capacity(),
                proposal.get_project_id(),
                proposal.get_current_capacity(),
            )
            return p

    @worktimeapp.marshal_list_with(activity)
    # @secured
    def get(self):
        adm = Businesslogic()
        activity = adm.get_all_activities()
        return activity


@worktimeapp.route('/activity/<int:id>')
@worktimeapp.param('id', 'Die ID der Aktivitaet')
class ActivityWithIDOperations(Resource):
    @worktimeapp.marshal_with(activity)
    # @secured
    def get(self, id):
        adm = Businesslogic()
        activity = adm.get_activity_by_id(id)
        return activity

    def get_project_id(self, id):
        adm = Businesslogic()
        activity = adm.get_all_by_project_id(id)
        return activity

    @worktimeapp.marshal_with(activity)
    # @secured
    def delete(self, id):
        adm = Businesslogic()
        activity = adm.get_activity_by_id(id)
        adm.delete_activity(activity)
        return ''

    @worktimeapp.marshal_with(activity)
    @worktimeapp.expect(activity, validate=True)
    # @secured
    def put(self, id):
        adm = Businesslogic()
        p = ActivityBO.from_dict(api.payload)

        if p is not None:
            p.set_id(id)
            adm.update_activity(p)
            return p, 200
        else:
            return '', 500


'''@worktimeapp.route('/activity/<str:name>')
@worktimeapp.param('name', 'Der Name der Aktivitaet')
class ActivityWithSTRINGOperations(Resource):
    @worktimeapp.marshal_with(activity)
    # @secured
    def get(self, name):
        adm = Businesslogic()
        activity = adm.get_by_name(name)
        return activity
'''


@worktimeapp.route('/events')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class EventListOperations(Resource):
    @worktimeapp.marshal_list_with(event)
    # #@secured
    def get(self):
        """Auslesen aller Event-Objekte.
        Sollten keine Event-Objekte verfügbar sein, so wird eine leere Sequenz zurückgegeben."""
        adm = Businesslogic()
        events = adm.get_all_events()
        return events

    @worktimeapp.marshal_with(event, code=200)
    # Wir erwarten ein Event-Objekt von Client-Seite.
    @worktimeapp.expect(event)
    # @secured
    def post(self):
        """Anlegen eines neuen Event-Objekts."""

        adm = Businesslogic()
        proposal = EventBO.from_dict(api.payload)

        if proposal is not None:
            c = adm.create_event(
                proposal.get_id(), proposal.get_time(), proposal.get_event_booking_id())
            return c, 200
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500


@worktimeapp.route('/event/<int:id>')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@worktimeapp.param('id', 'Die ID des Event-Objekts')
class EventOperations(Resource):
    @worktimeapp.marshal_with(event)
    # #@secured
    def get(self, id):
        """Auslesen eines bestimmten Event-Objekts.
        Das auszulesende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        cust = adm.get_event_by_id(id)
        return cust

    # @secured
    def delete(self, id):
        """Löschen eines bestimmten Event-Objekts.
        Das zu löschende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        event = adm.get_event_by_id(id)
        adm.delete_event(event)
        return '', 200

    @worktimeapp.marshal_with(event)
    @worktimeapp.expect(event, validate=True)
    # @secured
    def put(self, id):
        """Update eines bestimmten Event-Objekts.
        **ACHTUNG:** Relevante id ist die id, die mittels URI bereitgestellt und somit als Methodenparameter
        verwendet wird. Dieser Parameter überschreibt das ID-Attribut des im Payload der Anfrage übermittelten
        Event-Objekts.
        """
        adm = Businesslogic()
        ev = event.from_dict(api.payload)

        if ev is not None:
            """Hierdurch wird die id des zu überschreibenden (vgl. Update) Event-Objekts gesetzt.
            Siehe Hinweise oben.
            """
            ev.set_id(id)
            adm.save_event(ev)
            return '', 200
        else:
            return '', 500


"""
Going
"""


@worktimeapp.route('/goings')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class GoingListOperations(Resource):
    @worktimeapp.marshal_list_with(going)
    # #@secured
    def get(self):
        """Auslesen aller Event-Objekte.
        Sollten keine Event-Objekte verfügbar sein, so wird eine leere Sequenz zurückgegeben."""
        adm = Businesslogic()
        going = adm.get_all_goings()
        return going

    @worktimeapp.marshal_with(going, code=200)
    # Wir erwarten ein Event-Objekt von Client-Seite.
    @worktimeapp.expect(going)
    # @secured
    def post(self):
        """Anlegen eines neuen Event-Objekts."""

        adm = Businesslogic()
        proposal = GoingBO.from_dict(api.payload)

        if proposal is not None:
            c = adm.create_going(
                proposal.get_time())

            e = adm.create_event(
                "going",
                None,
                c.get_id(),
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None
            )

            eb = adm.create_event_booking(
                e.get_id()
            )
            return c, e, eb
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500


@worktimeapp.route('/going/<int:id>')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@worktimeapp.param('id', 'Die ID des Event-Objekts')
class GoingOperations(Resource):
    @worktimeapp.marshal_with(going)
    # #@secured
    def get(self, id):
        """Auslesen eines bestimmten Event-Objekts.
        Das auszulesende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        cust = adm.get_going_by_id(id)
        return cust

    # @secured
    def delete(self, id):
        """Löschen eines bestimmten Event-Objekts.
        Das zu löschende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        going = adm.get_going_by_id(id)
        adm.delete_going(going)
        return '', 200

    @worktimeapp.marshal_with(going)
    @worktimeapp.expect(going, validate=True)
    # @secured
    def put(self, id):
        """Update eines bestimmten Event-Objekts.
        **ACHTUNG:** Relevante id ist die id, die mittels URI bereitgestellt und somit als Methodenparameter
        verwendet wird. Dieser Parameter überschreibt das ID-Attribut des im Payload der Anfrage übermittelten
        Event-Objekts.
        """
        adm = Businesslogic()
        go = GoingBO.from_dict(api.payload)

        if go is not None:
            """Hierdurch wird die id des zu überschreibenden (vgl. Update) Event-Objekts gesetzt.
            Siehe Hinweise oben.
            """
            go.set_id(id)
            adm.save_event(go)
            return '', 200
        else:
            return '', 500


"""
Coming
"""


@worktimeapp.route('/comings')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class ComingListOperations(Resource):
    @worktimeapp.marshal_list_with(coming)
    # #@secured
    def get(self):
        """Auslesen aller Event-Objekte.
        Sollten keine Event-Objekte verfügbar sein, so wird eine leere Sequenz zurückgegeben."""
        adm = Businesslogic()
        coming = adm.get_all_comings()
        return coming

    @worktimeapp.marshal_with(coming, code=200)
    # Wir erwarten ein Event-Objekt von Client-Seite.
    @worktimeapp.expect(coming)
    # @secured
    def post(self):
        """Anlegen eines neuen Event-Objekts."""

        adm = Businesslogic()
        proposal = ComingBO.from_dict(api.payload)

        if proposal is not None:
            c = adm.create_coming(
                proposal.get_time())

            e = adm.create_event(
                "coming",
                c.get_id(),
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None
            )

            eb = adm.create_event_booking(
                e.get_id()
            )
            return c, e, eb
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500


@worktimeapp.route('/coming/<int:id>')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@worktimeapp.param('id', 'Die ID des Event-Objekts')
class ComingOperations(Resource):
    @worktimeapp.marshal_with(coming)
    # #@secured
    def get(self, id):
        """Auslesen eines bestimmten Event-Objekts.
        Das auszulesende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        cust = adm.get_coming_by_id(id)
        return cust

    # @secured
    def delete(self, id):
        """Löschen eines bestimmten Event-Objekts.
        Das zu löschende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        coming = adm.get_coming_by_id(id)
        adm.delete_coming(coming)
        return '', 200

    @worktimeapp.marshal_with(coming)
    @worktimeapp.expect(coming, validate=True)
    # @secured
    def put(self, id):
        """Update eines bestimmten Event-Objekts.
        **ACHTUNG:** Relevante id ist die id, die mittels URI bereitgestellt und somit als Methodenparameter
        verwendet wird. Dieser Parameter überschreibt das ID-Attribut des im Payload der Anfrage übermittelten
        Event-Objekts.
        """
        adm = Businesslogic()
        go = ComingBO.from_dict(api.payload)

        if go is not None:
            """Hierdurch wird die id des zu überschreibenden (vgl. Update) Event-Objekts gesetzt.
            Siehe Hinweise oben.
            """
            go.set_id(id)
            adm.save_event(go)
            return '', 200
        else:
            return '', 500


"""
VacationBegin
"""


@worktimeapp.route('/vacation_begins')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class VacationBeginListOperations(Resource):
    @worktimeapp.marshal_list_with(vacation_begin)
    # #@secured
    def get(self):
        """Auslesen aller Event-Objekte.
        Sollten keine Event-Objekte verfügbar sein, so wird eine leere Sequenz zurückgegeben."""
        adm = Businesslogic()
        vacation_begin = adm.get_all_vacation_begins()
        return vacation_begin

    @worktimeapp.marshal_with(vacation_begin, code=200)
    # Wir erwarten ein Event-Objekt von Client-Seite.
    @worktimeapp.expect(vacation_begin)
    # @secured
    def post(self):
        """Anlegen eines neuen Event-Objekts."""

        adm = Businesslogic()
        proposal = VacationBeginBO.from_dict(api.payload)

        if proposal is not None:
            c = adm.create_vacation_begin(
                proposal.get_time())

            e = adm.create_event(
                "vacationBegin",
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                c.get_id(),
                None,
                None,
                None
            )

            eb = adm.create_event_booking(
                e.get_id()
            )
            return c
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500


@worktimeapp.route('/vacation_begin/<int:id>')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@worktimeapp.param('id', 'Die ID des Event-Objekts')
class VacationBeginOperations(Resource):
    @worktimeapp.marshal_with(vacation_begin)
    # #@secured
    def get(self, id):
        """Auslesen eines bestimmten Event-Objekts.
        Das auszulesende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        cust = adm.get_vacation_begin_by_id(id)
        return cust

    # @secured
    def delete(self, id):
        """Löschen eines bestimmten Event-Objekts.
        Das zu löschende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        vacation_begin = adm.get_vacation_begin_by_id(id)
        adm.delete_vacation_begin(vacation_begin)
        return '', 200

    @worktimeapp.marshal_with(vacation_begin)
    @worktimeapp.expect(vacation_begin, validate=True)
    # @secured
    def put(self, id):
        """Update eines bestimmten Event-Objekts.
        **ACHTUNG:** Relevante id ist die id, die mittels URI bereitgestellt und somit als Methodenparameter
        verwendet wird. Dieser Parameter überschreibt das ID-Attribut des im Payload der Anfrage übermittelten
        Event-Objekts.
        """
        adm = Businesslogic()
        go = VacationBeginBO.from_dict(api.payload)

        if go is not None:
            """Hierdurch wird die id des zu überschreibenden (vgl. Update) Event-Objekts gesetzt.
            Siehe Hinweise oben.
            """
            go.set_id(id)
            adm.save_vacation_begin(go)
            return go, 200
        else:
            return '', 500


"""
VacationEnd
"""


@worktimeapp.route('/vacation_ends')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class VacationEndListOperations(Resource):
    @worktimeapp.marshal_list_with(vacation_end)
    # #@secured
    def get(self):
        """Auslesen aller Event-Objekte.
        Sollten keine Event-Objekte verfügbar sein, so wird eine leere Sequenz zurückgegeben."""
        adm = Businesslogic()
        vacation_end = adm.get_all_vacation_ends()
        return vacation_end

    @worktimeapp.marshal_with(vacation_end, code=200)
    # Wir erwarten ein Event-Objekt von Client-Seite.
    @worktimeapp.expect(vacation_end)
    # @secured
    def post(self):
        """Anlegen eines neuen Event-Objekts."""

        adm = Businesslogic()
        proposal = VacationEndBO.from_dict(api.payload)

        if proposal is not None:
            c = adm.create_vacation_end(
                proposal.get_time())

            e = adm.create_event(
                "vacationEnd",
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                c.get_id(),
                None,
                None
            )

            eb = adm.create_event_booking(
                e.get_id()
            )
            return c
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500


@worktimeapp.route('/vacation_end/<int:id>')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@worktimeapp.param('id', 'Die ID des Event-Objekts')
class VacationEndOperations(Resource):
    @worktimeapp.marshal_with(vacation_end)
    # #@secured
    def get(self, id):
        """Auslesen eines bestimmten Event-Objekts.
        Das auszulesende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        cust = adm.get_vacation_end_by_id(id)
        return cust

    # @secured
    def delete(self, id):
        """Löschen eines bestimmten Event-Objekts.
        Das zu löschende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        vacation_end = adm.get_vacation_end_by_id(id)
        adm.delete_vacation_end(vacation_end)
        return '', 200

    @worktimeapp.marshal_with(vacation_end)
    @worktimeapp.expect(vacation_end, validate=True)
    # @secured
    def put(self, id):
        """Update eines bestimmten Event-Objekts.
        **ACHTUNG:** Relevante id ist die id, die mittels URI bereitgestellt und somit als Methodenparameter
        verwendet wird. Dieser Parameter überschreibt das ID-Attribut des im Payload der Anfrage übermittelten
        Event-Objekts.
        """
        adm = Businesslogic()
        go = VacationEndBO.from_dict(api.payload)

        if go is not None:
            """Hierdurch wird die id des zu überschreibenden (vgl. Update) Event-Objekts gesetzt.
            Siehe Hinweise oben.
            """
            go.set_id(id)
            adm.save_vacation_end(go)
            return go, 200
        else:
            return '', 500


"""
FlexDayStart
"""


@worktimeapp.route('/flex_day_starts')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class FlexDayStartListOperations(Resource):
    @worktimeapp.marshal_list_with(flex_day_start)
    # #@secured
    def get(self):
        """Auslesen aller Event-Objekte.

        Sollten keine Event-Objekte verfügbar sein, so wird eine leere Sequenz zurückgegeben."""
        adm = Businesslogic()
        flex_day_start = adm.get_all_flex_day_starts()
        return flex_day_start

    @worktimeapp.marshal_with(flex_day_start, code=200)
    # Wir erwarten ein Event-Objekt von Client-Seite.
    @worktimeapp.expect(flex_day_start)
    # @secured
    def post(self):
        """Anlegen eines neuen Event-Objekts."""

        adm = Businesslogic()
        proposal = FlexDayStartBO.from_dict(api.payload)

        if proposal is not None:
            c = adm.create_flex_day_start(
                proposal.get_time())

            e = adm.create_event(
                "FlexDayBegin",
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                c.get_id(),
                None
            )

            eb = adm.create_event_booking(
                e.get_id()
            )
            return c
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500


@worktimeapp.route('/flex_day_start/<int:id>')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@worktimeapp.param('id', 'Die ID des Event-Objekts')
class FlexDayStartOperations(Resource):
    @worktimeapp.marshal_with(flex_day_start)
    # #@secured
    def get(self, id):
        """Auslesen eines bestimmten Event-Objekts.

        Das auszulesende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        cust = adm.get_flex_day_start_by_id(id)
        return cust

    # @secured
    def delete(self, id):
        """Löschen eines bestimmten Event-Objekts.

        Das zu löschende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        flex_day_start = adm.get_flex_day_start_by_id(id)
        adm.delete_flex_day_start(flex_day_start)
        return '', 200

    @worktimeapp.marshal_with(flex_day_start)
    @worktimeapp.expect(flex_day_start, validate=True)
    # @secured
    def put(self, id):
        """Update eines bestimmten Event-Objekts.

        **ACHTUNG:** Relevante id ist die id, die mittels URI bereitgestellt und somit als Methodenparameter
        verwendet wird. Dieser Parameter überschreibt das ID-Attribut des im Payload der Anfrage übermittelten
        Event-Objekts.
        """
        adm = Businesslogic()
        go = FlexDayStartBO.from_dict(api.payload)

        if go is not None:
            """Hierdurch wird die id des zu überschreibenden (vgl. Update) Event-Objekts gesetzt.
            Siehe Hinweise oben.
            """
            go.set_id(id)
            adm.save_event(go)
            return '', 200
        else:
            return '', 500


"""
FlexDayEnd
"""


@worktimeapp.route('/flex_day_ends')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class FlexDayEndListOperations(Resource):
    @worktimeapp.marshal_list_with(flex_day_end)
    # #@secured
    def get(self):
        """Auslesen aller Event-Objekte.

        Sollten keine Event-Objekte verfügbar sein, so wird eine leere Sequenz zurückgegeben."""
        adm = Businesslogic()
        flex_day_end = adm.get_all_flex_day_end()
        return flex_day_end

    @worktimeapp.marshal_with(flex_day_end, code=200)
    # Wir erwarten ein Event-Objekt von Client-Seite.
    @worktimeapp.expect(flex_day_end)
    # @secured
    def post(self):
        """Anlegen eines neuen Event-Objekts."""

        adm = Businesslogic()
        proposal = FlexDayEndBO.from_dict(api.payload)

        if proposal is not None:
            c = adm.create_flex_day_end(
                proposal.get_time())

            e = adm.create_event(
                "FlexDayEnd",
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                c.get_id()
            )

            eb = adm.create_event_booking(
                e.get_id()
            )
            return c
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500


@worktimeapp.route('/flex_day_end/<int:id>')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@worktimeapp.param('id', 'Die ID des Event-Objekts')
class FlexDayEndOperations(Resource):
    @worktimeapp.marshal_with(flex_day_end)
    # #@secured
    def get(self, id):
        """Auslesen eines bestimmten Event-Objekts.

        Das auszulesende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        cust = adm.get_flex_day_end_by_id(id)
        return cust

    # @secured
    def delete(self, id):
        """Löschen eines bestimmten Event-Objekts.

        Das zu löschende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        flex_day_end = adm.get_flex_day_end_by_id(id)
        adm.delete_flex_day_end(flex_day_end)
        return '', 200

    @worktimeapp.marshal_with(flex_day_end)
    @worktimeapp.expect(flex_day_end, validate=True)
    # @secured
    def put(self, id):
        """Update eines bestimmten Event-Objekts.

        **ACHTUNG:** Relevante id ist die id, die mittels URI bereitgestellt und somit als Methodenparameter
        verwendet wird. Dieser Parameter überschreibt das ID-Attribut des im Payload der Anfrage übermittelten
        Event-Objekts.
        """
        adm = Businesslogic()
        go = FlexDayEndBO.from_dict(api.payload)

        if go is not None:
            """Hierdurch wird die id des zu überschreibenden (vgl. Update) Event-Objekts gesetzt.
            Siehe Hinweise oben.
            """
            go.set_id(id)
            adm.save_event(go)
            return '', 200
        else:
            return '', 500


"""
IllnessEnd
"""


@worktimeapp.route('/illness_ends')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class IllnessEndListOperations(Resource):
    @worktimeapp.marshal_list_with(illness_end)
    # #@secured
    def get(self):
        """Auslesen aller Event-Objekte.
        Sollten keine Event-Objekte verfügbar sein, so wird eine leere Sequenz zurückgegeben."""
        adm = Businesslogic()
        illness_end = adm.get_all_illness_end()
        return illness_end

    @worktimeapp.marshal_with(illness_end, code=200)
    # Wir erwarten ein Event-Objekt von Client-Seite.
    @worktimeapp.expect(illness_end)
    # @secured
    def post(self):
        """Anlegen eines neuen Event-Objekts."""

        adm = Businesslogic()
        proposal = IllnessEndBO.from_dict(api.payload)

        if proposal is not None:
            c = adm.create_illness_end(
                proposal.get_time())

            e = adm.create_event(
                "illnessEnd",
                None,
                None,
                None,
                None,
                None,
                c.get_id(),
                None,
                None,
                None,
                None,
                None,
                None
            )

            eb = adm.create_event_booking(
                e.get_id()
            )
            return c
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500


@worktimeapp.route('/illness_end/<int:id>')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@worktimeapp.param('id', 'Die ID des Event-Objekts')
class IllnessEndOperations(Resource):
    @worktimeapp.marshal_with(illness_end)
    # #@secured
    def get(self, id):
        """Auslesen eines bestimmten Event-Objekts.
        Das auszulesende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        cust = adm.get_illness_end_by_id(id)
        return cust

    # @secured
    def delete(self, id):
        """Löschen eines bestimmten Event-Objekts.
        Das zu löschende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        illness_end = adm.get_illness_end_by_id(id)
        adm.delete_illness_end(illness_end)
        return '', 200

    @worktimeapp.marshal_with(illness_end)
    @worktimeapp.expect(illness_end, validate=True)
    # @secured
    def put(self, id):
        """Update eines bestimmten Event-Objekts.
        **ACHTUNG:** Relevante id ist die id, die mittels URI bereitgestellt und somit als Methodenparameter
        verwendet wird. Dieser Parameter überschreibt das ID-Attribut des im Payload der Anfrage übermittelten
        Event-Objekts.
        """
        adm = Businesslogic()
        go = IllnessEndBO.from_dict(api.payload)

        if go is not None:
            """Hierdurch wird die id des zu überschreibenden (vgl. Update) Event-Objekts gesetzt.
            Siehe Hinweise oben.
            """
            go.set_id(id)
            adm.save_illness_end(go)
            return go, 200
        else:
            return '', 500


"""
IllnessBegin
"""


@worktimeapp.route('/illness_begins')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class IllnessBeginListOperations(Resource):
    @worktimeapp.marshal_list_with(illness_begin)
    # #@secured
    def get(self):
        """Auslesen aller Event-Objekte.
        Sollten keine Event-Objekte verfügbar sein, so wird eine leere Sequenz zurückgegeben."""
        adm = Businesslogic()
        illness_begin = adm.get_all_illness_begins()
        return illness_begin

    @worktimeapp.marshal_with(illness_begin, code=200)
    # Wir erwarten ein Event-Objekt von Client-Seite.
    @worktimeapp.expect(illness_begin)
    # @secured
    def post(self):
        """Anlegen eines neuen Event-Objekts."""

        adm = Businesslogic()
        proposal = IllnessBeginBO.from_dict(api.payload)

        if proposal is not None:
            c = adm.create_illness_begin(
                proposal.get_time())

            e = adm.create_event(
                "illnessBegin",
                None,
                None,
                None,
                None,
                c.get_id(),
                None,
                None,
                None,
                None,
                None,
                None,
                None
            )

            eb = adm.create_event_booking(
                e.get_id()
            )
            return c
        else:
            # Wenn irgbeginetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500


@worktimeapp.route('/illness_begin/<int:id>')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@worktimeapp.param('id', 'Die ID des Event-Objekts')
class IllnessBeginOperations(Resource):
    @worktimeapp.marshal_with(illness_begin)
    # #@secured
    def get(self, id):
        """Auslesen eines bestimmten Event-Objekts.
        Das auszulesbegine Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        cust = adm.get_illness_begin_by_id(id)
        return cust

    # @secured
    def delete(self, id):
        """Löschen eines bestimmten Event-Objekts.
        Das zu löschbegine Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        illness_begin = adm.get_illness_begin_by_id(id)
        adm.delete_illness_begin(illness_begin)
        return '', 200

    @worktimeapp.marshal_with(illness_begin)
    @worktimeapp.expect(illness_begin, validate=True)
    # @secured
    def put(self, id):
        """Update eines bestimmten Event-Objekts.
        **ACHTUNG:** Relevante id ist die id, die mittels URI bereitgestellt und somit als Methodenparameter
        verwbeginet wird. Dieser Parameter überschreibt das ID-Attribut des im Payload der Anfrage übermittelten
        Event-Objekts.
        """
        adm = Businesslogic()
        go = IllnessBeginBO.from_dict(api.payload)

        if go is not None:
            """Hierdurch wird die id des zu überschreibbeginen (vgl. Update) Event-Objekts gesetzt.
            Siehe Hinweise oben.
            """
            go.set_id(id)
            adm.save_illness_begin(go)
            return go, 200
        else:
            return '', 500


"""
BreakBegin
"""


@worktimeapp.route('/break_begins')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class BreakBeginListOperations(Resource):
    @worktimeapp.marshal_list_with(break_begin)
    # #@secured
    def get(self):
        """Auslesen aller Event-Objekte.
        Sollten keine Event-Objekte verfügbar sein, so wird eine leere Sequenz zurückgegeben."""
        adm = Businesslogic()
        break_begin = adm.get_all_break_begins()
        return break_begin

    @worktimeapp.marshal_with(break_begin, code=200)
    # Wir erwarten ein Event-Objekt von Client-Seite.
    @worktimeapp.expect(break_begin)
    # @secured
    def post(self):
        """Anlegen eines neuen Event-Objekts."""

        adm = Businesslogic()
        proposal = BreakBeginBO.from_dict(api.payload)

        if proposal is not None:
            c = adm.create_break_begin(
                proposal.get_time())

            e = adm.create_event(
                "breakBegin",
                None,
                None,
                c.get_id(),
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
            )

            eb = adm.create_event_booking(
                e.get_id()
            )
            return c
        else:
            # Wenn irgbeginetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500


@worktimeapp.route('/break_begin/<int:id>')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@worktimeapp.param('id', 'Die ID des Event-Objekts')
class BreakBeginOperations(Resource):
    @worktimeapp.marshal_with(break_begin)
    # #@secured
    def get(self, id):
        """Auslesen eines bestimmten Event-Objekts.
        Das auszulesbegine Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        cust = adm.get_break_begin_by_id(id)
        return cust

    # @secured
    def delete(self, id):
        """Löschen eines bestimmten Event-Objekts.
        Das zu löschbegine Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        break_begin = adm.get_break_begin_by_id(id)
        adm.delete_break_begin(break_begin)
        return '', 200

    @worktimeapp.marshal_with(break_begin)
    @worktimeapp.expect(break_begin, validate=True)
    # @secured
    def put(self, id):
        """Update eines bestimmten Event-Objekts.
        **ACHTUNG:** Relevante id ist die id, die mittels URI bereitgestellt und somit als Methodenparameter
        verwbeginet wird. Dieser Parameter überschreibt das ID-Attribut des im Payload der Anfrage übermittelten
        Event-Objekts.
        """
        adm = Businesslogic()
        go = BreakBeginBO.from_dict(api.payload)

        if go is not None:
            """Hierdurch wird die id des zu überschreibbeginen (vgl. Update) Event-Objekts gesetzt.
            Siehe Hinweise oben.
            """
            go.set_id(id)
            adm.save_event(go)
            return '', 200
        else:
            return '', 500


"""
BreakEnd
"""


@worktimeapp.route('/break_ends')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class BreakEndListOperations(Resource):
    @worktimeapp.marshal_list_with(break_end)
    # #@secured
    def get(self):
        """Auslesen aller Event-Objekte.
        Sollten keine Event-Objekte verfügbar sein, so wird eine leere Sequenz zurückgegeben."""
        adm = Businesslogic()
        break_end = adm.get_all_break_ends()
        return break_end

    @worktimeapp.marshal_with(break_end, code=200)
    # Wir erwarten ein Event-Objekt von Client-Seite.
    @worktimeapp.expect(break_end)
    # @secured
    def post(self):
        """Anlegen eines neuen Event-Objekts."""

        adm = Businesslogic()
        proposal = BreakEndBO.from_dict(api.payload)

        if proposal is not None:
            c = adm.create_break_end(
                proposal.get_time())

            e = adm.create_event(
                "breakEnd",
                None,
                None,
                None,
                c.get_id(),
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None
            )

            eb = adm.create_event_booking(
                e.get_id()
            )
            return c
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500


@worktimeapp.route('/break_end/<int:id>')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@worktimeapp.param('id', 'Die ID des Event-Objekts')
class BreakEndOperations(Resource):
    @worktimeapp.marshal_with(break_end)
    # #@secured
    def get(self, id):
        """Auslesen eines bestimmten Event-Objekts.
        Das auszulesende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        cust = adm.get_break_end_by_id(id)
        return cust

    # @secured
    def delete(self, id):
        """Löschen eines bestimmten Event-Objekts.
        Das zu löschende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        break_end = adm.get_break_end_by_id(id)
        adm.delete_break_end(break_end)
        return '', 200

    @worktimeapp.marshal_with(break_end)
    @worktimeapp.expect(break_end, validate=True)
    # @secured
    def put(self, id):
        """Update eines bestimmten Event-Objekts.
        **ACHTUNG:** Relevante id ist die id, die mittels URI bereitgestellt und somit als Methodenparameter
        verwendet wird. Dieser Parameter überschreibt das ID-Attribut des im Payload der Anfrage übermittelten
        Event-Objekts.
        """
        adm = Businesslogic()
        go = BreakEndBO.from_dict(api.payload)

        if go is not None:
            """Hierdurch wird die id des zu überschreibenden (vgl. Update) Event-Objekts gesetzt.
            Siehe Hinweise oben.
            """
            go.set_id(id)
            adm.save_event(go)
            return '', 200
        else:
            return '', 500


"""
ProjectWorkEnd
"""


@worktimeapp.route('/project_work_ends')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class ProjectWorkEndListOperations(Resource):
    @worktimeapp.marshal_list_with(project_work_end)
    # #@secured
    def get(self):
        """Auslesen aller Event-Objekte.
        Sollten keine Event-Objekte verfügbar sein, so wird eine leere Sequenz zurückgegeben."""
        adm = Businesslogic()
        project_work_end = adm.get_all_project_work_ends()
        return project_work_end

    @worktimeapp.marshal_with(project_work_end, code=200)
    # Wir erwarten ein Event-Objekt von Client-Seite.
    @worktimeapp.expect(project_work_end)
    # @secured
    def post(self):
        """Anlegen eines neuen Event-Objekts."""

        adm = Businesslogic()
        proposal = ProjectWorkEndBO.from_dict(api.payload)

        if proposal is not None:
            c = adm.create_project_work_end(
                proposal.get_time())

            e = adm.create_event(
                "projectWorkEnd",
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                c.get_id(),
                None,
                None,
                None,
                None
            )

            eb = adm.create_event_booking(
                e.get_id()
            )
            return c
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500


@worktimeapp.route('/project_work_end/<int:id>')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@worktimeapp.param('id', 'Die ID des Event-Objekts')
class ProjectWorkEndOperations(Resource):
    @worktimeapp.marshal_with(project_work_end)
    # #@secured
    def get(self, id):
        """Auslesen eines bestimmten Event-Objekts.
        Das auszulesende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        cust = adm.get_project_work_end_by_id(id)
        return cust

    # @secured
    def delete(self, id):
        """Löschen eines bestimmten Event-Objekts.
        Das zu löschende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        project_work_end = adm.get_project_work_end_by_id(id)
        adm.delete_project_work_end(project_work_end)
        return '', 200

    @worktimeapp.marshal_with(project_work_end)
    @worktimeapp.expect(project_work_end, validate=True)
    # @secured
    def put(self, id):
        """Update eines bestimmten Event-Objekts.
        **ACHTUNG:** Relevante id ist die id, die mittels URI bereitgestellt und somit als Methodenparameter
        verwendet wird. Dieser Parameter überschreibt das ID-Attribut des im Payload der Anfrage übermittelten
        Event-Objekts.
        """
        adm = Businesslogic()
        go = ProjectWorkEndBO.from_dict(api.payload)

        if go is not None:
            """Hierdurch wird die id des zu überschreibenden (vgl. Update) Event-Objekts gesetzt.
            Siehe Hinweise oben.
            """
            go.set_id(id)
            adm.save_event(go)
            return '', 200
        else:
            return '', 500


"""
ProjectWorkBegin
"""


@worktimeapp.route('/project_work_begins')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class ProjectWorkBeginListOperations(Resource):
    @worktimeapp.marshal_list_with(project_work_begin)
    # #@secured
    def get(self):
        """Auslesen aller Event-Objekte.
        Sollten keine Event-Objekte verfügbar sein, so wird eine leere Sequenz zurückgegeben."""
        adm = Businesslogic()
        project_work_begin = adm.get_all_project_work_begins()
        return project_work_begin

    @worktimeapp.marshal_with(project_work_begin, code=200)
    # Wir erwarten ein Event-Objekt von Client-Seite.
    @worktimeapp.expect(project_work_begin)
    # @secured
    def post(self):
        """Anlegen eines neuen Event-Objekts."""

        adm = Businesslogic()
        proposal = ProjectWorkBeginBO.from_dict(api.payload)

        if proposal is not None:
            c = adm.create_project_work_begin(
                proposal.get_time())

            e = adm.create_event(
                "projectWorkBegin",
                None,
                None,
                None,
                None,
                None,
                None,
                c.get_id(),
                None,
                None,
                None,
                None,
                None
            )

            eb = adm.create_event_booking(
                e.get_id()
            )
            return c
        else:
            # Wenn irgbeginetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500


@worktimeapp.route('/project_work_begin/<int:id>')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@worktimeapp.param('id', 'Die ID des Event-Objekts')
class ProjectWorkBeginOperations(Resource):
    @worktimeapp.marshal_with(project_work_begin)
    # #@secured
    def get(self, id):
        """Auslesen eines bestimmten Event-Objekts.
        Das auszulesbegine Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        cust = adm.get_project_work_begin_by_id(id)
        return cust

    # @secured
    def delete(self, id):
        """Löschen eines bestimmten Event-Objekts.
        Das zu löschbegine Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        project_work_begin = adm.get_project_work_begin_by_id(id)
        adm.delete_project_work_begin(project_work_begin)
        return '', 200

    @worktimeapp.marshal_with(project_work_begin)
    @worktimeapp.expect(project_work_begin, validate=True)
    # @secured
    def put(self, id):
        """Update eines bestimmten Event-Objekts.
        **ACHTUNG:** Relevante id ist die id, die mittels URI bereitgestellt und somit als Methodenparameter
        verwbeginet wird. Dieser Parameter überschreibt das ID-Attribut des im Payload der Anfrage übermittelten
        Event-Objekts.
        """
        adm = Businesslogic()
        go = ProjectWorkBeginBO.from_dict(api.payload)

        if go is not None:
            """Hierdurch wird die id des zu überschreibbeginen (vgl. Update) Event-Objekts gesetzt.
            Siehe Hinweise oben.
            """
            go.set_id(id)
            adm.save_event(go)
            return '', 200
        else:
            return '', 500


"""
Timeinterval
"""


@worktimeapp.route('/timeinterval')
class TimeIntervalOperations(Resource):
    @worktimeapp.marshal_with(timeinterval)
    @worktimeapp.expect(timeinterval)
    # @secured
    def post(self):
        adm = Businesslogic()
        proposal = TimeIntervalBO.from_dict(api.payload)
        if proposal is not None:
            p = adm.create_timeinterval(
                proposal.get_type(),
                proposal.get_break_id(),
                proposal.get_illness_id(),
                proposal.get_project_duration_id(),
                proposal.get_project_work_id(),
                proposal.get_vacation_id(),
                proposal.get_work_id()
            )
        return p

    @worktimeapp.marshal_list_with(timeinterval)
    # @secured
    def get(self):
        adm = Businesslogic()
        timeinterval = adm.get_all_timeintervals()
        return timeinterval


@worktimeapp.route('timeinterval/<int:id>')
@worktimeapp.param('id', 'ID des Timeintervalls')
class TimeIntervalWithIDOperations(Resource):
    @worktimeapp.marshal_with(timeinterval)
    # @secured
    def get(self, id):
        adm = Businesslogic()
        timeinterval = adm.get_timeinterval_by_id(id)
        return timeinterval

    @worktimeapp.marshal_with(timeinterval)
    # @secured
    def delete(self, id):
        adm = Businesslogic()
        timeinterval = adm.get_timeinterval_by_id(id)
        adm.delete_timeinterval(timeinterval)

    @worktimeapp.marshal_with(timeinterval)
    @worktimeapp.expect(timeinterval, validate=True)
    # @secured
    def put(self, id):
        adm = Businesslogic()
        p = TimeIntervalBO.from_dict(api.payload)

        if p is not None:
            p.set_id(id)
            adm.save_timeinterval(p)
            return p, 200
        else:
            return '', 500


@worktimeapp.route('timeintervaltype/<string:type>')
@worktimeapp.param('type', 'Type des Timeintervalls')
class TimeIntervalWithTypeOperations(Resource):
    @worktimeapp.marshal_with(timeinterval)
    # @secured
    def get(self, type):
        adm = Businesslogic()
        timeinterval = adm.get_timeinterval_by_type(type)
        return timeinterval


"""
Break
"""


@worktimeapp.route('/break')
class BreakOperations(Resource):
    @worktimeapp.marshal_with(breaks)
    @worktimeapp.expect(breaks)
    # @secured
    def post(self):
        adm = Businesslogic()
        proposal = BreakBO.from_dict(api.payload)
        proposal_break_begin = BreakBeginBO.from_dict_timeinterval(api.payload)
        proposal_break_end = BreakEndBO.from_dict_timeinterval(api.payload)

        if proposal is not None:
            break_begin = adm.create_break_begin(
                proposal_break_begin.get_time()
            )
            ebe = adm.create_event(
                "breakbegin",
                None,
                None,
                break_begin.get_id(),
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
            )

            eb = adm.create_event_booking(
                ebe.get_id()
            )
            break_end = adm.create_break_end(
                proposal_break_end.get_time()
            )

            eee = adm.create_event(
                "breakend",
                None,
                None,
                None,
                break_end.get_id(),
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None
            )

            eb = adm.create_event_booking(
                eee.get_id()
            )

            p = adm.create_break(
                proposal.get_start(),
                proposal.get_end(),
                break_begin.get_id(),
                break_end.get_id(),

            )

            t = adm.create_timeinterval(
                proposal.get_type(),
                p.get_id(),
                None,
                None,
                None,
                None,
                None,
                None
            )

            tb = adm.create_timeinterval_booking(
                t.get_id()
            )
        return p

    @worktimeapp.marshal_list_with(breaks)
    # @secured
    def get(self):
        adm = Businesslogic()
        breaks = adm.get_all_breaks()
        return breaks


@worktimeapp.route('/break/<int:id>')
@worktimeapp.param('id', 'ID der Break')
class BreakWithIDOperations(Resource):
    @worktimeapp.marshal_with(breaks)
    # @secured
    def get(self, id):
        adm = Businesslogic()
        breaks = adm.get_break_by_id(id)
        return breaks

    @worktimeapp.marshal_with(breaks)
    # @secured
    def delete(self, id):
        adm = Businesslogic()
        breaks = adm.get_break_by_id(id)
        adm.delete_break(breaks)

    @worktimeapp.marshal_with(breaks)
    @worktimeapp.expect(breaks, validate=True)
    # @secured
    def put(self, id):
        adm = Businesslogic()
        p = BreakBO.from_dict(api.payload)
        proposal_break_begin = BreakBeginBO.from_dict_timeinterval(
            api.payload)
        proposal_break_end = BreakEndBO.from_dict_timeinterval(
            api.payload)

        if p is not None:
            proposal_break_begin.set_id(p.get_start_event())
            proposal_break_end.set_id(p.get_end_event())
            p.set_id(id)
            adm.save_break_begin(proposal_break_begin)
            adm.save_break_end(proposal_break_end)
            adm.save_break(p)
            return p, 200
        else:
            return '', 500


@worktimeapp.route('breakdate/<string:start>')
@worktimeapp.param('start', 'Start von Break')
class FindBreakByDate(Resource):
    @worktimeapp.marshal_with(breaks)
    # @secured
    def get(self, start):
        adm = Businesslogic()
        breaks = adm.get_breaks_by_date(start)
        return breaks


@worktimeapp.route('breakperiod/<string:start>/<string:end>')
@worktimeapp.param('start', 'Start von Break')
class FindBreakByTimePeriod(Resource):
    @worktimeapp.marshal_with(breaks)
    # @secured
    def get(self, start, end):
        adm = Businesslogic()
        breaks = adm.get_breaks_by_time_period(start, end)
        return breaks


"""
Illness
"""


@worktimeapp.route('/illness')
class IllnessOperations(Resource):
    @worktimeapp.marshal_with(illness)
    @worktimeapp.expect(illness)
    # @secured
    def post(self):
        adm = Businesslogic()
        proposal = IllnessBO.from_dict(api.payload)
        if proposal is not None:
            p = adm.create_illness(
                proposal.get_start(),
                proposal.get_end(),
                proposal.get_start_event(),
                proposal.get_end_event(),
            )

            t = adm.create_timeinterval(
                proposal.get_type(),
                None,
                p.get_id(),
                None,
                None,
                None,
                None,
                None
            )

            ti = adm.create_timeinterval_booking(
                t.get_id()
            )
        return p

    @worktimeapp.marshal_list_with(illness)
    # @secured
    def get(self):
        adm = Businesslogic()
        illness = adm.get_all_illnesses()
        return illness


@worktimeapp.route('illness/<int:id>')
@worktimeapp.param('id', 'ID der Illness')
class IllnessWithIDOperations(Resource):
    @worktimeapp.marshal_with(illness)
    # @secured
    def get(self, id):
        adm = Businesslogic()
        illness = adm.get_illness_by_id(id)
        return illness

    @worktimeapp.marshal_with(illness)
    # @secured
    def delete(self, id):
        adm = Businesslogic()
        illness = adm.get_illness_by_id(id)
        adm.delete_illness(illness)

    @worktimeapp.marshal_with(illness)
    @worktimeapp.expect(illness, validate=True)
    # @secured
    def put(self, id):
        adm = Businesslogic()
        p = IllnessBO.from_dict(api.payload)
        proposal_illness_begin = IllnessBeginBO.from_dict_timeinterval(
            api.payload)
        proposal_illness_end = IllnessEndBO.from_dict_timeinterval(
            api.payload)

        if p is not None:
            if (p.get_start_event() and p.get_end_event()) == None:
                p.set_id(id)
                adm.save_illness(p)
            elif not ((p.get_start_event() and p.get_end_event()) == None):
                p.set_id(id)
                proposal_illness_begin.set_id(p.get_start_event())
                proposal_illness_end.set_id(p.get_end_event())
                adm.save_illness(p)
                adm.save_illness_begin(proposal_illness_begin)
                adm.save_illness_end(proposal_illness_end)
            elif not (p.get_start_event() == None):
                p.set_id(id)
                proposal_illness_begin.set_id(p.get_start_event())
                adm.save_illness(p)
                adm.save_illness_begin(proposal_illness_begin)
            elif not (p.get_end_event() == None):
                p.set_id(id)
                proposal_illness_end.set_id(p.get_start_event())
                adm.save_illness(p)
                adm.save_illness_end(proposal_illness_end)
            return p, 200
        else:
            return '', 500


@worktimeapp.route('illnessdate/<string:start>')
@worktimeapp.param('start', 'Start von Illness')
class FindIllnessByDate(Resource):
    @worktimeapp.marshal_with(illness)
    # @secured
    def get(self, start):
        adm = Businesslogic()
        proposal = FlexDayBO.from_dict(api.payload)
        if proposal is not None:
            p = adm.create_flex_day(
                proposal.get_start(),
                proposal.get_end(),
                proposal.get_start_event(),
                proposal.get_end_event(),
                proposal.get_type(),
            )
        return p


@worktimeapp.route('illnessperiod/<string:start>/<string:end>')
@worktimeapp.param('start', 'Start von Illness')
class FindIllnessByTimePeriod(Resource):
    @worktimeapp.marshal_with(illness)
    # @secured
    def get(self, start, end):
        adm = Businesslogic()
        illness = adm.get_illnesses_by_time_period(start, end)
        return illness


"""
FlexDay
"""


@worktimeapp.route('/flexday')
class FlexDayOperations(Resource):
    @worktimeapp.marshal_with(flexday)
    @worktimeapp.expect(flexday)
    # @secured
    def post(self):
        adm = Businesslogic()
        proposal = FlexDayBO.from_dict(api.payload)
        proposal_flexday_start = FlexDayStartBO.from_dict_timeinterval(
            api.payload)
        proposal_flexday_end = FlexDayEndBO.from_dict_timeinterval(api.payload)
        if proposal is not None:
            flex_day_start = adm.create_flex_day_start(
                proposal_flexday_start.get_time()
            )
            ebe = adm.create_event(
                "FlexDayStart",
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                flex_day_start.get_id(),
                None
            )

            e = adm.create_event_booking(
                ebe.get_id()
            )
            flex_day_end = adm.create_flex_day_end(
                proposal_flexday_end.get_time()
            )

            eee = adm.create_event(
                "FlexDayEnd",
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                flex_day_end.get_id()
            )

            eb = adm.create_event_booking(
                eee.get_id()
            )
            p = adm.create_flex_day(
                proposal.get_start(),
                proposal.get_end(),
                flex_day_start.get_id(),
                flex_day_end.get_id()
            )
            t = adm.create_timeinterval(
                proposal.get_type(),
                None,
                None,
                None,
                None,
                None,
                p.get_id(),
                None
            )

            tw = adm.create_timeinterval_booking(
                t.get_id()
            )
        return p

    @worktimeapp.marshal_list_with(flexday)
    # @secured
    def get(self):
        adm = Businesslogic()
        flexday = adm.get_all_flex_days()
        return flexday


@worktimeapp.route('/flexday/<int:id>')
@worktimeapp.param('id', 'ID der FlexDay')
class FlexDayWithIDOperations(Resource):
    @worktimeapp.marshal_with(flexday)
    # @secured
    def get(self, id):
        adm = Businesslogic()
        flexday = adm.get_flex_day_by_id(id)
        return flexday

    @worktimeapp.marshal_with(flexday)
    # @secured
    def delete(self, id):
        adm = Businesslogic()
        flexday = adm.get_flex_day_by_id(id)
        adm.delete_flex_day(flexday)

    @worktimeapp.marshal_with(flexday)
    @worktimeapp.expect(flexday, validate=True)
    # @secured
    def put(self, id):
        adm = Businesslogic()
        p = FlexDayBO.from_dict(api.payload)
        proposal_flexday_begin = FlexDayStartBO.from_dict_timeinterval(
            api.payload)
        proposal_flexday_end = FlexDayEndBO.from_dict_timeinterval(
            api.payload)

        if p is not None:
            proposal_flexday_begin.set_id(p.get_start_event())
            proposal_flexday_end.set_id(p.get_end_event())
            p.set_id(id)
            adm.save_flex_day_start(proposal_flexday_begin)
            adm.save_flex_day_end(proposal_flexday_end)
            adm.save_flex_day(p)
            return p, 200
        else:
            return '', 500


@worktimeapp.route('flexdaydate/<string:start>')
@worktimeapp.param('start', 'Start von FlexDay')
class FindBreakByDate(Resource):
    @worktimeapp.marshal_with(flexday)
    # @secured
    def get(self, start):
        adm = Businesslogic()
        flexday = adm.get_flex_days_by_date(start)
        return flexday


@worktimeapp.route('flexdayperiod/<string:start>/<string:end>')
@worktimeapp.param('start', 'Start von FlexDay')
class FindBreakByTimePeriod(Resource):
    @worktimeapp.marshal_with(flexday)
    # @secured
    def get(self, start, end):
        adm = Businesslogic()
        flexday = adm.get_flex_days_by_time_period(start, end)
        return flexday


"""
ProjectDuration
"""


@worktimeapp.route('/projectduration')
class ProjectDurationOperations(Resource):
    @worktimeapp.marshal_with(projectduration)
    @worktimeapp.expect(projectduration)
    # @secured
    def post(self):
        adm = Businesslogic()
        proposal = ProjectDurationBO.from_dict(api.payload)
        if proposal is not None:
            p = adm.create_project_duration(
                proposal.get_start(),
                proposal.get_end(),
                proposal.get_start_event(),
                proposal.get_end_event(),
                proposal.get_project_id()
            )
            t = adm.create_timeinterval(
                proposal.get_type(),
                None,
                None,
                p.get_id(),
                None,
                None,
                None,
                None
            )

            tb = adm.create_timeinterval_booking(
                t.get_id()
            )
        return p

    @worktimeapp.marshal_list_with(projectduration)
    # @secured
    def get(self):
        adm = Businesslogic()
        projectduration = adm.get_all_project_durations()
        return projectduration


@worktimeapp.route('projectduration/<int:id>')
@worktimeapp.param('id', 'ID der ProjectDuration')
class ProjecDurationWithIDOperations(Resource):
    @worktimeapp.marshal_with(projectduration)
    # @secured
    def get(self, id):
        adm = Businesslogic()
        projectduration = adm.get_project_duration_by_id(id)
        return projectduration

    @worktimeapp.marshal_with(projectduration)
    # @secured
    def delete(self, id):
        adm = Businesslogic()
        projectduration = adm.get_project_duration_by_id(id)
        adm.delete_project_duration(projectduration)

    @worktimeapp.marshal_with(projectduration)
    @worktimeapp.expect(projectduration, validate=True)
    # @secured
    def put(self, id):
        adm = Businesslogic()
        p = ProjectDurationBO.from_dict(api.payload)

        if p is not None:
            p.set_id(id)
            adm.save_project_duration(p)
            return p, 200
        else:
            return '', 500


@worktimeapp.route('projectdurationdate/<string:start>')
@worktimeapp.param('start', 'Start von ProjectDuration')
class FindProjectDurationByDate(Resource):
    @worktimeapp.marshal_with(projectduration)
    # @secured
    def get(self, start):
        adm = Businesslogic()
        projectduration = adm.get_project_durations_by_date(start)
        return projectduration


@worktimeapp.route('projectdurationperiod/<string:start>/<string:end>')
@worktimeapp.param('start', 'Start von ProjectDuration')
class FindProjectDurationByTimePeriod(Resource):
    @worktimeapp.marshal_with(projectduration)
    # @secured
    def get(self, start, end):
        adm = Businesslogic()
        projectduration = adm.get_project_durations_by_time_period(start, end)
        return projectduration


@worktimeapp.route('projectdurationproject/<int:projectid>')
@worktimeapp.param('id', 'Id von Project')
class FindProjectDurationByProjectId(Resource):
    @worktimeapp.marshal_with(projectduration)
    # @secured
    def get(self, id):
        adm = Businesslogic()
        projectduration = adm.get_project_duration_by_project_id(id)
        return projectduration


"""
ProjectWork
"""


@worktimeapp.route('/projectwork')
class ProjectWorkOperations(Resource):
    @worktimeapp.marshal_with(projectwork)
    @worktimeapp.expect(projectwork)
    # @secured
    def post(self):
        adm = Businesslogic()
        proposal = ProjectWorkBO.from_dict(api.payload)
        proposal_projectwork_start = ProjectWorkBeginBO.from_dict_timeinterval(
            api.payload)
        proposal_projectwork_end = ProjectWorkEndBO.from_dict_timeinterval(
            api.payload)
        if proposal is not None:
            project_work_begin = adm.create_project_work_begin(
                proposal_projectwork_start.get_time()
            )
            ebe = adm.create_event(
                "projectWorkBegin",
                None,
                None,
                None,
                None,
                None,
                None,
                project_work_begin.get_id(),
                None,
                None,
                None,
                None,
                None
            )

            eb = adm.create_event_booking(
                ebe.get_id()
            )
            project_work_end = adm.create_project_work_end(
                proposal_projectwork_end.get_time()
            )
            eee = adm.create_event(
                "projectWorkEnd",
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                project_work_end.get_id(),
                None,
                None,
                None,
                None
            )

            eb = adm.create_event_booking(
                eee.get_id()
            )
            p = adm.create_project_work(
                proposal.get_start(),
                proposal.get_end(),
                project_work_begin.get_id(),
                project_work_end.get_id(),
                proposal.get_activity_id()
            )
            t = adm.create_timeinterval(
                proposal.get_type(),
                None,
                None,
                None,
                p.get_id(),
                None,
                None,
                None
            )

            td = adm.create_timeinterval_booking(
                t.get_id()
            )
        return p

    @worktimeapp.marshal_list_with(projectwork)
    # @secured
    def get(self):
        adm = Businesslogic()
        projectwork = adm.get_all_project_works()
        return projectwork


@worktimeapp.route('projectwork/<int:id>')
@worktimeapp.param('id', 'ID der ProjectWork')
class ProjecWorkWithIDOperations(Resource):
    @worktimeapp.marshal_with(projectwork)
    # @secured
    def get(self, id):
        adm = Businesslogic()
        projectwork = adm.get_project_work_by_id(id)
        return projectwork

    @worktimeapp.marshal_with(projectwork)
    # @secured
    def delete(self, id):
        adm = Businesslogic()
        projectwork = adm.get_project_work_by_id(id)
        adm.delete_project_work(projectwork)

    @worktimeapp.marshal_with(projectwork)
    @worktimeapp.expect(projectwork, validate=True)
    # @secured
    def put(self, id):
        adm = Businesslogic()
        p = ProjectWorkBO.from_dict(api.payload)
        proposal_project_work_begin = ProjectWorkBeginBO.from_dict_timeinterval(
            api.payload)
        proposal_project_work_end = ProjectWorkEndBO.from_dict_timeinterval(
            api.payload)

        if p is not None:
            proposal_project_work_begin.set_id(p.get_start_event())
            proposal_project_work_end.set_id(p.get_end_event())
            p.set_id(id)
            adm.save_project_work_begin(proposal_project_work_begin)
            adm.save_project_work_end(proposal_project_work_end)
            adm.save_project_work(p)
            return p, 200
        else:
            return '', 500


@worktimeapp.route('projectworkdate/<string:start>')
@worktimeapp.param('start', 'Start von ProjectWork')
class FindProjectWorkByDate(Resource):
    @worktimeapp.marshal_with(projectwork)
    # @secured
    def get(self, start):
        adm = Businesslogic()
        projectwork = adm.get_project_works_by_date(start)
        return projectwork


@worktimeapp.route('projectworkperiod/<string:start>/<string:end>')
@worktimeapp.param('start', 'Start von ProjectWork')
class FindProjectWorkByTimePeriod(Resource):
    @worktimeapp.marshal_with(projectwork)
    # @secured
    def get(self, start, end):
        adm = Businesslogic()
        projectwork = adm.get_project_works_by_time_period(start, end)
        return projectwork


@worktimeapp.route('projectworkactivity/<int:activitytid>')
@worktimeapp.param('id', 'Id von Project')
class FindProjectWorkByProjectId(Resource):
    @worktimeapp.marshal_with(projectwork)
    # @secured
    def get(self, id):
        adm = Businesslogic()
        projectwork = adm.get_project_works_by_activity_id(id)
        return projectwork


"""
Vacation
"""


@worktimeapp.route('/vacation')
class VacationOperations(Resource):
    @worktimeapp.marshal_with(vacation)
    @worktimeapp.expect(vacation)
    # @secured
    def post(self):
        adm = Businesslogic()
        proposal = VacationBO.from_dict(api.payload)
        if proposal is not None:
            p = adm.create_vacation(
                proposal.get_start(),
                proposal.get_end(),
                proposal.get_start_event(),
                proposal.get_end_event(),
                proposal.get_type(),
            )

            t = adm.create_timeinterval(
                proposal.get_type(),
                None,
                None,
                None,
                None,
                p.get_id(),
                None,
                None
            )

            tb = adm.create_timeinterval_booking(
                t.get_id()
            )
        return p

    @worktimeapp.marshal_list_with(vacation)
    # @secured
    def get(self):
        adm = Businesslogic()
        vacation = adm.get_all_vacations()
        return vacation


@worktimeapp.route('/vacation/<int:id>')
@worktimeapp.param('id', 'ID der Vacation')
class VacationWithIDOperations(Resource):
    @worktimeapp.marshal_with(vacation)
    # @secured
    def get(self, id):
        adm = Businesslogic()
        vacation = adm.get_vacation_by_id(id)
        return vacation

    @worktimeapp.marshal_with(vacation)
    # @secured
    def delete(self, id):
        adm = Businesslogic()
        vacation = adm.get_vacation_by_id(id)
        adm.delete_vacation(vacation)

    @worktimeapp.marshal_with(vacation)
    @worktimeapp.expect(vacation, validate=True)
    # @secured
    def put(self, id):
        adm = Businesslogic()
        p = VacationBO.from_dict(api.payload)
        proposal_vacation_begin = VacationBeginBO.from_dict_timeinterval(
            api.payload)
        proposal_vacation_end = VacationEndBO.from_dict_timeinterval(
            api.payload)

        if p is not None:
            if (p.get_start_event() and p.get_end_event()) == None:
                p.set_id(id)
                adm.save_vacation(p)
            elif not ((p.get_start_event() and p.get_end_event()) == None):
                p.set_id(id)
                proposal_vacation_begin.set_id(p.get_start_event())
                proposal_vacation_end.set_id(p.get_end_event())
                adm.save_vacation(p)
                adm.save_vacation_begin(proposal_vacation_begin)
                adm.save_vacation_end(proposal_vacation_end)
            elif not (p.get_start_event() == None):
                p.set_id(id)
                proposal_vacation_begin.set_id(p.get_start_event())
                adm.save_vacation(p)
                adm.save_vacation_begin(proposal_vacation_begin)
            elif not (p.get_end_event() == None):
                p.set_id(id)
                proposal_vacation_end.set_id(p.get_start_event())
                adm.save_vacation(p)
                adm.save_vacation_end(proposal_vacation_end)
            return p, 200
        else:
            return '', 500


@worktimeapp.route('vacationdate/<string:start>')
@worktimeapp.param('start', 'Start von Vacation')
class FindVacationByDate(Resource):
    @worktimeapp.marshal_with(vacation)
    # @secured
    def get(self, start):
        adm = Businesslogic()
        vacation = adm.get_vacations_by_date(start)
        return vacation


@worktimeapp.route('vacationperiod/<string:start>/<string:end>')
@worktimeapp.param('start', 'Start von Vacation')
class FindVacationByTimePeriod(Resource):
    @worktimeapp.marshal_with(vacation)
    # @secured
    def get(self, start, end):
        adm = Businesslogic()
        vacation = adm.get_vacations_by_time_period(start, end)
        return vacation


"""
Work
"""


@worktimeapp.route('/work')
class WorkOperations(Resource):
    @worktimeapp.marshal_with(work)
    @worktimeapp.expect(work)
    # @secured
    def post(self):
        adm = Businesslogic()
        proposal = WorkBO.from_dict(api.payload)
        proposal_coming = ComingBO.from_dict_timeinterval(api.payload)
        proposal_going = GoingBO.from_dict_timeinterval(api.payload)

        if proposal is not None:
            coming = adm.create_coming(
                proposal_coming.get_time()
            )

            ebe = adm.create_event(
                "coming",
                coming.get_id(),
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None
            )

            eb = adm.create_event_booking(
                ebe.get_id()
            )
            going = adm.create_going(
                proposal_going.get_time()
            )

            eee = adm.create_event(
                "going",
                None,
                going.get_id(),
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None
            )

            eb = adm.create_event_booking(
                eee.get_id()
            )

            p = adm.create_work(
                proposal.get_start(),
                proposal.get_end(),
                coming.get_id(),
                going.get_id())

            t = adm.create_timeinterval(
                proposal.get_type(),
                None,
                None,
                None,
                None,
                None,
                None,
                p.get_id()
            )

            tw = adm.create_timeinterval_booking(
                t.get_id()
            )
        print(p.get_start_event())

    @worktimeapp.marshal_list_with(work)
    # @secured
    def get(self):
        adm = Businesslogic()
        work = adm.get_all_works()
        return work


@worktimeapp.route('work/<int:id>')
@worktimeapp.param('id', 'ID der Work')
class WorkWithIDOperations(Resource):
    @worktimeapp.marshal_with(work)
    # @secured
    def get(self, id):
        adm = Businesslogic()
        work = adm.get_work_by_id(id)
        return work

    @worktimeapp.marshal_with(work)
    # @secured
    def delete(self, id):
        adm = Businesslogic()
        work = adm.get_work_by_id(id)
        adm.delete_work(work)

    @worktimeapp.marshal_with(work)
    @worktimeapp.expect(work, validate=True)
    # @secured
    def put(self, id):
        adm = Businesslogic()
        p = WorkBO.from_dict(api.payload)
        proposal_coming = ComingBO.from_dict_timeinterval(api.payload)
        proposal_going = GoingBO.from_dict_timeinterval(api.payload)

        if p is not None:
            proposal_coming.set_id(p.get_start_event())
            proposal_going.set_id(p.get_end_event())
            p.set_id(id)
            adm.save_coming(proposal_coming)
            adm.save_going(proposal_going)
            adm.save_work(p)
            return p, 200
        else:
            return '', 500


@worktimeapp.route('workdate/<string:start>')
@worktimeapp.param('start', 'Start von Work')
class FindWorkByDate(Resource):
    @worktimeapp.marshal_with(work)
    # @secured
    def get(self, start):
        adm = Businesslogic()
        work = adm.get_works_by_date(start)
        return work


@worktimeapp.route('vacationperiod/<string:start>/<string:end>')
@worktimeapp.param('start', 'Start von Work')
class FindWorkByTimePeriod(Resource):
    @worktimeapp.marshal_with(work)
    # @secured
    def get(self, start, end):
        adm = Businesslogic()
        work = adm.get_works_by_time_period(start, end)
        return work


"""
Combined Methodes
"""


@worktimeapp.route('userintervalbookings/<int:userid>')
@worktimeapp.param('userid', 'ID des Users')
class TimeintervalBookingsForUser(Resource):
    pass


@worktimeapp.route('userintervalbookings/<int:userid>')
@worktimeapp.param('userid', 'ID des Users')
class EventBookingsForUser(Resource):
    pass


'''Booking Routes @author Mihriban Dogan (https://github.com/mihriban-dogan)'''


@worktimeapp.route('/booking/timeintervalbooking/<int:id>')
@worktimeapp.param('id', 'Die User ID')
class TimeIntervalBookingOperationsWithParam(Resource):
    @worktimeapp.marshal_with(timeinterval_with_events)
    def get(self, id):
        adm = Businesslogic()
        user = adm.get_user_by_id(id)

        # Haben wir eine brauchbare Referenz auf ein Customer-Objekt bekommen?
        if user is not None:
            # Jetzt erst lesen wir die Konten des Customer aus.
            timeintervalbookings = adm.get_all_timeinterval_bookings_for_user(
                user)
            return timeintervalbookings


@worktimeapp.route('/booking/timeintervalbooking')
class TimeintervalBookingOperations(Resource):
    @worktimeapp.marshal_with(booking)
    @worktimeapp.expect(booking)
    def post(self):
        adm = Businesslogic()
        proposal = BookingBO.from_dict(api.payload)
        if proposal is not None:
            t = 2
            time.sleep(t)
            b = adm.create_booking_for_timeinterval(
                proposal.get_user_id(),
                proposal.get_work_time_account_id(),
                "T",
                None
            )

            if proposal.get_type() == "vacation" or proposal.get_type() == "illness" or proposal.get_type() == "projectduration":
                pass
            elif proposal.get_type() == "projectwork":
                p = adm.add_delta_for_project_work(b)
            else:
                d = adm.add_delta(b)

            return b

        else:
            return ''


@worktimeapp.route('/booking/eventbooking')
class EventBookingOperations(Resource):
    @worktimeapp.marshal_with(booking)
    @worktimeapp.expect(booking)
    def post(self):
        adm = Businesslogic()
        proposal = BookingBO.from_dict(api.payload)
        if proposal is not None:
            t = 2
            time.sleep(t)
            b = adm.create_booking_for_event(
                proposal.get_user_id(),
                proposal.get_work_time_account_id(),
                "E",
                None
            )
            return b
        else:
            return ''


@worktimeapp.route('/booking/eventbooking/<int:id>')
@worktimeapp.param('id', 'Die User ID')
class EventBookingOperationsWithParam(Resource):
    @worktimeapp.marshal_with(event_subclass)
    def get(self, id):
        adm = Businesslogic()
        user = adm.get_user_by_id(id)

        # Haben wir eine brauchbare Referenz auf ein Customer-Objekt bekommen?
        if user is not None:
            # Jetzt erst lesen wir die Konten des Customer aus.
            eventbookings = adm.get_all_event_bookings_for_user(user)
            return eventbookings


@worktimeapp.route('/booking/eventbooking/<int:id>/vacation&illness')
@worktimeapp.param('id', 'Die User ID')
class EventBookingOperationsWithParam(Resource):
    @worktimeapp.marshal_with(event_subclass)
    def get(self, id):
        adm = Businesslogic()
        user = adm.get_user_by_id(id)

        # Haben wir eine brauchbare Referenz auf ein Customer-Objekt bekommen?
        if user is not None:
            # Jetzt erst lesen wir die Konten des Customer aus.
            eventbookings = adm.get_all_vacation_illness_event_bookings_for_user(
                user)
            return eventbookings


"""
Nachdem wir nun sämtliche Resourcen definiert haben, die wir via REST bereitstellen möchten,
müssen nun die App auch tatsächlich zu starten.
Diese Zeile ist leider nicht Teil der Flask-Doku! In jener Doku wird von einem Start via Kommandozeile ausgegangen.
Dies ist jedoch für uns in der Entwicklungsumgebung wenig komfortabel. Deshlab kommt es also schließlich zu den 
folgenden Zeilen. 
**ACHTUNG:** Diese Zeile wird nur in der lokalen Entwicklungsumgebung ausgeführt und hat in der Cloud keine Wirkung!
"""
if __name__ == '__main__':
    app.run(debug=True)
