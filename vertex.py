from dataclasses import dataclass
from typing import TypeVar, Generic

T = TypeVar("T")


@dataclass(frozen=True)
class Vertex(Generic[T]):
    value: T

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return isinstance(other, Vertex) and self.value == other.value

    def __str__(self):
        return self.value

    def __unicode__(self):
        return self.__str__

    def __repr__(self):
        return self.__str__
