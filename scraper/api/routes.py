from flask import Flask, request, jsonify, render_template, url_for, redirect, flash
from bs4 import BeautifulSoup
import requests
from api import app, db
#from api.forms import HomeForm
from api.models import History
from api.urlscraper import links
import csv

# Create initial test data.
#def RunningScraper():
#	return links


@app.route("/", methods=['GET', 'POST'] )
@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template('home.html')


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/scrape/all', methods=['GET'])
def api_all():
		#TODO make a render template
		return jsonify(links)

@app.route('/newscrape', methods=['GET'])
def new_scrape():
		#TODO make a render template
		url = 'https://terrasect.com/'
		r = requests.get(url)
		html_content = r.text
		soup = BeautifulSoup(html_content, 'lxml')

		links = soup.find_all('a')
		links = [a.get('href') for a in soup.find_all('a', href=True)]
		#linkadd = jsonify(links)
		history = History()
		db.session.add(history)
		db.session.commit()
		#Writing file
		csv_file = open('cms_scrape.csv', 'w')
		csv_writer = csv.writer(csv_file)
		csv_writer.writerow(['Links'])
		csv_writer.writerow([links])
		csv_file.close()
		return render_template('newscrape.html', links=links)
		#return jsonify(links)

@app.route('/history', methods=['GET'])
def history():
		#TODO make a render template
		historydb = History.query.all()
		return render_template('history.html', historydb=historydb)
		#return jsonify(links)



