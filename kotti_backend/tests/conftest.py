# -*- coding: utf-8 -*-

"""
Created on 2015-06-22
:author: Davide Moro (davide.moro@gmail.com)
"""
from pytest import fixture

pytest_plugins = "kotti"


@fixture(scope='session')
def custom_settings():
    return {
        'kotti.use_workflow': 'kotti_backend:workflows/private_workflow.zcml',
        'kotti.populators': 'kotti_backend.populate.populate',
        'kotti.configurators': 'kotti_tinymce.kotti_configure '
                               'kotti_backend.kotti_configure'}
