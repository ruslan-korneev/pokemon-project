from apps.inventory.models import Inventory
from apps.loot.models import Pokeball, PokeballInventory


def get_starting_loot(sender, instance, profile):
    # create inventory for master
    inventory = Inventory()
    inventory.save()
    # create profile for master
    profile.user = instance
    profile.inventory = inventory
    profile.save()

    pokeball = Pokeball.objects.get_or_create(name='Poke Ball', level=1)[0]
    PokeballInventory.objects.create(
        pokeball=pokeball, inventory=profile.inventory, quantity=20)

    pokeball = Pokeball.objects.get_or_create(name='Great Ball', level=2)[0]
    PokeballInventory.objects.create(
        pokeball=pokeball, inventory=profile.inventory, quantity=10)

    pokeball = Pokeball.objects.get_or_create(name='Ultra Ball', level=3)[0]
    PokeballInventory.objects.create(
        pokeball=pokeball, inventory=profile.inventory, quantity=10)