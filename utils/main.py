import os  # ファイル操作を行う
import glob  # 指定したディレクトリにあるファイルの一覧を取得
import sys  # コマンドライン引数を操作するためのモジュール
from tqdm import tqdm  # プログレスバーを表示するための非標準ライブラリ

from resize_img import resize_jpg


def convert_img(file_dir: str) -> None:
    try:
        # 指定拡張子の画像をすべて収集（大文字/小文字で別パターンを列挙）
        patterns = ["*.jpg", "*.JPG", "*.jpeg", "*.JPEG", "*.png", "*.PNG"]
        images = []
        for p in patterns:
            images.extend(glob.glob(os.path.join(file_dir, p)))
        # 安定した順序で処理するためソート
        images.sort()

        if len(images) == 0:
            print(
                f"ルートに`{file_dir}`フォルダが存在しません（この場合は自動的に新規作成します）。または処理対象データが存在しません。"
            )
            # ルートに file_dir フォルダが存在しない場合のみ作成
            if os.path.exists(f"{file_dir}") is False:
                os.mkdir(f"{file_dir}")
            sys.exit()

        # 画像のリサイズ処理
        for img in tqdm(images, desc="画像を処理中"):
            resize_jpg(img)

    except Exception as e:
        print(f"コアモジュール`convert_img`の実行失敗 | {e}")
        return


# 一つ上の階層（ルートディレクトリ）に素材格納フォルダを用意
if len(sys.argv) < 2:
    print("リサイズ希望数値（px）を入力してください。例：960")
    sys.exit()
elif len(sys.argv) > 2:
    print("指定できるコマンドライン引数（リサイズ希望数値）は1つまでです")
    sys.exit()

convert_img("../src")
