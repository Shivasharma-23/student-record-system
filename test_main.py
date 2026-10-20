
import json
import os
import tempfile
import unittest
from unittest.mock import patch
import student_manager
import main
class TestStudentManagement(unittest.TestCase):

    def setUp(self):
        # Keep the real student data safe.
        self.original_file = main.FILE_NAME
        self.original_students = main.students

        self.temp_dir = tempfile.TemporaryDirectory()
        main.FILE_NAME = os.path.join(
            self.temp_dir.name, "test_students.json"
        )
        student_manager.FILE_NAME = main.FILE_NAME
        main.students = {}

    def tearDown(self):
        main.FILE_NAME = self.original_file
        student_manager.FILE_NAME = self.original_file
        main.students = self.original_students
        self.temp_dir.cleanup()

    def test_add_student(self):
        with patch("builtins.input",
                   side_effect=["101", "Rahul"]):
            main.add_student()
        self.assertEqual(main.students["101"], "Rahul")
        with open(main.FILE_NAME, "r") as file:
            saved = json.load(file)
        self.assertEqual(saved["101"], "Rahul")

    def test_duplicate_student_id(self):
        main.students["101"] = "Rahul"

        with patch("builtins.input",
                   side_effect=["101"]):
            main.add_student()

        self.assertEqual(len(main.students), 1)
        self.assertEqual(main.students["101"], "Rahul")

    def test_search_existing_student(self):
        main.students["101"] = "Rahul"

        with patch("builtins.input", return_value="101"):
            with patch("builtins.print") as mock_print:
                main.search_student()

        mock_print.assert_any_call("Student found!")

    def test_update_student(self):
        main.students["101"] = "Rahul"

        with patch("builtins.input",
                   side_effect=["101", "Aman"]):
            main.update_student()

        self.assertEqual(main.students["101"], "Aman")

        with open(main.FILE_NAME, "r") as file:
            saved = json.load(file)

        self.assertEqual(saved["101"], "Aman")

    def test_delete_student(self):
        main.students["101"] = "Rahul"

        with patch("builtins.input",
                   side_effect=["101", "yes"]):
            main.delete_student()

        self.assertNotIn("101", main.students)

        with open(main.FILE_NAME, "r") as file:
            saved = json.load(file)

        self.assertNotIn("101", saved)

    def test_empty_student_id(self):
        with patch("builtins.input", side_effect=["", "Zoro"]):
            with patch("builtins.print") as mock_print:
                main.add_student()

        mock_print.assert_any_call("Student ID cannot be empty.")
        self.assertEqual(main.students, {})

    def test_empty_student_name(self):
        with patch("builtins.input", side_effect=["105", ""]):
            with patch("builtins.print") as mock_print:
                main.add_student()

        mock_print.assert_any_call("Name cannot be empty.")
        self.assertNotIn("105", main.students)

if __name__ == "__main__":
    unittest.main()
