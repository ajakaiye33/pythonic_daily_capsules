# import requests
# url = "https://finance.yahoo.com/quote/AAPL?p=AAPL"
#
#
# response = requests.get(url)
# # print(response)
# # print(response.status_code)
#
# indicators = ["Previous Close",
#               "open", "Bid", "Ask", "Day'Range", "Volume", "Avg. Volume", "Market Cap", "Beta", "PE Ratio (TTM)",
#               "EPS (TTM)",
#               "Earnings Date",
#               "Dividend & Yield",
#               "Ex-Dividend Date",
#               "1y Target Est"]
#
#
# # see the text of the html page
#
# htmltext = response.text
# split_lst = htmltext.split("Previous Close")
# after_first_split = split_lst[1].split("\">")
# after_second_split = after_first_split.split("</td>")
# data = after_second_split[0]


from word2number import w2n
print(w2n.word_to_num("one"))
