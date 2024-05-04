
def fizzbuzz( number):
    
    if( not (number % 3 or number % 5)):
        return "FizzBuzz"
    
    if( not number % 3):
        return "Fizz"
    
    if( not number % 5):
        return "Buzz"
    
    #else
    return str( number)

if __name__ == "__main__":

    while True:
        n = int( input( "\nn= "))
        output = []
        try: 
            for x in range( n):
                output.append(fizzbuzz( x+1))
        except ValueError:
            print( "input a real number")
        else:
            print( output)