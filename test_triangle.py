from console_wrapper import console_wrapper
import unittest

#-------------------------------------
# class TriangleTest
#
# Brief: Comprises test tasks for Triangle.exe console
#        Subtesting is enabled for the argument reordering and varying within one test task 
#-------------------------------------
class TriangleTest(unittest.TestCase):
    triangle=console_wrapper('.','triangle.exe')
    #
    # tests correct values for scalene triangle in decimal citation
    # the maximum int32 and int64 values are 2147483647 and 9223372036854775807 respectively
    def test_correct_scalene_dec_values(self):
        values=['2 3 4','4 3 2','3 2 4','2 4 3','2147483647 2147483646 2147483645','04 03 02']
        for i in values:
            with self.subTest('args={0}'.format(i)):
                self.triangle.run_console(i,5)
                self.assertEqual(self.triangle.ret_code, 0, ''.join(self.triangle.ret_errs[0]))        
                self.assertTrue(len(self.triangle.ret_out) > 0, 'No output was found while correct values were passed')        
                self.assertEqual(len(self.triangle.ret_out[0]), 1, 'Unexpected output:{}'.format(self.triangle.ret_out[0][0]))        
                self.assertEqual(self.triangle.ret_out[0][0], 'True:3\n', 'Output pattern was not matched')  
    #
    # tests correct values for isosceles triangle in decimal citation
    # the maximum int32 and int64 values are 2147483647 and 9223372036854775807 respectively
    def test_correct_isosceles_dec_values(self):
        values=['3 3 4','4 3 3','3 4 3','2147483647 2147483647 2147483645']
        for i in values:
            with self.subTest('args={0}'.format(i)):
                self.triangle.run_console(i,5)
                self.assertEqual(self.triangle.ret_code, 0, ''.join(self.triangle.ret_errs[0]))        
                self.assertTrue(len(self.triangle.ret_out) > 0, 'No output was found while correct values were passed')        
                self.assertEqual(len(self.triangle.ret_out[0]), 1, 'Unexpected output:{}'.format(self.triangle.ret_out[0][0]))        
                self.assertEqual(self.triangle.ret_out[0][0], 'True:1\n', 'Output pattern was not matched')  
    #
    # tests correct values for equilateral triangle in decimal citation
    # the maximum int32 and int64 values are 2147483647 and 9223372036854775807 respectively
    def test_correct_equilateral_dec_values(self):
        values=['3 3 3','2147483647 2147483647 2147483647']
        for i in values:
            with self.subTest('args={0}'.format(i)):
                self.triangle.run_console(i,5)
                self.assertEqual(self.triangle.ret_code, 0, ''.join(self.triangle.ret_errs[0]))        
                self.assertTrue(len(self.triangle.ret_out) > 0, 'No output was found while correct values were passed')        
                self.assertEqual(len(self.triangle.ret_out[0]), 1, 'Unexpected output:{}'.format(self.triangle.ret_out[0][0]))        
                self.assertEqual(self.triangle.ret_out[0][0], 'True:2\n', 'Output pattern was not matched')  
    #
    # tests positive decimal values unappropriate for triangle
    def test_incorrect_positive_dec_values(self):
        values=['1 2 3','3 2 1','2 3 1','1 2 4','4 2 1','2 4 1']
        for i in values:
            with self.subTest('args={0}'.format(i)):
                self.triangle.run_console(i,5)
                self.assertEqual(self.triangle.ret_code, 0, ''.join(self.triangle.ret_errs[0]))        
                self.assertTrue(len(self.triangle.ret_out) > 0, 'No output was found while incorrect values were passed')        
                self.assertEqual(len(self.triangle.ret_out[0]), 2, 'Unexpected output:{}'.format(self.triangle.ret_out[0][0]))        
                self.assertEqual(self.triangle.ret_out[0][1], 'False:0\n', 'Output pattern was not matched')        
    #
    # tests zero and negative values unappropriate for triangle
    def test_incorrect_zero_and_negative_values(self):
        values=['0 20 20','20 0 20','20 20 0','0 0 10','0 10 0','10 0 0','0 0 0','-1 20 20','20 -1 20','20 20 -1','-1 -1 10','-1 10 -1','10 -1 -1','-1 -1 -1']
        for i in values:
            with self.subTest('args={0}'.format(i)):
                self.triangle.run_console(i,5)
                self.assertEqual(self.triangle.ret_code, 0, ''.join(self.triangle.ret_errs[0]))        
                self.assertTrue(len(self.triangle.ret_out) > 0, 'No output was found while incorrect values were passed')        
                self.assertEqual(len(self.triangle.ret_out[0]), 2, 'Unexpected output:{}'.format(self.triangle.ret_out[0][0]))        
                self.assertEqual(self.triangle.ret_out[0][1], 'False:0\n', 'Output pattern was not matched')        
    #
    # tests incorrect over bound integer values
    # the maximum int32 and int64 values are 2147483647 and 9223372036854775807 respectively
    def test_integer_overflow(self):
        values=['2147483648 2147483648 2147483648','9223372036854775808 9223372036854775808 9223372036854775808']
        for i in values:
            with self.subTest('args={0}'.format(i)):
                self.triangle.run_console(i,5)
                self.assertEqual(self.triangle.ret_code, 0, ''.join(self.triangle.ret_errs[0]))        
                self.assertTrue(len(self.triangle.ret_out) > 0, 'No output was found while incorrect values were passed')        
                self.assertEqual(len(self.triangle.ret_out[0]), 2, 'Unexpected output:{}'.format(self.triangle.ret_out[0][0]))        
                self.assertEqual(self.triangle.ret_out[0][1], 'False:0\n', 'Output pattern was not matched')        
    #
    # tests incorrect parameters number
    def test_incorrect_parameters_number(self):
        values=['3 4 5 6']
        for i in values:
            with self.subTest('args={0}'.format(i)):
                self.triangle.run_console(i,5)
                self.assertEqual(self.triangle.ret_code, 0, ''.join(self.triangle.ret_errs[0]))        
                self.assertTrue(len(self.triangle.ret_out) > 0, 'No output was found while incorrect values were passed')        
                self.assertEqual(len(self.triangle.ret_out[0]), 2, 'Unexpected output:{}'.format(self.triangle.ret_out[0][0]))        
                self.assertEqual(self.triangle.ret_out[0][1], 'False:0\n', 'Output pattern was not matched')        
    #
    # tests incorrect delimeters (dot, comma, colon, semicolon, dash)
    def test_incorrect_delimeters(self):
        values=['02.03.04','02,03,04','02:03:04','02;03;04','02-03-04','02.03.04 02.03.04 02.03.04','02,03,04 02,03,04 02,03,04','02:03:04 02:03:04 02:03:04','02;03;04 02;03;04 02;03;04','02-03-04 02-03-04 02-03-04']
        for i in values:
            with self.subTest('args={0}'.format(i)):
                self.triangle.run_console(i,5)
                self.assertEqual(self.triangle.ret_code, 0, ''.join(self.triangle.ret_errs[0]))        
                self.assertTrue(len(self.triangle.ret_out) > 0, 'No output was found while incorrect values were passed')        
                self.assertEqual(len(self.triangle.ret_out[0]), 2, 'Unexpected output:{}'.format(self.triangle.ret_out[0][0]))        
                self.assertEqual(self.triangle.ret_out[0][1], 'False:0\n', 'Output pattern was not matched')        
    #
    # tests incorrect special symbols input
    def test_incorrect_special_symbols_input(self):
        values=['“[|]’~<!--@/*$%^&#*/()?>,.*/\\ “[|]’~<!--@/*$%^&#*/()?>,.*/\\ “[|]’~<!--@/*$%^&#*/()?>,.*/\\ ']
        for i in values:
            with self.subTest('args={0}'.format(i)):
                self.triangle.run_console(i,5)
                self.assertEqual(self.triangle.ret_code, 0, ''.join(self.triangle.ret_errs[0]))        
                self.assertTrue(len(self.triangle.ret_out) > 0, 'No output was found while incorrect values were passed')        
                self.assertEqual(len(self.triangle.ret_out[0]), 2, 'Unexpected output:{}'.format(self.triangle.ret_out[0][0]))        
                self.assertEqual(self.triangle.ret_out[0][1], 'False:0\n', 'Output pattern was not matched')        


if __name__ == '__main__':
    unittest.main()
