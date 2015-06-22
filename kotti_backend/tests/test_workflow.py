import pytest
from kotti.resources import (
    File,
    Image,
    )


class TestFileImageWorkflow:

    @pytest.mark.parametrize("factory", [File, Image])
    def test_default_workflow_iface(self, factory, db_session, root, filedepot,
                                    config):
        from kotti.interfaces import IDefaultWorkflow
        config.include('kotti_backend')
        instance = factory(data='file content',
                           name=u'content',
                           title=u'content')
        assert IDefaultWorkflow.providedBy(instance)
