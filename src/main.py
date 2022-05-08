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
from server.BankAdministration import BankAdministration
from server.bo.Customer import Customer
from server.bo.Account import Account
from server.bo.Transaction import Transaction

# Außerdem nutzen wir einen selbstgeschriebenen Decorator, der die Authentifikation übernimmt
# from SecurityDecorator import secured

"""
Instanzieren von Flask. Am Ende dieser Datei erfolgt dann erst der 'Start' von Flask.
"""
app = Flask(__name__)

"""
Alle Ressourcen mit dem Präfix /bank für **Cross-Origin Resource Sharing** (CORS) freigeben.
Diese eine Zeile setzt die Installation des Package flask-cors voraus. 

Sofern Frontend und Backend auf getrennte Domains/Rechnern deployed würden, wäre sogar eine Formulierung
wie etwa diese erforderlich:
CORS(app, resources={r"/bank/*": {"origins": "*"}})
Allerdings würde dies dann eine Missbrauch Tür und Tor öffnen, so dass es ratsamer wäre, nicht alle
"origins" zuzulassen, sondern diese explizit zu nennen. Weitere Infos siehe Doku zum Package flask-cors.
"""
CORS(app, resources=r'/bank/*')

"""
In dem folgenden Abschnitt bauen wir ein Modell auf, das die Datenstruktur beschreibt, 
auf deren Basis Clients und Server Daten austauschen. Grundlage hierfür ist das Package flask-restx.
"""
api = Api(app, version='1.0', title='BankBeispiel API',
    description='Eine rudimentäre Demo-API für doppelte Buchführung in Banken.')

"""Anlegen eines Namespace

Namespaces erlauben uns die Strukturierung von APIs. In diesem Fall fasst dieser Namespace alle
Bank-relevanten Operationen unter dem Präfix /bank zusammen. Eine alternative bzw. ergänzende Nutzung
von Namespace könnte etwa sein, unterschiedliche API-Version voneinander zu trennen, um etwa 
Abwärtskompatibilität (vgl. Lehrveranstaltungen zu Software Engineering) zu gewährleisten. Dies ließe
sich z.B. umsetzen durch /bank/v1, /bank/v2 usw."""
banking = api.namespace('bank', description='Funktionen des BankBeispiels')

"""Nachfolgend werden analog zu unseren BusinessObject-Klassen transferierbare Strukturen angelegt.

BusinessObject dient als Basisklasse, auf der die weiteren Strukturen Customer, Account und Transaction aufsetzen."""
bo = api.model('BusinessObject', {
    'id': fields.Integer(attribute='_id', description='Der Unique Identifier eines Business Object'),
})

"""Users, Customers, Accounts & Transactions sind BusinessObjects..."""
user = api.inherit('User', bo, {
    'name': fields.String(attribute='_name', description='Name eines Benutzers'),
    'email': fields.String(attribute='_email', description='E-Mail-Adresse eines Benutzers'),
    'user_id': fields.String(attribute='_user_id', description='Google User ID eines Benutzers')
})

customer = api.inherit('Customer', bo, {
    'first_name': fields.String(attribute='_first_name', description='Vorname eines Kunden'),
    'last_name': fields.String(attribute='_last_name', description='Nachname eines Kunden')
})

account = api.inherit('Account', bo, {
    'owner': fields.Integer(attribute='_owner', description='Unique Id des Kontoinhabers')
})

transaction = api.inherit('Transaction', bo, {
    'source_account': fields.Integer(attribute='_source_account', description='Unique Id des Quellkontos'),
    'target_account': fields.Integer(attribute='_target_account', description='Unique Id des Zielkontos'),
    'amount': fields.Float(attribute='_amount', description='Betrag bzw. Wert der Buchung')
})


