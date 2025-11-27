from database.DB_connect import DBConnect
from model.hub import Hub
from model.tratta import Tratta

class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    # TODO

    @staticmethod
    def get_tratte():
        cnx = DBConnect.get_connection()
        result = []
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT LEAST(s.id_hub_origine, s.id_hub_destinazione) AS id_hub1,
		                GREATEST(s.id_hub_origine, s.id_hub_destinazione) AS id_hub2,
		                SUM(s.valore_merce) AS somma_valore, COUNT(*) AS num_spedizioni
                        FROM spedizione s 
                        GROUP BY id_hub1, id_hub2
                        HAVING id_hub1 != id_hub2"""

        cursor.execute(query)
        for row in cursor:
            tratta = Tratta(_id_hub1=row['id_hub1'], _id_hub2=row['id_hub2'],
                            _somma_valore=row['somma_valore'], _num_spedizioni=row['num_spedizioni'])
            result.append(tratta)
        cursor.close()
        cnx.close()
        return result


    @staticmethod
    def get_hub():
        cnx = DBConnect.get_connection()
        result = []
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT *
                        FROM hub"""
        cursor.execute(query)
        for row in cursor:
            hub = Hub(id=row["id"], codice=row["codice"], nome=row["nome"], citta=row["citta"],
                      stato=row["stato"], latitudine=row["latitudine"], longitudine=row["longitudine"])
            result.append(hub)
        cursor.close()
        cnx.close()
        return result
