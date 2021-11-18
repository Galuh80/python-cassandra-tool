from cassandra.cluster import Cluster

class Connector:

    # Cassandra Connection
    def createConnection():
        session = Cluster(['127.0.0.1'])
        if session is not None:
            return session.connect('pln')
        else:
            print("Connection failed")