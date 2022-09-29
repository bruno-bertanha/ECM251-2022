class Product():
    def __init__(self, price, name, image, description=None):
        self._name = name
        self._price = price
        self._description = description
        self._image = image

    def __str__(self):
        return f'{self._name}: R$ {self._price}'
    
    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_description(self):
        return self._description
    
    def get_image(self):
        return self._image