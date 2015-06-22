from pyramid.i18n import LocalizerRequestMixin
from pyramid.threadlocal import get_current_registry
from kotti.populate import (
    populate_users,
    _ROOT_ATTRS,
    _ABOUT_ATTRS,
    )
from kotti import (
    DBSession,
    get_settings,
    )
from kotti.resources import (
    Document,
    Node,
    )
from kotti_backend.security import SITE_ACL


def populate():
    """
    Create the root node (:class:`~kotti.resources.Document`) and the 'about'
    subnode in the nodes tree if there are no nodes yet.
    """
    lrm = LocalizerRequestMixin()
    lrm.registry = get_current_registry()
    lrm.locale_name = get_settings()['pyramid.default_locale_name']
    localizer = lrm.localizer

    if DBSession.query(Node.id).count() == 0:
        localized_root_attrs = dict(
            [(k, localizer.translate(v)) for k, v in _ROOT_ATTRS.iteritems()])
        root = Document(**localized_root_attrs)
        root.__acl__ = SITE_ACL
        DBSession.add(root)
        localized_about_attrs = dict(
            [(k, localizer.translate(v)) for k, v in _ABOUT_ATTRS.iteritems()])
        root['about'] = Document(**localized_about_attrs)
        DBSession.flush()

    populate_users()
