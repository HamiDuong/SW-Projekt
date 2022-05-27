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
#from attr import attributes
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
from server.Businesslogic import Businesslogic
from server.bo import ProjectBO
from server.bo import ProjectUserBO
from server.bo import ActivityBO
#from SecurityDecorator import secured

from server.bo.timeinterval.BreakBO import BreakBO
from server.bo.timeinterval.IllnessBO import IllnessBO
from server.bo.timeinterval.ProjectDurationBO import ProjectDurationBO
from server.bo.timeinterval.ProjectWorkBO import ProjectWorkBO
from server.bo.timeinterval.TimeIntervalBO import TimeIntervalBO
from server.bo.timeinterval.VacationBO import VacationBO
from server.bo.timeinterval.WorkBO import WorkBO
from src.server.bo.timeinterval.FlexDayBO import FlexDayBO


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
    'worktimeapp', description='Funktionen des BankBeispiels')

"""Nachfolgend werden analog zu unseren BusinessObject-Klassen transferierbare Strukturen angelegt.

BusinessObject dient als Basisklasse, auf der die weiteren Strukturen User, Events, Projects, etc. aufsetzen."""
bo = api.model('BusinessObject', {
    'id': fields.Integer(attribute='_id', description='Der Unique Identifier eines Business Object'),
    'date_of_last_change': fields.DateTime(attribute='_date_of_last_change', description='Zeitpunkt der letzten Änderung')
})

"""Users"""
user = api.inherit('User', bo, {
    'first_name': fields.String(attribute='_first_name', description='Vorname eines Benutzers'),
    'last_name': fields.String(attribute='_last_name', description='Nachname eines Benutzers'),
    'mail_adress': fields.String(attribute='_mail_adress', description='E-Mail-Adresse eines Benutzers'),
    'user_name': fields.String(attribute='_user_name', description='User Name eines Benutzers')
})

"""WorkTimeAccount"""
Worktimeaccount = api.inherit('Object', bo, {
    'user_id': fields.Integer(attribute='_user_id', description='User ID eines Benutzers')
})

'''Project'''
project = api.inherit('Project', bo, {
    'name': fields.String(attribute='_name', description='Der Name des Projekts'),
    'commissioner': fields.String(attribute='_commissioner', description='Der Name des Projektleiter'),
    'user_id': fields.Integer(attribute='_user_id', description='Die ID eines Benutzer'),
    'duration': fields.Float(attribute='_duration', description='Die Dauer einer Aktivität')
})

'''ProjectUser'''
projectuser = api.inherit('ProjectUser', bo, {
    'project_id': fields.Integer(attribute='_project_id', description='Die ID eines Projektmitglieds'),
    'user_id': fields.Integer(attribute='_user_id', description='Die ID eines Benutzer'),
    'capacity': fields.Float(attribute='_capacity', description='Die Kapazität eines Projekts')
})

'''Activity'''
activity = api.inherit('Activity', bo, {
    'name': fields.String(attribute='_name', description='Der Name des Projekts'),
    'capacity': fields.Float(attribute='_capacity', description='Die Kapazität eines Projekts'),
    'project_id': fields.Integer(attribute='_project_id', description='Die ID eines Projekts')

})

'''Event'''
event = api.inherit('Event', bo, {
    'event_id': fields.Integer(attribute='_event_id', description='Die ID des Events'),
    'time': fields.Float(attribute='_time', description='Der Event-Zeitpunkt'),
    'event_booking_id': fields.Integer(attribute='_event_booking_id', description='Die ID der Buchung')
})

"""
Timeinterval und zugehörige Subklassen
"""
timeinterval = api.inherit('TimeInterval', bo, {
    '_type': fields.String(attribute='_type', description='Art des Intervals'),
    '_break_id': fields.Integer(attribute='_break_id', descriptiong= 'Fremdschlüssel zu BreakBO'),
    '_illness_id': fields.Integer(attribute='_illness_id', descriptiong= 'Fremdschlüssel zu IllnessBO'),
    '_project_duration_id': fields.Integer(attribute='_project_duration_id', descriptiong= 'Fremdschlüssel zu ProjectDurationBO'),
    '_project_work_id': fields.Integer(attribute='_project_work_id', descriptiong= 'Fremdschlüssel zu ProjectWorkBO'),
    '_vacation_id': fields.Integer(attribute='_vacation_id', descriptiong= 'Fremdschlüssel zu VacationBO'),
    '_work_id': fields.Integer(attribute='_work_id', descriptiong= 'Fremdschlüssel zu WorkBO')
})

