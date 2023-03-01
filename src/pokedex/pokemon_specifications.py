"""ポケモン諸元値コレクション"""
import json
import time

from typing import Final
from src.pokedex.model.pokemon_spec import PokemonSpec
from src.pokedex.repository.pokemon_spec import IPokemonSpecRepository


class PokemonSpecifications():

    """ポケモン諸元値の一覧を保持、収集するコレクションクラス。
    """

    MIN_POKEMON_NUMBER: Final[int] = 1
    MAX_POKEMON_NUMBER: Final[int] = 1008
    collection: Final[list[PokemonSpec]] = []

    def __init__(self, repository: IPokemonSpecRepository):
        """コンストラクタ

        Args:
            repository (IPokemonSpecRepository): ポケモン諸元値リポジトリ
        """
        self.repository = repository

    def fetch_all(self):
        """ポケモン諸元値を全取得
        """
        for pokemon_id in range(self.MIN_POKEMON_NUMBER, self.MAX_POKEMON_NUMBER + 1):
            pokemon_spec = self.repository.fetch_by_id(pokemon_id)
            self.collection.append(pokemon_spec)
            time.sleep(0.5)

    def to_json(self) -> str:
        """全ポケモン諸元値をJSONに変換

        Returns:
            str: JSON文字列
        """
        specifications: list[dict] = []
        for spec in self.collection:
            specifications.append(json.loads(spec.to_json()))
        return json.dumps({"全ポケモンリスト": specifications}, ensure_ascii=False)
