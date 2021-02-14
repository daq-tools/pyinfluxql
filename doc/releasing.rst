#####################
Release a new version
#####################

- Make sure the working tree is clean
- Update ``CHANGES.rst`` and bump version in ``setup.py``
- Run ``git commit -a -m "Bump version to 0.1.1"``
- Tag repository: ``git tag 0.1.1``
- Push: ``git push && git push --tags``
- Create ``sdist`` package: ``python setup.py sdist``
- Upload to PyPI: ``twine upload --skip-existing --verbose dist/*.tar.gz``