breaks = api.inherit('Break', bo, {
    '_start': fields.DateTime(attribute='_start', description='Startpunkt des Intervalls'),
    '_end': fields.DateTime(attribute='_end', description='Endpunkt des Intervalls'),
    '_start_event': fields.Integer(attribute='_start', description='Fremdschlüssel zum Startevent'),
    '_end_event': fields.Integer(attribute='_end', description='Fremdschlüssel zum Endevent'),
    '_type': fields.String(attribute='_type', description='Art des Intervals')
})

illness = api.inherit('Illness', bo, {
    '_start': fields.DateTime(attribute='_start', description='Startpunkt des Intervalls'),
    '_end': fields.DateTime(attribute='_end', description='Endpunkt des Intervalls'),
    '_start_event': fields.Integer(attribute='_start', description='Fremdschlüssel zum Startevent'),
    '_end_event': fields.Integer(attribute='_end', description='Fremdschlüssel zum Endevent'),
    '_type': fields.String(attribute='_type', description='Art des Intervals')
})

vacation = api.inherit('Vacation', bo, {
    '_start': fields.DateTime(attribute='_start', description='Startpunkt des Intervalls'),
    '_end': fields.DateTime(attribute='_end', description='Endpunkt des Intervalls'),
    '_start_event': fields.Integer(attribute='_start', description='Fremdschlüssel zum Startevent'),
    '_end_event': fields.Integer(attribute='_end', description='Fremdschlüssel zum Endevent'),
    '_type': fields.String(attribute='_type', description='Art des Intervals')
})

work = api.inherit('Work', bo, {
    '_start': fields.DateTime(attribute='_start', description='Startpunkt des Intervalls'),
    '_end': fields.DateTime(attribute='_end', description='Endpunkt des Intervalls'),
    '_start_event': fields.Integer(attribute='_start', description='Fremdschlüssel zum Startevent'),
    '_end_event': fields.Integer(attribute='_end', description='Fremdschlüssel zum Endevent'),
    '_type': fields.String(attribute='_type', description='Art des Intervals')
})

flexday = api.inherit('FlexDay', bo, {
    '_start': fields.DateTime(attribute='_start', description='Startpunkt des Intervalls'),
    '_end': fields.DateTime(attribute='_end', description='Endpunkt des Intervalls'),
    '_start_event': fields.Integer(attribute='_start', description='Fremdschlüssel zum Startevent'),
    '_end_event': fields.Integer(attribute='_end', description='Fremdschlüssel zum Endevent'),
    '_type': fields.String(attribute='_type', description='Art des Intervals')
})

projectduration = api.inherit('ProjectDuration', bo, {
    '_start': fields.DateTime(attribute='_start', description='Startpunkt des Intervalls'),
    '_end': fields.DateTime(attribute='_end', description='Endpunkt des Intervalls'),
    '_start_event': fields.Integer(attribute='_start', description='Fremdschlüssel zum Startevent'),
    '_end_event': fields.Integer(attribute='_end', description='Fremdschlüssel zum Endevent'),
    '_type': fields.String(attribute='_type', description='Art des Intervals'),
    '_project_id': fields.Integer(attribute='_project_id', description='Fremschlüssel zum Projekt')
})

projectwork = api.inherit('ProjectWork', bo, {
    '_start': fields.DateTime(attribute='_start', description='Startpunkt des Intervalls'),
    '_end': fields.DateTime(attribute='_end', description='Endpunkt des Intervalls'),
    '_start_event': fields.Integer(attribute='_start', description='Fremdschlüssel zum Startevent'),
    '_end_event': fields.Integer(attribute='_end', description='Fremdschlüssel zum Endevent'),
    '_type': fields.String(attribute='_type', description='Art des Intervals'),
    '_activity_id': fields.Integer(attribute='_activity_id', description='Fremschlüssel zur Aktivity')
})

# Tatsächliche Funktionen beginnen ab hier.

@worktimeapp.route('/user')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class UserListOperations(Resource):
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
        adm = user()

        proposal = UserBO.from_dict(api.payload)

        """RATSCHLAG: Prüfen Sie stets die Referenzen auf valide Werte, bevor Sie diese verwenden!"""
        if proposal is not None:
            """ Wir verwenden lediglich Vor- und Nachnamen des Proposals für die Erzeugung
            eines User-Objekts. Das serverseitig erzeugte Objekt ist das maßgebliche und 
            wird auch dem Client zurückgegeben. 
            """
            c = adm.create_user(proposal.get_first_name(), proposal.get_last_name(
            ), proposal.get_mail_adress(), proposal.get_user_name())
            return c, 200
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500


