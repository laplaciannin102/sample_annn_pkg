# sample_annn_pkg

---

## table of contents

- [sample_annn_pkg](#sample_annn_pkg)
  - [table of contents](#table-of-contents)
  - [how to install](#how-to-install)
  - [Github repository](#github-repository)
  - [ディレクトリ構成](#ディレクトリ構成)
  - [requirements.txtについて](#requirementstxtについて)
  - [.pypirc](#pypirc)
  - [MANIFEST.in](#manifestin)
  - [登録](#登録)
    - [TestPyPI](#testpypi)
    - [PyPI](#pypi)
  - [参考](#参考)
    - [公式](#公式)
    - [Qiita系](#qiita系)
    - [色々](#色々)
    - [sample module](#sample-module)

---

## how to install

```shell
pip install sample_annn_pkg
```

## Github repository

- []

---

## ディレクトリ構成

```
├── .gitignore
├── LICENSE
├── MANIFEST.in
├── README.md
├── sample_annn_pkg
│   ├── __init__.py
│   ├── dependency.py
│   ├── scripts
│   │   ├── __init__.py
│   │   └── command.py
│   └── verify.py
├── requirements.txt
└── setup.py
```

## requirements.txtについて

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

## .pypirc

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

## MANIFEST.in

- 必要なファイルはMANIFEST.inに書き込んでおく

```
include README.md
include README.rst
include requirements.txt
include LICENSE
```

## 登録

### TestPyPI

- TestPyPIへのパッケージアップロード
  - パッケージ情報登録は不要.
  - アップロードするパッケージの`setup.py`があるディレクトリで、下記コマンドを実行.

`python setup.py sdist upload -r testpypi`

- TestPyPIからのインストール
  - 変更後のリポジトリURLからインストールする

`pip install --index-url https://test.pypi.org/simple/ PACKAGE_NAME`

### PyPI
- PyPIへのパッケージアップロード
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

