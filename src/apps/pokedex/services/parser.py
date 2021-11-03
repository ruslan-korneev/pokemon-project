from apps.pokedex.models import PokedexPokemon


class PokemonParse:
    def __init__(self, data):
        self.data = data
        self.pokemons = self.parse_pokemons()

    def parse_pokemons(self):
        pokemons = self.data.split('\n')
        pokemons = [
            PokedexPokemon.objects.create(
                name=identifier, species_id=species_id, height=height,
                weight=weight, base_experience=base_experience, order=order)
            for id, identifier, species_id, height, weight, base_experience, order, is_default
            in (pokemon.split(',') for pokemon in pokemons[1:])
        ]
        return pokemons