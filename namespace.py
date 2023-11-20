# define a function in the global namespace
def func():
    print("I'm a function in the global namespace")
# define a variable in the global namespace
x = 10

def main():
    # define a function in the local namespace
    def func():
        print("I'm a function in the local namespace")
    # define a variable in the local namespace
    x = 20
    # use the global function
    func()  # prints "I am a function in the global namespace"
    # use the local variable
    print(x)    # prints 20
main()  # calling main() function
func()  # calling global function func()
