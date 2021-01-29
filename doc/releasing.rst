#####################
Release a new version
#####################

- Update ``CHANGES.rst``
- Run ``git commit -m "Bump version to 0.1.1"``
- Tag repository: ``git tag 0.1.1``
- Push: ``git push && git push --tags``
- Create ``sdist`` package: ``python setup.py sdist``
- Upload to PyPI: ``twine upload --skip-existing --verbose dist/*.tar.gz``
