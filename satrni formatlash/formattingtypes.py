""" Formatting types """
#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.

#Use "<" to left-align the value:

txt = "We have {:<8} chickens."
print(txt.format(49))

#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.

#Use ">" to right-align the value:

txt = "We have {:>8} chickens."
print(txt.format(49))

#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.

#Use "^" to center-align the value:

txt = "We have {:^8} chickens."
print(txt.format(49))

#To demonstrate, we insert the number 8 to specify the available space for the value.

#Use "=" to place the plus/minus sign at the left most position:

txt = "The temperature is {:=8} degrees celsius."
print(txt.format(-35))

#Use "+" to always indicate if the number is positive or negative:

txt = "The temperature is between {:+} and {:+} degrees celsius."
print(txt.format(-3, 7))

#Use "-" to always indicate if the number is negative (positive numbers are displayed without any sign):

txt = "The temperature is between {:-} and {:-} degrees celsius."
print(txt.format(-3, +7))

#Use "," to add a comma as a thousand separator:

txt = "The universe is {:,} years old."
print(txt.format(13800000000))

#Use "_" to add a underscore character as a thousand separator:

txt = "The universe is {:_} years old."
print(txt.format(13800000000))

#Use "b" to convert the number into binary format:

txt = "The binary version of {0} is {0:b}"
print(txt.format(5))

#Use "c" to converts the value into the corresponding unicode character:

txt = "The UNICODE character of {0} value is {0:c}"
print(txt.format(5))

#Use "d" to convert a number, in this case a binary number, into decimal number format:

txt = "We have {:d} chickens."
print(txt.format(0b101))

#Use "e" to convert a number into scientific number format (with a lower-case e,with a upper-case E):

txtl = "We have {:e} chickens."
txtu = "We have {:E} chickens."

print(txtl.format(5))
print(txtu.format(5))

#Use "f" to convert a number into a fixed point number, default with 6 decimals, but use a period followed by a number to specify the number of decimals:

txt = "The price is {:.2f} dollars."
print(txt.format(45))

#without the ".2" inside the placeholder, this number will be displayed like this:

txt = "The price is {:f} dollars."
print(txt.format(45))

# 	General format (using a upper case E for scientific notations):

print("{:G}".format(12.3384649))

#Use "o" to convert the number into octal format:

txt = "The octal version of {0} is {0:o}"
print(txt.format(10))

#Use "x" to convert the number into Hex format:

txt = "The Hexadecimal version of {0} is {0:x}"
print(txt.format(255))

#Use "X" to convert the number into upper-case Hex format:

txt = "The Hexadecimal version of {0} is {0:X}"
print(txt.format(255))

# Use "n" Number format look like as decimal format:

print("{:n}".format(0b111))

#Use "%" to convert the number into a percentage format:

txt = "You scored {:%}"
print(txt.format(0.25))

#Or, without any decimals:

txt = "You scored {:.0%}"
print(txt.format(0.25))