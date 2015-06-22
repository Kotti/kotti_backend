class TestSecurity:

    def test_populate_acl(self, db_session, root):
        from kotti_backend.security import SITE_ACL
        allow_everyone_view = [item for item in SITE_ACL
                               if item[0] == 'Allow' and
                               item[1] == 'System.everyone' and
                               item[2] == ['view']]
        assert allow_everyone_view == []
