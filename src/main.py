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

"""Users, Users, Accounts & Transactions sind BusinessObjects..."""
user = api.inherit('User', bo, {
    'name': fields.String(attribute='_name', description='Name eines Benutzers'),
    'email': fields.String(attribute='_email', description='E-Mail-Adresse eines Benutzers'),
    'user_id': fields.String(attribute='_user_id', description='Google User ID eines Benutzers')
})

"""Buisnessobject"""
Businessobject = api.inherit('Object', bo, {
    'Attribut1': fields.DatenFormat(attribute='_attribut1', description='Erklärung des Attributs'),
    'Attribut2': fields.String(attribute='_attribut2', description='Erklärung des Attributs'),
    'Attribut_mit_mehreren_worten': fields.String(attribute='_attribut_mit_mehreren_worten', description='Erklärung des Attributs')
})

##Tatsächliche Funktionen beginnen ab hier.


@worktimeapp.route('/projects')
@worktimeapping.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class UserListOperations(Resource):
    @worktimeapping.marshal_list_with(user)
    #@secured
    def get(self):
        """Auslesen aller User-Objekte.

        Sollten keine User-Objekte verfügbar sein, so wird eine leere Sequenz zurückgegeben."""
        adm = Businesslogic()
        users = adm.get_all_users()
        return users

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
        adm = businesslogic()

        proposal = User.from_dict(api.payload)

        """RATSCHLAG: Prüfen Sie stets die Referenzen auf valide Werte, bevor Sie diese verwenden!"""
        if proposal is not None:
            """ Wir verwenden lediglich Vor- und Nachnamen des Proposals für die Erzeugung
            eines User-Objekts. Das serverseitig erzeugte Objekt ist das maßgebliche und 
            wird auch dem Client zurückgegeben. 
            """
            c = adm.create_user(proposal.get_first_name(), proposal.get_last_name())
            return c, 200
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500


@worktimeapping.route('/users/<int:id>')
@worktimeapping.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@worktimeapping.param('id', 'Die ID des User-Objekts')
class UserOperations(Resource):
    @worktimeapping.marshal_with(user)
    #@secured
    def get(self, id):
        """Auslesen eines bestimmten User-Objekts.

        Das auszulesende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        cust = adm.get_user_by_id(id)
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

@worktimeapping.route('/users-by-name/<string:lastname>')
@worktimeapping.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@worktimeapping.param('lastname', 'Der Nachname des Kunden')
class UsersByNameOperations(Resource):
    @worktimeapping.marshal_with(user)
    #@secured
    def get(self, lastname):
        """ Auslesen von User-Objekten, die durch den Nachnamen bestimmt werden.

        Die auszulesenden Objekte werden durch ```lastname``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        cust = adm.get_user_by_name(lastname)
        return cust





@worktimeapping.route('/users/<int:id>/accounts')
@worktimeapping.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@worktimeapping.param('id', 'Die ID des User-Objekts')
class UserRelatedAccountOperations(Resource):
    @worktimeapping.marshal_with(account)
    #@secured
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

    @worktimeapping.marshal_with(account, code=201)
    #@secured
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

#BeispielFunktion für Bedingungen

@worktimeapping.route('/transactions/<int:id>')
@worktimeapping.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@worktimeapping.param('id', 'Die ID des Transaction-Objekts.')
class TransactionOperations(Resource):
    @worktimeapping.marshal_with(transaction)
    #@secured
    def get(self, id):
        """Auslesen eines bestimmten Transaction-Objekts.

        Das auszulesende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        trans = adm.get_transaction_by_id(id)

        if trans is not None:
            return trans
        else:
            return '', 500  # Wenn es keine Transaktion unter id gibt.

    #@secured
    def delete(self, id):
        """Löschen eines bestimmten Transaction-Objekts.

        Das zu löschende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = Businesslogic()
        trans = adm.get_transaction_by_id(id)

        if trans is not None:
            adm.delete_transaction(trans)
            return '', 200
        else:
            return '', 500  # Wenn unter id keine Transaction existiert.

    @worktimeapping.marshal_with(transaction)
    #@secured
    def put(self, id):
        """Update eines bestimmten Transaction-Objekts.

        **ACHTUNG:** Relevante id ist die id, die mittels URI bereitgestellt und somit als Methodenparameter
        verwendet wird. Dieser Parameter überschreibt das ID-Attribut des im Payload der Anfrage übermittelten
        User-Objekts.
        """
        adm = Businesslogic()
        t = Transaction.from_dict(api.payload)

        if t is not None:
            """Hierdurch wird die id des zu überschreibenden (vgl. Update) Transaction-Objekts gesetzt.
            Siehe Hinweise oben.
            """
            t.set_id(id)
            adm.save_transaction(t)
            return '', 200
        else:
            return '', 500




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

