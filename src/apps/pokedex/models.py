from django.db import models


class PokedexPokemon(models.Model):
    name = models.CharField('Pokemon Name', max_length=256)
    species_id = models.PositiveIntegerField('Pokemon ID')
    height = models.PositiveIntegerField('Pokemon Height')
    weight = models.PositiveIntegerField('Pokemon Weight')
    base_experience = models.PositiveIntegerField('Pokemon Base Exp')
    order = models.PositiveIntegerField('Pokemon Order')

    def __str__(self):
        return f"#{self.species_id} {self.name.capitalize()}"

    class Meta:
        db_table = 'pokedex_pokemons'
        verbose_name = 'Pokemon'
        verbose_name_plural = 'Pokemons'
        ordering = ('species_id',)
