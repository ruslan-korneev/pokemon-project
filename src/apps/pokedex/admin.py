from django.contrib import admin

from apps.pokedex.models import PokedexPokemon


@admin.register(PokedexPokemon)
class PokedexPokemonAdmin(admin.ModelAdmin):
    list_display = ('name', 'species_id', 'height', 'weight', 'base_experience', 'order')
    search_fields = ('name', 'species_id')