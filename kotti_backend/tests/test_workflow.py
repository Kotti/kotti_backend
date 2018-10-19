import pytest

from kotti.resources import File
from kotti_image.resources import Image


class TestFileImageWorkflow:

    def make_document(self, root):
        from kotti.resources import Document
        doc = root['doc'] = Document()
        from kotti import DBSession
        DBSession.flush()
        DBSession.refresh(doc)
        return doc

    @pytest.mark.parametrize("factory", [File, Image])
    def test_default_workflow_iface(self, factory, db_session, root, filedepot,
                                    config):
        from kotti.interfaces import IDefaultWorkflow
        config.include('kotti.views')  # custom predicates
        config.include('kotti_backend')
        instance = factory(name=u'content',
                           title=u'content')
        assert IDefaultWorkflow.providedBy(instance)

    def test_private_workflow(self, app, root):
        doc = self.make_document(root)
        assert doc.state == u'private'

    def test_private_workflow_name(self, app, root):
        doc = self.make_document(root)
        from kotti.workflow import get_workflow
        wf = get_workflow(doc)
        assert wf.name == u'private_workflow'
