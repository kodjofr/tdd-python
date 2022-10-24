import unittest

from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Jim', 'Halpert', 50000)
        self.emp_2 = Employee('Pam', 'Beesly', 60000)

    def tearDown(self):
        pass

    def test_email(self):
        self.assertEqual(self.emp_1.email, 'jim.halpert@dundermifflin.com')
        self.assertEqual(self.emp_2.email, 'pam.beesly@dundermifflin.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Jim Halpert')
        self.assertEqual(self.emp_2.fullname, 'Pam Beesly')

