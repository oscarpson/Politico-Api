import unittest
from app.tests.base_test import BaseTest

class PoliticalParty(BaseTest):    
    def test_add_party(self):
        resp=self.client1.post('/api/v1/parties',data=self.add_party,content_type='application/json')        
        self.assertEqual(resp.json[0]["status"],201)

    def test_get_parties(self):        
        resp=self.client().get('/api/v1/parties',content_type='application/json')  
        self.assertEqual(resp.status_code,200)    

    def test_get_specific_party(self): 
        self.client().post('/api/v1/parties',data=self.add_party,content_type='application/json')               
        resp=self.client().get('/api/v1/parties/2',content_type='applicaion/json')         
        self.assertEqual(resp.json["status"],200)
    def test_delete_specific_party(self): 
        self.client().post('/api/v1/parties',data=self.add_party,content_type='application/json')        
        resp=self.client().delete('/api/v1/parties/1',data=self.add_party,content_type='application/json')
        self.assertEqual(resp.json["status"],200)  
    def test_update_specific_party(self):        
        self.client().post('/api/v1/parties',data=self.add_party,content_type='application/json')  
        resp=self.client().patch('/api/v1/parties/2/Chama Cha Wanaume Pekee',content_type='application/json')        
        self.assertEqual(resp.json["status"],200)

        
    
       
           
     