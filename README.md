# convert-img-py
ルートの特定フォルダ（`src`）に指定した画像（`jpg`,`png`）のリサイズ及びリネームを実施するPythonスクリプト  
※プログラム実行前に`src`フォルダを用意せずともプログラム実行時に有無を検知して（無ければ）自動的に作成します  
※[`画像 -> pdf`変換ツール](./README.md#utilsimg-to-pdf-画像---pdf変換ツール)も用意しています  

> [!NOTE]
> - 同一ファイル名の画像データはリネーム及びリサイズ処理後に別途フォルダに移動  
> `utils/convert_img.py`内の`adjustedfile_copy_to_numbering_dir`メソッドの処理によって、同一ファイル名の画像データはリネーム及びリサイズ処理後に別途フォルダに移動します。

```bash
# プログラム実行時は一つの引数（希望するリサイズ数値の入力）が必要です
python main.py 960
```

## `utils/img-to-pdf`： `画像 -> pdf`変換ツール
`files` ディレクトリ内の画像（.jpg, .jpeg, .png）をPDFに変換（出力先は`dist`フォルダ）するツール

- `utils\img-to-pdf\image_to_pdf.py`：画像を個別pdfに変換
```py
# convert-img-py\utils\img-to-pdf で以下コマンドを実行
python image_to_pdf.py
```

- `utils\img-to-pdf\images_to_single_pdf.py`：複数画像を一つのpdfに変換
```py
# convert-img-py\utils\img-to-pdf で以下コマンドを実行
python images_to_single_pdf.py
```

## 使用方法
### 仮想環境を構築（初回のみ）
ターミナル／コマンドプロンプトを開いてルート（ファイルの最上階層）にいる状態で以下フローを実行
```bash
mkdir venv # venv ディレクトリ（仮想環境ディレクトリ）を作成
cd venv    # 作成した仮想環境ディレクトリ（`venv`）へ移動

# 新しい仮想環境を作成してアクティベート
# WindowsOS の場合: python -m venv env
python3 -m venv env # env{は仮想環境名}

# WindowsOS の場合: env\Scripts\activate
source env/bin/activate

# 仮想環境をアクティベートした状態で、パス指定して`requirements.txt`から各種ライブラリをインストール
pip install -r ../requirements.txt # `../requirements.txt`なのは`requirements.txt`がルート直下にあるため
```

### 仮想環境を立ち上げる（初回以降）
```bash
# 1. 仮想環境を格納しているディレクトリへ移動（存在しない場合は上記を参照に新規作成）
cd venv

# 2. 仮想環境をアクティベート
# WindowsOS の場合: env\Scripts\activate
source env/bin/activate
```

### `main.py`を実行する
必ず仮想環境をアクティベートした状態で以下フローを実行
```bash
# 仮想環境をアクティベートした直後だと`venv`ディレクトリへいるためルートに移動する
cd ../

# utils ディレクトリへ移動
cd utils

# --- リサイズ及びリネーム処理実行 ---

# WindowsOS の場合:
# python main.py 960

python3 main.py 960 # 960 の部分は任意のリサイズ幅（ピクセル単位）を指定
```
