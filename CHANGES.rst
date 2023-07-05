Changes
=======

5.0 (2023-07-05)
----------------

- Drop support for Python 2.7, 3.5, 3.6.

- Add back support for Python 3.5.

- Add support for Python 3.10, 3.11.


4.3.0 (2020-10-14)
------------------

- Port ``.browser`` sub-package to Python 3.

- Add support for Python 3.7, 3.8 and 3.9.

- Drop support for running the tests using ``python setup.py test``.

- Drop support for Python 3.4 and 3.5.


4.2.0 (2017-07-25)
------------------

- Add support for Python 3.5 and 3.6.

- Drop support for Python 2.6 and 3.3.

- Convert doctests to Sphinx, including building docs and testing doctest
  snippets under ``tox``.


4.1.1 (2014-01-10)
------------------

- Add explicit dependency on ``persistent`` (required but not declared).

- Add explicit dependency on ``zope.annotation`` (required but not declared).


4.1.0 (2014-12-26)
------------------

- Add support for PyPy. (PyPy3 is pending release of a fix for:
  https://bitbucket.org/pypy/pypy/issue/1946)

- Add support for Python 3.4.


4.0.1 (2014-12-20)
------------------

- Add support for testing on Travis-CI.


4.0.0 (2013-02-20)
------------------

- Add support for Python 3.3.

- Replace deprecated ``zope.component.adapts`` usage with equivalent
  ``zope.component.adapter`` decorator.

- Replace deprecated ``zope.interface.implements`` usage with equivalent
  ``zope.interface.implementer`` decorator.

- Drop support for Python 2.4 and 2.5.


3.8.2 (2010-02-19)
------------------

- Update <DATETIME> regex normalizer to guard against test failure when
  a datetime's microseconds value is zero.


3.8.1 (2010-12-14)
------------------

- Add missing test dependency on zope.configuration and missing dependency
  of security.zcml on zope.security's meta.zcml.


3.8.0 (2010-09-14)
------------------

- Register the annotators also for (object, event), so copy-pasting a
  folder, changes the dublin core data of the contained objects, too. The
  changed annotators are the following:

  - ``zope.dublincore.timeannotators.ModifiedAnnotator``
  - ``zope.dublincore.timeannotators.CreatedAnnotator``
  - ``zope.dublincore.creatorannotator.CreatorAnnotator``


3.7.0 (2010-08-19)
------------------

- Remove backward-compatibility shims for deprecated ``zope.app.dublincore.*``
  permissions.

- Remove include the zcml configuration of ``zope.dublincore.browser``.

- Use python`s doctest instead of deprecated ``zope.testing.doctest``.


3.6.3 (2010-04-23)
------------------

- Restore backward-compatible ``zope.app.dublincore.*`` permissions,
  mapping them onto the new permissions using the ``<meta:redefinePermission>``
  directive.  These shims will be removed in 3.7.0.

- Add unit (not functional) test for loadability of ``configure.zcml``.


3.6.2 (2010-04-20)
------------------

- Repair regression introduced in 3.6.1:  the renamed permissions were
  not updated in other ZCML files.


3.6.1 (2010-04-19)
------------------

- Rename the ``zope.app.dublincore.*`` permissions to
  ``zope.dublincore.*``.  Applications may need to fix up grants based on the
  old permissions.

- Add tests for ``zope.dublincore.timeannotators``.

- Add not declared dependency on ``zope.lifecycleevent``.


3.6.0 (2009-12-02)
------------------

- Remove the marker interface IZopeDublinCoreAnnotatable which doesn't seem
  to be used.

- Make the registration of ZDCAnnotatableAdapter conditional, lifting the
  dependency on zope.annotation and thereby the ZODB, leaving it as a test
  dependency.


3.5.0 (2009-09-15)
------------------

- Add missing dependencies.

- Get rid of any testing dependencies beyond zope.testing.

- Include browser ZCML configuration only if zope.browserpage is installed.

- Specify i18n domain in package's ``configure.zcml``, because we use message
  IDs for permission titles.

- Remove unused imports, fix one test that was inactive because of being
  overriden by another one by a mistake.


3.4.2 (2009-01-31)
------------------

- Declare dependency on zope.datetime.


3.4.1 (2009-01-26)
------------------

- Test dependencies are declared in a `test` extra now.

- Fix: Make CreatorAnnotator not to fail if participation principal is None


3.4.0 (2007-09-28)
------------------

No further changes since 3.4.0a1.


3.4.0a1 (2007-04-22)
--------------------

Initial release as a separate project, corresponds to zope.dublincore
from Zope 3.4.0a1
