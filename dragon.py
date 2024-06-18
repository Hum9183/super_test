# -*- coding: utf-8 -*-
class Dragon(object):
    def __init__(self, hp, atk):
        self.__hp = hp
        self.__atk = atk

    def attack(self):
        print(u'攻撃!')
