Coding Grace README

# Steps to get django site running locally on your machine
- `heroku login`

## If you haven't forked the heroku app before. (Ref: [Forking App on Heroku](https://devcenter.heroku.com/articles/fork-app))
`heroku fork -a sourceapp targetapp`


Where `sourceapp` is `coding-grace`.

This will give you an instance to the live database, and also port over the apps installed with it automagically.

Now we will export the environment settings:

`eval $(heroku config -a <app> --shell | sed -E 's/^([A-Z_]+=)(.*)/export \1"\2"/g')` where `<app>` is the name of your heroku app.

To see if this works, type the following in your terminal. 

`echo $DJANGO_SECRET_KEY`

This is a custom environment variable. 

`echo echo $DATABASE_URL`

Compare with the database URL in your app settings via Heroke dashboard. They should be the same.

You can see your forked heroku app on <targetapp>.herokuapp.com.

To run is locally:

`python manage.py runserver --settings=codinggrace_django.settings_heroku_dev`


# Handy stuff
## Adding a new social application to allauth
Social Accounts › Social applications

## Getting latest database snapshot
Get latest copy of the data and overides the targetapp's database

Example: `heroku pgbackups:transfer --app coding-grace-dev coding-grace::CHARCOAL HEROKU_POSTGRESQL_OLIVE`

You can get the pg names from your dashboard.

# Mentions
Navy bg image from http://subtlepatterns.com/navy/

# Quesions?
Email: website@codinggrace.com


ARCHIVE

# Previous way of running locally on your machine
python manage.py runserver --settings=codinggrace_django.settings