import shutil
import os
import sys
import datetime

# バックアップを取得したいディレクトリのパス
backup_src_directory_path = "./src/"

# バックアップ先のディレクトリのパス
backup_dist_directory_path = "./backup/" 

# ディレクトリの一覧を入れるリスト
directory_list = []

# バックアップを取得したいディレクトリがなければ終わる
if os.path.isdir(backup_src_directory_path) == False:
  print("バックアップ先のディレクトリがありません")
  sys.exit()

# バックアップ先のディレクトリがなければ作成する
if os.path.isdir(backup_dist_directory_path) == False:
  os.mkdir(backup_dist_directory_path)

# 今回バックアップファイルをすべて入れるディレクトリを作成する
backup_dist_directory_path += datetime.datetime.now().strftime("%Y%m%d") + "/"
os.mkdir(backup_dist_directory_path)

# バックアップを取得したいディレクトリの一覧を取得する
directory_list = os.listdir(backup_src_directory_path)

for filename in directory_list:
  try:
    # ディレクトリならば
    if os.path.isdir(backup_src_directory_path + filename):
      shutil.copytree(backup_src_directory_path + filename, backup_dist_directory_path + filename)
    # ディレクトリでなければ
    else:
      shutil.copy2(backup_src_directory_path + filename, backup_dist_directory_path + filename)
    
  except Exception as e:
    print(e)
    print("バックアップに異常が発生しました")

