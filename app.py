import lxml.html
from urllib.request import urlopen
from bs4 import BeautifulSoup
from flask import Flask, jsonify

app = Flask(__name__)

LISTING_URL = 'https://chrome.google.com/webstore/detail/uc-davis-schedule-helper/eaiohlimbkhifknljidephnpadioaiab?hl=en-US&gl=US'

@app.route('/users', methods=['GET'])
def get_users():
    page = urlopen(LISTING_URL)
    soup = BeautifulSoup(page, "html.parser")
    num_users = soup.find('span', {'class': 'e-f-ih'}).text

    return jsonify(num_users)

if __name__ == '__main__':
    app.run()
