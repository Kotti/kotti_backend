class TestPopulate:

    def test_populate_about(self, db_session, root):
        assert 'about' in root

    def test_populate_acl(self, db_session, root):
        allow_everyone_view = [item for item in root.__acl__
                               if item[0] == 'Allow' and
                               item[1] == 'System.everyone' and
                               item[2] == ['view']]
        assert allow_everyone_view == []
