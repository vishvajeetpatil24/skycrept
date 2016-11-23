'''
	This File is written for testing of mod_poodle module.
	Author - Vishvajeet Patil
'''
import mod_poodle
input_str = "Katrina"
print(mod_poodle.poodle_test(input_str)[1])
mod_poodle.generate()
encr_str = mod_poodle.encrypt(list(map(ord,input_str)))
print(mod_poodle.poodle(encr_str))