import unittest
class TeststudentBasics(unittest.TestCase):
    def test_student_dictionary(self):
        students ={}
        students["101"] = "Rahul"
        self.assertIn("101", students)
        self.assertEqual(students["101"],"Rahul")
    def test_student_id_is_a_string(self):
        students_id = "102"
        self.assertIsInstance(students_id,str)
if __name__ =="__main__":
    unittest.main()