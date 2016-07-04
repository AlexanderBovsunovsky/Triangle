from console_wrapper import console_wrapper
import unittest

hexadecimal_input=False
octal_input=False
binary_input=False
float_delimeter=','

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
    # tests correct values for scalene triangle in hexadecimal citation
    @unittest.skipUnless(hexadecimal_input, 'applicable only with hexadecimal values parsing') 
    def test_correct_scalene_hex_values(self):
        values=['0x02 0x03 0x04','0x04 0x03 0x02','0x03 0x02 0x04','0x02 0x04 0x03','0x7FFFFFFF 0x7FFFFFFE 0x7FFFFFFD']
        for i in values:
            with self.subTest('args={0}'.format(i)):
                self.triangle.run_console(i,5)
                self.assertEqual(self.triangle.ret_code, 0, ''.join(self.triangle.ret_errs[0]))        
                self.assertTrue(len(self.triangle.ret_out) > 0, 'No output was found while correct values were passed')        
                self.assertEqual(len(self.triangle.ret_out[0]), 1, 'Unexpected output:{}'.format(self.triangle.ret_out[0][0]))        
                self.assertEqual(self.triangle.ret_out[0][0], 'True:3\n', 'Output pattern was not matched')  
    #
    # tests correct values for scalene triangle in octal citation
    @unittest.skipUnless(octal_input, 'applicable only with octal values parsing') 
    def test_correct_scalene_oct_values(self):
        values=['0o02 0o03 0o04','0o04 0o03 0o02','0o03 0o02 0o04','0o02 0o04 0o03','0o17777777777 0o17777777776 0o17777777775']
        for i in values:
            with self.subTest('args={0}'.format(i)):
                self.triangle.run_console(i,5)
                self.assertEqual(self.triangle.ret_code, 0, ''.join(self.triangle.ret_errs[0]))        
                self.assertTrue(len(self.triangle.ret_out) > 0, 'No output was found while correct values were passed')        
                self.assertEqual(len(self.triangle.ret_out[0]), 1, 'Unexpected output:{}'.format(self.triangle.ret_out[0][0]))        
                self.assertEqual(self.triangle.ret_out[0][0], 'True:3\n', 'Output pattern was not matched')  
    #
    # tests correct values for scalene triangle in binary citation
    @unittest.skipUnless(binary_input, 'applicable only with binary values parsing') 
    def test_correct_scalene_bin_values(self):
        values=['0b10 0b11 0b100','0b100 0b11 0b10','0b11 0b10 0b100','0b10 0b100 0b11','0b1111111111111111111111111111111 0b1111111111111111111111111111110 0b1111111111111111111111111111101']
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
    # tests correct values for isosceles triangle in hexadecimal citation
    @unittest.skipUnless(hexadecimal_input, 'applicable only with hexadecimal values parsing') 
    def test_correct_isosceles_hex_values(self):
        values=['0x03 0x03 0x04','0x04 0x03 0x03','0x03 0x04 0x03','0x7FFFFFFF 0x7FFFFFFF 0x7FFFFFFD']
        for i in values:
            with self.subTest('args={0}'.format(i)):
                self.triangle.run_console(i,5)
                self.assertEqual(self.triangle.ret_code, 0, ''.join(self.triangle.ret_errs[0]))        
                self.assertTrue(len(self.triangle.ret_out) > 0, 'No output was found while correct values were passed')        
                self.assertEqual(len(self.triangle.ret_out[0]), 1, 'Unexpected output:{}'.format(self.triangle.ret_out[0][0]))        
                self.assertEqual(self.triangle.ret_out[0][0], 'True:1\n', 'Output pattern was not matched')  
    #
    # tests correct values for isosceles triangle in octal citation
    @unittest.skipUnless(octal_input, 'applicable only with octal values parsing') 
    def test_correct_isosceles_oct_values(self):
        values=['0o03 0o03 0o04','0o04 0o03 0o03','0o03 0o04 0o03','0o17777777777 0o17777777777 0o17777777775']
        for i in values:
            with self.subTest('args={0}'.format(i)):
                self.triangle.run_console(i,5)
                self.assertEqual(self.triangle.ret_code, 0, ''.join(self.triangle.ret_errs[0]))        
                self.assertTrue(len(self.triangle.ret_out) > 0, 'No output was found while correct values were passed')        
                self.assertEqual(len(self.triangle.ret_out[0]), 1, 'Unexpected output:{}'.format(self.triangle.ret_out[0][0]))        
                self.assertEqual(self.triangle.ret_out[0][0], 'True:1\n', 'Output pattern was not matched')  
    #
    # tests correct values for isosceles triangle in binary citation
    @unittest.skipUnless(binary_input, 'applicable only with binary values parsing') 
    def test_correct_isosceles_bin_values(self):
        values=['0b11 0b11 0b100','0b100 0b11 0b11','0b11 0b100 0b11','0b1111111111111111111111111111111 0b1111111111111111111111111111111 0b1111111111111111111111111111101']
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
    # tests correct values for equilateral triangle in hexadecimal citation
    @unittest.skipUnless(hexadecimal_input, 'applicable only with hexadecimal values parsing') 
    def test_correct_equilateral_hex_values(self):
        values=['0x03 0x03 0x03','0x7FFFFFFF 0x7FFFFFFF 0x7FFFFFFF']
        for i in values:
            with self.subTest('args={0}'.format(i)):
                self.triangle.run_console(i,5)
                self.assertEqual(self.triangle.ret_code, 0, ''.join(self.triangle.ret_errs[0]))        
                self.assertTrue(len(self.triangle.ret_out) > 0, 'No output was found while correct values were passed')        
                self.assertEqual(len(self.triangle.ret_out[0]), 1, 'Unexpected output:{}'.format(self.triangle.ret_out[0][0]))        
                self.assertEqual(self.triangle.ret_out[0][0], 'True:2\n', 'Output pattern was not matched')  
    #
    # tests correct values for equilateral triangle in octal citation
    @unittest.skipUnless(octal_input, 'applicable only with octal values parsing') 
    def test_correct_equilateral_oct_values(self):
        values=['0o03 0o03 0o03','0o17777777777 0o17777777777 0o17777777777']
        for i in values:
            with self.subTest('args={0}'.format(i)):
                self.triangle.run_console(i,5)
                self.assertEqual(self.triangle.ret_code, 0, ''.join(self.triangle.ret_errs[0]))        
                self.assertTrue(len(self.triangle.ret_out) > 0, 'No output was found while correct values were passed')        
                self.assertEqual(len(self.triangle.ret_out[0]), 1, 'Unexpected output:{}'.format(self.triangle.ret_out[0][0]))        
                self.assertEqual(self.triangle.ret_out[0][0], 'True:2\n', 'Output pattern was not matched')  
    #
    # tests correct values for equilateral triangle in binary citation
    @unittest.skipUnless(binary_input, 'applicable only with binary values parsing') 
    def test_correct_equilateral_bin_values(self):
        values=['0b11 0b11 0b11','0b1111111111111111111111111111111 0b1111111111111111111111111111111 0b1111111111111111111111111111111']
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
        values=['','3','3 4','3 4 5 6']
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
    #
    # tests correct float(double) input with comma delimeter
    @unittest.skipIf(float_delimeter!=',', 'applicable only with comma as float delimeter') 
    def test_correct_float_comma_input(self):
        values=['1,175494351e–38 1,175494352e–38 1,175494353e–38','1,192092896e–07 1,192092897e–07 1,192092898e–07','3,01 3,02 3,03','3,402823464e+38 3,402823465e+38 3,402823466e+38']
        for i in values:
            with self.subTest('args={0}'.format(i)):
                self.triangle.run_console(i,5)
                self.assertEqual(self.triangle.ret_code, 0, ''.join(self.triangle.ret_errs[0]))        
                self.assertTrue(len(self.triangle.ret_out) > 0, 'No output was found while correct values were passed')        
                self.assertEqual(len(self.triangle.ret_out[0]), 1, 'Unexpected output:{}'.format(self.triangle.ret_out[0][0]))        
                self.assertEqual(self.triangle.ret_out[0][0], 'True:3\n', 'Output pattern was not matched')  
 
    #
    # tests incorrect float input with comma delimeter
    # the smallest positive numbers x, such that x + 1.0 is not equal to 1.0, for double and long double are 1.192092896e–07F and 2.2204460492503131e–016 respectively
    # the minimum positive values for double and long double are 1.175494351e–38F and 2.2250738585072014e–308  respectively     
    # the maximum representable floating-point numbers  for double and long double are 3.402823466e+38F and 1.7976931348623158e+308 respectively    
    @unittest.skipIf(float_delimeter!=',', 'applicable only with comma as float delimeter') 
    def test_incorrect_float_comma_input(self):
        values=['2,2250738585072014e–308 2,2250738585072013e–308 2,2250738585072014e–308','1,175494351e–38 1,175494350e–38 1,175494351e–38','1,192092896e–07 1,192092895e–07 1,192092896e–07','3,402823467e+38 3,402823466e+38 3,402823467e+38','1,7976931348623159e+308 1,7976931348623158e+308 1,7976931348623159e+308']
        for i in values:
            with self.subTest('args={0}'.format(i)):
                self.triangle.run_console(i,5)
                self.assertEqual(self.triangle.ret_code, 0, ''.join(self.triangle.ret_errs[0]))        
                self.assertTrue(len(self.triangle.ret_out) > 0, 'No output was found while incorrect values were passed')        
                self.assertEqual(len(self.triangle.ret_out[0]), 2, 'Unexpected output:{}'.format(self.triangle.ret_out[0][0]))        
                self.assertEqual(self.triangle.ret_out[0][1], 'False:0\n', 'Output pattern was not matched')        
    # 
    # tests correct float(double) input with dot delimeter
    @unittest.skipIf(float_delimeter!='.', 'applicable only with dot as float delimeter') 
    def test_correct_float_dot_input(self):
        values=['1.175494351e–38 1.175494352e–38 1.175494353e–38','1.192092896e–07 1.192092897e–07 1.192092898e–07','3.01 3.02 3.03','3.402823464e+38 3.402823465e+38 3.402823466e+38']
        for i in values:
            with self.subTest('args={0}'.format(i)):
                self.triangle.run_console(i,5)
                self.assertEqual(self.triangle.ret_code, 0, ''.join(self.triangle.ret_errs[0]))        
                self.assertTrue(len(self.triangle.ret_out) > 0, 'No output was found while correct values were passed')        
                self.assertEqual(len(self.triangle.ret_out[0]), 1, 'Unexpected output:{}'.format(self.triangle.ret_out[0][0]))        
                self.assertEqual(self.triangle.ret_out[0][0], 'True:3\n', 'Output pattern was not matched')  
    # 
    # tests incorrect float input with dot delimeter
    # the smallest positive numbers x, such that x + 1.0 is not equal to 1.0, for double and long double are 1.192092896e–07F and 2.2204460492503131e–016 respectively
    # the minimum positive values for double and long double are 1.175494351e–38F and 2.2250738585072014e–308  respectively           
    # the maximum representable floating-point numbers  for double and long double are 3.402823466e+38F and 1.7976931348623158e+308 respectively
    @unittest.skipIf(float_delimeter!='.', 'applicable only with dot as float delimeter') 
    def test_incorrect_float_dot_input(self):
        values=['2.2250738585072014e–308 2.2250738585072013e–308 2.2250738585072014e–308','1.175494351e–38 1.175494350e–38 1.175494351e–38','1.192092896e–07 1.192092895e–07 1.192092896e–07','3.402823467e+38 3.402823466e+38 3.402823467e+38','1.7976931348623159e+308 1.7976931348623158e+308 1.7976931348623159e+308']
        for i in values:
            with self.subTest('args={0}'.format(i)):
                self.triangle.run_console(i,5)
                self.assertEqual(self.triangle.ret_code, 0, ''.join(self.triangle.ret_errs[0]))        
                self.assertTrue(len(self.triangle.ret_out) > 0, 'No output was found while incorrect values were passed')        
                self.assertEqual(len(self.triangle.ret_out[0]), 2, 'Unexpected output:{}'.format(self.triangle.ret_out[0][0]))        
                self.assertEqual(self.triangle.ret_out[0][1], 'False:0\n', 'Output pattern was not matched')        


if __name__ == '__main__':
    unittest.main()
