# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

This project was originally forked from [django-url-filter](https://github.com/miki725/django-url-filter). If you wish to see the CHANGELOG pre-fork, visit [HISTORY.rst](https://github.com/miki725/django-url-filter/blob/master/HISTORY.rst).

## [Unreleased]

## [0.4.3] - 2023-05-04

### Added

-   Support for Python3.11

### Fixed

-   README (Thanks @aseidma)
-   CI - it had broke due to a django upgrade

### Changed

-   Do not enforce Django version according to the Python version (Thanks @arianesc)
-   Upgraded Github Actions
-   Upgraded Poetry
-   Upgraded isort


## [0.4.0] - 2022-06-17

### Added

-   Support for Django v4
-   Poetry for package management.
-   Github Actions for CI.

### Changed

-   Renamed forked package to `django-ufilter`.
-   In `django_ufilter.integrations.drf`, renamed `DjangoFilterBackend` to `DRFFilterBackend`.
-   Import sorter from `importanize` to `isort`.
-   Pin versions on the hooks of the `pre-commit` configuration file.
-   Moved all configurations to `pyproject.toml` on which support exists.
-   `HISTORY.rst` to `CHANGELOG.md` following the KeepAChangelog format.
-   `AUTHORS.rst` to `AUTHORS.md`

### Removed

-   Support for SQLAlchemy.
-   Support for CoreAPI.
-   Support for all unsupported Python versions.
-   Support for all unsupported Django versions.
-   TravisCI and DroneCI.
-   `setup.py`, `setup.cfg`, `requirements*.txt`, `MANIFEST.in`, `Makefile`.
-   `__author__` and `__email__` - These are already available on `pyproject.toml`.

[Unreleased]: https://github.com/Qu4tro/django-ufilter/compare/v0.4.3...HEAD
[0.4.3]: https://github.com/Qu4tro/django-ufilter/releases/tag/v0.4.3
[0.4.0]: https://github.com/Qu4tro/django-ufilter/releases/tag/v0.4.0
