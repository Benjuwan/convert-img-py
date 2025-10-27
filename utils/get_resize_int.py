import sys  # コマンドライン引数を操作するためのモジュール


# 記事画像のリサイズ値を取得
def get_resize_int() -> int | None:
    try:
        # リサイズ値
        resize_int: int = int(sys.argv[1])
        return resize_int

    except Exception as e:
        print(f"リサイズ値の取得処理エラー | {e}")
        return None


if __name__ == "__main__":
    get_resize_int()
