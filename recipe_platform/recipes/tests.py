# from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Recipe, Rating
from django.contrib.auth.models import User

class RecipeModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.recipe = Recipe.objects.create(seller=self.user, name='Test Recipe', description='Delicious!', image='../../picture.jpg')

    def test_recipe_creation(self):
        self.assertEqual(self.recipe.name, 'Test Recipe')
        self.assertEqual(self.recipe.seller.username, 'testuser')
