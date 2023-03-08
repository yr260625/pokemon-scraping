"""ポケモン諸元値コレクション"""
import json
from typing import Final
from src.pokedex.model.pokemon_spec import PokemonSpec


class PokemonSpecifications():
    """ポケモン諸元値の一覧を保持、収集するコレクションクラス。
    """

    __MAX_POKEMON_NUMBER: Final[int] = 1008

    def __init__(self, collection: list[PokemonSpec]):
        """コンストラクタ

        Args:
            repository (IPokemonSpecRepository): ポケモン諸元値リポジトリ
        """
        self.__collection: Final[list[PokemonSpec]] = collection

    def can_add(self) -> bool:
        """コレクションに追加可能かどうか

        Returns:
            bool: 追加可能かどうか
        """
        return len(self.__collection) < self.__MAX_POKEMON_NUMBER

    def add(self, pokemon_spec: PokemonSpec):
        """ポケモン諸元値をコレクションに追加

        Args:
            pokemon_spec (PokemonSpec): ポケモン諸元値

        Returns:
            PokemonSpecifications: ポケモン諸元値コレクション
        """
        collection: Final[list[PokemonSpec]] = self.__collection[:]
        collection.append(pokemon_spec)
        return PokemonSpecifications(collection)

    def to_json(self) -> str:
        """全ポケモン諸元値をJSONに変換

        Returns:
            str: JSON文字列
        """
        specifications: list[dict] = []
        for spec in self.__collection:
            specifications.append(json.loads(spec.to_json()))
        return json.dumps({"全ポケモンリスト": specifications}, ensure_ascii=False)
