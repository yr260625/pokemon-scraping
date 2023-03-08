"""ポケモン図鑑ユースケース"""
import time
from typing import Final
from src.pokedex.model.pokemon_spec import PokemonSpec
from src.pokedex.repository.pokemon_spec import IPokemonSpecRepository
from src.pokedex.model.pokemon_specifications import PokemonSpecifications


class PokedexUsecases():
    """ポケモン図鑑に関するユースケース
    """

    def __init__(self, repository: IPokemonSpecRepository):
        """コンストラクタ

        Args:
            repository (IPokemonSpecRepository): ポケモン諸元値リポジトリ
        """
        self.__repository: Final[IPokemonSpecRepository] = repository

    def complete(self) -> PokemonSpecifications:
        """ポケモン諸元値全収集
        """
        print('ポケモン諸元値収集中...')
        pokemon_specifications = PokemonSpecifications([])
        pokemon_id = 1
        while pokemon_specifications.can_add():
            pokemon_spec: PokemonSpec = self.__repository.fetch_by_id(pokemon_id)
            pokemon_specifications: PokemonSpecifications = pokemon_specifications.add(pokemon_spec)
            pokemon_id += 1
            time.sleep(0.5)
        return pokemon_specifications
