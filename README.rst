i2a
===

i2a creates ASCII art from images right on your terminal.

Installation
------------

Step 1: Install dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

OSX:
````

.. code:: bash

    $ brew install libtiff libjpeg webp little-cms2

Linux (Ubuntu):
```````````````

.. code:: bash

    $ sudo apt-get build-dep python-imaging
    $ sudo apt-get install libjpeg8 libjpeg62-dev libfreetype6 libfreetype6-dev

For other operating systems, check out the instructions
`on this page <http://pillow.readthedocs.org/en/latest/installation.html>`__ .

Step 2: Install i2a
~~~~~~~~~~~~~~~~~~~

Option 1: `Pip <https://pypi.python.org/pypi/i2a>`__
````````````````````````````````````````````````````

.. code:: bash

    $ pip install i2a

Option 2: From source
`````````````````````

.. code:: bash

    $ git clone --recursive http://github.com/mavidser/i2a.git
    $ cd i2a/
    $ python setup.py install

Usage
-----

Basic usage
~~~~~~~~~~~

.. code:: bash

    $ i2a image.jpg

Colored output
~~~~~~~~~~~~~~

.. code:: bash

    $ i2a --colors image.jpg

Write the art to a file
~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    $ i2a image.jpg > ascii.txt

If the terminal has a light background
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    $ i2a image.jpg --invert

or

::

    $ i2a image.jpg --bg=BLACK

Options
-------

A complete list of available options:

-  ``--colors`` : Show colored output. i2a assumes that the terminal
   supports 256 colors.
-  ``--bold`` : Show bold characters. Makes the output is easier on eyes.
-  ``--invert`` : Invert the colors. Suitable for a light background.
-  ``--bg=(BLACK|WHITE)``: Specify your own background color.
-  ``--height=<val>`` : Set the height in number of characters.
-  ``--width=<val>`` : Set the width in number of characters.
-  ``--contrast=<factor>`` : Manually set contrast (default value: 1.5,
   for original image: 1.0).
-  ``--alt-chars`` : Use an alternate set of (more detailed) characters.

Contributing
------------

-  Create an issue in the `issue
   tracker <https://github.com/mavidser/i2a/issues>`__ describing the
   feature.
-  Fork the project.
-  Create a new branch - ``git checkout -b new-feature``
-  Commit the changes and push to your branch -
   ``git push origin new-feature``
-  Open a `pull request <https://github.com/mavidser/i2a/pulls>`__,
   referencing the issue you created.

License
-------

See the
`LICENSE <https://github.com/mavidser/i2a/blob/master/LICENSE>`__ file.

