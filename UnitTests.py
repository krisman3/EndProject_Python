# import random
# import unittest
# import main
# import unittest.mock
#
# class TestsForTaskTwo(unittest.TestCase):
#
#     def test_player_choice(self):
#         # List of acceptable values:
#         random_num = str(random.randint(1,10))
#         print(f"Random number generated: {random_num}")
#         with unittest.mock.patch('builtins.input', return_value=random_num):
#             self.failIfEqual(main.player_guess(2), '')
