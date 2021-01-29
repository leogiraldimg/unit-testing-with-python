import unittest

from phonebook import PhoneBook

class PhoneBookTest(unittest.TestCase):
    def setUp(self) -> None:
        self.phonebook = PhoneBook()

    # def tearDown(self) -> None:
    #     pass

    def test_lookup_by_name(self):
        self.phonebook.add("Bob", "12345")
        number = self.phonebook.lookup("Bob")
        self.assertEqual("12345", number)

    def test_missing_name(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())