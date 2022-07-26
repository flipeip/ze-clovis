from django.test import TestCase
from codigo.models import Config

class TestesDeConfig(TestCase):
    def setUp(self):
        Config.get_singleton()
    
    def test_singleton_is_first_entry(self):
        singleton = Config.get_singleton()
        self.assertEqual(singleton, Config.objects.first())
    
    def test_if_no_more_than_one_config_after_getting_singleton(self):
        Config.get_singleton()
        self.assertEqual(len(Config.objects.all()), 1)