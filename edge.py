from dataclasses import dataclass


@dataclass(frozen=True)
class Edge:
    cost: int

    def __hash__(self):
        return hash(self.cost)

    def __eq__(self, other):
        return isinstance(other, Edge) and self.cost == other.cost

    def __lt__(self, other):
        return isinstance(other, Edge) and self.cost < other.cost

    def __str__(self):
        return self.cost

    def __unicode__(self):
        return self.__str__

    def __repr__(self):
        return self.__str__