@banking.route('/customers')
@banking.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class CustomerListOperations(Resource):
    @banking.marshal_list_with(customer)
    #@secured
    def get(self):
        """Auslesen aller Customer-Objekte.

        Sollten keine Customer-Objekte verfügbar sein, so wird eine leere Sequenz zurückgegeben."""
        adm = BankAdministration()
        customers = adm.get_all_customers()
        return customers

    @banking.marshal_with(customer, code=200)
    @banking.expect(customer)  # Wir erwarten ein Customer-Objekt von Client-Seite.
    #@secured
    def post(self):
        """Anlegen eines neuen Customer-Objekts.

        **ACHTUNG:** Wir fassen die vom Client gesendeten Daten als Vorschlag auf.
        So ist zum Beispiel die Vergabe der ID nicht Aufgabe des Clients.
        Selbst wenn der Client eine ID in dem Proposal vergeben sollte, so
        liegt es an der BankAdministration (Businesslogik), eine korrekte ID
        zu vergeben. *Das korrigierte Objekt wird schließlich zurückgegeben.*
        """
        adm = BankAdministration()

        proposal = Customer.from_dict(api.payload)

        """RATSCHLAG: Prüfen Sie stets die Referenzen auf valide Werte, bevor Sie diese verwenden!"""
        if proposal is not None:
            """ Wir verwenden lediglich Vor- und Nachnamen des Proposals für die Erzeugung
            eines Customer-Objekts. Das serverseitig erzeugte Objekt ist das maßgebliche und 
            wird auch dem Client zurückgegeben. 
            """
            c = adm.create_customer(proposal.get_first_name(), proposal.get_last_name())
            return c, 200
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500


@banking.route('/customers/<int:id>')
@banking.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@banking.param('id', 'Die ID des Customer-Objekts')
class CustomerOperations(Resource):
    @banking.marshal_with(customer)
    #@secured
    def get(self, id):
        """Auslesen eines bestimmten Customer-Objekts.

        Das auszulesende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = BankAdministration()
        cust = adm.get_customer_by_id(id)
        return cust

    #@secured
    def delete(self, id):
        """Löschen eines bestimmten Customer-Objekts.

        Das zu löschende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = BankAdministration()
        cust = adm.get_customer_by_id(id)
        adm.delete_customer(cust)
        return '', 200

    @banking.marshal_with(customer)
    @banking.expect(customer, validate=True)
    #@secured
    def put(self, id):
        """Update eines bestimmten Customer-Objekts.

        **ACHTUNG:** Relevante id ist die id, die mittels URI bereitgestellt und somit als Methodenparameter
        verwendet wird. Dieser Parameter überschreibt das ID-Attribut des im Payload der Anfrage übermittelten
        Customer-Objekts.
        """
        adm = BankAdministration()
        c = Customer.from_dict(api.payload)

        if c is not None:
            """Hierdurch wird die id des zu überschreibenden (vgl. Update) Customer-Objekts gesetzt.
            Siehe Hinweise oben.
            """
            c.set_id(id)
            adm.save_customer(c)
            return '', 200
        else:
            return '', 500

@banking.route('/customers-by-name/<string:lastname>')
@banking.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@banking.param('lastname', 'Der Nachname des Kunden')
class CustomersByNameOperations(Resource):
    @banking.marshal_with(customer)
    #@secured
    def get(self, lastname):
        """ Auslesen von Customer-Objekten, die durch den Nachnamen bestimmt werden.

        Die auszulesenden Objekte werden durch ```lastname``` in dem URI bestimmt.
        """
        adm = BankAdministration()
        cust = adm.get_customer_by_name(lastname)
        return cust


@banking.route('/accounts')
@banking.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class AccountListOperations(Resource):
    @banking.marshal_list_with(account)
    #@secured
    def get(self):
        """Auslesen aller Acount-Objekte.

        Sollten keine Account-Objekte verfügbar sein, so wird eine leere Sequenz zurückgegeben."""
        adm = BankAdministration()
        account_list = adm.get_all_accounts()
        return account_list


@banking.route('/accounts/<int:id>')
@banking.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@banking.param('id', 'Die ID des Account-Objekts')
class AccountOperations(Resource):
    @banking.marshal_with(account)
    #@secured
    def get(self, id):
        """Auslesen eines bestimmten Account-Objekts.

        Das auszulesende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = BankAdministration()
        acc = adm.get_account_by_id(id)
        return acc

    #@secured
    def delete(self, id):
        """Löschen eines bestimmten Account-Objekts.

        Das zu löschende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = BankAdministration()
        acc = adm.get_account_by_id(id)
        adm.delete_account(acc)
        return '', 200

    @banking.marshal_with(account)
    #@secured
    def put(self, id):
        """Update eines bestimmten Account-Objekts.

        **ACHTUNG:** Relevante id ist die id, die mittels URI bereitgestellt und somit als Methodenparameter
        verwendet wird. Dieser Parameter überschreibt das ID-Attribut des im Payload der Anfrage übermittelten
        Customer-Objekts.
        """
        adm = BankAdministration()
        a = Account.from_dict(api.payload)

        if a is not None:
            """Hierdurch wird die id des zu überschreibenden (vgl. Update) Account-Objekts gesetzt.
            Siehe Hinweise oben.
            """
            a.set_id(id)
            adm.save_account(a)
            return '', 200
        else:
            return '', 500


