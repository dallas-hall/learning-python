from pprint import pprint


def make_pizza_args(size, *args):
	print(f"The {size} pizza will have the following toppings:")
	for topping in args:
		print(f"\t* {topping}")


def make_pizza_kwargs(size, **kwargs):
	print(f"The {size} pizza will have the following toppings:")
	for topping in kwargs["toppings"]:
		print(f"\t* {topping}")
	kwargs["size"] = size
	return kwargs


def rename_me_after_importing(msg):
	print(msg)
