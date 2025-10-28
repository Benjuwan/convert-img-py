import os  # ファイル操作を行う
import sys  # コマンドライン引数を操作するためのモジュール

from convert_img import convert_img

# 画像素材フォルダのパス
FILE_DIR: str = "../src"

if len(sys.argv) < 2:
    # ルートに FILE_DIR フォルダが存在しない場合のみ作成
    if os.path.exists(FILE_DIR) is False:
        print(f"{FILE_DIR} フォルダが存在しないため作成しました")
        os.mkdir(FILE_DIR)
        sys.exit()
    else:
        print("リサイズ希望数値（px）を入力してください。例：960")
        sys.exit()

elif len(sys.argv) > 2:
    print("指定できるコマンドライン引数（リサイズ希望数値）は1つまでです")
    sys.exit()

convert_img("../src")
