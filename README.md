# geo_app
django restful api consumer example app


This is a simple app that just dose a geo-lookup on an ip address
The sample IP is in views.py
The API is hardcoded in views.py (I know... this is bad, bad practice)

Instructions:

1.  create your virtual environment
2.  clone this repo
3.  pip install the requirements.txt
4.  run migrations (python manage.py migrate) ... this is optional as there are no DB models in this application
5.  start django and go to:  http://127.0.0.1:8000/
6.  If you see 'Requested IP:' and 'Country:' with values of  108.4.16.142 and United States, it worked.

Note this is a cheesey app that just illustrates how to render results from a RESTful API and how to integrate bootstrap into your templates.
