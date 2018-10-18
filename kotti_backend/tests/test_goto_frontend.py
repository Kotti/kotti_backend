from kotti.testing import user


class TestGotoFrontend:

    def dummy_request(self, context, settings, environ):
        from kotti.testing import DummyRequest
        dummy_request = DummyRequest()
        dummy_request.registry.settings = settings
        dummy_request.environ = environ
        dummy_request.context = context

        _resource_url = dummy_request.resource_url
        dummy_request._resource_url = _resource_url

        def resource_url(context, *args, **kwargs):
            app_url = kwargs.pop('app_url', None)
            if app_url is not None:
                return dummy_request._resource_url(context, app_url=app_url)
            else:
                return dummy_request._resource_url(
                    context,
                    app_url='http://example.com{0}'.format(environ['SCRIPT_NAME']),
                    *args,
                    **kwargs
                    )
        dummy_request.resource_url = resource_url
        return dummy_request

    def _create_file(self, config):
        from kotti.resources import File
        return File(b"file contents", u"myf\xfcle.png", u"image/png")

    def test_goto_frontend_default(self, root, content):
        from kotti_backend.views.goto_frontend import goto_frontend_view
        from pyramid.httpexceptions import HTTPFound
        settings = {}
        environ = {'SCRIPT_NAME': '/cms'}
        dummy_request = self.dummy_request(root['about'], settings, environ)

        assert dummy_request.resource_url(root['about']) == 'http://example.com/cms/about/'

        import mock
        with mock.patch('kotti_backend.views.goto_frontend.get_root') as get_root:
            get_root.return_value = root
            resp = goto_frontend_view(dummy_request)

        assert resp.location == 'http://example.com/about/'
        assert isinstance(resp, HTTPFound)

    def test_goto_frontend_custom_url(self, root, content):
        from kotti_backend.views.goto_frontend import goto_frontend_view
        from pyramid.httpexceptions import HTTPFound
        settings = {'kotti_backend.frontend_url': 'http://google.com'}
        environ = {'SCRIPT_NAME': '/cms'}
        dummy_request = self.dummy_request(root['about'], settings, environ)

        assert dummy_request.resource_url(root['about']) == 'http://example.com/cms/about/'

        import mock
        with mock.patch('kotti_backend.views.goto_frontend.get_root') as get_root:
            get_root.return_value = root
            resp = goto_frontend_view(dummy_request)

        assert resp.location == 'http://google.com/about/'
        assert isinstance(resp, HTTPFound)

    def test_goto_frontend_not_publishable_types(self, config, root, content, filedepot):
        file_obj = self._create_file(config)
        root['file'] = file_obj
        from kotti_backend.views.goto_frontend import goto_frontend_view
        from pyramid.httpexceptions import HTTPFound
        settings = {'kotti_backend.not_publishable_types': ('File',)}
        environ = {'SCRIPT_NAME': '/cms'}
        dummy_request = self.dummy_request(root['file'], settings, environ)

        assert dummy_request.resource_url(root['file']) == 'http://example.com/cms/file/'

        import mock
        with mock.patch('kotti_backend.views.goto_frontend.get_root') as get_root:
            get_root.return_value = root
            resp = goto_frontend_view(dummy_request)

        assert resp.location == 'http://example.com/'
        assert isinstance(resp, HTTPFound)

    def test_goto_frontend_edit_links(self, root, app, config, content):
        config.include('kotti.views')
        config.include('kotti.views.edit.actions')
        config.include('kotti_backend')
        assert len([item.name for item in root['about'].type_info.edit_links
                    if hasattr(item, 'name') and item.name == 'goto_frontend']) == 1
