first_variable = "PYTHON"
print("Value of first:", first_variable)
print("Reference of first:", id(first_variable))

print("--------------")

second_variable = first_variable # making an alias
print("Value of second:", second_variable)
print("Reference of second:", id(second_variable))
