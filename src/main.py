
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
from SecurityDecorator import secured


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
    'name': fields.String(attribute='_name', description='Der Name des Projekts'),
    'capacity': fields.Float(attribute='_capacity', description='Die Kapazität eines Projekts'),
    'project_id': fields.Integer(attribute='_project_id', description='Die ID eines Projekts'),
    'duration': fields.Float(attribute='_duration', description='Die Dauer einer Aktivität')

})

'''Event'''
event = api.inherit('Event', bo, {
    'event_id': fields.Integer(attribute='_event_id', description='Die ID des Events'),
    'time': fields.Float(attribute='_time', description='Der Event-Zeitpunkt'),
    'event_booking_id': fields.Integer(attribute='_event_booking_id', description='Die ID der Buchung')
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
        cust = adm.get_user_by_mail_adress(mail_adress)
        return cust


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
        adm = businesslogic()

        proposal = User.from_dict(api.payload)

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
        c = User.from_dict(api.payload)

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
    @worktimeapp.marshal_with(account)
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

    @worktimeapp.marshal_with(account, code=201)
    # #@secured
    def post(self, id):
        """Anlegen eines Kontos für einen gegebenen User.

        Das neu angelegte Konto wird als Ergebnis zurückgegeben.

        **Hinweis:** Unter der id muss ein User existieren, andernfalls wird Status Code 500 ausgegeben."""
        adm = Businesslogic()
        """Stelle fest, ob es unter der id einen User gibt. 
        Dies ist aus Gründen der referentiellen Integrität sinnvoll!
        """
        cust = adm.get_user_by_id(id)

        if cust is not None:
            # Jetzt erst macht es Sinn, für den User ein neues Konto anzulegen und dieses zurückzugeben.
            result = adm.create_account_for_user(cust)
            return result
        else:
            return "User unknown", 500


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
                proposal.get_user_id()
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


@worktimeapp.route('/project/<str:name>')
@worktimeapp.param('name', 'Der Name des Projekts')
class ProjectWithSTRINGOperations(Resource):
    @worktimeapp.marshal_with(project)
    # @secured
    def get(self, name):
        adm = Businesslogic()
        activity = adm.get_by_project_name(name)
        return activity


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
                proposal.get_project_id(),
                proposal.get_duration()
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


@worktimeapp.route('/activity/<str:name>')
@worktimeapp.param('name', 'Der Name der Aktivitaet')
class ActivityWithSTRINGOperations(Resource):
    @worktimeapp.marshal_with(activity)
    # @secured
    def get(self, name):
        adm = Businesslogic()
        activity = adm.get_by_name(name)
        return activity


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
    # @secured
    def get(self, event_booking_id):
        """ Auslesen von Event-Objekten, die durch den Nachnamen bestimmt werden.

        Die auszulesenden Objekte werden durch ```event_booking_id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        event = adm.get_event_by_name(event_booking_id)
        return event


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
