import glob
import os
import shutil


# 重複ファイル（同一ファイル名）を別フォルダへ移動
def _copy_to_numbering_dir(duplicated_imgfiles: list[str]) -> None:
    try:
        NUMBERING_DIR = "../src/_dist/_numbering"

        if os.path.exists(NUMBERING_DIR) is False:
            print(f"{NUMBERING_DIR} フォルダを新規作成")
            os.makedirs(NUMBERING_DIR)

        for i, imgfile in enumerate(duplicated_imgfiles):
            origin_filename = os.path.basename(imgfile)
            numbering_filename = f"{i + 1}__{origin_filename}"

            # 連番付与したファイルパスを生成し、当該フォルダへとコピー
            dest_path = os.path.join(NUMBERING_DIR, numbering_filename)
            shutil.copy2(imgfile, dest_path)

            # 連番付与前の画像が不要な場合は、上記`copy2`のコードを消して以下一行を有効化する
            # shutil.move(imgfile, dest_path)

            # `imgfile`が`src/_dist`に存在する場合、該当画像ファイル名を表示
            if NUMBERING_DIR.split("/_numbering")[0] in imgfile:
                print(f"- {imgfile} には同一ファイル名が存在しています。")

                # 連番付与前の画像が不要な場合はこの一行、または上記`shutil.move`の部分を有効化する
                # os.remove(imgfile)

    except Exception as e:
        print(f"_copy_to_numbering_dir エラー | {e}")
        return


# リネーム及びリサイズ後、ファイル名に "__" が含まれている場合
# `../src/_dist/_numbering`フォルダへ移動
def adjustedfile_copy_to_numbering_dir(img_file: str = "../src/_dist") -> None:
    try:
        # 同一ファイル名の画像ファイルパス格納リスト
        duplicated_imgfiles = []

        # 指定ディレクトリ以下の（全階層にある）全画像ファイルを再帰的に取得
        all_images = glob.glob(f"{img_file}**/*.*", recursive=True)

        # 重複チェック用に全画像の「ファイル名（拡張子なし）リスト」を作成（※`.count`は完全一致を検知するため）
        all_img_filenames = [os.path.basename(img).split(".")[0] for img in all_images]

        # 画像ファイル名に連番を付与してコピーを作成
        for img in all_images:
            file_name = os.path.basename(img).split(".")[0]

            if all_img_filenames.count(file_name) > 1:
                duplicated_imgfiles.append(img)

        if len(duplicated_imgfiles) > 0:
            _copy_to_numbering_dir(duplicated_imgfiles)

    except Exception as e:
        print(f"リネーム・リサイズ後のファイル移動エラー | {e}")
        return


if __name__ == "__main__":
    adjustedfile_copy_to_numbering_dir()
