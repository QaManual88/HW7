def say_hi(name: str, age: int) -> None:
  print(f"Hi,my name is {name} and I'm {age} years old")


name = input("Enter your name: ")
age = int(input("Enter your age: "))
say_hi(name, age)