#from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from Marathon_App.models import CustomUser


# Create your tests here.

class Read_User_Test(APITestCase):
    
    """ Read User Test Case"""
    
    def setUp(self):
        
        """ Test case init data """  
        
        self.user1 = CustomUser.objects.create(username='test',email='test@gmail.com',password='test@123',
                            first_name='test1',last_name='test2',date_of_birth='2021-12-16',
                            phone_number='8798345678',street='abc',city='xyz',state='MH',country='IND')
        
        self.user2 = CustomUser.objects.create(username='abc',email='abc@gmail.com',password='abc@123',
                            first_name='abc1',last_name='abc2',date_of_birth='2021-12-11',
                           phone_number='7865453432',street='prq',city='ppur',state='MH',country='IND')
          
    def test_user_can_read_user_list(self):
        
        """ User can read user list """
        
        url=reverse('user-list')
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
        print("GET Method status code:",response.status_code) 
               
    def test_user_can_read_user_detail(self):
        
        """ User can read user detail """
        
        self.client.force_authenticate(self.user1)
        url=reverse('user-detail',args=[self.user1.id])
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
        print("GET Method status code:",response.status_code) 
        
    def test_Anonymous_user_can_read_user_detail(self):
        
        """ Anonymous User Test """
        
        url=reverse('user-detail',args=[self.user2.id])
        response=self.client.get(url)
        self.assertEqual(response.status_code,404)
        print("GET Method status code:",response.status_code) 
        

class Create_User_Test(APITestCase):  
    
    """ Create User Test Case"""  
      
    def test_user_can_create(self):
        
        """ User can create """
        
        url=reverse('user-list')
        data = {'username':'admin','email':'admin@gmail.com',
                'password':'admin@123','first_name':'admin1',
                'last':'admin2','date_of_birth':'2021-12-22',
                'phone_number':9876543456,'street':'FC road',
                'city':'pune','state':'MH','country':'India'}
        response=self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,201)
        print("POST method status code:",response.status_code)
        
    def test_anonymous_user_can_create(self):
        
        """ Anonymous User Test """
        
        url=reverse('user-list')
        data = {'username':'demo','email':'demo@gmail.com',
                'password':'demo@123','first_name':'demo1',
                'last':'demo2','date_of_birth':'2021-12-20',
                'phone_number':7865435678,'street':'pqr',
                'city':'abc','state':'MH','country':'India'}
        response=self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,201)
        print("POST method status code:",response.status_code)
  
class User_Update_Test(APITestCase): 
    
    """ Update User Test Case"""  
    
    def setUp(self):
        
        """ Test case init data """  
        
        self.user3 = CustomUser.objects.create(username='nik',email='nikita@gmail.com',password='nikita@123',
                            first_name='nikita',last_name='kamble',date_of_birth='1998-09-10',
                            phone_number='9665272424',street='Isbavi',city='ppur',state='MH',country='IND') 
        
        self.user4 = CustomUser.objects.create(username='priyank',email='priyanka@gmail.com',password='priyanka@123',
                           first_name='priyanka',last_name='bhosale',date_of_birth='1998-12-01',
                            phone_number='9373476678',street='shivaji nagar',city='ppur',state='MH',country='IND') 
        
                                 
    def test_user_can_update(self):
        
        """ User can update """
       
        url=reverse('user-detail', args=[self.user3.id])
        data = {'username':'xyz','email':'xyz@gmail.com',
                'password':'xyz@123','first_name':'xyz1',
                'last':'xyz2','date_of_birth':'2021-12-12',
                'phone_number':9865453432,'street':'dfg',
                'city':'pune','state':'Maharashtra','country':'india'}
        self.client.force_authenticate(self.user3)
        response = self.client.put(url,data,format='json')
        self.assertEqual(response.status_code,200)
        print("PUT method status code:",response.status_code)
        
    def test_anonymous_user_can_update(self):
        
        """ Anonymous User Test """
           
        url=reverse('user-detail', args=[self.user4.id])
        data = {'username':'lmn','email':'lmn@gmail.com',
                'password':'lmn@123','first_name':'lmn1',
                'last':'lmn2','date_of_birth':'2020-11-12',
                'phone_number':7545658544,'street':'asd',
                'city':'pune','state':'Maharashtra','country':'india'}
        response = self.client.put(url,data,format='json')
        self.assertEqual(response.status_code,404)
        print("PUT method status code:",response.status_code)
        
        
class User_Delete_Test(APITestCase):
    
    """ Delete User Test Case"""  
    
    def setUp(self): 
        
        """ Test case init data """  
        
        self.user5 = CustomUser.objects.create(username='example',email='example@gmail.com',password='example@123',
                            first_name='example1',last_name='example2',date_of_birth='2021-12-02',
                            phone_number='8877665434',street='MG Road',city='solapur',state='MH',country='IND') 
        
        self.user6 = CustomUser.objects.create(username='pqr',email='pqr@gmail.com',password='pqr@123',
                            first_name='pqr1',last_name='pqr2',date_of_birth='2021-12-24',
                            phone_number='8765765676',street='mnp',city='ppur',state='MH',country='IND') 
        
    
    def test_user_can_delete(self):
        
        """ User can Delete """
        
        self.client.force_authenticate(self.user5)
        url=reverse('user-detail', args=[self.user5.id])
        response = self.client.delete(url,self.user5.id,format='json')
        self.assertEqual(response.status_code,204)
        print("DELETE method status code:",response.status_code)
        
    def test_Anonymous_user_can_delete(self):
        
        """ Anonymous User Test """
            
        url=reverse('user-detail', args=[self.user6.id])
        response = self.client.delete(url,self.user6.id,format='json')
        self.assertEqual(response.status_code,404)
        print("DELETE method status code:",response.status_code)
