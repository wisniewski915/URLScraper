from flask import Flask, request, jsonify, render_template, url_for, redirect, flash
from bs4 import BeautifulSoup
import requests
from api import app, db
#from api.forms import HomeForm
from api.models import History
from api.urlscraper import links, RunScraper
import csv


#TODO: add a Runction check and display if any errors


#Home Routing
@app.route("/", methods=['GET', 'POST'] )
@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template('home.html')


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/scrape/all', methods=['GET'])
def api_all():
		#Shows the latest scrape
		return jsonify(links)

@app.route('/newscrape', methods=['GET'])
def new_scrape():
		#When called will generate a new scrape, and write to csv file, and add to history
		#TODO Define these in another location
		RunScraper()
		#linkadd = jsonify(links)
		history = History()
		db.session.add(history)
		db.session.commit()
		#Writing file
		csv_file = open('scrape.csv', 'w')
		csv_writer = csv.writer(csv_file)
		csv_writer.writerow(['Links'])
		csv_writer.writerow([links])
		csv_file.close()
		return render_template('newscrape.html', links=links)


@app.route('/history', methods=['GET'])
def history():
		#Show DB Date and time
		historydb = History.query.all()
		return render_template('history.html', historydb=historydb)




