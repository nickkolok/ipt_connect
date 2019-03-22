# Create your tests here.
from django.test import TestCase
from models import ipt_mean

class  Test(TestCase):

    def test_ipt_mean(self):

        input_data = [
            [1, 2, 3],
            [2, 3, 3, 4],
            [0, 1, 1, 1, 1, 1],
            [3, 3, 3, 3, 3, 3, 3, 3, 3],
            [3, 5, 5, 6, 7, 7, 7],
            [0, 0]
        ]
        res_data = [
            2.5,
            3.33333333333,
            1.0,
            3.0,
            6.0,
            0.0
        ]
        for i in range(len(input_data)):
            print (i, self.assertEqual(ipt_mean(input_data[i]), res_data[i]))
