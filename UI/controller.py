import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_tratte(self, e):
        """
        Funzione che controlla prima se il valore del costo inserito sia valido (es. non deve essere una stringa) e poi
        popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Hub presenti
        * Numero di Tratte
        * Lista di Tratte che superano il costo indicato come soglia
        """
        # TODO
        treshold = self._view.guadagno_medio_minimo.value


        if not treshold:
            self._view.show_alert("Nessun guadagno minimo inserito")
            return
        try:
            minimo = float(treshold)
            self._model.costruisci_grafo(minimo)
            num_hub = self._model.get_num_nodes()
            num_tratte = self._model.get_num_edges()
            tratte = self._model.get_all_edges()

            self._view.lista_visualizzazione.controls.clear()
            self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di hub: {num_hub}"))
            self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di tratte: {num_tratte}"))

            counter = 0
            for u, v, peso in tratte:
                counter += 1
                self._view.lista_visualizzazione.controls.append(
                    ft.Text(f"{counter}) {u.nome} ({u.stato}) -> {v.nome} ({v.stato}) -- Guadagno medio per spedizione € {peso:.2f}")
                )
            self._view.update()

        except ValueError:
            self._view.show_alert("Inserisci guadagno minimo valido")
            return









