def includeme(config):  # pragma: no cover
    """ [Optional] Change the default view for the site root (@@contents).
        Useful if you want to use your kotti instance like a
        private content administration area.
    """
    config.add_route('home', '/')
    config.add_view('kotti.views.edit.actions.contents',
                    route_name=u'home',
                    permission=u'view',
                    renderer='kotti:templates/edit/contents.pt',
                    )