@worktimeapp.route('/users/<string:mail_adress>')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@worktimeapp.param('mail_adress', 'Die E-Mail-Adresse eines Benutzers')
class UserOperations(Resource):
    @worktimeapp.marshal_with(user)
    # #@secured
    def get(self, id):
        """Auslesen eines bestimmten User-Objekts.

        Das auszulesende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        cust = adm.get_user_by_mail_adress(id)
        return cust

    # #@secured
    def delete(self, id):
        """Löschen eines bestimmten User-Objekts.

        Das zu löschende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        cust = adm.get_user_by_id(id)
        adm.delete_user(cust)
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
        c = UserBO.from_dict(api.payload)

        if c is not None:
            """Hierdurch wird die id des zu überschreibenden (vgl. Update) User-Objekts gesetzt.
            Siehe Hinweise oben.
            """
            c.set_id(id)
            adm.save_user(c)
            return '', 200
        else:
            return '', 500


@worktimeapp.route('/users-by-name/<string:user_name>')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@worktimeapp.param('user_name', 'Der User Name des Benutzers')
class UsersByNameOperations(Resource):
    @worktimeapp.marshal_with(user)
    # #@secured
    def get(self, user_name):
        """ Auslesen von User-Objekten, die durch den User Name bestimmt werden.

        Die auszulesenden Objekte werden durch ```user_name``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        cust = adm.get_user_by_user_name(user_name)
        return cust


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


@worktimeapp.route('/users/<string:mail_adress>')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@worktimeapp.param('id', 'Die E-Mail-Adresse eines Benutzers')
class UserRelatedAccountOperations(Resource):
    @worktimeapp.marshal_with(user)
    # #@secured
    def get(self, mail_adress):
        """Auslesen von User-Objekten, die durch die E-Mail_Adresse bestimmt werden.

        Die auszulesenden Objekte werden durch ```mail_adress``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        usr = adm.get_user_by_mail_adress(mail_adress)
        return usr


@worktimeapp.route('/users/<string:user_name>')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@worktimeapp.param('id', 'Die E-Mail-Adresse eines Benutzers')
class UserRelatedAccountOperations(Resource):
    @worktimeapp.marshal_with(user)
    # #@secured
    def get(self, user_name):
        """Auslesen von User-Objekten, die durch den User Namen bestimmt werden.

        Die auszulesenden Objekte werden durch ```user_name``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        cust = adm.get_user_by_user_name(user_name)
        return cust


@worktimeapp.route('/WorkTimeAccount')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class WorkTimeAccountListOperations(Resource):
    @worktimeapp.marshal_list_with(Worktimeaccount)
    # #@secured
    def get(self):
        """Auslesen aller WorkTimeAccount-Objekte.

        Sollten keine User-Objekte verfügbar sein, so wird eine leere Sequenz zurückgegeben."""
        adm = Businesslogic()
        worktimeaccounts = adm.get_all_worktimeaccounts()
        return worktimeaccounts

    @worktimeapp.marshal_with(Worktimeaccount, code=200)
    # Wir erwarten ein Worktimeaccount-Objekt von Client-Seite.
    @worktimeapp.expect(Worktimeaccount)
    # #@secured
    def post(self):
        """Anlegen eines neuen Worktimeaccount-Objekts.

        **ACHTUNG:** Wir fassen die vom Client gesendeten Daten als Vorschlag auf.
        So ist zum Beispiel die Vergabe der ID nicht Aufgabe des Clients.
        Selbst wenn der Client eine ID in dem Proposal vergeben sollte, so
        liegt es an der Businesslogic (Businesslogik), eine korrekte ID
        zu vergeben. *Das korrigierte Objekt wird schließlich zurückgegeben.*
        """
        adm = Worktimeaccount()

        proposal = WorkTimeAccountBO.from_dict(api.payload)

        """RATSCHLAG: Prüfen Sie stets die Referenzen auf valide Werte, bevor Sie diese verwenden!"""
        if proposal is not None:
            """ Wir verwenden lediglich Vor- und Nachnamen des Proposals für die Erzeugung
            eines Worktimeaccount-Objekts. Das serverseitig erzeugte Objekt ist das maßgebliche und 
            wird auch dem Client zurückgegeben. 
            """
            c = adm.create_Worktimeaccount(proposal.get_user_id(), )
            return c, 200
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500


