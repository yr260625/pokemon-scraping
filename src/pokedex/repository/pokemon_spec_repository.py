from abc import ABCMeta, abstractmethod
from src.pokedex.model.pokemon_spec import PokemonSpec


class IPokemonSpecRepository(metaclass=ABCMeta):

    @abstractmethod
    def findById(self, id: int) -> PokemonSpec:
        raise NotImplementedError
