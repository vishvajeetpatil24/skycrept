#Summary of some important functions of strings

#Conversion specifiers -- %d %c %E %e %f %g %x %X %o %s %i %u
char = '$'
print("%c is one of the special characters and %d is example of prime number. %s is suppoosed to be the string. %E is the exponential number. %x is the hexadecimal number\n\
	%f is the example of the floating number.%u is the unsigned integer."%(char,13,str(0x6f),1.3e10,30,3.12,2))
print("%*d"%(3,3.12)) #The starting position at the left end is 1
print("%#o"%(15)) #Changes the base of converaion to octal
print("%#x"%(21)) #Changes rhe base of conversation to hexadecimal

#Some common functions will be added here with the passage of time