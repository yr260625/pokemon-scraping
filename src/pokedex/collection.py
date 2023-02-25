import json
import time
from typing import Final
from src.pokedex.model.pokemon_spec import PokemonSpec
from src.pokedex.repository.pokemon_spec_repository import IPokemonSpecRepository


class Pokedex():

    """ポケモン諸元値の一覧(ポケモン図鑑)を保持、収集するコレクションクラス。
    """

    MIN_POKEMON_NUMBER: Final[int] = 1
    MAX_POKEMON_NUMBER: Final[int] = 1008

    def __init__(self, repository: IPokemonSpecRepository):
        """コンストラクタ

        Args:
            repository (IPokemonSpecRepository): ポケモン諸元値リポジトリ
        """
        self.repository = repository
        self.pokedex: tuple[PokemonSpec] = tuple()

    def add(self, pokemon_spec: PokemonSpec):
        """ポケモン諸元値オブジェクトをポケモン図鑑に追加

        Args:
            pokemon_spec (PokemonSpec): ポケモン諸元値オブジェクト
        """
        pokedex = list(self.pokedex)
        pokedex.append(pokemon_spec)
        self.pokedex = tuple(pokedex)

    def releaseAll(self):
        """ポケモン図鑑を全解放
        """
        try:
            for id in range(self.MIN_POKEMON_NUMBER, self.MAX_POKEMON_NUMBER + 1):
                _pokemon_spec = self.repository.findById(id)
                self.add(_pokemon_spec)
                time.sleep(0.5)
        except Exception as e:
            print('エラーが発生しました。: No.=' + f'{id}')
            print(e)

    def to_json(self) -> str:
        """ポケモン図鑑に追加された全てのポケモン諸元値をJSONに変換

        Returns:
            str: JSON文字列
        """
        _specs = []
        for spec in self.pokedex:
            _specs.append(json.loads(spec.to_json()))
        return json.dumps({"全ポケモンリスト": _specs}, ensure_ascii=False)
