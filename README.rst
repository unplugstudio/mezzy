
Mezzy
=====

A collection of utilities for Mezzanine projects. Mezzy’s main goal is to abstract-out common patterns used in Mezzanine sites. It does so by providing small, decoupled, drop-in APIs for several aspects of a Django / Mezzanine project.

What’s in the box
-----------------

``mezzy.utils`` contains Model and Admin mixins. Right now it focuses on creating fairly complex model hierarchies in the admin as an alternative to nested inlines. It also contains some helpers for templates.

Among other template tags provided my ``mezzy_tags`` the ``clean`` filter is made to remove unwanted HTML tags and attributes that aren’t allowed for Mezzanine by default. This is useful when you have a ``RichTextField`` and you need its content without videos, iframes, flash, etc.

Install
-------

1. Install via pip: ``pip install mezzy``.
2. Add ``mezzy`` your ``INSTALLED_APPS``.
3. Use the parts you want.

Contributing
------------

Review contribution guidelines at CONTRIBUTING.md_.

.. _CONTRIBUTING.md: CONTRIBUTING.md