@banking.route('/customers/<int:id>/accounts')
@banking.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@banking.param('id', 'Die ID des Customer-Objekts')
class CustomerRelatedAccountOperations(Resource):
    @banking.marshal_with(account)
    #@secured
    def get(self, id):
        """Auslesen aller Acount-Objekte bzgl. eines bestimmten Customer-Objekts.

        Das Customer-Objekt dessen Accounts wir lesen möchten, wird durch die ```id``` in dem URI bestimmt.
        """
        adm = BankAdministration()
        # Zunächst benötigen wir den durch id gegebenen Customer.
        cust = adm.get_customer_by_id(id)

        # Haben wir eine brauchbare Referenz auf ein Customer-Objekt bekommen?
        if cust is not None:
            # Jetzt erst lesen wir die Konten des Customer aus.
            account_list = adm.get_accounts_of_customer(cust)
            return account_list
        else:
            return "Customer not found", 500

    @banking.marshal_with(account, code=201)
    #@secured
    def post(self, id):
        """Anlegen eines Kontos für einen gegebenen Customer.

        Das neu angelegte Konto wird als Ergebnis zurückgegeben.

        **Hinweis:** Unter der id muss ein Customer existieren, andernfalls wird Status Code 500 ausgegeben."""
        adm = BankAdministration()
        """Stelle fest, ob es unter der id einen Customer gibt. 
        Dies ist aus Gründen der referentiellen Integrität sinnvoll!
        """
        cust = adm.get_customer_by_id(id)

        if cust is not None:
            # Jetzt erst macht es Sinn, für den Customer ein neues Konto anzulegen und dieses zurückzugeben.
            result = adm.create_account_for_customer(cust)
            return result
        else:
            return "Customer unknown", 500


@banking.route('/accounts/<int:id>/balance')
@banking.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@banking.param('id', 'Die ID des Account-Objekts')
class AccountBalanceOperations(Resource):
    @banking.doc('Read balance of given account')
    #@secured
    def get(self, id):
        """Auslesen des Kontostands bzw. des Saldos eines bestimmten Account-Objekts.

        Das Account-Objekt dessen Saldo wir auslesen möchten, wird durch die ```id``` in dem URI bestimmt.
        """
        adm = BankAdministration()
        # Zunächst benötigen wir das durch id gegebene Konto.
        acc = adm.get_account_by_id(id)

        # Haben wir eine brauchbare Referenz auf ein Account-Objekt bekommen?
        if acc is not None:
            # Jetzt erst lesen wir den Saldo des Kontos aus.
            balance = adm.get_balance_of_account(acc)
            return balance
        else:
            return 0, 500


@banking.route('/cash-account')
@banking.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class CashAccountOperations(Resource):
    @banking.marshal_with(account)
    #@secured
    def get(self):
        """Auslesen des Kassenkontos (Cash Account) der Bank.

        Sollten keine Cash Account-Objekt verfügbar sein, so wird Response Status 500 zurückgegeben."""
        adm = BankAdministration()
        acc = adm.get_cash_account()
        if acc is not None:
            return acc
        else:
            return '', 500


