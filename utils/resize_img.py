from PIL import Image  # 画像を扱う非標準ライブラリ
import shutil

from rename_img import rename_jpg
from get_resize_int import get_resize_int


# リサイズ処理
def resize_jpg(origin_filepath: str | None = None) -> None:
    if origin_filepath is None:
        return None

    try:
        # 加工元ファイルをコピー（このコピーファイルが処理対象となる）
        origin_filepath_dist = shutil.copy2(origin_filepath, "../src/_dist")

        renamed_filepath = rename_jpg(origin_filepath_dist)

        if renamed_filepath is None:
            return

        # with文で（リネーム済みパスの）jpgファイルを画像データとして開く
        # with文により処理後自動で閉じられる
        with Image.open(renamed_filepath) as img:
            # リサイズ値取得
            resized_width: int | None = get_resize_int()

            if resized_width is None:
                print("リサイズ値が取得できませんでした。処理を中断します。")
                return

            # アスペクト比を維持したまま幅を指定サイズに
            w_percent: float = resized_width / int(img.size[0])
            # 元画像の 高さ（浮動小数点数）と 幅%を乗算して height 固定値（整数）を算出
            height = int(int(img.size[1]) * w_percent)

            # リサイズ実行
            resized_img = img.resize(
                (resized_width, height),
                # 第二引数は「リサイズ時の補間アルゴリズム」
                # NEAREST （低品質だが高速）, BILINEAR （中程度の品質）, BICUBIC （高品質）
                Image.Resampling.BILINEAR,
            )

            # リサイズ処理した内容で保存
            resized_img.save(
                # 第1引数：保存先のファイルパス（必須）. 以下引数は全てオプション
                renamed_filepath,  # 変更されたパス（リネーム済みパス）に保存
                # optimize ：Trueの場合、ファイルサイズを最適化
                optimize=True,
                # 画像解像度をタプル形式で指定(x方向: int, y方向: int)
                dpi=(72, 72),
            )

    except Exception as e:
        print(f"リサイズ処理エラー | {e}")
        return


if __name__ == "__main__":
    resize_jpg()
