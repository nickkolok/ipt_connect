# Create your tests here.
from django.test import TestCase
from models import ipt_mean

class  Test(TestCase):

    def test_ipt_mean(self):

        input_data = [
            [1, 2, 3],
            [3, 2, 3, 4],
            [1, 4, 9, 1, 4, 2, 0, 2],
            [1, 4, 9, 1, 4, 2]
        ]
        res_data = [
            2.5,
            3.0,
            3.33333333333,
            4.0
        ]
        for i in range(len(input_data)):
            print (i, self.assertEqual(ipt_mean(input_data[i]), res_data[i]))
