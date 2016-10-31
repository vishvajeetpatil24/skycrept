#Lists

pizza_outlets = ['Dominos', 'Pizzahut', 'Chicago Pizza', 'American Pizza']
print(pizza_outlets[1:])
print(pizza_outlets[:])
pizza = pizza_outlets
print(pizza[:3])
print(pizza[1:2])
pizza = pizza + ["Smokin' Joes", "Largo Pizzeria", "Cheesiano Pizza"]
print(pizza)
pizza[3:4] = []
print(pizza)
for x in range(len(pizza)):
	print(pizza[x])
###############################################
for x in pizza:
	print(x)