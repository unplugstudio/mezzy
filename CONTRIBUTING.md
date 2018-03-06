# Contributing

Hello! Thanks for your interest in contributing to this project. To get started:

- Thoroughly review our [Code of Conduct]. All contributors must comply with it fully
- Fork the repository
- Work on a feature branch on your fork
- Run tests (see below)
- If all tests pass, commit according to our guidelines (see below)
- Create a pull request
- That's it!

## Running tests

You will need to install `tox` in your Python environment. You should have Python installations for 2.7 and 3.6. To run the test suite simply call `tox` from the project root.

Tests will also be run automatically when you add commits to your pull request.

## Commit guidelines

Please use the [Angular commit format] in your pull requests. This keeps the commit history relevant and human-readable, and generates very nice and useful changelogs.

### Commit format

```
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

### Valid types

- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation only changes
- **style**: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
- **refactor**: A code change that neither fixes a bug nor adds a feature
- **perf**: A code change that improves performance
- **test**: Adding missing or correcting existing tests
- **chore**: Changes to the build process or auxiliary tools and libraries such as documentation generation


## Publishing to PyPI

This is intended for project maintainers with publish access to PyPI. As a contributor you won't be required to do this.

```bash
rm -rf dist/
python setup.py sdist
python setup.py bdist_wheel
twine upload dist/*
```

[Code of Conduct]: CODE_OF_CONDUCT.md
[Angular commit format]: https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#commit-message-format
