# sample_annn_pkg

- author: laplaciannin102

---

## Table of Contents

- [sample_annn_pkg](#sample_annn_pkg)
  - [Table of Contents](#table-of-contents)
  - [How to install](#how-to-install)
  - [Github repository](#github-repository)
  - [PyPI repository](#pypi-repository)
    - [TestPyPI](#testpypi)
    - [PyPI](#pypi)
  - [Directory structure](#directory-structure)
  - [Easy installation sample](#easy-installation-sample)
  - [How to upload pypi package](#how-to-upload-pypi-package)

---

## How to install

```shell
pip install sample_annn_pkg
```

## Github repository

- [https://github.com/laplaciannin102/sample_annn_pkg](https://github.com/laplaciannin102/sample_annn_pkg)

## PyPI repository

### TestPyPI

- [https://pypi.org/project/sample_annn_pkg/](https://pypi.org/project/sample_annn_pkg/)

### PyPI

- [https://test.pypi.org/project/sample_annn_pkg/](https://test.pypi.org/project/sample_annn_pkg/)

---

## Directory structure

```
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
```

## Easy installation sample

- command

```shell
>> git clone https://github.com/laplaciannin102/sample_annn_pkg.git
>> cd sample_annn_pkg
>> python setup.py sdist upload -r testpypi
>> pip install --index-url https://test.pypi.org/simple/ sample_annn_pkg
```

- python

```python
>>> import sample_annn_pkg as sap
>>> sap.func02()
# success!!
# poyo
```

---

## How to upload pypi package

- access to this URL
  - [https://github.com/laplaciannin102/sample_annn_pkg/blob/master/docs/how_to_upload_pypi_pkg.md](https://github.com/laplaciannin102/sample_annn_pkg/blob/master/docs/how_to_upload_pypi_pkg.md)

