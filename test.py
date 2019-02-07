import unittest
import pytest
import json
from app.api.app import create_app 


class OfficeTest(unittest.TestCase):   

    def setUp(self):
        
        self.app =create_app()
        
        self.app = self.app.test_client()
        self.BASE_URL = 'http://127.0.0.1:5000/api/v1/offices'        
        self.add_office=json.dumps({"type":"Government","name":"Senate"})
        self.add_party=json.dumps({"name":"Chaa chetu","hqAddress":"Thika","logoUrl":"images"})



    def tearDown(self):            
        self.app.testing = False
        self.app = None
        self.BASE_URL = None
    def test_get_offices(self):
        resp=self.app.get('/api/v1/offices', content_type='application/json')  
        self.assertEqual(resp.status_code, 200)

    def test_get_parties(self):
        resp=self.app.get('/api/v1/parties',content_type='applicaion/json')  
        self.assertEqual(resp.status_code,200) 

    def test_get_specific_party(self):        
        self.app.post('/api/v1/parties',data=self.add_party,content_type='applicaion/json')
        resp=self.app.get('/api/v1/parties/1',content_type='applicaion/json')  
        self.assertEqual(resp.json["status"],200)  

    def test_delete_specific_party(self):
        self.app.post('/api/v1/parties',data=self.add_party,content_type='applicaion/json')
        resp=self.app.delete('/api/v1/parties/1',content_type='applicaion/json')  
        self.assertEqual(resp.json["status"],200) 

    def test_patch_specific_party(self):
        self.app.post('/api/v1/parties',data=self.add_party,content_type='applicaion/json')
        resp=self.app.patch('/api/v1/parties/1/Chama Cha Wanaume Pekee',content_type='applicaion/json')  
        self.assertEqual(resp.json["status"],200) 
             


if __name__ == '__main__':
    unittest.main()        

