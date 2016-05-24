## Temp Converter
selection = input('Fahrenheit to Celsius(F) or Celsius to Fahrenheit(C):')
Temp = float(input('Temperature:'))
if selection == 'F':
	C = (5/9)*(Temp - 32)
	print('%.2f C = %d F' %(Temp, C))
elif selection == 'C':
	F = (9/5) * (Temp + 32)
	print('%.2f F = %d C' %(Temp, F))
else:
	print('Enter Valid Selection')