@worktimeapp.route('/worktimeaccounts/<int:user_id>')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@worktimeapp.param('user_id', 'Die User-ID eines Benutzers')
class WorktimeaccountRelatedAccountOperations(Resource):
    @worktimeapp.marshal_with(Worktimeaccount)
    # #@secured
    def get(self, user_id):
        """Auslesen von User-Objekten, die durch den User Namen bestimmt werden.

        Die auszulesenden Objekte werden durch ```user_id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        cust = adm.get_user_by_user_name(user_id)
        return cust


@worktimeapp.route('/projects')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class UserListOperations(Resource):
    @worktimeapp.marshal_list_with(user)
    # #@secured
    def get(self):
        """Auslesen aller User-Objekte.

        Sollten keine User-Objekte verfügbar sein, so wird eine leere Sequenz zurückgegeben."""
        adm = Businesslogic()
        users = adm.get_all_users()
        return users

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

        proposal = user.from_dict(api.payload)

        """RATSCHLAG: Prüfen Sie stets die Referenzen auf valide Werte, bevor Sie diese verwenden!"""
        if proposal is not None:
            """ Wir verwenden lediglich Vor- und Nachnamen des Proposals für die Erzeugung
            eines User-Objekts. Das serverseitig erzeugte Objekt ist das maßgebliche und 
            wird auch dem Client zurückgegeben. 
            """
            c = adm.create_user(proposal.get_first_name(),
                                proposal.get_last_name())
            return c, 200
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500


@worktimeapp.route('/users/<int:id>')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@worktimeapp.param('id', 'Die ID des User-Objekts')
class UserOperations(Resource):
    @worktimeapp.marshal_with(user)
    # #@secured
    def get(self, id):
        """Auslesen eines bestimmten User-Objekts.

        Das auszulesende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        cust = adm.get_user_by_id(id)
        return cust

    # #@secured
    def delete(self, id):
        """Löschen eines bestimmten User-Objekts.

        Das zu löschende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        cust = adm.get_user_by_id(id)
        adm.delete_user(cust)
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
        c = user.from_dict(api.payload)

        if c is not None:
            """Hierdurch wird die id des zu überschreibenden (vgl. Update) User-Objekts gesetzt.
            Siehe Hinweise oben.
            """
            c.set_id(id)
            adm.save_user(c)
            return '', 200
        else:
            return '', 500


@worktimeapp.route('/users-by-name/<string:lastname>')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@worktimeapp.param('lastname', 'Der Nachname des Kunden')
class UsersByNameOperations(Resource):
    @worktimeapp.marshal_with(user)
    # #@secured
    def get(self, lastname):
        """ Auslesen von User-Objekten, die durch den Nachnamen bestimmt werden.

        Die auszulesenden Objekte werden durch ```lastname``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        cust = adm.get_user_by_name(lastname)
        return cust


@worktimeapp.route('/users/<int:id>/accounts')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@worktimeapp.param('id', 'Die ID des User-Objekts')
class UserRelatedAccountOperations(Resource):
    @worktimeapp.marshal_with(user)
    # #@secured
    def get(self, id):
        """Auslesen aller Acount-Objekte bzgl. eines bestimmten User-Objekts.

        Das User-Objekt dessen Accounts wir lesen möchten, wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        # Zunächst benötigen wir den durch id gegebenen User.
        cust = adm.get_user_by_id(id)

        # Haben wir eine brauchbare Referenz auf ein User-Objekt bekommen?
        if cust is not None:
            # Jetzt erst lesen wir die Konten des User aus.
            account_list = adm.get_accounts_of_user(cust)
            return account_list
        else:
            return "User not found", 500

# Project
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
                proposal.get_duration()
            )
            return p

    @worktimeapp.marshal_list_with(project)
    # @secured
    def get(self):
        adm = Businesslogic()
        project = adm.get_all_projects()
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
    def get_user(self, id):
        adm = Businesslogic()
        project = adm.get_projects_by_user_id(id)
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


'''@worktimeapp.route('/project/<str:name>')
@worktimeapp.param('name', 'Der Name des Projekts')
class ProjectWithSTRINGOperations(Resource):
    @worktimeapp.marshal_with(project)
    # @secured
    def get(self, name):
        adm = Businesslogic()
        activity = adm.get_by_project_name(name)
        return activity'''


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
            p = adm.create_project(
                proposal.get_name(),
                proposal.get_capacity(),
                proposal.get_project_id()
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
        """Anlegen eines neuen Event-Objekts.

        **ACHTUNG:** Wir fassen die vom Client gesendeten Daten als Vorschlag auf.
        So ist zum Beispiel die Vergabe der ID nicht Aufgabe des Clients.
        Selbst wenn der Client eine ID in dem Proposal vergeben sollte, so
        liegt es an der BankAdministration (Businesslogik), eine korrekte ID
        zu vergeben. *Das korrigierte Objekt wird schließlich zurückgegeben.*
        """
        adm = Businesslogic()

        proposal = event.from_dict(api.payload)

        """RATSCHLAG: Prüfen Sie stets die Referenzen auf valide Werte, bevor Sie diese verwenden!"""
        if proposal is not None:
            """ Wir verwenden lediglich Vor- und Nachnamen des Proposals für die Erzeugung
            eines Event-Objekts. Das serverseitig erzeugte Objekt ist das maßgebliche und 
            wird auch dem Client zurückgegeben. 
            """
            c = adm.create_event(
                proposal.get_id(), proposal.get_time(), proposal.get_event_booking_id())
            return c, 200
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500


@worktimeapp.route('/events/<int:id>')
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


@worktimeapp.route('/events-by-event_booking_id/<int:event_booking_id>')
@worktimeapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@worktimeapp.param('event_booking_id', 'Die ID der zugehörigen Ereignsisbuchung')
class EventsByNameOperations(Resource):
    @worktimeapp.marshal_with(event)
    #@secured
    def get(self, event_booking_id):
        """ Auslesen von Event-Objekten, die durch den Nachnamen bestimmt werden.

        Die auszulesenden Objekte werden durch ```event_booking_id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        event = adm.get_event_by_name(event_booking_id)
        return event

