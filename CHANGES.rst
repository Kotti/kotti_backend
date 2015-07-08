History
=======

0.2.0 (2015-07-08)
------------------

- Add optional "Goto frontend" edit links on backend


0.1.4 (2015-07-02)
------------------

- Add more tests

- Add optional pyramid.includes setting ``kotti_backend.views.override_root_view```.
  Include it if you want to override the root with the ``@@contents`` view


0.1.3 (2015-06-25)
------------------

- Add important note on README

0.1.2 (2015-06-25)
------------------

- Add support for third party plugins with decoupled frontend (public view permission ``pview``)


0.1.1 (2015-06-25)
------------------

- No more automatic override for ``kotti.use_workflow`` ini setting.
  Now you have to add ``kotti.use_workflow = kotti_backend:workflows/private_workflow.zcml``


0.1.0 (2015-06-22)
------------------

- Create package with ``pcreate -s kotti kotti_backend``.
