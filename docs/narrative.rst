Using :mod:`zope.dublincore`
============================

Dublin Core Properties
----------------------

A dublin core property allows us to use properties from dublin core
by simply defining a property as DCProperty.

.. testsetup::

   from zope.annotation.attribute import AttributeAnnotations
   from zope.component import event
   from zope.component import provideAdapter
   from zope.testing.cleanup import setUp
   from zope.dublincore.testing import setUpDublinCore
   setUp()
   provideAdapter(AttributeAnnotations)
   setUpDublinCore()

.. doctest::

   >>> from zope.dublincore import property

   >>> from zope.interface import implementer
   >>> from zope.annotation.interfaces import IAttributeAnnotatable
   >>> @implementer(IAttributeAnnotatable)
   ... class DC(object):
   ...     title   = property.DCProperty('title')
   ...     author  = property.DCProperty('creators')
   ...     authors = property.DCListProperty('creators')
   >>> obj = DC()
   >>> obj.title = u'My title'
   >>> print(obj.title)
   My title

Let's see if the title is really stored in dublin core:

.. doctest::

   >>> from zope.dublincore.interfaces import IZopeDublinCore
   >>> print(IZopeDublinCore(obj).title)
   My title

Even if a dublin core property is a list property we can set and get the
property as scalar type:

.. doctest::

   >>> obj.author = u'me'
   >>> print(obj.author)
   me

DCListProperty acts on the list:

.. doctest::

   >>> obj.authors == (u'me',)
   True
   >>> obj.authors = [u'I', u'others']
   >>> obj.authors == (u'I', u'others')
   True
   >>> print(obj.author)
   I


Dublin Core metadata as content data
------------------------------------

Sometimes we want to include data in content objects which mirrors one
or more Dublin Core fields.  In these cases, we want the Dublin Core
structures to use the data in the content object rather than keeping a
separate value in the annotations typically used.  What fields we want
to do this with can vary, however, and we may not want the Dublin Core
APIs to constrain our choices of field names for our content objects.

To deal with this, we can use speciallized adapter implementations
tailored to specific content objects.  To make this a bit easier,
there is a factory for such adapters.

Let's take a look at the simplest case of this to start with.  We have
some content object with a `title` attribute that should mirror the
Dublin Core `title` field:

.. doctest::

   >>> @implementer(IAttributeAnnotatable)
   ... class Content(object):
   ...     title = u""
   ...     description = u""

To avoid having a discrepency between the `title` attribute of our
content object and the equivalent Dublin Core field, we can provide a
specific adapter for our object:

.. doctest::

   >>> from zope.dublincore import annotatableadapter

   >>> factory = annotatableadapter.partialAnnotatableAdapterFactory(
   ...     ["title"])

This creates an adapter factory that maps the Dublin Core `title`
field to the `title` attribute on instances of our `Content` class.
Multiple mappings may be specified by naming the additional fields in
the sequence passed to `partialAnnotatableAdapterFactory()`.  (We'll
see later how to use different attribute names for Dublin Core
fields.)

Let's see what happens when we use the adapter.

When using the adapter to retrieve a field set to use the content
object, the value stored on the content object is used:

.. doctest::

   >>> content = Content()
   >>> adapter = factory(content)

   >>> print(adapter.title)
   <BLANKLINE>

   >>> content.title = u'New Title'
   >>> print(adapter.title)
   New Title

If we set the relevant Dublin Core field using the adapter, the
content object is updated:

.. doctest::

   >>> adapter.title = u'Adapted Title'
   >>> print(content.title)
   Adapted Title

Dublin Core fields which are not specifically mapped to the content
object do not affect the content object:

.. doctest::

   >>> adapter.description = u"Some long description."
   >>> print(content.description)
   <BLANKLINE>
   >>> print(adapter.description)
   Some long description.


Using arbitrary field names
###########################

We've seen the simple approach, allowing a Dublin Core field to be
stored on the content object using an attribute of the same name as
the DC field.  However, we may want to use a different name for some
reason.  The `partialAnnotatableAdapterFactory()` supports this as
well.

If we call `partialAnnotatableAdapterFactory()` with a mapping instead
of a sequence, the mapping is used to map Dublin Core field names to
attribute names on the content object.

Let's look at an example where we want the `abstract` attribute on the
content object to be used for the `description` Dublin Core field:

.. doctest::

   >>> @implementer(IAttributeAnnotatable)
   ... class Content(object):
   ...     abstract = u""

