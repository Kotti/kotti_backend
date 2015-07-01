from pytest import mark
from pytest import fixture


class TestViews:

    @mark.user('admin')
    def test_root_view_admin(self, webtest, root):
        # default view is folder contents
        resp = webtest.get('/')
        assert resp.status_code == 200

    def test_root_view(self, webtest, root):
        # view requires authentication
        resp = webtest.get('/')
        assert resp.status_code == 302
