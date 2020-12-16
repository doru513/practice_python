

import zipfile, os
print(os.getcwd())

def backup_to_zip(folder):
  

  folder = os.path.abspath(folder)

  number = 1
  while True:
    
    zip_filename = os.path.basename(folder) + "_" + str(number) + ".zip"
    if not os.path.exists(zip_filename):
      break
    number = number + 1

    #zip作成
  print("Creating {}...".format(zip_filename))
  backup_zip = zipfile.ZipFile(zip_filename, "w")

  for foldername, subfolders, filenames in os.walk(folder):
    print("Adding files in {}...".format(foldername))
    #現在のフォルダをZIPに追加
    backup_zip.write(foldername)
    #現在のフォルダの中の全ファイルをZIPに追加
    for filename in filenames:
      new_base = os.path.basename(folder) + "_"
      if filename.startswith(new_base) and filename.endswith(".zip"):
        continue
      backup_zip.write(os.path.join(foldername, filename))
  backup_zip.close()
  print("Done.")

backup_to_zip("C:\\delicious")