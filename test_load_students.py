
import json
import os
import tempfile
import unittest
from unittest.mock import patch

import main


class TestLoadStudents(unittest.TestCase):

    def test_missing_file_returns_empty_dictionary(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "missing.json")

            with patch.object(main, "FILE_NAME", path):
                self.assertEqual(main.load_students(), {})

    def test_valid_json_loads_students(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "students.json")

            with open(path, "w", encoding="utf-8") as file:
                json.dump({"101": "Rahul"}, file)

            with patch.object(main, "FILE_NAME", path):
                self.assertEqual(
                    main.load_students(),
                    {"101": "Rahul"}
                )

    def test_corrupted_json_raises_error(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "students.json")

            with open(path, "w", encoding="utf-8") as file:
                file.write("{broken data")

            with patch.object(main, "FILE_NAME", path):
                with self.assertRaises(ValueError):
                    main.load_students()

    def test_json_list_raises_error(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "students.json")

            with open(path, "w", encoding="utf-8") as file:
                json.dump([], file)

            with patch.object(main, "FILE_NAME", path):
                with self.assertRaises(ValueError):
                    main.load_students()


if __name__ == "__main__":
    unittest.main()
