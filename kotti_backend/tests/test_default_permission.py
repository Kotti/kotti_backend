class TestDefaultPermission:

    def test_changed_default_permission(self, config):
        from pyramid.interfaces import IDefaultPermission
        config.include('kotti_backend')
        assert config.registry.getUtility(IDefaultPermission) == 'view'
