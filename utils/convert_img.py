import os  # ファイル操作を行う
import sys  # コマンドライン引数を操作するためのモジュール
import glob  # 指定したディレクトリにあるファイルの一覧を取得
from tqdm import tqdm  # プログレスバーを表示するための非標準ライブラリ

from resize_img import resize_jpg
from adjustedfile_copy_to_numbering_dir import adjustedfile_copy_to_numbering_dir


def convert_img(file_dir: str | None = None, FILE_DIR: str | None = None) -> None:
    if file_dir is None:
        return

    try:
        entry_resize_int = sys.argv[1]
        isInt: bool = entry_resize_int.isdecimal()
        if isInt is False or int(entry_resize_int) <= 0:
            print(
                f"正の整数値（リサイズ希望数値）を入力してください。入力されたのは「{entry_resize_int}」です。"
            )
            sys.exit()

        # 指定拡張子の画像をすべて収集（大文字/小文字で別パターンを列挙）
        patterns = ["*.jpg", "*.JPG", "*.jpeg", "*.JPEG", "*.png", "*.PNG"]
        images = []
        for p in patterns:
            images.extend(glob.glob(os.path.join(file_dir, p)))
        # 安定した順序で処理するためソート
        images.sort()

        if FILE_DIR and os.path.exists(FILE_DIR) is False:
            print(f"{FILE_DIR} フォルダが存在しないため作成しました_2")
            os.makedirs(FILE_DIR)
            sys.exit()

        if len(images) == 0:
            print(f"{file_dir} フォルダに画像が見当たりません。")
            sys.exit()

        # 画像のリサイズ処理
        for img in tqdm(images, desc="画像を処理中"):
            resize_jpg(img)

        # リネーム及びリサイズ後に、ファイル名の重複をチェックして同一ファイル名の画像データは別フォルダへ移動（`src/_dist/_numbering`）させる
        adjustedfile_copy_to_numbering_dir()

    except Exception as e:
        print(f"コアモジュール`convert_img`の実行失敗 | {e}")
        return


if __name__ == "__main__":
    convert_img()
