from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()

        self._all_hubs = []
        self._tratte_valide = []

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """
        # TODO
        self.G.clear()
        self._all_hubs.clear()
        self._tratte_valide.clear()

        self._all_hubs = DAO.get_hub()
        self.G.add_nodes_from(self._all_hubs)
        tratte = DAO.get_tratte()

        for tratta in tratte:
            id_hub1 = tratta['id_hub1']
            id_hub2 = tratta['id_hub2']
            somma_valore = tratta['somma_valore']
            num_spedizioni = tratta['num_spedizioni']
            guadagno_medio = somma_valore / num_spedizioni

            u = None
            v = None

            for hub in self._all_hubs:
                if hub.id == id_hub1:
                    u = hub
                    break
            for hub in self._all_hubs:
                if hub.id == id_hub2:
                    v = hub
                    break

            if guadagno_medio >= threshold:
                self.G.add_edge(u,v, weight=guadagno_medio)
                self._tratte_valide.append((u, v, guadagno_medio))


    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        # TODO
        return self.G.number_of_edges()

    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        # TODO
        return self.G.number_of_nodes()

    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        # TODO
        return self._tratte_valide

