"""起動スクリプト"""
import traceback
from src.pokedex.collection import Pokedex
from src.pokedex.infrastructure.pokemon_spec import PokemonSpecRepository

if __name__ == '__main__':
    try:
        print('処理を開始します。')
        pokedex = Pokedex(PokemonSpecRepository())
        print('ポケモン図鑑収集中...')
        pokedex.release_all()
        print('ポケモン図鑑出力中...')
        print(pokedex.to_json())
        print('処理が完了しました。')
    except Exception as error:
        print(error)
        print(traceback.format_exc())
