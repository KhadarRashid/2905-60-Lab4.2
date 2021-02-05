'''
Practice using
 assertTrue
 assertFalse
 assertIsNone
 assertIsNotNone
 assertIn
 assertNotIn
'''

from studentlists import ClassList, StudentError
from unittest import TestCase
import unittest

class TestStudentLists(TestCase):

    def test_add_student_check_student_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        self.assertIn('Test Student', test_class.class_list)

        test_class.add_student('Another Test Student')
        self.assertIn('Test Student', test_class.class_list)
        self.assertIn('Another Test Student', test_class.class_list)


    def test_add_student_already_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        with self.assertRaises(StudentError):
            test_class.add_student('Test Student')


    # adds and removes a student, 
    # and asserts the student is removed. Use assertNotIn
    def test_add_remove_student_ensure_removed(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        test_class.remove_student('Test Student')
        self.assertNotIn('Test Student', test_class.class_list)


    # adds some example students, 
    # then removes a student not in the list, and asserts a StudentError is raised
    def test_remove_student_not_in_the_list_raises_student_error(self):
        test_class = ClassList(4)
        test_class.add_student('Alice')
        test_class.add_student('Bob')

        with self.assertRaises(StudentError):
            test_class.remove_student('Carl')

    
    # a test that removes a student from an 
    # empty list, and asserts a StudentError is raised
    def test_remove_student_from_empty_list_raises_student_error(self):
        test_class = ClassList(6)

        with self.assertRaises(StudentError):
            test_class.remove_student('Carl')


    def test_is_enrolled_when_student_present(self):
        test_class = ClassList(2)
        test_class.add_student('Snoop Dogg')
        test_class.add_student('Martha Stewart')
        self.assertTrue(test_class.is_enrolled('Snoop Dogg'))
        self.assertTrue(test_class.is_enrolled('Martha Stewart'))


    def test_is_enrolled_empty_class_list(self):
        test_class = ClassList(2)
        self.assertFalse(test_class.is_enrolled('Snoop Dogg'))


    # adds some example students to a test class,
    ## then, call is_enrolled for a student who is not enrolled. 
    # Use assertFalse to verify is_enrolled returns False.

    def test_student_not_in_class_is_not_enrolled(self):
        test_class = ClassList(4)
        test_class.add_student('Alice')
        test_class.add_student('Bob')   

        self.assertFalse(test_class.is_enrolled('carl'))     

    def test_string_with_students_enrolled(self):
        test_class = ClassList(2)
        test_class.add_student('Taylor Swift')
        test_class.add_student('Kanye West')
        self.assertEqual('Taylor Swift, Kanye West', str(test_class))


    def test_string_empty_class(self):
        test_class = ClassList(2)
        self.assertEqual('', str(test_class))


    def test_index_of_student_student_present(self):
        test_class = ClassList(3)
        test_class.add_student('Harry')
        test_class.add_student('Hermione')
        test_class.add_student('Ron')

        self.assertEqual(1, test_class.index_of_student('Harry'))
        self.assertEqual(2, test_class.index_of_student('Hermione'))
        self.assertEqual(3, test_class.index_of_student('Ron'))

        # This assert passes, but it's redundant - the first assert statement will fail if
        # the method call returns None
        self.assertIsNotNone(test_class.index_of_student('Harry'))


  
    # test for index_of_student when the class_list list is empty.  
    # Assert index_of_student returns None for a student if the list is empty. 
    # use assertIsNone.
    def test_index_of_student_class_list_empty(self):
        test_class = ClassList(6)

        # Expecting a 'None' value here.
        self.assertIsNone(test_class.index_of_student('Munchkin'))

 
    ## TODO write another test for index_of_student. In the case when the 
    # class_list is not empty but has some students.
    # assert that searching for a student name that is not in the list, returns None.
    def test_index_of_student_student_not_present(self):
        test_class = ClassList(3)
        test_class.add_student('Ryu')
        test_class.add_student('Chun-Li')
        test_class.add_student('Ken')

        self.assertEqual(1, test_class.index_of_student('Ryu'))
        self.assertEqual(2, test_class.index_of_student('Chun-Li'))
        self.assertEqual(3, test_class.index_of_student('Ken'))

        # expecting a none value if student is not in the list
        self.assertIsNone(test_class.index_of_student('Dumbledore'))

   
    # test for your new is_class_full method when the class is full. 
    # use assertTrue.

    def test_is_class_full_when_class_full(self):
        test_class = ClassList(3)
        test_class.add_student('Ryu')
        test_class.add_student('Chun-Li')
        test_class.add_student('Ken')

        # expexting class to be full
        self.assertTrue(test_class.is_class_full)
    
    # test for your new is_class_full method for when is empty, 
    # and when it is not full. Use assertFalse.

    def test_is_class_empty_or_class_not_full(self):
        test_class = ClassList(6)
        test_class.add_student('Ryu')
        test_class.add_student('Chun-Li')
        test_class.add_student('Ken')

        # not adding any people to this list
        test_class2 = ClassList(5)

        # expexting class to not be full
        self.assertFalse(test_class.is_class_full())
        # expecting class to be empty
        self.assertFalse(test_class2.is_class_full())

    


if __name__ == '__main__':
    unittest.main()
