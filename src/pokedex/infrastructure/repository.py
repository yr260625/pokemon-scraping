from typing import Final
import bs4
import requests
from src.pokedex.model.pokemon_spec import PokemonSpec
from src.pokedex.repository.pokemon_spec_repository import IPokemonSpecRepository


class PokemonSpecRepository(IPokemonSpecRepository):
    """ポケモン諸元値リポジトリクラス

    Args:
        IPokemonSpecRepository (_type_): ポケモン諸元値リポジトリインターフェース
    """

    BASE_URL: Final[str] = 'https://zukan.pokemon.co.jp/detail/'

    def findById(self, id: int) -> PokemonSpec:
        """ポケモン諸元値取得

        Args:
            id (int): ポケモン図鑑No.

        Returns:
            PokemonSpec: ポケモン諸元値オブジェクト

        Raises:
            HTTPError: ステータスコードが400系 or 500系
        """
        _res = requests.get(self.BASE_URL + f'{id}')
        _res.raise_for_status()
        _soup = bs4.BeautifulSoup(_res.text, 'html.parser')
        _raw_spec = _soup.select_one('#json-data').text
        return PokemonSpec.createFromRawSpec(_raw_spec)
