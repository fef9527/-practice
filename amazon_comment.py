# 抓取Amazon評論
import urllib.request as req
import bs4
import pandas as pd
url = "https://www.amazon.com/Neocutis-Neo-Firm-D%C3%A9collet%C3%A9-Firming/product-reviews/B07XKF2737/ref=cm_cr_" \
      "dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
# 建立一個request物件,附加request header物件
request = req.Request(url, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                                                   "(KHTML,"" like Gecko) Chrome/102.0.0.0 Safari/537.36"})
with req.urlopen(request)as response:
    data = response.read().decode("utf-8")

# 解析原始碼,取得文章標題
root = bs4.BeautifulSoup(data, "html.parser")
# print(root.prettify())#查看整理過的HTML

Star = []
Comment = []
Title = []
Date = []


star = root.find_all("a", class_="a-link-normal")
for stars in star:
    if stars.i != None:
        sta = stars.span.string.replace("out of 5 stars", "")
        Star.insert(100, sta)


title = root.find_all("a", class_="a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold")
for titles in title:
    # 如果標題中包含a標籤,則印出來
    if titles.span != None:
        ti = titles.span.string
        Title.insert(11, ti)




comment = root.find_all("span", class_="a-size-base review-text review-text-content")
for comments in comment:
    if comments.span != None:
        com = comments.span.string
        Comment.insert(100, com)
     

date = root.find_all("span",{"data-hook":"review-date"})
for dates in date:
    if dates.span == None:
        dat = dates.string.replace("Reviewed in the United States on", "")
        da = dat.replace("January", "1").replace("February", "2").replace("March", "3").replace("April", "4").replace("May", "5").replace("June", "6").replace("July", "7").replace("August", "8").replace("September", "9") .replace("October", "10").replace("November", "11").replace("December", "12").replace(",", "")
        new_da = da[1:]
        date_year = new_da[5:10].replace(" ","")
        date_month= new_da[2:4].replace(" ","")
        date_day = new_da[0:1].replace(" ","")
        DAte =date_year+"/"+date_month+"/"+date_day
        Date.insert(100, DAte)

Data = pd.DataFrame({"Date":Date,"Star":Star,"Title":Title,"Comment":Comment})
Data.to_excel('data.xlsx')



