from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from kotti.interfaces import IContent
from kotti.resources import get_root


@view_config(
    name='goto_frontend',
    context=IContent,
    if_setting_has_value=('kotti_backend.goto_frontend', True),
    permission='view',
    )
def goto_frontend_view(request):
    settings = request.registry.settings
    not_publishable_types = settings.get('kotti_backend.not_publishable_types',
                                         ()
                                        )
    context = request.context
    parent = context.parent
    while context.type_info.name in not_publishable_types and parent is not None:
        context = context.parent
    script_name = request.environ.get('SCRIPT_NAME')
    frontend_url = settings.get('kotti_backend.frontend_url', None)
    app_url = None
    if frontend_url is not None:
        # use a custom frontend url
        app_url = frontend_url
    elif script_name is not None:
        # default setup with script name (default: /cms)
        root = get_root()
        app_url = ''.join(request.resource_url(root).rsplit(script_name)).rstrip('/')
    return HTTPFound(
        request.resource_url(
            context,
            app_url=app_url,
            )
        )


def includeme(config):
    config.scan(__name__)
