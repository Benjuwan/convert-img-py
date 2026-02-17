import os
from PIL import Image


def convert_images_to_single_pdf():
    """
    filesディレクトリ内の画像をすべてまとめて1つのPDFに変換し、distディレクトリに保存するスクリプト
    対応フォーマット: .jpg, .jpeg, .png
    """
    files_dir = "files"
    dist_dir = "dist"
    output_filename = "all_images.pdf"

    # 対応する拡張子
    extensions = (".jpg", ".jpeg", ".png")

    # dist または filesディレクトリが存在しない場合は作成
    if not os.path.exists(dist_dir) or not os.path.exists(files_dir):
        try:
            if not os.path.exists(dist_dir) and not os.path.exists(files_dir):
                os.makedirs(dist_dir)
                os.makedirs(files_dir)
                print(f"ディレクトリを作成しました: {dist_dir}, {files_dir}")
            elif not os.path.exists(dist_dir):
                os.makedirs(dist_dir)
                print(f"ディレクトリを作成しました: {dist_dir}")
            elif not os.path.exists(files_dir):
                os.makedirs(files_dir)
                print(f"ディレクトリを作成しました: {files_dir}")
        except OSError as e:
            print(f"ディレクトリ作成エラー: {e}")
            return

    # filesディレクトリ内のファイルを取得
    if not os.path.exists(files_dir):
        print(f"エラー: '{files_dir}' ディレクトリが見つかりません。")
        return

    # ファイル名順にソートして読み込む（ページ順序を確定させるため）
    files = sorted([f for f in os.listdir(files_dir) if f.lower().endswith(extensions)])

    if not files:
        print(
            f"'{files_dir}' ディレクトリ内に画像ファイル(jpg, jpeg, png)が見つかりませんでした。"
        )
        return

    print(f"{len(files)} 枚の画像を検出しました。1つのPDFに結合を開始します...")

    images = []
    try:
        # 画像をすべて開いてRGB変換し、リストに格納
        for filename in files:
            image_path = os.path.join(files_dir, filename)
            img = Image.open(image_path).convert("RGB")
            images.append(img)
            print(f"読み込み: {filename}")

        if images:
            output_path = os.path.join(dist_dir, output_filename)

            # 最初の画像をベースに、残りの画像をappendして保存
            # images[0] を保存し、images[1:] を追加する
            first_image = images[0]
            rest_images = images[1:]

            first_image.save(output_path, save_all=True, append_images=rest_images)
            print(f"変換完了: {os.path.basename(output_path)} を作成しました。")

    except Exception as e:
        print(f"変換失敗: {e}")

    print("すべての処理が完了しました。")


if __name__ == "__main__":
    convert_images_to_single_pdf()
