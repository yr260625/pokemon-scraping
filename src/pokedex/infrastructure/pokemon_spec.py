"""ポケモン諸元値リポジトリ"""
from typing import Final
import bs4
import requests
from src.pokedex.model.pokemon_spec import PokemonSpec
from src.pokedex.repository.pokemon_spec import IPokemonSpecRepository


class PokemonSpecRepository(IPokemonSpecRepository):
    """ポケモン諸元値リポジトリクラス

    Args:
        IPokemonSpecRepository (_type_): ポケモン諸元値リポジトリインターフェース
    """

    BASE_URL: Final[str] = 'https://zukan.pokemon.co.jp/detail'
    TIME_OUT: Final[int] = 5

    def fetch_by_id(self, pokemon_id: int) -> PokemonSpec:
        """ポケモン諸元値取得

        Args:
            id (int): 図鑑No.

        Returns:
            PokemonSpec: ポケモン諸元値オブジェクト

        Raises:
            HTTPError: ステータスコードが400系 or 500系
            ParseError: HTMLパース失敗
        """
        try:
            res = requests.get(f'{self.BASE_URL}/{pokemon_id}', timeout=self.TIME_OUT)
            res.raise_for_status()
            soup = bs4.BeautifulSoup(res.text, 'html.parser')
            json_data = soup.select_one('#json-data')
            if json_data is None:
                raise ParseError
            return PokemonSpec.create(json_data.text)
        except Exception as e:
            print(f'ID:{pokemon_id}のポケモン諸元値を取得できませんでした。')
            raise e


class ParseError(Exception):
    """HTMLパース失敗
    """
