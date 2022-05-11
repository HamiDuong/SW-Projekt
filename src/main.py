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
api = Api(app, version='1.0', title='BankBeispiel API',
    description='Eine rudimentäre Demo-API für doppelte Buchführung in Banken.')

"""Anlegen eines Namespace

Namespaces erlauben uns die Strukturierung von APIs. In diesem Fall fasst dieser Namespace alle
Bank-relevanten Operationen unter dem Präfix /worktimeapp zusammen. Eine alternative bzw. ergänzende Nutzung
von Namespace könnte etwa sein, unterschiedliche API-Version voneinander zu trennen, um etwa 
Abwärtskompatibilität (vgl. Lehrveranstaltungen zu Software Engineering) zu gewährleisten. Dies ließe
sich z.B. umsetzen durch /worktimeapp/v1, /worktimeapp/v2 usw."""
worktimeapping = api.namespace('worktimeapp', description='Funktionen des BankBeispiels')

"""Nachfolgend werden analog zu unseren BusinessObject-Klassen transferierbare Strukturen angelegt.

BusinessObject dient als Basisklasse, auf der die weiteren Strukturen User, Account und Transaction aufsetzen."""
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

##Tatsächliche Funktionen beginnen ab hier.


@worktimeapp.route('/user')
@worktimeapping.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class UserListOperations(Resource):
    @worktimeapping.marshal_list_with(user)
    #@secured
    def get(self):
        """Auslesen aller User-Objekte.

        Sollten keine User-Objekte verfügbar sein, so wird eine leere Sequenz zurückgegeben."""
        adm = Businesslogic()
        user = adm.get_all_users()
        return user

    @worktimeapping.marshal_with(user, code=200)
    @worktimeapping.expect(user)  # Wir erwarten ein User-Objekt von Client-Seite.
    #@secured
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
            c = adm.create_user(proposal.get_first_name(), proposal.get_last_name(), proposal.get_mail_adress(), proposal.get_user_name() )
            return c, 200
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500


@worktimeapping.route('/users/<string:mail_adress>')
@worktimeapping.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@worktimeapping.param('mail_adress', 'Die E-Mail-Adresse eines Benutzers')
class UserOperations(Resource):
    @worktimeapping.marshal_with(user)
    #@secured
    def get(self, id):
        """Auslesen eines bestimmten User-Objekts.

        Das auszulesende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        cust = adm.get_user_by_mail_adress(id)
        return cust

    #@secured
    def delete(self, id):
        """Löschen eines bestimmten User-Objekts.

        Das zu löschende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        cust = adm.get_user_by_id(id)
        adm.delete_user(cust)
        return '', 200

    @worktimeapping.marshal_with(user)
    @worktimeapping.expect(user, validate=True)
    #@secured
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


@worktimeapping.route('/users-by-name/<string:user_name>')
@worktimeapping.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@worktimeapping.param('user_name', 'Der User Name des Benutzers')
class UsersByNameOperations(Resource):
    @worktimeapping.marshal_with(user)
    #@secured
    def get(self, user_name):
        """ Auslesen von User-Objekten, die durch den User Name bestimmt werden.

        Die auszulesenden Objekte werden durch ```user_name``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        cust = adm.get_user_by_user_name(user_name)
        return cust


@worktimeapping.route('/users-by-name/<string:last_name>')
@worktimeapping.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@worktimeapping.param('last_name', 'Der Nachname des Benutzers')
class UsersByNameOperations(Resource):
    @worktimeapping.marshal_with(user)
    #@secured
    def get(self, last_name):
        """ Auslesen von User-Objekten, die durch den Nachnamen bestimmt werden.

        Die auszulesenden Objekte werden durch ```last_name``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        cust = adm.get_user_by_last_name(last_name)
        return cust




@worktimeapping.route('/users/<string:mail_adress>')
@worktimeapping.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@worktimeapping.param('id', 'Die E-Mail-Adresse eines Benutzers')
class UserRelatedAccountOperations(Resource):
    @worktimeapping.marshal_with(user)
    #@secured
    def get(self, mail_adress):
        """Auslesen von User-Objekten, die durch die E-Mail_Adresse bestimmt werden.

        Die auszulesenden Objekte werden durch ```mail_adress``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        cust = adm.get_user_by_mail_adress(mail_adress)
        return cust       



@worktimeapping.route('/users/<string:user_name>')
@worktimeapping.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@worktimeapping.param('id', 'Die E-Mail-Adresse eines Benutzers')
class UserRelatedAccountOperations(Resource):
    @worktimeapping.marshal_with(user)
    #@secured
    def get(self, user_name):
        """Auslesen von User-Objekten, die durch den User Namen bestimmt werden.

        Die auszulesenden Objekte werden durch ```user_name``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        cust = adm.get_user_by_user_name(user_name)
        return cust    




@worktimeapp.route('/WorkTimeAccount')
@worktimeapping.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class WorkTimeAccountListOperations(Resource):
    @worktimeapping.marshal_list_with(Worktimeaccount)
    #@secured
    def get(self):
        """Auslesen aller WorkTimeAccount-Objekte.

        Sollten keine User-Objekte verfügbar sein, so wird eine leere Sequenz zurückgegeben."""
        adm = Businesslogic()
        worktimeaccounts = adm.get_all_worktimeaccounts()
        return worktimeaccounts

    @worktimeapping.marshal_with(Worktimeaccount, code=200)
    @worktimeapping.expect(Worktimeaccount)  # Wir erwarten ein Worktimeaccount-Objekt von Client-Seite.
    #@secured
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


@worktimeapping.route('/worktimeaccounts/<int:user_id>')
@worktimeapping.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@worktimeapping.param('user_id', 'Die User-ID eines Benutzers')
class WorktimeaccountRelatedAccountOperations(Resource):
    @worktimeapping.marshal_with(Worktimeaccount)
    #@secured
    def get(self, user_id):
        """Auslesen von User-Objekten, die durch den User Namen bestimmt werden.

        Die auszulesenden Objekte werden durch ```user_id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        cust = adm.get_user_by_user_name(user_id)
        return cust                



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

