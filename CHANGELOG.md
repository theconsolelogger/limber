# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]


## [0.2.0] - 2020-12-27
### Changed
- Upgrade limberframework to version 0.2.0.

## [0.1.1] - 2020-08-11
### Added
- CACHE_PATH environment variable for use with the FileStore class.

### Changed
- Update limberframework to 0.1.1.
- Application base_path construction.

## [0.1.0] - 2020-08-10
### Added
- Documentation files: README.md; LICENSE.txt; CONTRIBUTING.md; CODEOFCONDUCT.md; and, CHANGELOG.md.
- Project files: Pipfile; Pipfile.lock; setup.py; .gitignore; .python-version.
- Routing mechanism for API routes.
- Alembic for database migrations.
- User and ApiKey models and migration scripts.
- Configurations for app, cache, and database.
- Add storage and cache folders for caching system.
- Add http folders for handling requests and generating responses.
- Create welcome route.
- Establish main script to setup the application.

### Changes
- Pipenv to poetry for package management.
