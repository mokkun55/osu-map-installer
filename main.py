# 必要モジュールのインポート
import glob
import shutil
import subprocess


osu = r"C:\Users\mokku\AppData\Local\osu!\Songs" #osuインストール先
install = r"C:\Users\mokku\Downloads" #ダウンロードフォルダ

file_move = glob.glob(f"{install}\\*osz")

for file_name_i in file_move:
    shutil.move(file_name_i, osu) #iをsongに移動

print("移動が完了しました")

openosu = input("osuを開きますか？  yes(enter)/no(esc)")
if openosu == "" :
    subprocess.Popen(r"C:\Users\mokku\AppData\Local\osu!\osu!.exe")
else :
    exit

exit
