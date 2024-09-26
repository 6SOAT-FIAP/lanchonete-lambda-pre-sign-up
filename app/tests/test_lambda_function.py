import unittest
from src.lambda_function import lambda_handler

class TestLambdaFunction(unittest.TestCase):

    def setUp(self):
        self.event = {
            'userName': '',
            'response': {}
        }
        self.context = {}

    def test_valid_cpf(self):
        self.event['userName'] = '12345678901A'
        response = lambda_handler(self.event, self.context)
        self.assertTrue(response['response']['autoConfirmUser'])

    def test_invalid_cpf_non_digit(self):
        self.event['userName'] = '1234567890A'
        with self.assertRaises(Exception) as context:
            lambda_handler(self.event, self.context)
        self.assertEqual(str(context.exception), "O CPF nao e valido")

    def test_invalid_cpf_length(self):
        self.event['userName'] = '123456789'
        with self.assertRaises(Exception) as context:
            lambda_handler(self.event, self.context)
        self.assertEqual(str(context.exception), "O CPF nao e valido")

if __name__ == '__main__':
    unittest.main()