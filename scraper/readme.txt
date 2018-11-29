#URL-Scraper

#Github
	Location: https://github.com/wisniewski915/URLScraper

## Instalation
	We assume that Python, Quasar, and Node have been installed globally on your machine. If not you can follow
	Resource section below, to begin installations.

##Quickstart
	(In this example we are on Windows 10)
	Download the project from Gitub(https://github.com/wisniewski915/URLScraper) we use Sourcetree to clone project to Desktop directory.

	Open Command-Line(cmd)

	Navigate to file directory that has run.py.
	Our location: c:\\Users\John\Desktop\Donescraper\scraper>
	Now we have to set up the db, this use sqlalchemy and set a local file directory db instance
		...scraper>pyhton
		>>from api import db
		>>db.create_all()
		>>from api.models import history
		exit python
		>>exit()
		We will be returned to our orignal directory.
		Now we can launch the app.
		...scraper>pyhton run.py
-----------------------------------------------------------------------------------------------------------------
Command Line print example:
	d:\Program Files\Python\lib\site-packages\flask_sqlalchemy\__init__.py:794: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
  'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
 * Serving Flask app "api" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
d:\Program Files\Python\lib\site-packages\flask_sqlalchemy\__init__.py:794: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
  'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
 * Debugger is active!
 * Debugger PIN: 263-735-185
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [29/Nov/2018 13:57:43] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [29/Nov/2018 13:57:46] "GET /newscrape HTTP/1.1" 200 -
127.0.0.1 - - [29/Nov/2018 13:57:47] "GET /history HTTP/1.1" 200 -
127.0.0.1 - - [29/Nov/2018 13:57:48] "GET /api/v1/resources/scrape/all HTTP/1.1" 200 -
-----------------------------------------------------------------------------------------------------------------
Now we need to copy and paste *http://127.0.0.1:5000/* into a webbroswer. In this case we used Chrome.
We will be greeted with the home screen and a nav drawer on the left.
 -Home: Will open a new app homw
 -Show Scrape: Will show a scrape
 -New Scrape: Will rescrape the webpage and add it to History db, will also put a csv(scsrape) file in the root file.
 -History: Will display date and time of scrape performed.
 	*Top of CMD read out shows d:\ for SQLAlchemy as that is our install locations.

##Rootfolder
	run.py: Will run app when called
	scrape.csv: will be created here during a new scrape

##scraper folder
	Contains Quasar framework import, Quasar was embeded into layout.html


## API folder
	##Tempalte Folder
		Contains .html files with base layout and route layouts
	__init__.py: initializes app
	models.py: contains db instance set up
	routes.py: Contains the routes to pages, runs functions to scrape and write to db, creates csv file	
	urlscraper.py: Contains logic to scrape website
	site.db: Once site is ran, this is the sb file created.


## Resources
	Quasar Intallion
		https://quasar-framework.org/guide/index.html

	Python Flask
		http://flask.pocoo.org/

	Python
		https://www.python.org/

	Node and NPM installation
		https://nodejs.org/en

	Sourcetree
		https://www.sourcetreeapp.com/

	## License
	[MIT](https://choosealicense.com/licenses/mit/)