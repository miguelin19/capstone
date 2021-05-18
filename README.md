# Casting agency

Capstone project for the Udacity Full stack nanodegree.

API for a casting agency with three roles (assistant, director, producer) which have different permissions managing the movies and actors.

webpage URL: https://smiguel-capstone.herokuapp.com/

Heroku-git repo: https://git.heroku.com/smiguel-capstone.git

## Installing Dependencies

### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

### Setting up the Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

### Installing the pip dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:
```
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.

#Running the server locally

Make the changes necessary to config.py nd execute the following commands:
```
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
```
## Roles and permissions:

-Casting Assistant

permissions-
```
get:actors|get:movies
```
login-
```
email:celiacarra@gmail.com
password:Password01!
```

-Casting Director

permissions-
```
get:actors|get:movies 
delete:actors|post:actors
patch:actors|patch:movies
```
login-
```
email:miguel_carra19@hotmail.com
password:Password01!
```
-Executive Producer

permissions-
```
get:actors|get:movies 
delete:actors|post:actors
delete:movies|post:movies
patch:actors|patch:movies
```
login-
```
email:xmiguel.carra94@gmail.com
password:Password01!
```

## Endpoints

GET /authorization/url 

Returns the login URL.
```
{
    "url":"https://dev-wf6q6hhs.eu.auth0.com/authorize?audience=http://127.0.0.1:5000&response_type=token&client_id=59ikZ4u56vwZop8jhTDBGkLmOSmwuLKU&redirect_uri=http://localhost:8080"
}
```


GET /movies

Returns success, number of movies an a list containing all movies.
```
{
      'success' : True,
      'movies' : [{
                    'title' : 'movie1',
                    'release_date' : '1999-01-08 04:05:06'
        },
        {
                    'title' : 'movie2',
                    'release_date' : '1999-01-08 04:05:06'
        }],
      'total_movies' : len(movies)
    }
```

GET /actors

Returns success, number of actors an a list containing all actors.
```
{
      'success' : True,
      'actors' : [{
                    'name' : 'actor1',
                    'gender':'male',
                    'age':45
                  },{
                    'name' : 'actor2',
                    'gender':'male',
                    'age':45
    }],
      'total_actors' : len(actors)
    }
```

POST /movies

Returns success, number of movies an a list containing all movies, incluing the posted one.
```
{
        'success' : True,
        'movies' : [{
                      'title' : 'movie1',
                      'release_date' : '1999-01-08 04:05:06'
        },
        {
                      'title' : 'movie2',
                      'release_date' : '1999-01-08 04:05:06'
        }],
        'total_movies' : len(movies)
      }
```

POST /actors

Returns success, number of actors an a list containing all actors, including the posted one.
```
{
        'success' : True,
        'actors' : [{
                      'name' : 'actor1',
                      'gender':'male',
                      'age':45
    }],
        'total_actors' : len(actors)
      }
```

PATCH /movies/<int:id>

Returns success and the details of the patched movie.
```
{
        'success' : True,
        'movie' : {
                    'title' : 'movie1',
                    'release_date' : '1999-01-08 04:05:06'
        }
      }
```

PATCH /actors/<int:id>

Returns success and the details of the patched actor.
```
{
        'success': True,
        'actor' : {
                    'name' : 'actor1',
                    'gender':'male',
                    'age':45
    }
      }
```

DELETE /movies/<int:id>

Returns success and the id of the deleted movie.
```
{
        'success' : True,
        'deleted_movie_id' : 1
      }
```

DELETE /actors/<int:id>

Returns success and the id of the deleted actor.
```
{
        'success' : True,
        'deleted_actor_id' : 1
      }

```