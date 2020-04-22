# Mezzy

Utilities for [Mezzanine](http://mezzanine.jupo.org/) sites

[![PyPI version](https://badge.fury.io/py/mezzy.svg)](https://badge.fury.io/py/mezzy)
![Workflow status](https://github.com/unplugstudio/mezzy/workflows/Test%20and%20release/badge.svg)

## Installation

1. Install via pip: `pip install mezzy`
1. Add to `"mezzy"` to `INSTALLED_APPS` (if using the template tags)

## Features

### Utilities

Found in `mezzy.utils`

- `admin` mixins to create "nested" inline admin experiences
- `forms` mixins for more accessible and user-friendly forms
- `models` abstract model classes for common inline patterns
- `tests` TestCase mixin for class-based and function-based views

### Template tags and filters

`mezzy_tags` provides the following:

- `microtemplate`: Filter that parses certain variables in the value param. It can be used to allow some templating capabilities in admin fields. Default template tokens can be found in `mezzy.defaults`.
- `load_theme`: Tag that adds the `SiteConfiguration` to the context. It also uses the request object as cache to avoid some DB hits.
- `clean`: Filter that removes HTML tags and attributes that aren't allowed for Mezzanine by default, even if the user has disabled filtering.

## Contributing

Review contribution guidelines at [CONTRIBUTING.md].

[CONTRIBUTING.md]: CONTRIBUTING.md
