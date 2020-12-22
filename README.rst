sample_annn_pkg
===============

-  author: laplaciannin102

--------------

Table of Contents
-----------------

-  `sample_annn_pkg`_

   -  `Table of Contents`_
   -  `How to install`_
   -  `Github repository`_
   -  `PyPI repository`_

      -  `TestPyPI`_
      -  `PyPI`_

   -  `Directory structure`_
   -  `Easy installation sample`_
   -  `How to upload pypi package`_

--------------

How to install
--------------

.. code:: shell

   pip install sample_annn_pkg

Github repository
-----------------

-  https://github.com/laplaciannin102/sample_annn_pkg

PyPI repository
---------------

TestPyPI
~~~~~~~~

-  https://pypi.org/project/sample_annn_pkg/

PyPI
~~~~

-  https://test.pypi.org/project/sample_annn_pkg/

--------------

Directory structure
-------------------

::

   sample_annn_pkg
   ├── .gitignore
   ├── LICENSE
   ├── MANIFEST.in
   ├── README.md
   ├── README.rst
   ├── sample_annn_pkg
   │   ├── __init__.py
   │   ├── sample_main_module.py
   │   └── sample_sub_module.py
   ├── requirements.txt
   └── setup.py

Easy installation sample
------------------------

-  command

.. code:: shell

   >> git clone https://github.com/laplaciannin102/sample_annn_pkg.git
   >> cd sample_annn_pkg
   >> python setup.py sdist upload -r testpypi
   >> pip install --index-url https://test.pypi.org/simple/ sample_annn_pkg

-  python

.. code:: python

   >>> import sample_annn_pkg as sap
   >>> sap.func02()
   # success!!
   # poyo

--------------

How to upload pypi package
--------------------------

-  access to this URL

   -  https://github.com/laplaciannin102/sample_annn_pkg/blob/master/docs/how_to_upload_pypi_pkg.md

.. _sample_annn_pkg: #sample_annn_pkg
.. _Table of Contents: #table-of-contents
.. _How to install: #how-to-install
.. _Github repository: #github-repository
.. _PyPI repository: #pypi-repository
.. _TestPyPI: #testpypi
.. _PyPI: #pypi
.. _Directory structure: #directory-structure
.. _Easy installation sample: #easy-installation-sample
.. _How to upload pypi package: #how-to-upload-pypi-package