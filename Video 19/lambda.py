founding_fathers = ['George Washington', 'John Adams','Benjamin Franklin','Alexander Hamilton','James Madison']
get_last_name = lambda name : name.split()[-1]
print(get_last_name('John Adams'))
founding_fathers.sort(key=get_last_name)
print(founding_fathers)