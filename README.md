# Cab-Booking-Sytsem

Instructions:
* `pip install -r requirements.txt`
* `python manage.py syncdata`
* `python manage.py makmigrations`
* `python manage.py migrate` 
* `python manage.py runserver`
# API endpoints to visit
* http://127.0.0.1:8000/cab/user/register —- for registering user (the data will be saved in User table )

* http://127.0.0.1:8000/cab/user/login —-  for logging in the application(login using email and password)

    input must be in JSON form 
    e.g.: {“email”:(your registered email ID),”pswd”:”(Your pswd)”}

* http://127.0.0.1:8000/cab/user/set/location —- after logging in you will be redirected to this page
    Here Enter the source and destination of your Ride in the given placeholders.
* To view the path of Ride Click on “See in Map” Button
* To check the availability of Cab Click on “Back to DRF” button — this will redirect to http://127.0.0.1:8000/cab/bookings/available(Blank list appears, since no Cab details are available in database)


**NOTE** : Database schema is well explained in **Schema.png**