age = int(input("How old are you "))#var

#If goes first ELIF goes middle and ELSE goes end
if age == 100:
    print("you are a century old")
elif age >= 18:
    print("You are an adult")
elif age < 0:
    print("you haven't born yet")
else:
    print("you are an child")
