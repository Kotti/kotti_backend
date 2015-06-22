# -*- coding: utf-8 -*-

"""
Created on 2015-06-22
:author: Davide Moro (davide.moro@gmail.com)
"""

pytest_plugins = "kotti"

from pytest import fixture


@fixture(scope='session')
def custom_settings():
    import kotti_backend.resources
    kotti_backend.resources  # make pyflakes happy
    return {
        'kotti.configurators': 'kotti_tinymce.kotti_configure '
                               'kotti_backend.kotti_configure'}
