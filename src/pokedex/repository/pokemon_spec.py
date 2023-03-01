"""ポケモン諸元値リポジトリーインターフェース"""
from abc import ABCMeta, abstractmethod
from src.pokedex.model.pokemon_spec import PokemonSpec


class IPokemonSpecRepository(metaclass=ABCMeta):

    """ポケモンの諸元値を取得、保持するリポジトリーのインターフェース
    """

    @abstractmethod
    def fetch_by_id(self, pokemon_id: int) -> PokemonSpec:
        """ポケモン諸元値取得
        """
        raise NotImplementedError
