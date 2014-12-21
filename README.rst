``zope.dublincore`` provides a Dublin Core support for Zope-based web
applications.  This includes:

* an ``IZopeDublinCore`` interface definition that can be implemented
  by objects directly or via an adapter to support DublinCore
  metadata.

* an ``IZopeDublinCore`` adapter for annotatable objects (objects
  providing ``IAnnotatable`` from ``zope.annotation``).

* a partial adapter for objects that already implement some of the
  ``IZopeDublinCore`` API,

* a "Metadata" browser page (which by default appears in the ZMI),

* subscribers to various object lifecycle events that automatically
  set the created and modified date and some other metadata.
