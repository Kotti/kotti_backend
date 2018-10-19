from pytest import mark


class TestViews:

    @mark.user('admin')
    def test_root_view_admin(self, webtest):
        # admin can view
        resp = webtest.get('/')
        assert resp.status_code == 200

    def test_root_view(self, webtest):
        # view requires authentication
        resp = webtest.get('/')
        assert resp.status_code == 302

    @mark.user('admin')
    def test_root_view_admin_default(self, webtest):
        # admin can view
        resp = webtest.get('/')
        assert b'/@@contents' not in resp.body
