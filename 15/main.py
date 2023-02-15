from modelos.item import Item

item1 = Item(199, 'Dark Souls')
item2 = Item(
    preco=350,
    nome='Dark Souls II',
    descricao='Vai sofrer muito!'
)

print(item1.get_nome())
    