"""
Timeinterval
"""
@worktimeapp.route('/timeinterval')
class TimeIntervalOperations(Resource):
    @worktimeapp.marshal_with(timeinterval)
    @worktimeapp.expect(timeinterval)
    #@secured
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
    #@secured
    def get(self):
        adm = Businesslogic()
        timeinterval = adm.get_all_timeintervals()
        return timeinterval

@worktimeapp.route('timeinterval/<int:id>')
@worktimeapp.param('id', 'ID des Timeintervalls')
class TimeIntervalWithIDOperations(Resource):
    @worktimeapp.marshal_with(timeinterval)
    #@secured
    def get(self, id):
        adm = Businesslogic()
        timeinterval = adm.get_timeinterval_by_id(id)
        return timeinterval

    @worktimeapp.marshal_with(timeinterval)
    #@secured
    def delete(self, id):
        adm = Businesslogic()
        timeinterval = adm.get_timeinterval_by_id(id)
        adm.delete_timeinterval(timeinterval)

    @worktimeapp.marshal_with(timeinterval)
    @worktimeapp.expect(timeinterval, validate=True)
    #@secured
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
    #@secured
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
    #@secured
    def post(self):
        adm = Businesslogic()
        proposal = BreakBO.from_dict(api.payload)
        if proposal is not None:
            p = adm.create_break(
                proposal.get_start(),
                proposal.get_end(),
                proposal.get_start_event(),
                proposal.get_end_event(),
                proposal.get_type(),
            )
        return p

    @worktimeapp.marshal_list_with(breaks)
    #@secured
    def get(self):
        adm = Businesslogic()
        breaks = adm.get_all_breaks()
        return breaks

@worktimeapp.route('break/<int:id>')
@worktimeapp.param('id', 'ID der Break')
class BreakWithIDOperations(Resource):
    @worktimeapp.marshal_with(breaks)
    #@secured
    def get(self, id):
        adm = Businesslogic()
        breaks = adm.get_break_by_id(id)
        return breaks

    @worktimeapp.marshal_with(breaks)
    #@secured
    def delete(self, id):
        adm = Businesslogic()
        breaks = adm.get_break_by_id(id)
        adm.delete_break(breaks)

    @worktimeapp.marshal_with(breaks)
    @worktimeapp.expect(breaks, validate=True)
    #@secured
    def put(self, id):
        adm = Businesslogic()
        p = BreakBO.from_dict(api.payload)

        if p is not None:
            p.set_id(id)
            adm.save_break(p)
            return p, 200
        else:
            return '', 500

# @worktimeapp.route('breakdate/<DateTime:start>')
# @worktimeapp.param('start', 'Start von Break')
# class FindBreakByDate(Resource):
#     @worktimeapp.marshal_with(breaks)
#     #@secured
#     def get(self, start):
#         adm = Businesslogic()
#         breaks = adm.get_breaks_by_date(start)
#         return breaks

# @worktimeapp.route('breakperiod/<date:start>/<date:end>')
# @worktimeapp.param('start', 'Start von Break', 'end', 'Ende von Break')
# class FindBreakByTimePeriod(Resource):
#     @worktimeapp.marshal_with(breaks)
#     #@secured
#     def get(self, start, end):
#         adm = Businesslogic()
#         breaks = adm.get_breaks_by_time_period(start, end)
#         return breaks

