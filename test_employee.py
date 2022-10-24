import unittest

from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        print('setUp')
        emp_1 = Employee('Jim', 'Halpert', 50000)
        emp_2 = Employee('Pam', 'Beesly', 60000)

    def tearDown(self):
        pass

    def test_email(self):
        emp_1 = Employee('Jim', 'Halpert', 50000)
        emp_2 = Employee('Pam', 'Beesly', 60000)

        self.assertEqual(emp_1.email, 'jim.halpert@dundermifflin.com')
        self.assertEqual(emp_2.email, 'pam.beesly@dundermifflin.com')

    def test_fullname(self):
        emp_1 = Employee('Jim', 'Halpert', 50000)
        emp_2 = Employee('Pam', 'Beesly', 60000)

        self.assertEqual(emp_1.fullname, 'Jim Halpert')
        self.assertEqual(emp_2.fullname, 'Pam Beesly')

