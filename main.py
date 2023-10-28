# 必要モジュールのインポート
import glob
import shutil
import subprocess

from dotenv import load_dotenv
import dotenv
load_dotenv()

import os

setup = os.getenv('setup')

# osu = r"C:\Users\mokku\AppData\Local\osu!\Songs" #osuインストール先
# install = r"C:\Users\mokku\Downloads" #ダウンロードフォルダ

def main():
    osu = os.getenv('osu')
    install = os.getenv('install')
    osu_exe = os.getenv('osu_exe')

    file_move = glob.glob(f"{install}\\*osz")

    for file_name_i in file_move:
        shutil.move(file_name_i, osu) #iをsongに移動

    print("移動が完了しました")

    openosu = input("osuを開きますか？  yes(enter)/no(esc)")
    if openosu == "" :
        subprocess.Popen(osu_exe)
    else :
        exit

if setup != '1' :
    print('初回起動ですファイルの初期設定をします')
    dotenv_file = dotenv.find_dotenv() #envファイル
    dotenv.set_key(dotenv_file, "setup", '1') #書き換え

    set_osu = input('osuインストール先:')
    dotenv.set_key(dotenv_file, "osu", set_osu+'\Songs')
    dotenv.set_key(dotenv_file, "osu_exe", set_osu+'\osu!.exe')

    set_install = input('ダウンロードフォルダ:')
    dotenv.set_key(dotenv_file, "install", set_install)

    main()
else :
    main()

exit
