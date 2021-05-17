import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Movie,Actor,database_path

#retrieving tokens from environment variables
CAST_ASSISTANT_TOKEN = os.environ.get('CAST_ASSISTANT_TOKEN')
CAST_DIRECTOR_TOKEN = os.environ.get('CAST_DIRECTOR_TOKEN')
EXECUTIVE_PRODUCER_TOKEN = os.environ.get('EXECUTIVE_PRODUCER_TOKEN')

class CastingAgency(unittest.TestCase):

    new_actor = {
        'name' : 'actor1',
        'gender':'male',
        'age':45
    }

    new_null_actor = {
        'name' : '',
        'gender': '',
        'age': None
    }

    new_movie = {
        'title' : 'movie1',
        'release_date' : '1999-01-08 04:05:06'
    }

    new_null_movie = {
        'title' : '',
        'release_date' : ''
    }

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = database_path
        setup_db(self.app, self.database_path)

        #bin to current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            #create tables
            self.db.create_all()
    
    def tearDown(self):
        pass

    """ Endpoint Tests """
    def test_get_movies(self):
        res = self.client().get('/movies', headers={"Authorization": "Bearer {}".format(EXECUTIVE_PRODUCER_TOKEN)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['total_movies'])
        self.assertTrue(data['movies'])
    
    def test_404_get_empty_movies(self):
        res = self.client().get('/movies', headers={"Authorization": "Bearer {}".format(EXECUTIVE_PRODUCER_TOKEN)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code,404)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'],'Not found')
    
    def test_get_actors(self):
        res = self.client().get('/actors', headers={"Authorization": "Bearer {}".format(EXECUTIVE_PRODUCER_TOKEN)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['total_actors'])
        self.assertTrue(data['actors'])
    
    def test_404_get_empty_actors(self):
        res = self.client().get('/actors', headers={"Authorization": "Bearer {}".format(EXECUTIVE_PRODUCER_TOKEN)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code,404)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'],'Not found')

    def test_delete_movie(self):
        res = self.client().delete('/movies/1', headers={"Authorization": "Bearer {}".format(EXECUTIVE_PRODUCER_TOKEN)})
        data = json.loads(res.data)
        movie = Movie.query.filter(Movie.id==1).one_or_none()
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertEqual(data['deleted_movie_id'],1)

    def test_404_delete_non_existing_movie(self):
        res = self.client().delete('/movies/1000', headers={"Authorization": "Bearer {}".format(EXECUTIVE_PRODUCER_TOKEN)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code,404)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'],'Not found')
    
    def test_delete_actor(self):
        res = self.client().delete('/actors/1', headers={"Authorization": "Bearer {}".format(EXECUTIVE_PRODUCER_TOKEN)})
        data = json.loads(res.data)
        actor = Actor.query.filter(Actor.id==1).one_or_none()
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertEqual(data['deleted_actor_id'],1)

    def test_404_delete_non_existing_actor(self):
        res = self.client().delete('/actors/1000', headers={"Authorization": "Bearer {}".format(EXECUTIVE_PRODUCER_TOKEN)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code,404)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'],'Not found')

    def test_post_movie(self):
        res = self.client().post('/movies' ,json=self.new_movie, headers={"Authorization": "Bearer {}".format(EXECUTIVE_PRODUCER_TOKEN)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['movies'])
        self.assertTrue(data['total_movies'])
    
    def test_post_actor(self):
        res = self.client().post('/actors' ,json=self.new_actor, headers={"Authorization": "Bearer {}".format(EXECUTIVE_PRODUCER_TOKEN)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['actors'])
        self.assertTrue(data['total_actors'])
    
    def test_422_post_movie(self):
        res = self.client().post('/movies' ,json=self.new_null_movie, headers={"Authorization": "Bearer {}".format(EXECUTIVE_PRODUCER_TOKEN)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code,422)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'],'unprocessable')
    
    def test_422_post_actor(self):
        res = self.client().post('/actors' ,json=self.new_null_actor, headers={"Authorization": "Bearer {}".format(EXECUTIVE_PRODUCER_TOKEN)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code,422)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'],'unprocessable')
    
    def test_patch_movie(self):
        res = self.client().patch('/movies/1', json={
        'title' : 'movie1',
        'release_date' : '1999-01-08 04:05:06'
    }, headers={"Authorization": "Bearer {}".format(EXECUTIVE_PRODUCER_TOKEN)})
        data = json.loads(res.data)
        movie = Movie.query.filter(Movie.id==1).one_or_none()
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertEqual(data['deleted_movie_id'],1)

    def test_404_patch_non_existing_movie(self):
        res = self.client().patch('/movies/1000', json={
        'title' : 'movie1',
        'release_date' : '1999-01-08 04:05:06'
    }, headers={"Authorization": "Bearer {}".format(EXECUTIVE_PRODUCER_TOKEN)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code,404)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'],'Not found')
    
    def test_patch_actor(self):
        res = self.client().patch('/actors/1', json = {
        'name' : 'actorx',
        'gender':'male',
        'age':50
    }, headers={"Authorization": "Bearer {}".format(EXECUTIVE_PRODUCER_TOKEN)})
        data = json.loads(res.data)
        actor = Actor.query.filter(Actor.id==1).one_or_none()
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertEqual(data['deleted_actor_id'],1)

    def test_404_patch_non_existing_actor(self):
        res = self.client().patch('/actors/1000', json = {
        'name' : 'actorx',
        'gender':'male',
        'age':50
    }, headers={"Authorization": "Bearer {}".format(EXECUTIVE_PRODUCER_TOKEN)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code,404)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'],'Not found')

    """ RBAC Tests """
    def test_get_movies_assistant(self):
        res = self.client().get('/movies', headers={"Authorization": "Bearer {}".format(CAST_ASSISTANT_TOKEN)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['total_movies'])
        self.assertTrue(data['movies'])
    
    def test_401_delete_actor_assistant(self):
        res = self.client().delete('/actors/1', headers={"Authorization": "Bearer {}".format(CAST_ASSISTANT_TOKEN)})
        data = json.loads(res.data)
        actor = Actor.query.filter(Actor.id==1).one_or_none()
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'], 'unauthorized')

    def test_post_actor_director(self):
        res = self.client().post('/actors' ,json=self.new_actor, headers={"Authorization": "Bearer {}".format(CAST_DIRECTOR_TOKEN)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['actors'])
        self.assertTrue(data['total_actors'])
    
    def test_401_delete_movie(self):
        res = self.client().delete('/movies/1', headers={"Authorization": "Bearer {}".format(CAST_DIRECTOR_TOKEN)})
        data = json.loads(res.data)
        movie = Movie.query.filter(Movie.id==1).one_or_none()
        self.assertEqual(data['success'],False)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['message'], 'unauthorized')
    
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
