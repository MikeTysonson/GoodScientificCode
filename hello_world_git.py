#changed
import monkey
import sys
def print_palmtress(num):

    for i in range(num):
        sys.stdout.write(' /|\ \n')
    for i in range(num):
        sys.stdout.write('  | ')
    sys.stdout.write('\n\n')

def print_rabbit(num):
    for i in range(num):
        sys.stdout.write(' \\/ ')
    sys.stdout.write('\n')
    for i in range(num):
        sys.stdout.write(' oo ')
    sys.stdout.write('\n')
    for i in range(num):
        sys.stdout.write(' ** ')
    sys.stdout.write('\n')

def addition(num_1,num_2):
    print(num_1+num_2)

if __name__== "__main__" :
    print("Hello, monkeys!")
    print("Starting to understand git. This is my second commit!")
    print("Hello, world, again!")
    print("I think I already understood the basic concepct of add and commit. Really?")

    monkey.print_monkeys([0,1,2,3,4,5])
    print_palmtress(10)
    print_rabbit(10)
    addition(1,2)
