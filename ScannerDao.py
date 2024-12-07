from MySqlDB import MySqlDB

class ScannerDao:
    def __init__(self):
        self.db = MySqlDB()
        self.insert_statement = "INSERT INTO " + self.db.get_table_name() + "\
        (domain, open_ports) VALUES ('{}', '{}')"
        self.select_statement = "SELECT ts,open_ports FROM "+ self.db.get_table_name() + " WHERE \
        domain = '{}' ORDER BY ts DESC LIMIT 10"

    def save_port_history(self, domain, open_ports):
        self.db.connect()
        query = self.insert_statement.format(domain, open_ports)
        print(query)
        self.db.insertQuery(query)
        self.db.close_connection()

    def get_port_history(self, domain):
        self.db.connect()
        query = self.select_statement.format(domain)
        cursor = self.db.executeQuery(query)
        history = {}
        for ts,open_ports in cursor:
            history[str(ts)] = open_ports
        cursor.close()
        self.db.close_connection()
        return history
