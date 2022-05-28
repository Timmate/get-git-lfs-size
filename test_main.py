from unittest import TestCase

from main import get_size_bytes, read_lines

TEST_FILE_PATH = 'test-file-sizes.txt'


class Test(TestCase):
    def test_get_size_bytes_repo(self):
        self.assertEqual(get_size_bytes(read_lines(TEST_FILE_PATH)), 25019400)

    def test_get_size_bytes_folder1(self):
        self.assertEqual(get_size_bytes(read_lines(TEST_FILE_PATH, folder='DATA/images_plants')), 19400)

    def test_get_size_folder2(self):
        self.assertEqual(get_size_bytes(read_lines(TEST_FILE_PATH, folder='DATA/images_full')), 25 * 10 ** 6)
