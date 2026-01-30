import unicodedata  # Unicodeデータベースへのアクセスを提供
import os  # ファイル操作を行う


# リネーム処理
def rename_jpg(origin_filepath: str | None = None) -> str | None:
    if origin_filepath is None:
        return None

    try:
        # 新しいファイル名を生成（単なる文字列の編集）
        # 文字列を正規化（NFKCで合成済み文字として扱う）
        normalized_path = unicodedata.normalize("NFKC", origin_filepath)
        new_filepath = (
            normalized_path.replace("ページ", "page")
            if normalized_path.count("ページ") > 0
            else normalized_path
        )

        # ファイルの実際の名前を変更（パスとして扱うために必要な別処理）
        # 置換対象の文字列が画像ファイル名に存在しない場合、
        # 渡ってきた画像パスのまま返却（＝何も処理せずそのまま返却される）
        os.rename(origin_filepath, new_filepath)

        return new_filepath

    except Exception as e:
        print(f"リネーム処理エラー | {e}")
        return None


if __name__ == "__main__":
    rename_jpg()
