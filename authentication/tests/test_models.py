from rest_framework.test import APITestCase
from authentication.models import User

class TestUserModel(APITestCase):
    def test_create_user(self):
        user=User.objects.create_user(username="user", email="user@email.com", password="password123!@")
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, "user@email.com")
    
    def test_create__super_user(self):
        user=User.objects.create_superuser(username="user", email="user@email.com", password="password123!@")
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, "user@email.com")
    
    def test_raises_error_when_no_username(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(username="", email="user@email.com", password="password123!@")

    def test_raises_error_when_no_email(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(username="user", email="", password="password123!@")
        
    def test_cant_create_super_user_with_no_is_staff_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True.'):
            User.objects.create_superuser(
                username='user', email='user@email.com', password='password123!@', is_staff=False)

    def test_cant_create_super_user_with_no_super_user_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True.'):
            User.objects.create_superuser(
                username='user', email='user@email.com', password='password123!@', is_superuser=False)
            