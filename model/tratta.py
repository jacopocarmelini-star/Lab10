from dataclasses import dataclass

@dataclass
class Tratta:
    _id_hub1 : int
    _id_hub2 : int
    _somma_valore : float
    _num_spedizioni : int

    @property
    def guadagno_medio(self) -> float:
        if self._num_spedizioni == 0:
            return 0.0

        return (self._somma_valore / self._num_spedizioni)


    def __eq__(self, other):
        return isinstance(other, Tratta) and self._id_hub1 == other._id_hub1 and self._id_hub2 == other._id_hub2

    def __str__(self):
        return f"Tratta {self._id_hub1}-{self._id_hub2} (Media: {self.guadagno_medio:.2f})"

    def __repr__(self):
        return f"Tratta({self._id_hub1}, {self._id_hub2})"

    def __hash__(self):
        return hash((self._id_hub1, self._id_hub2))
