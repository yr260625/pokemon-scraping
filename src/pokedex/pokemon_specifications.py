"""ポケモン諸元値コレクション"""
import json
import time

from typing import Final, List, Dict
from src.pokedex.model.pokemon_spec import PokemonSpec
from src.pokedex.repository.pokemon_spec import IPokemonSpecRepository


class PokemonSpecifications():
    """ポケモン諸元値の一覧を保持、収集するコレクションクラス。
    """

    __MIN_POKEMON_NUMBER: Final[int] = 1
    __MAX_POKEMON_NUMBER: Final[int] = 1008
    __collection: Final[List[PokemonSpec]] = []

    def __init__(self, repository: IPokemonSpecRepository):
        """コンストラクタ

        Args:
            repository (IPokemonSpecRepository): ポケモン諸元値リポジトリ
        """
        self.repository: IPokemonSpecRepository = repository

    def fetch_all(self):
        """ポケモン諸元値を全取得
        """
        for pokemon_id in range(self.__MIN_POKEMON_NUMBER, self.__MAX_POKEMON_NUMBER + 1):
            pokemon_spec: PokemonSpec = self.repository.fetch_by_id(pokemon_id)
            self.__collection.append(pokemon_spec)
            time.sleep(0.5)

    def to_json(self) -> str:
        """全ポケモン諸元値をJSONに変換

        Returns:
            str: JSON文字列
        """
        specifications: List[Dict] = []
        for spec in self.__collection:
            specifications.append(json.loads(spec.to_json()))
        return json.dumps({"全ポケモンリスト": specifications}, ensure_ascii=False)