@banking.route('/transactions')
@banking.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class TransactionListOperations(Resource):
    @banking.doc('Create a new transaction')
    @banking.marshal_with(transaction, code=201)
    @banking.expect(transaction)
    #@secured
    def post(self):
        """Erstellen einer neuen Buchung (Transaction-Objekt).

        **ACHTUNG:** Wir fassen die vom Client gesendeten Daten als Vorschlag auf.
        So ist zum Beispiel die Vergabe der ID nicht Aufgabe des Clients.
        Selbst wenn der Client eine ID in dem Proposal vergeben sollte, so
        liegt es an der BankAdministration (Businesslogik), eine korrekte ID
        zu vergeben. *Das korrigierte Objekt wird schließlich zurückgegeben.*
        """
        adm = BankAdministration()

        proposal = Transaction.from_dict(api.payload)

        """RATSCHLAG: Prüfen Sie stets die Referenzen auf valide Werte, bevor Sie diese verwenden!"""
        if proposal is not None:
            """ Wir verwenden lediglich Source, Target und Amount des Proposals für die Erzeugung
            eines Transaction-Objekts. Das serverseitig erzeugte Objekt ist das maßgebliche und 
            wird auch dem Client zurückgegeben. 
            """
            source = proposal.get_source_account()
            target = proposal.get_target_account()
            value = proposal.get_amount()
            result = adm.create_transaction_for(source, target, value)
            return result, 200
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500


@banking.route('/transactions/<int:id>')
@banking.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@banking.param('id', 'Die ID des Transaction-Objekts.')
class TransactionOperations(Resource):
    @banking.marshal_with(transaction)
    #@secured
    def get(self, id):
        """Auslesen eines bestimmten Transaction-Objekts.

        Das auszulesende Objekt wird durch die ```id``` in dem URI bestimmt.
        """
        adm = BankAdministration()
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
        adm = BankAdministration()
        trans = adm.get_transaction_by_id(id)

        if trans is not None:
            adm.delete_transaction(trans)
            return '', 200
        else:
            return '', 500  # Wenn unter id keine Transaction existiert.

    @banking.marshal_with(transaction)
    #@secured
    def put(self, id):
        """Update eines bestimmten Transaction-Objekts.

        **ACHTUNG:** Relevante id ist die id, die mittels URI bereitgestellt und somit als Methodenparameter
        verwendet wird. Dieser Parameter überschreibt das ID-Attribut des im Payload der Anfrage übermittelten
        Customer-Objekts.
        """
        adm = BankAdministration()
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


@banking.route('/account/<int:id>/debits')
@banking.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@banking.param('id', 'Die ID des Account-Objekts.')
class DebitOperations(Resource):
    @banking.marshal_with(transaction)
    #@secured
    def get(self, id):
        """Auslesen aller Abbuchungen bzgl. eines bestimmten Account-Objekts.

        **HINWEISE:** Debits sind Abbuchungen, also Transaction-Objekte, die das Konto *belasten*.
        Man könnte sie auch als Sollbuchungen auffassen (vgl. Rechnungswesen).
        Das Account-Objekt dessen Abbuchungen wir auslesen möchten, wird durch die ```id``` in dem URI bestimmt.
        """
        adm = BankAdministration()
        # Zunächst benötigen wir das durch id gegebene Account-Objekt.
        acc = adm.get_account_by_id(id)

        # Haben wir eine brauchbare Referenz auf ein Customer-Objekt bekommen?
        if acc is not None:
            # Jetzt erst lesen wir die Konten des Customer aus.
            debits = adm.get_debits_of_account(acc)
            return debits
        else:
            return "Account not found", 500

@banking.route('/account/<int:id>/credits')
@banking.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@banking.param('id', 'Die ID des Account-Objekts.')
class CreditOperations(Resource):
    @banking.marshal_with(transaction)
    #@secured
    def get(self, id):
        """Auslesen aller Guthabenbuchungen bzgl. eines bestimmten Account-Objekts.

        **HINWEISE:** Credits sind Guthabenbuchungen, also Transaction-Objekte, die den Kontostand *positiv erhöhen*.
        Man könnte sie auch als Habenbuchungen auffassen (vgl. Rechnungswesen).
        Das Account-Objekt dessen Guthabenbuchungen wir auslesen möchten, wird durch die ```id``` in dem URI bestimmt.
        """
        adm = BankAdministration()
        # Zunächst benötigen wir das durch id gegebene Account-Objekt.
        acc = adm.get_account_by_id(id)

        # Haben wir eine brauchbare Referenz auf ein Customer-Objekt bekommen?
        if acc is not None:
            # Jetzt erst lesen wir die Konten des Customer aus.
            credits = adm.get_credits_of_account(acc)
            return credits
        else:
            return "Account not found", 500



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

