from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid
import validators
import psycopg2
import random

# configuration
DEBUG = True


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

con = psycopg2.connect(
  database="postgres",
  user="postgres",
  password="tonimo83",
  host="127.0.0.1",
  port="5432")
cursor = con.cursor()

URLS = []

@app.route('/books', methods=['GET', 'POST'])
def all_url():


    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        URLS.clear()
        url = post_data.get('url')
        if validators.url(url) == True:
            hash = 'http://{}/{}'.format('client', uuid.uuid4().hex)

            cursor.execute("INSERT INTO URLS (ID, URL, HASH) VALUES ({}, '{}', '{}')".format(random.randint(0, pow(10, 6)),url, hash))
            con.commit()
            response_object['message'] = 'Book added!'


            cursor.execute("SELECT id, url, hash from URLS")
            rows = cursor.fetchall()

            URLS.append({
                'url': rows[-1][1],
                'hash': rows[-1][2]
            })

            response_object['urls'] = URLS

    else:
        if len(URLS) == 0:
            return jsonify("Incorrect link specified")
        else:
            response_object['urls'] = URLS

    return jsonify(response_object)

if __name__ == '__main__':
    app.run()