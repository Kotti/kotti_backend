kotti_backend
*************

This plugin turns Kotti CMS into a private content administration area.
Basically ``kotti_backend`` let you achieve the same goals described here (`Kotti CMS intranet`_).

What ``kotti_backend`` does:

1. define and load a new ``private_workflow``. If you are installing kotti_backend on
   an existing Kotti installation you'll need to call ``kotti-reset-workflow yourinifile.ini --purge-existing``
   (be extremely **careful** because all your published contents will be converted to the
   private state)

2. apply the above workflow to ``File`` and ``Image`` (they are workflowless by default)

3. set a default fallback permission to all views

4. override the default populator with a custom ACL (no allow view for everyone)


|build status|_

`Find out more about Kotti`_

Development happens at https://github.com/Kotti/kotti_backend

.. |build status| image:: https://secure.travis-ci.org/Kotti/kotti_backend.png?branch=master
.. _build status: http://travis-ci.org/Kotti/kotti_backend
.. _Find out more about Kotti: http://pypi.python.org/pypi/Kotti
.. _Kotti CMS intranet: http://davidemoro.blogspot.it/2015/02/kotti-cms-intranet.html

Setup
=====

To enable the extension in your Kotti site, activate the configurator::

    kotti.configurators =
        kotti_backend.kotti_configure

    kotti.use_workflow = kotti_backend:workflows/private_workflow.zcml

If you are going to install ``kotti_backend`` on an already existing site you'll need to reset the
workflow: read the docs and backup first. See `Kotti security`_

.. _Kotti security: http://kotti.readthedocs.org/en/latest/developing/basic/security.html

Development
===========

Contributions to kotti_backend are highly welcome.
Just clone its `Github repository`_ and submit your contributions as pull requests.

.. _tracker: https://github.com/Kotti/kotti_backend/issues
.. _Github repository: https://github.com/Kotti/kotti_backend
