import qrcode
import random, string

def randomname(n):
    randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
    return ''.join(randlst)

url_row = input("URLをここに入力してください：")
img_name = input("保存する画像の名前を入力してください（拡張子不要,無入力の場合ランダム）：")
if img_name == "":
    img_name = randomname(8)

f_version = input("QRコードのバージョンを指定してください（デフォルト6）：")
version = 6
if f_version != "":
    version = int(f_version)
qr = qrcode.QRCode(
    version=version,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
)
qr.add_data(url_row)
img = qr.make_image(fill_color="black", back_color="white")
img.save(f"img/{img_name}.png")
print(f"QRコード画像がimg/{img_name}.pngに保存されました。")