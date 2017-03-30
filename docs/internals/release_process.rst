Release Process
===============

1. Update local checkout

   Make sure your developer checkout of VOC is up to date with a::

    $ git pull

2. Confirm that the trunk currently builds for JDK and Android::

    $ ant clean
    $ ant

   Fix any problems that are identified

3. Make release related changes

  * **Release history** in ``docs/internals/releases.rst``
  * **Build number** in ``build.xml``
  * **Version number** in ``voc/__init__.py``

4. Push to Github to get confirmation of a clean CI build.

5. When CI passes, merge.

6. Update your checkout of the main ``pybee/voc`` repository

7. Tag the release. There is a version tag for VOC, plus tags for each
   of the support libraries that will be released::

    $ git tag v0.1.2
    $ git tag 3.4-b3
    $ git tag 3.5-b3
    $ git tag 3.6-b3
    $ git push —tags

8. Build the PyPI packages::

    $ python setup.py sdist bdist_wheel

9. Upload the PyPI packages::

    $ twine upload dist/voc-0.1.2*

10. Create the GitHub release for each support package versions, and upload
    the support zipfile.

11. Check that Read The Docs has updated
