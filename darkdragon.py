# -*- coding: utf-8 -*-
from .dragon import Dragon


class DarkDragon(Dragon):
    def __init__(self, hp, atk):
        print(id(self.__class__), 'class of self')
        print(id(DarkDragon), 'in DarkDragon class')
        super(DarkDragon, self).__init__(hp, atk)
