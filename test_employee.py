import unittest
from unittest.mock import patch

import requests

from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')


    def setUp(self):
        """
        create two employees for every single test
        :return: emp_1, emp_2
        """
        print('setUp')
        self.emp_1 = Employee('Jim', 'Halpert', 50000)
        self.emp_2 = Employee('Pam', 'Beesly', 60000)

    def tearDown(self):
        print("tear down")
        pass

    def test_email(self):
        print("test email")
        self.assertEqual(self.emp_1.email, 'jim.halpert@dundermifflin.com')
        self.assertEqual(self.emp_2.email, 'pam.beesly@dundermifflin.com')


    def test_fullname(self):
        print("test fullname")
        self.assertEqual(self.emp_1.fullname, 'Jim Halpert')
        self.assertEqual(self.emp_2.fullname, 'Pam Beesly')


    def test_apply_raise(self):
        print("test apply raise")
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    # mocking a test (the test will not make a real request)

    def test_monthly_schedule(self):
        with patch("employee.requests.get") as mocket_get:
            mocket_get.return_value.ok = True
            mocket_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocket_get.assert_called_with('http://company.com/Halpert/May')
            self.assertEqual(schedule, 'Success')

            mocket_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocket_get.assert_called_with('http://company.com/Beesly/June')
            self.assertEqual(schedule, 'Bad Response!')
