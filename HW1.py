class NonNegative:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Cannot be negative.')
        instance.__dict__[self.name] = value
    def __set_name__(self, owner, name):
        self.name = name


class Road:
    _length = NonNegative()
    _width = NonNegative()
    """ Класс дорожного полотна """
    # удельная масса 1кв.м. дорожного полотна толщиной 1 см (тонн)
    _surface_spec_gravity: float = 0.02

    def __init__(self, length: [int, float], width: [int, float]):
        """
        :param length: Длина дорожного полотна в метрах
        :param width: Ширина дорожного полотна в метрах
        """
        self._length = float(length)
        self._width = float(width)

    def get_surface_gravity(self, thickness: float) -> [float, None]:
        """ Рассчет массы дорожного полотна заданной толщина
        :param thickness: Толщина дорожного покрытия в сантиметрах
        :return: Масса дорожного полотна в тоннах если все ОК, иначе None
        """
        try:
            return (self._length * self._width
                    * thickness * self._surface_spec_gravity)
        except TypeError:
            return None


if __name__ == '__main__':
    try:
        road = Road(5000, 10)
        print(
            'Масса дорожного покрытия составит:',
            road.get_surface_gravity(20),
            'тонн'
        )
    except TypeError:
        print('класс Road требует 2 позиционных аргумента')