"""
Illness
"""
@worktimeapp.route('/illness')
class IllnessOperations(Resource):
    @worktimeapp.marshal_with(illness)
    @worktimeapp.expect(illness)
    #@secured
    def post(self):
        adm = Businesslogic()
        proposal = IllnessBO.from_dict(api.payload)
        if proposal is not None:
            p = adm.create_illness(
                proposal.get_start(),
                proposal.get_end(),
                proposal.get_start_event(),
                proposal.get_end_event(),
                proposal.get_type(),
            )
        return p

    @worktimeapp.marshal_list_with(illness)
    #@secured
    def get(self):
        adm = Businesslogic()
        illness = adm.get_all_illnesses()
        return illness

@worktimeapp.route('illness/<int:id>')
@worktimeapp.param('id', 'ID der Illness')
class IllnessWithIDOperations(Resource):
    @worktimeapp.marshal_with(illness)
    #@secured
    def get(self, id):
        adm = Businesslogic()
        illness = adm.get_illness_by_id(id)
        return illness

    @worktimeapp.marshal_with(illness)
    #@secured
    def delete(self, id):
        adm = Businesslogic()
        illness = adm.get_illness_by_id(id)
        adm.delete_illness(illness)

    @worktimeapp.marshal_with(illness)
    @worktimeapp.expect(illness, validate=True)
    #@secured
    def put(self, id):
        adm = Businesslogic()
        p = BreakBO.from_dict(api.payload)

        if p is not None:
            p.set_id(id)
            adm.save_illness(p)
            return p, 200
        else:
            return '', 500

# @worktimeapp.route('illnessdate/<date:start>')
# @worktimeapp.param('start', 'Start von Illness')
# class FindIllnessByDate(Resource):
#     @worktimeapp.marshal_with(illness)
#     #@secured
#     def get(self, start):
#         adm = Businesslogic()
#         illness = adm.get_illnesses_by_date(start)
#         return illness

# @worktimeapp.route('illnessperiod/<date:start>/<date:end>')
# @worktimeapp.param('start', 'Start von Illness', 'end', 'Ende von Illness')
# class FindIllnessByTimePeriod(Resource):
#     @worktimeapp.marshal_with(illness)
#     #@secured
#     def get(self, start, end):
#         adm = Businesslogic()
#         illness = adm.get_illnesses_by_time_period(start, end)
#         return illness

"""
FlexDay
"""
@worktimeapp.route('/flexday')
class BreakOperations(Resource):
    @worktimeapp.marshal_with(flexday)
    @worktimeapp.expect(flexday)
    #@secured
    def post(self):
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

    @worktimeapp.marshal_list_with(flexday)
    #@secured
    def get(self):
        adm = Businesslogic()
        flexday = adm.get_all_flex_days()
        return flexday

@worktimeapp.route('flexday/<int:id>')
@worktimeapp.param('id', 'ID der FlexDay')
class BreakWithIDOperations(Resource):
    @worktimeapp.marshal_with(flexday)
    #@secured
    def get(self, id):
        adm = Businesslogic()
        flexday = adm.get_flex_day_by_id(id)
        return flexday

    @worktimeapp.marshal_with(flexday)
    #@secured
    def delete(self, id):
        adm = Businesslogic()
        flexday = adm.get_flex_day_by_id(id)
        adm.delete_flex_day(flexday)

    @worktimeapp.marshal_with(flexday)
    @worktimeapp.expect(flexday, validate=True)
    #@secured
    def put(self, id):
        adm = Businesslogic()
        p = FlexDayBO.from_dict(api.payload)

        if p is not None:
            p.set_id(id)
            adm.save_flex_day(p)
            return p, 200
        else:
            return '', 500

# @worktimeapp.route('flexdaydate/<DateTime:start>')
# @worktimeapp.param('start', 'Start von FlexDay')
# class FindBreakByDate(Resource):
#     @worktimeapp.marshal_with(flexday)
#     #@secured
#     def get(self, start):
#         adm = Businesslogic()
#         flexday = adm.get_flex_days_by_date(start)
#         return flexday

# @worktimeapp.route('flexdayperiod/<date:start>/<date:end>')
# @worktimeapp.param('start', 'Start von FlexDay', 'end', 'Ende von Flexday')
# class FindBreakByTimePeriod(Resource):
#     @worktimeapp.marshal_with(flexday)
#     #@secured
#     def get(self, start, end):
#         adm = Businesslogic()
#         flexday = adm.get_flex_days_by_time_period(start, end)
#         return flexday

