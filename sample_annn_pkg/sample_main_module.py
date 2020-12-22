# -*- coding: utf-8 -*-
from . import sample_sub_module as ssm

def func01():
    return 'poyo'


def func02():

    if ssm.return_true():
        print('success!!')
        print(func01())
    else:
        print('failed!!')
        print('error')
