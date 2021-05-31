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
│   ├── _version.py
│   ├── sample_main_module.py
│   ├── sample_sub_module.py
│   └── datasets
│       ├── __init__.py
│       ├── load_datasets.py
│       └── sample_data
│           ├── sample_data.csv
│           └── sample_data.xlsx
├── tests
│   ├── __init__.py
│   └── test_main_moduleXXX.py
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
>>> df0 = sap.datasets.load_sample_data0() # load csv
# load sample data0
# file format: csv
# sample pandas.DataFrame:
#    col1  col2  col3
# 0     1     2     3
# 1     4     5     6
# 2     7     8     9
>>> df1 = sap.datasets.load_sample_data1() # load excel
# load sample data1
# file format: excel
# sample pandas.DataFrame:
#    col4  col5  col6
# 0  hoge    10    11
# 1  fuga    12    13
# 2  poyo    14    15
# 3  piyo    16    17
```

---

## How to upload pypi package

- access to this URL
  - [https://github.com/laplaciannin102/sample_annn_pkg/blob/master/docs/how_to_upload_pypi_pkg.md](https://github.com/laplaciannin102/sample_annn_pkg/blob/master/docs/how_to_upload_pypi_pkg.md)

