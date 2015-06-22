# -*- coding: utf-8 -*-

"""
Created on 2015-06-22
:author: Davide Moro (davide.moro@gmail.com)
"""

from kotti.resources import File
from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('kotti_backend')


def kotti_configure(settings):
    """ Add a line like this to you .ini file::

            kotti.configurators =
                kotti_backend.kotti_configure

        to enable the ``kotti_backend`` add-on.

    :param settings: Kotti configuration dictionary.
    :type settings: dict
    """

    settings['pyramid.includes'] += ' kotti_backend'
    settings['kotti.alembic_dirs'] += ' kotti_backend:alembic'
    settings['kotti.available_types'] += ' kotti_backend.resources.CustomContent'
    settings['kotti.fanstatic.view_needed'] += ' kotti_backend.fanstatic.css_and_js'
    File.type_info.addable_to.append('CustomContent')


def includeme(config):
    """ Don't add this to your ``pyramid_includes``, but add the
    ``kotti_configure`` above to your ``kotti.configurators`` instead.

    :param config: Pyramid configurator object.
    :type config: :class:`pyramid.config.Configurator`
    """

    config.add_translation_dirs('kotti_backend:locale')
    config.add_static_view('static-kotti_backend', 'kotti_backend:static')

    config.scan(__name__)
