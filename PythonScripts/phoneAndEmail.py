import pyperclip,re

phone_regex =  re.compile(r"""(
  (\d{3}|\(\d{3}\))?
  (\s|-|\.)?
  (\d{3})
  (\s|-|\.)
  (\d{4})
  (\s*(ext|x|ext.)\s*(\d{2,5}))?
)""", re.VERBOSE)

#電子メール
email_regex = re.compile(r"""(
  [a-zA-Z0-9._%+-]+ #ユーザー名
  @                 #@
  [a-zA-Z0-9.-]+    #ドメイン
  (\.[a-zA-Z]{2,4}) #.なんか
)""", re.VERBOSE)

#クリップボード
text = str(pyperclip.paste())
matches = []
for groups in phone_regex.findall(text):
  phone_num = "-".join([groups[1], groups[3], groups[5]]) #groups[0]は？
  print("group[0]: "+groups[6])
  if groups[8] != "":
    phone_num += " x" + groups[8]
  matches.append(phone_num)
for groups in email_regex.findall(text):
  matches.append(groups[0])

#検索結果
if len(matches) > 0:
  pyperclip.copy("\n".join(matches))
  print("クリップボードにコピーされました:")
  print("\n".join(matches))
else:
  print("みつかりませんでした")