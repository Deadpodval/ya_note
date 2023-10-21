from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from notes.models import Note

User = get_user_model()


class TestNoteCreation(TestCase):
    NOTE_ALT_TEXT = 'Измененный текст заметки'

    @classmethod
    def setUpTestData(cls):
        cls.author = User.objects.create(username='Fucking Slave')
        cls.note = Note.objects.create(
            title=f'Title',
            text=f'Text',
            slug=f'title',
            author=cls.author,
        )
        cls.url = reverse('notes:edit', args=(cls.note.slug,))
        cls.form_data = {
            'title': cls.note.title,
            'text': cls.NOTE_ALT_TEXT,
        }
        cls.reader = User.objects.create(username='Boss of the jim')

    def test_anonymous_user_cant_edit_note(self):
        self.client.post(self.url, data=self.form_data)

        note_text = Note.objects.get(slug=self.note.slug).text
        self.assertEqual(note_text, 'Text')

    def test_user_cant_edit_another_user_note(self):
        self.client.force_login(self.reader)
        self.client.post(self.url, data=self.form_data)

        note_text = Note.objects.get(slug=self.note.slug).text
        self.assertEqual(note_text, 'Text')

    def test_user_can_edit_note(self):
        self.client.force_login(self.author)
        self.client.post(self.url, data=self.form_data)
        self.note.refresh_from_db()
        self.assertEqual(self.note.text, self.NOTE_ALT_TEXT)
