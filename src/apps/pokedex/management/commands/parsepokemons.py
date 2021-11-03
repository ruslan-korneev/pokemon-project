from django.core.management.base import BaseCommand

from apps.pokedex.data.pokemons import pokemons_data
from apps.pokedex.services.parser import PokemonParse


class Command(BaseCommand):
    help = 'Parse books and save them to DB'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Processing... 🚀'))
        PokemonParse(pokemons_data)
        self.stdout.write(self.style.SUCCESS('Successfully parsed products 🎉'))
