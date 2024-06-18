# -*- coding: utf-8 -*-
from .darkdragon import DarkDragon


def main():
    print(id(DarkDragon), 'in main function')
    dark_dragon = DarkDragon(130, 80)
    dark_dragon.attack()
