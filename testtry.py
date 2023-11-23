
testv = input("Ta connerie")

try:
    testv = int(testv)
except ValueError:
    print("invalid input")
else:
    print("tout vas bien")
    print(testv, "bonjour")
