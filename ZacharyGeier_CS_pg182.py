def main():
    # Initialize times
    times = 3
    print("Before the call, variable", "times is", times)
    
    # Invoke nPrintln and display times
    nPrint("Welcome to CS!", times)
    print("After the call, variable", "times is", times)

# Print the message n times
def nPrint(message, n):
    while n > 0:
        print("n = ", n)
        print(message)
        n -= 1
main()
