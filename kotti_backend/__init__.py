# -*- coding: utf-8 -*-

"""
Created on 2015-06-22
:author: Davide Moro (davide.moro@gmail.com)
"""
from zope.interface import implementer
from kotti.interfaces import IDefaultWorkflow
from kotti.resources import File
from kotti.resources import Image


def kotti_configure(settings):
    """ Add a line like this to you .ini file::

            kotti.configurators =
                kotti_backend.kotti_configure

        to enable the ``kotti_backend`` add-on.

    :param settings: Kotti configuration dictionary.
    :type settings: dict
    """

    settings['pyramid.includes'] += ' kotti_backend'
    settings['kotti.populators'] = 'kotti_backend.populate.populate'
    settings['kotti.use_workflow'] = 'kotti_backend:workflows/private_workflow.zcml'


def includeme(config):
    """ Don't add this to your ``pyramid_includes``, but add the
    ``kotti_configure`` above to your ``kotti.configurators`` instead.

    :param config: Pyramid configurator object.
    :type config: :class:`pyramid.config.Configurator`
    """

    # Set a default permission.
    # If you want to bypass the default permission for certain views,
    # you can decorate them with a special permission
    # (``NO_PERMISSION_REQUIRED`` from ``pyramid.security`` which indicates
    # that the view should always be executable by entirely anonymous users,
    # regardless of the default permission.
    config.set_default_permission('view')

    # Assign the default workflow for files and images
    implementer(IDefaultWorkflow)(Image)
    implementer(IDefaultWorkflow)(File)
