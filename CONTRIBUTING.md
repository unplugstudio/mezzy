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

You will need to install `tox` globally in your environment. To run the test suite simply call `tox` (or `tox -p auto` to run in parallel) from the project root. Check `setup.cfg` for the tox configuration and required Python versions.

Tests will also be run automatically in Continuos Integration when you add commits to your pull request. All tests must pass to merge your pull request.

## Commit guidelines

Please follow the [conventional commits guidelines](https://www.conventionalcommits.org/).

## Publishing to PyPI

This project uses [semantic-release](https://github.com/semantic-release/semantic-release) and automatically publishes a new release when commits are pushed or merged into the `master` branch. Version numbers follow SemVer.

[Code of Conduct]: CODE_OF_CONDUCT.md
[Angular commit format]: https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#commit-message-format
