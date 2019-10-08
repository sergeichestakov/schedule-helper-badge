import lxml.html
from urllib.request import urlopen
from bs4 import BeautifulSoup

LISTING_URL = 'https://chrome.google.com/webstore/detail/uc-davis-schedule-helper/eaiohlimbkhifknljidephnpadioaiab?hl=en-US&gl=US'

page = urlopen(LISTING_URL)
soup = BeautifulSoup(page, "html.parser")
num_users = soup.find('span', {'class': 'e-f-ih'}).text
print(num_users)