"""
ProjectDuration
"""
@worktimeapp.route('/projectduration')
class ProjectDurationOperations(Resource):
    @worktimeapp.marshal_with(projectduration)
    @worktimeapp.expect(projectduration)
    #@secured
    def post(self):
        adm = Businesslogic()
        proposal = ProjectDurationBO.from_dict(api.payload)
        if proposal is not None:
            p = adm.create_project_duration(
                proposal.get_start(),
                proposal.get_end(),
                proposal.get_start_event(),
                proposal.get_end_event(),
                proposal.get_type(),
                proposal.get_project_id()
            )
        return p

    @worktimeapp.marshal_list_with(projectduration)
    #@secured
    def get(self):
        adm = Businesslogic()
        projectduration = adm.get_all_project_durations()
        return projectduration

@worktimeapp.route('projectduration/<int:id>')
@worktimeapp.param('id', 'ID der ProjectDuration')
class ProjecDurationWithIDOperations(Resource):
    @worktimeapp.marshal_with(projectduration)
    #@secured
    def get(self, id):
        adm = Businesslogic()
        projectduration = adm.get_project_duration_by_id(id)
        return projectduration

    @worktimeapp.marshal_with(projectduration)
    #@secured
    def delete(self, id):
        adm = Businesslogic()
        projectduration = adm.get_project_duration_by_id(id)
        adm.delete_project_duration(projectduration)

    @worktimeapp.marshal_with(projectduration)
    @worktimeapp.expect(projectduration, validate=True)
    #@secured
    def put(self, id):
        adm = Businesslogic()
        p = ProjectDurationBO.from_dict(api.payload)

        if p is not None:
            p.set_id(id)
            adm.save_project_duration(p)
            return p, 200
        else:
            return '', 500

# @worktimeapp.route('projectdurationdate/<date:start>')
# @worktimeapp.param('start', 'Start von ProjectDuration')
# class FindProjectDurationByDate(Resource):
#     @worktimeapp.marshal_with(projectduration)
#     #@secured
#     def get(self, start):
#         adm = Businesslogic()
#         projectduration = adm.get_project_durations_by_date(start)
#         return projectduration

# @worktimeapp.route('projectdurationperiod/<date:start>/<date:end>')
# @worktimeapp.param('start', 'Start von ProjectDuration', 'end', 'Ende von ProjectDuration')
# class FindProjectDurationByTimePeriod(Resource):
#     @worktimeapp.marshal_with(projectduration)
#     #@secured
#     def get(self, start, end):
#         adm = Businesslogic()
#         projectduration = adm.get_project_durations_by_time_period(start, end)
#         return projectduration

@worktimeapp.route('projectdurationproject/<int:projectid>')
@worktimeapp.param('id', 'Id von Project')
class FindProjectDurationByProjectId(Resource):
    @worktimeapp.marshal_with(projectduration)
    #@secured
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
    #@secured
    def post(self):
        adm = Businesslogic()
        proposal = ProjectWorkBO.from_dict(api.payload)
        if proposal is not None:
            p = adm.create_project_work(
                proposal.get_start(),
                proposal.get_end(),
                proposal.get_start_event(),
                proposal.get_end_event(),
                proposal.get_type(),
                proposal.get_activity_id()
            )
        return p

    @worktimeapp.marshal_list_with(projectwork)
    #@secured
    def get(self):
        adm = Businesslogic()
        projectwork = adm.get_all_project_works()
        return projectwork

@worktimeapp.route('projectwork/<int:id>')
@worktimeapp.param('id', 'ID der ProjectWork')
class ProjecWorkWithIDOperations(Resource):
    @worktimeapp.marshal_with(projectwork)
    #@secured
    def get(self, id):
        adm = Businesslogic()
        projectwork = adm.get_project_work_by_id(id)
        return projectwork

    @worktimeapp.marshal_with(projectwork)
    #@secured
    def delete(self, id):
        adm = Businesslogic()
        projectwork = adm.get_project_work_by_id(id)
        adm.delete_project_work(projectwork)

    @worktimeapp.marshal_with(projectwork)
    @worktimeapp.expect(projectwork, validate=True)
    #@secured
    def put(self, id):
        adm = Businesslogic()
        p = ProjectWorkBO.from_dict(api.payload)

        if p is not None:
            p.set_id(id)
            adm.save_project_work(p)
            return p, 200
        else:
            return '', 500

# @worktimeapp.route('projectworkdate/<date:start>')
# @worktimeapp.param('start', 'Start von ProjectWork')
# class FindProjectWorkByDate(Resource):
#     @worktimeapp.marshal_with(projectwork)
#     #@secured
#     def get(self, start):
#         adm = Businesslogic()
#         projectwork = adm.get_project_works_by_date(start)
#         return projectwork

# @worktimeapp.route('projectworkperiod/<date:start>/<date:end>')
# @worktimeapp.param('start', 'Start von ProjectWork', 'end', 'Ende von ProjectWork')
# class FindProjectWorkByTimePeriod(Resource):
#     @worktimeapp.marshal_with(projectwork)
#     #@secured
#     def get(self, start, end):
#         adm = Businesslogic()
#         projectwork = adm.get_project_works_by_time_period(start, end)
#         return projectwork

