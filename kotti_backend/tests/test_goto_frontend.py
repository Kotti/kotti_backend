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

    def test_goto_frontend(self, root, content, settings):
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
