from django.test import TestCase

# Create your tests here.
class NeighbourHoodTestClass(TestCase):

    def setUp(self):
        self.ann = Neighbourhood(Name="Try",Location="Townie",Occupants="12")

    def test_instance(self):
        self.assertTrue(isinstance(self.ann,neighbourhood))

    def tearDown(self):
        neighbourhood.objects.all().delete()

    def test_save_method(self):
        self.ann.save_neighbourhood()
        neighbourHood = Neighbourhood.objects.all()
        self.assertTrue(len(neighbourHood)>0)

    def test_delete_method(self):
        self.ann.delete_neighbourhood('Site')
        neighbourHood = Neighbourhood.objects.all()
        self.assertTrue(len(neighbourHood)==0)

class BusinessTestClass(TestCase):
    def setUp(self):
        self.ann = business(Business_name="Services",Owner_name="Try",Business_email="services@gmail.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.ann,business))

    def tearDown(self):
        business.objects.all().delete()

    def test_save_method(self):
        self.ann.save_business()
        business= Business.objects.all()
        self.assertTrue(len(business)>0)

    def test_delete_method(self):
        self.ann.delete_business('Site')
        business = Business.objects.all()
        self.assertTrue(len(business)==0)



class PostsTestClass(TestCase):
    def setUp(self):
        self.ann = posts(post="business",Location="Townie",business="Services",Owner_name="Try")

    def test_instance(self):
        self.assertTrue(isinstance(self.ann,post))

    def tearDown(self):
        Posts.objects.all().delete()

    def test_save_method(self):
        self.ann.save_post()
        post = Posts.objects.all()
        self.assertTrue(len(neighbourHood)>0)

    def test_delete_method(self):
        self.ann.delete_post('Site')
        post = Posts.objects.all()
        self.assertTrue(len(post)==0)


