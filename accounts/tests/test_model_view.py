from django.test import TestCase
from taptap.models import Taptap
from django.utils import timezone
from django.urls import reverse
from accounts.models import MyUser
from accounts.views import login_view
from django.urls import reverse



# models test
class MyUserTest(TestCase):

    def create_user(self):
            user=MyUser(username='temitayo',password='texplode',phone_number='07063419292',first_name='akanbi',last_name='bakare',email='bakakan@gmail.com')
            return user

    def test_user_creation(self):
        w = self.create_user()
        self.assertTrue(isinstance(w, MyUser))
        self.assertTrue(w.__str__(), 'MyUser %s'%w.username)


    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        MyUser.objects.create(username='temitayo',password='texplode',phone_number='07063419292',first_name='akanbi',last_name='bakare',email='bakakan@gmail.com')



    def test_username_label(self):
        user_w=MyUser.objects.get(username='temitayo')
        field_label = user_w._meta.get_field('username').verbose_name
        self.assertEquals(field_label,'username')

    def test_first_name_label(self):
        user_w=MyUser.objects.get(username='temitayo')
        field_label = user_w._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label,'first name')







class UserListViewTest(TestCase):

    @classmethod
    def setUpTestViewData(cls):
        
        number_of_users = 15
        for user_num in range(number_of_users):
            MyUser.objects.create(username='temitayo%s'%user_num,password='texplode%s'%user_num,phone_number='0706341929%s'%user_num,first_name='akanbi%s'%user_num,last_name='bakare%s'%user_num,email='bakakan@gmail.com%s'%user_num)
           
    def test_view_url_exists_at_desired_location(self): 
        resp = self.client.get('/login/') 
        self.assertEqual(resp.status_code, 200)  
           
    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('login'))
        self.assertEqual(resp.status_code, 200)
        
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('login'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'login.html')
)