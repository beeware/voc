Release Process
===============

.. note:: For Developers Only!

    This guide is provided for the benefit of the VOC team. As an end user,
    you shouldn't ever need to use these instructions.

So, it's time for a new VOC release! Here's how to publish a new version so
others can benefit from the changes that have been made recently.

1. Update local checkout

   Make sure your developer checkout of VOC is up to date with a::

    $ git pull

2. Confirm that the trunk currently builds for JDK and Android on each version
   of Python you're planning to support::

    $ ant clean
    $ ant

   Fix any problems that are identified

3. Make release related changes

  * **Release history** in ``docs/background/releases.rst``
  * **Build number** in ``build.xml``
  * **Version number** in ``voc/__init__.py``

4. Push to Github to get confirmation of a clean CI build.

5. When CI passes, merge.

6. Update your checkout of the main ``beeware/voc`` repository

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

10. Check that you have AWS credentials in a file named  ``.env`` file in the
    root directory of your project checkout::

    AWS_ACCESS_KEY_ID=...
    AWS_SECRET_ACCESS_KEY=...
    AWS_REGION=us-west-2

11. Upload the support zipfile to S3::

    $ python tools/upload b3

11. Check that Read The Docs has updated.
