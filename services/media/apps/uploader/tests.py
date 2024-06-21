import os
from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from django.urls import reverse

class TestUpload(APITestCase):
    path = 'media\\test\image\\test.png'
    root = settings.BASE_DIR
    # print('cek')

    def setUp(self) -> None:
        super().setUp()

        file_path = os.path.join(self.root, self.path)
        with open(file_path, 'rb') as f:
            file_content = f.read()

        self.file = SimpleUploadedFile('test2.png', file_content, content_type='image/png')

        print('file', self.file)

    def test_upload_file(self):
        header = {
            'X-Consumer-Custom-Id': '9854b3b8-90ba-46ad-8b3c-4e0b99d03c98'
        }

        data = {
            'file': self.file
        }

        response = self.client.post(reverse('uploader|upload'), data=data, headers=header)

        self.assertEqual(response.status_code, 200)