We can create the adapter factory by passing a mapping to
`partialAnnotatableAdapterFactory()`:

.. doctest::

   >>> factory = annotatableadapter.partialAnnotatableAdapterFactory(
   ...     {"description": "abstract"})

We can check the effects of the adapter as before:

.. doctest::

   >>> content = Content()
   >>> adapter = factory(content)

   >>> print(adapter.description)
   <BLANKLINE>

   >>> content.abstract = u"What it's about."
   >>> print(adapter.description)
   What it's about.

   >>> adapter.description = u'Change of plans.'
   >>> print(content.abstract)
   Change of plans.


Limitations
###########

The current implementation has a number of limitations to be aware of;
hopefully these can be removed in the future.

- Only simple string properties, like `title`, are supported.  This is
  largely because other field types have not been given sufficient
  thought.  Attempting to use this for other fields will cause a
  `ValueError` to be raised by `partialAnnotatableAdapterFactory()`.

- The CMF-like APIs are not supported in the generated adapters.  It
  is not clear that these APIs are used, but content object
  implementations should be aware of this limitation.

Time annotators
---------------

Time annotators store the creation resp. last modification time of an object.
We will use a simple ``Content`` class as our example.

.. doctest::

   >>> class Content(object):
   ...     created = None
   ...     modified = None

The annotations are stored on the ``IZopeDublinCore`` adapter. This dummy
adapter reads and writes from/to the context object.

.. doctest::

   >>> from zope.component import provideAdapter
   >>> from zope.dublincore.interfaces import IZopeDublinCore
   >>> class DummyDublinCore(object):
   ...     def __init__(self, context):
   ...         self.__dict__['context'] = context
   ...
   ...     def __getattr__(self, name):
   ...         return getattr(self.context, name)
   ...
   ...     def __setattr__(self, name, value):
   ...         setattr(self.context, name, value)

   >>> provideAdapter(DummyDublinCore, (Content,), IZopeDublinCore)

Created annotator
#################

The created annotator sets creation and modification time to current time.

.. doctest::

   >>> content = Content()

It is registered for the ``ObjectCreatedEvent``:

.. doctest::

   >>> from zope.dublincore import timeannotators
   >>> timeannotators._NOW = 'NOW'
   >>> from zope.component import provideHandler
   >>> from zope.dublincore.timeannotators import CreatedAnnotator
   >>> from zope.lifecycleevent.interfaces import IObjectCreatedEvent
   >>> provideHandler(CreatedAnnotator, (IObjectCreatedEvent,))

   >>> from zope.event import notify
   >>> from zope.lifecycleevent import ObjectCreatedEvent
   >>> notify(ObjectCreatedEvent(content))

Both ``created`` and ``modified`` get set:

.. doctest::

   >>> content.created
   'NOW'
   >>> content.modified
   'NOW'

The created annotator can also be registered for (object, event):

.. doctest::

   >>> from zope.component import subscribers
   >>> provideHandler(CreatedAnnotator, (None, IObjectCreatedEvent,))
   >>> content = Content()
   >>> ignored = subscribers((content, ObjectCreatedEvent(content)), None)

Both ``created`` and ``modified`` get set this way, too:

.. doctest::

   >>> content.created
   'NOW'
   >>> content.modified
   'NOW'



Modified annotator
##################

The modified annotator only sets the modification time to current time.

.. doctest::

   >>> content = Content()

It is registered for the ``ObjectModifiedEvent``:

.. doctest::

   >>> from zope.dublincore.timeannotators import ModifiedAnnotator
   >>> from zope.lifecycleevent.interfaces import IObjectModifiedEvent
   >>> provideHandler(ModifiedAnnotator, (IObjectModifiedEvent,))

   >>> from zope.lifecycleevent import ObjectModifiedEvent
   >>> notify(ObjectModifiedEvent(content))

Only ``modified`` gets set:

.. doctest::

   >>> print(content.created)
   None
   >>> content.modified
   'NOW'

The modified annotator can also be registered for (object, event):

.. doctest::

   >>> provideHandler(ModifiedAnnotator, (None, IObjectModifiedEvent,))
   >>> content = Content()
   >>> ignored = subscribers((content, ObjectModifiedEvent(content)), None)

``modified`` gets set, this way, too:

.. doctest::

   >>> print(content.created)
   None
   >>> content.modified
   'NOW'

.. testcleanup::

   from zope.testing.cleanup import tearDown
   tearDown()
   from zope.dublincore import timeannotators
   timeannotators._NOW = None
