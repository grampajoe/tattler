"""
Tests for the Tattler plugin.
"""
import unittest
import tattler

from .fake_module import fake_object, fake_function, fake_factory


class TestTattler(unittest.TestCase):
    """Tests for tattler."""
    def setUp(self):
        self.tattler = tattler.Tattler()
        self.tattler._paths = [
            'tests.test_tattler.fake_function',
            'tests.test_tattler.fake_object.method',
            'tests.fake_module.FakeClass.method',
        ]
        self.tattler.init()

    def tearDown(self):
        self.tattler.destroy()

    def test_tattle(self):
        """Test calling functions we're tattling on."""
        self.tattler.start()

        with self.assertRaises(tattler.TattleTale):
            fake_function()

        with self.assertRaises(tattler.TattleTale):
            fake_object.method()

        self.tattler.stop()

        # Should not raise anything
        fake_function()
        fake_object.method()

    def test_tattle_not_started(self):
        """Test initializing the plugin but not starting it."""
        # Should not raise anything
        fake_function()
        fake_object.method()

    def test_tattle_method(self):
        """Test that a method receives the correct value of self."""
        another_fake = fake_factory()
        result = another_fake.method()

        assert result is another_fake
