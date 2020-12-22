# sample_annn_pkg

- author: laplaciannin102
- date: 2020/12/23

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
  - [各ファイルの説明 or 書き方](#各ファイルの説明-or-書き方)
    - [README.md / README.rst](#readmemd--readmerst)
    - [LICENSE](#license)
    - [requirements.txt](#requirementstxt)
    - [MANIFEST.in](#manifestin)
    - [.pypirc](#pypirc)
  - [登録](#登録)
    - [前提](#前提)
    - [TestPyPI](#testpypi-1)
    - [PyPI](#pypi-1)
  - [参考](#参考)
    - [公式](#公式)
    - [Qiita系](#qiita系)
    - [色々](#色々)
    - [sample module](#sample-module)

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

## 各ファイルの説明 or 書き方

### README.md / README.rst

- README.md: Githubに表示するためのMarkdown形式Readmeファイル
- README.md: PyPIに表示するためのsetup.pyからlong_descriptionとして読み込むためのRST形式Readmeファイル
  - RST: reStructuredTextの略.
  - `pandoc --from markdown --to rst` 等でRST形式に変換してしまうと楽.

### LICENSE

- MITなどのライセンス情報を記入.

### requirements.txt

```
# pypiに存在するパッケージ名はそのまま書いていい
numpy
# バージョン指定したいときは等式を使う
scipy == 1.2.2
# pypiに存在しないパッケージの時は git://リポジトリのURL.git
git://git@github.com/foo/foo.git
# プライベートリポジトリの場合は+sshをつける git+ssh://git@github.com/foo/foo.git
git+ssh://git@github.com/foo/foo.git
```

### MANIFEST.in

- 必要なファイルはMANIFEST.inに書き込んでおく

```
include README.md
include README.rst
include requirements.txt
include LICENSE
```

### .pypirc

- C:\Users\<user> ディレクトリに.pypircというファイルを作成する
  - C:\Users\<user>\.pypirc

- 中身
  - PyPIとTestPyPIに登録した際のユーザ名とパスワードを書き込む

```
[distutils]
index-servers =
  pypi
  testpypi

[pypi]
repository=https://upload.pypi.org/legacy/
username=<PyPI username>
password=<PyPI password>

[testpypi]
repository=https://test.pypi.org/legacy/
username=<TestPyPI username>
password=<TestPyPI password>
```


---

## 登録

### 前提

- 最終的には **PyPI** に登録するが, 先に試験的に **TestPyPI** に登録することができる.

- 先に **.pypirc** の作成をしておく必要がある.

### TestPyPI

- TestPyPIへのパッケージアップロード.
  - パッケージ情報登録は不要.
  - アップロードするパッケージの`setup.py`があるディレクトリで, 下記コマンドを実行.

`python setup.py sdist upload -r testpypi`

- TestPyPIからのインストール.
  - 変更後のリポジトリURLからインストールする.

`pip install --index-url https://test.pypi.org/simple/ <PACKAGE_NAME>`

### PyPI

- PyPIへのパッケージアップロード.
  - TestPyPIと同様にパッケージ情報登録は不要.

`python setup.py sdist upload`

---

## 参考

### 公式

- [6. Python Package Index (PyPI)](https://docs.python.org/ja/3.6/distutils/packageindex.html)
- [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)

### Qiita系

- [（インターン向けに書いた）Pythonパッケージを作る方法](https://qiita.com/Ultra-grand-child/items/7717f823df5a30c27077)

- [自作のPythonパッケージをPyPIに登録してpip install可能にする](https://qiita.com/shonansurvivors/items/0fbcbfde129f2d26301c)

- [PyPIデビューしたい人の為のPyPI登録の手順](https://qiita.com/kinpira/items/0a4e7c78fc5dd28bd695)

- [PyPI 新URLへの登録・アップロード](https://qiita.com/ukiuki-satoshi/items/77ef1e39598226f1cff7)

### 色々

- [PyPIに自作パッケージを登録する際にrequirements.txtを使用する方法](https://trsasasusu.com/blog/53/)

### sample module

- [github.com/navdeep-G/samplemod](https://github.com/kennethreitz/samplemod)

