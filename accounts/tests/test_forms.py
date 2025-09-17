from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import SimpleTestCase

from DjangoClub import settings
from accounts.forms import UserRegistrationForm, ProfileImageForm


class TestRegistrationForm(SimpleTestCase):

    def test_valid_data(self):
        """
            Acceptance Test
        """
        form = UserRegistrationForm(data={'username': 'rezamobaraki', 'email': 'rezamobaraki@gmail.com', 'password': 'rezamobaraki'})
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        """
                Rejection Test
        """
        form = UserRegistrationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)


class TestProfileImageForm(SimpleTestCase):
    def test_valid_data(self):
        upload_file = open(f"{settings.AWS_LOCAL_STORAGE}/ch-avatar_1.png", "br")
        file_dict = {'file': SimpleUploadedFile(upload_file.name, upload_file.read())}
        form = ProfileImageForm(file_dict)
        self.assertTrue(form.is_valid())
