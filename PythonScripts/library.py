#! python3
import requests, bs4, os, sys, time, re
from selenium import webdriver

#スタート
print("ようこそ")
print("東京情報大学図書館の図書の情報取得します。")
print("東京情報大学図書館のサービスセンターにアクセスします。")
time.sleep(3)

#サービスセンターにアクセス
browser = webdriver.Chrome("C:\\Users\\j19275ht\\chromedriver.exe")
browser.get("https://www-std01.ufinity.jp/tuislib/?page_id=13")
#サービスセンターの検索ボックスにアクセス
input_library = browser.find_element_by_class_name("opac_keyword_input")


time.sleep(1)
#コマンドラインでサービスセンターで読みたい本の名前を検索

#TODO ここで、for文で複数の本を選択できるようにしたい（負荷をかけないようにするため）
#なにか変数に入れて検索をかけていく
if len(sys.argv) > 1:
  input_library.send_keys(sys.argv[1])
#コマンドラインがなければinput()で入れる
else:
  print("検索する本の名前を入力してください: ")
  input_library.send_keys(input())
#検索

time.sleep(1)
print("本のタイトルを取得しています")
time.sleep(1)
input_library.submit()

time.sleep(3)
#TODO ここで検索を止めないようにするためコマンドライン引数のlenが終わったら終了、余ってたら次にするためのif文を使う
try:
  browser.get(browser.current_url)
except:
  print("検索結果は存在しませんでした。")
  print("終了します")
  browser.close()
  exit()

#なぜか2重アクセスされるためここでsllep
time.sleep(3)

html = browser.page_source.encode('utf-8')
soup = bs4.BeautifulSoup(html, "html.parser")
#本の名前と請求記号、資料ID、状態を取得

book_title_html = soup.select('.opac_book_title')
book_symbol_html = soup.select(".seikyu > a")
book_id_html = soup.select(".siryoid")
book_status_html = soup.select(".jyoutai")
book_first_number = soup.select(".opac_list_no_area")


book_title = str(book_title_html[0].getText())
try:
  book_symbol = str(book_symbol_html[0].getText())
except IndexError:
  #TODO できればここで一番上の検索結果を取りたい。
  print("検索結果が複数あります。")
  print("タイトルが抽象的な可能性があります。")
  print("終了します")
  browser.close()
  exit()


book_id = str(book_id_html[1].getText())
book_status = str(book_status_html[1].getText())

#もし状態が配架済、整理中なら次へ、そうでなければprint(貸し出されているか、予約されています)
if book_status == "配架済" or book_status == "整理中":
  library_write = open("C:\\Users\\j19275ht\\Desktop\\library_infomation.txt", "a")
  library_write.write(book_title + ",")
  library_write.write(book_symbol + ",")
  library_write.write(book_id)
  library_write.close()
  print("本の情報の書き込みが終了しました")
  print("終了します")
else:
  print("この本はすでに借りられているか、予約されています")
  print("終了します")

browser.close()
exit()