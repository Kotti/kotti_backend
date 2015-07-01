from pytest import mark


class TestViews:

    @mark.user('admin')
    def test_root_view_admin(self, webtest, root):
        # admin can view
        resp = webtest.get('/')
        assert resp.status_code == 200

    def test_root_view(self, webtest, root):
        # view requires authentication
        resp = webtest.get('/')
        assert resp.status_code == 302
