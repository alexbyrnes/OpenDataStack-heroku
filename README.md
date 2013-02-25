OpenDataStack-heroku
====================

Open Data Stack for Heroku

Clone this repo

    $ git clone https://github.com/alexbyrnes/OpenDataStack-heroku.git
  
[Install and log in to heroku](https://devcenter.heroku.com/articles/quickstart):

    $ wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh
    $ heroku login

Create app:

    $ cd OpenDataStack-heroku
    $ heroku create opendatastack -s cedar
    $ git push heroku master
    $ heroku ps:scale web=1

Add a free dev instance of Postgres:

    $ heroku addons:add heroku-postgresql:dev

(note color of your database 'HEROKU_POSTGRESQL_<COLOR>_URL')

Get the connection string for your database:

    $ heroku config | grep HEROKU_POSTGRESQL

Edit config.py so 'HEROKU_POSTGRESQL_PURPLE_URL' matches the color of your database:

    $ vim config.py
    $ git commit -am 'Added connection string'
    $ git push heroku master
    
Add some data:

    $ curl https://data.cityofchicago.org/api/views/28km-gtjn/rows.csv?accessType=DOWNLOAD | csvsql  --no-constraints --insert --table firehouses --db "<DB_CONNECTION_STRING>"

View the data through your app:

    $ curl http://<YOUR APP>.herokuapp.com/api/action/datastore_search_sql?q=select%20*%20from%20firehouses  


    
