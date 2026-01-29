from PIL import Image  # 画像を扱う非標準ライブラリ
import shutil

from rename_img import rename_jpg
from get_resize_int import get_resize_int
from adjustedfile_move_to_numbering_dir import adjustedfile_move_to_numbering_dir


# リサイズ処理
def resize_jpg(img_file: str | None = None) -> None:
    if img_file is None:
        return None

    try:
        # 加工元ファイルをコピー（このコピーファイルが処理対象となる）
        img_file_dist = shutil.copy2(img_file, "../src/_dist")

        renamed_file: str | None = rename_jpg(img_file_dist)

        if renamed_file is None:
            return

        # with文で（リネーム済みパスの）jpgファイルを画像データとして開く
        # with文により処理後自動で閉じられる
        with Image.open(renamed_file) as img:
            width = get_resize_int()  # リサイズ値

            if width is None:
                print("リサイズ値が取得できませんでした。処理を中断します。")
                return

            # アスペクト比を維持したまま幅を指定サイズに
            w_percent: float = width / int(img.size[0])
            # 元画像の 高さ（浮動小数点数）と 幅%を乗算して height 固定値（整数）を算出
            height = int(int(img.size[1]) * w_percent)

            # リサイズ実行
            resized_img = img.resize(
                (width, height),
                # 第二引数は「リサイズ時の補間アルゴリズム」
                # NEAREST （低品質だが高速）, BILINEAR （中程度の品質）, BICUBIC （高品質）
                Image.Resampling.BILINEAR,
            )

            # リサイズ処理した内容で保存
            resized_img.save(
                # 第1引数：保存先のファイルパス（必須）. 以下引数は全てオプション
                renamed_file,  # 変更されたパス（リネーム済みパス）に保存
                # optimize ：Trueの場合、ファイルサイズを最適化
                optimize=True,
                # 画像解像度をタプル形式で指定(x方向: int, y方向: int)
                dpi=(72, 72),
            )

            adjustedfile_move_to_numbering_dir(renamed_file)

    except Exception as e:
        print(f"リサイズ処理エラー | {e}")
        return


if __name__ == "__main__":
    resize_jpg()
