from database.DB_connect import DBConnect

class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    # TODO

    @staticmethod
    def get_tratte():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT LEAST(s.id_hub_origine, s.id_hub_destinazione) AS id_hub1,
		                GREATEST(s.id_hub_origine, s.id_hub_destinazione) AS id_hub2,
		                SUM(s.valore_merce) AS somma_valore, COUNT(*) AS num_spedizioni
                        FROM spedizione s 
                        GROUP BY id_hub1, id_hub2
                        HAVING id_hub1 != id_hub2"""

        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        cnx.close()
        return results

    @staticmethod
    def get_hub():
        cnx =DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT *
                    FROM hub"""
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        cnx.close()
        return results
