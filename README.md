# Mezzy

A collection of utilities for Mezzanine projects. Mezzy's main goal is to
abstract-out common patterns used in Mezzanine sites. It does so by providing
small, decoupled, drop-in APIs for several aspects of a Django / Mezzanine
project.

## What's in the box

**`mezzy.utils`** contains Model and Admin mixins. Right now it focuses on
creating fairly complex model hierarchies in the admin as an alternative to
nested inlines. It also contains some helpers for templates.

**`mezzy.management`** contains helper management commands (like `gruntserver`,
to start Grunt when you start `runserver`).

## Install

1. Install via pip: `pip install mezzy`.
1. Add to your `INSTALLED_APPS`.
1. Use the parts you want.