@worktimeapp.route('projectworkactivity/<int:activitytid>')
@worktimeapp.param('id', 'Id von Project')
class FindProjectWorkByProjectId(Resource):
    @worktimeapp.marshal_with(projectwork)
    #@secured
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
    #@secured
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
                None
            )
        return p

    @worktimeapp.marshal_list_with(vacation)
    #@secured
    def get(self):
        adm = Businesslogic()
        vacation = adm.get_all_vacations()
        return vacation

@worktimeapp.route('vacation/<int:id>')
@worktimeapp.param('id', 'ID der Vacation')
class VacationWithIDOperations(Resource):
    @worktimeapp.marshal_with(vacation)
    #@secured
    def get(self, id):
        adm = Businesslogic()
        vacation = adm.get_vacation_by_id(id)
        return vacation

    @worktimeapp.marshal_with(vacation)
    #@secured
    def delete(self, id):
        adm = Businesslogic()
        vacation = adm.get_vacation_by_id(id)
        adm.delete_vacation(vacation)

    @worktimeapp.marshal_with(vacation)
    @worktimeapp.expect(vacation, validate=True)
    #@secured
    def put(self, id):
        adm = Businesslogic()
        p = VacationBO.from_dict(api.payload)

        if p is not None:
            p.set_id(id)
            adm.save_vacation(p)
            return p, 200
        else:
            return '', 500

# @worktimeapp.route('vacationdate/<date:start>')
# @worktimeapp.param('start', 'Start von Vacation')
# class FindVacationByDate(Resource):
#     @worktimeapp.marshal_with(vacation)
#     #@secured
#     def get(self, start):
#         adm = Businesslogic()
#         vacation = adm.get_vacations_by_date(start)
#         return vacation

# @worktimeapp.route('vacationperiod/<date:start>/<date:end>')
# @worktimeapp.param('start', 'Start von Vacation', 'end', 'Ende von Vacation')
# class FindVacationByTimePeriod(Resource):
#     @worktimeapp.marshal_with(vacation)
#     #@secured
#     def get(self, start, end):
#         adm = Businesslogic()
#         vacation = adm.get_vacations_by_time_period(start, end)
#         return vacation

"""
Work
"""
@worktimeapp.route('/work')
class WorkOperations(Resource):
    @worktimeapp.marshal_with(work)
    @worktimeapp.expect(work)
    #@secured
    def post(self):
        adm = Businesslogic()
        proposal = WorkBO.from_dict(api.payload)
        if proposal is not None:
            p = adm.create_work(
                proposal.get_start(),
                proposal.get_end(),
                proposal.get_start_event(),
                proposal.get_end_event(),
                proposal.get_type(),
            )
        return p

    @worktimeapp.marshal_list_with(work)
    #@secured
    def get(self):
        adm = Businesslogic()
        work = adm.get_all_works()
        return work

@worktimeapp.route('work/<int:id>')
@worktimeapp.param('id', 'ID der Work')
class WorkWithIDOperations(Resource):
    @worktimeapp.marshal_with(work)
    #@secured
    def get(self, id):
        adm = Businesslogic()
        work = adm.get_work_by_id(id)
        return work

    @worktimeapp.marshal_with(work)
    #@secured
    def delete(self, id):
        adm = Businesslogic()
        work = adm.get_work_by_id(id)
        adm.delete_work(work)

    @worktimeapp.marshal_with(work)
    @worktimeapp.expect(work, validate=True)
    #@secured
    def put(self, id):
        adm = Businesslogic()
        p = WorkBO.from_dict(api.payload)

        if p is not None:
            p.set_id(id)
            adm.save_work(p)
            return p, 200
        else:
            return '', 500

# @worktimeapp.route('workdate/<date:start>')
# @worktimeapp.param('start', 'Start von Work')
# class FindWorkByDate(Resource):
#     @worktimeapp.marshal_with(work)
#     #@secured
#     def get(self, start):
#         adm = Businesslogic()
#         work = adm.get_works_by_date(start)
#         return work

# @worktimeapp.route('vacationperiod/<date:start>/<date:end>')
# @worktimeapp.param('start', 'Start von Work', 'end', 'Ende von Work')
# class FindWorkByTimePeriod(Resource):
#     @worktimeapp.marshal_with(work)
#     #@secured
#     def get(self, start, end):
#         adm = Businesslogic()
#         work = adm.get_works_by_time_period(start, end)
#         return work

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
