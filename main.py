"""起動スクリプト"""
import traceback
from src.pokedex.model.pokemon_specifications import PokemonSpecifications
from src.pokedex.usecases import PokedexUsecases
from src.pokedex.infrastructure.pokemon_spec import PokemonSpecRepository

if __name__ == '__main__':
    try:
        print('処理を開始します。')
        pokedex_usecases = PokedexUsecases(PokemonSpecRepository())
        completed_pokedex: PokemonSpecifications = pokedex_usecases.complete()
        print(completed_pokedex.to_json())
        print('処理が完了しました。')
    except Exception as error:
        print(error)
        print(traceback.format_exc())
