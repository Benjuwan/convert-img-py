import os
from PIL import Image


def convert_images_to_pdf():
    """
    filesディレクトリ内の画像をPDFに変換し、distディレクトリに保存するスクリプト
    対応フォーマット: .jpg, .jpeg, .png
    """
    files_dir = "files"
    dist_dir = "dist"

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

    files = [f for f in os.listdir(files_dir) if f.lower().endswith(extensions)]

    if not files:
        print(
            f"'{files_dir}' ディレクトリ内に画像ファイル(jpg, jpeg, png)が見つかりませんでした。"
        )
        return

    print(f"{len(files)} 枚の画像を検出しました。変換を開始します...")

    for filename in files:
        image_path = os.path.join(files_dir, filename)
        name_without_ext = os.path.splitext(filename)[0]

        # PDFとして保存（Pillowでは `save()`メソッド※ で拡張子を`.pdf`にするだけで画像をPDFに変換できる）
        pdf_path = os.path.join(dist_dir, f"{name_without_ext}.pdf")

        try:
            with Image.open(image_path) as image:
                # PDF保存のためにRGBモードに変換（透過PNGなどの対策）
                rgb_image = image.convert("RGB")
                # ※PDFとして保存
                rgb_image.save(pdf_path)
                print(f"変換完了: {filename} -> {os.path.basename(pdf_path)}")
        except Exception as e:
            print(f"変換失敗: {filename} - {e}")

    print("すべての処理が完了しました。")


if __name__ == "__main__":
    convert_images_to_pdf()
