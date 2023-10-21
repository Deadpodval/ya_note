from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from notes.models import Note

User = get_user_model()


class TestHomePage(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.author = User.objects.create(username='Fucking Slave')
        all_notes = [
            Note(
                title=f'Title{index_add}',
                text=f'Text{index_add}',
                slug=f'title{index_add}',
                author=cls.author,
            ) for index_add in range(100)
        ]
        Note.objects.bulk_create(all_notes)
        cls.list_url = reverse('notes:list')

    def test_notes_order(self):
        self.client.force_login(self.author)
        response = self.client.get(self.list_url)
        object_list = response.context['object_list']
        all_dates = [note.id for note in object_list]
        sorted_dates = sorted(all_dates)
        self.assertEqual(all_dates, sorted_dates)
