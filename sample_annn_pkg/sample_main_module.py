# -*- coding: utf-8 -*-


# --------------------------------------------------------------------------------
# Load modules
# --------------------------------------------------------------------------------

from . import sample_sub_module as ssm



# --------------------------------------------------------------------------------
# Functions
# --------------------------------------------------------------------------------


def func01():
    return 'poyo'


def func02():

    if ssm.return_true():
        print('success!!')
        print(func01())

        return 12345

    else:
        print('failed!!')
        print('error')

        return 54321



# --------------------------------------------------------------------------------
# Classes
# --------------------------------------------------------------------------------


class PoyoClass():

    def __init__(self):
        self.set_hoge(100)
        
    
    def set_hoge(self, hoge):
        self.hoge = hoge
        print('hoge num: {}'.format(self.hoge))


    def get_hoge(self):
        return self.hoge


