# LightNetwork
> LightNetwork

#### Video Demo:  [![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/IBxm5wASHvA/0.jpg)](https://youtu.be/IBxm5wASHvA)



>[Try it](https://lightnetwork.onrender.com)

**`https://lightnetwork.onrender.com` Try it**


#### Description:

What is LightNetwork ?

Its a twitter-like web app, but more light and python, javascript are
the building blocks.

What each of the files contains and does?

First, network/urls.py, where the URL configuration for this app is defined.

network/views.py to see the views that are associated with each of these routes.

Notice that several parts of the template are wrapped in a check for if user.is_authenticated, so that different content can be rendered depending on whether the user is signed in or not.

network/models.py. I started with a User model that represents each user of the application. Because it inherits from AbstractUser, it will already have fields for a username, email, password, etc.

certain design choices:

We decided to use bootstraps Modal in when editing posts, since we
think its more user friendly. 


How to run your application?


1. **PostgreSQL and PostGIS**
    - [Download](https://www.postgresql.org/download/) .

    - [Install](https://postgis.net/install/).

2. **`python3.7` and `pip3`**

    >NOTE : Try [WSL](https://ubuntu.com/wsl).

3. **Django and other dependencies**
    `pip3 install -r requirements.txt`

4. **Execute these lines of code**

    `./build.sh` or `sh build.sh`




# credits to:
    (cs50).

    