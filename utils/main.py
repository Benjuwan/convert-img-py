import os  # ファイル操作を行う
import sys  # コマンドライン引数を操作するためのモジュール

from convert_img import convert_img

# 画像素材フォルダのパス（※`_dist`は処理画像の保存場所）
FILE_DIR: str = "../src/_dist"

if len(sys.argv) < 2:
    # ルートに FILE_DIR フォルダが存在しない場合のみ作成
    if os.path.exists(FILE_DIR) is False:
        print(f"{FILE_DIR} フォルダが存在しないため作成しました")
        # `.makedirs`： 再帰的にフォルダ作成を実施（`src`dir がなければソレを作ってから`_dist`dir を作成する）
        os.makedirs(FILE_DIR)
        sys.exit()
    else:
        print("リサイズ希望数値（px）を入力してください。例：960")
        sys.exit()

elif len(sys.argv) > 2:
    print("指定できるコマンドライン引数（リサイズ希望数値）は1つまでです")
    sys.exit()

convert_img("../src")
