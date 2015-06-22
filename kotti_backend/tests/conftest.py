# -*- coding: utf-8 -*-

"""
Created on 2015-06-22
:author: Davide Moro (davide.moro@gmail.com)
"""

pytest_plugins = "kotti"

from pytest import fixture


@fixture(scope='session')
def custom_settings():
    return {
        'kotti.configurators': 'kotti_tinymce.kotti_configure '
                               'kotti_backend.kotti_configure'}
