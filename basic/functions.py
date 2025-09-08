# #Arbitrary Arguments, *args
# def my_function(*kids):
#   print("The youngest child is " + kids[1])

# my_function("Emil", "Tobias", "Linus")

# # Keyword Arguments
# def my_function2(child3, child2, child1):
#   print("The youngest child is " + child3)
#   print("The youngest child is " + child2)
#   print("The youngest child is " + child1)

# my_function2(child1 = "Emil", child2 = "Tobias", child3 = "Linus") 

# # Arbitrary Keyword Arguments, **kwargs
# def my_function3(**kid):
#   print("His last name is " + kid["fname"])

# my_function3(fname = "Tobias", lname = "Refsnes") 

# # Default Parameter Value
# def my_function4(country = "Norway"):
#   print("I am from " + country)

# my_function4("Sweden")
# my_function4("India")
# my_function4()
# my_function4("Brazil") 

# # Passing a List as an Argument
# def my_function5(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function5(fruits)

# # Return
# def my_function6(x):
#   return 5 * x

# print(my_function6(3))
# print(my_function6(5))
# print(my_function6(9)) 

# # Positional-Only Arguments && Keyword-Only Arguments
# def my_function7(x,y,z, /):
#   print( f"{x} is  {y} a {z}") #string interpolation 

# my_function7( 3,2,4) 

# def my_function8(*,x,y,z):
#   print( f"{x} is  {y} a {z}") #string interpolation 

# my_function8( x=3,y=2,z=4) 

# def my_function9(a, b, /, *, c, d):
#   print(a + b + c + d)

# my_function9(5, 6, c = 7, d = 8) 

# # Recurrsion
# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("Recursion Example Results:")
# tri_recursion(6)

# # lambda
# my_function10 = lambda a, b : a * b
# res = my_function10(5, 6)
# print(res)
# print(type(res))  
# print(my_function10(5, 6))

# def my_function11(b) :return lambda a : a * b

# mydoubler = my_function11(2)

# print(mydoubler(11))

# def countdown(n):
#     """Generator function that yields values instead of returning"""
#     while n > 0:
#         yield n
#         n -= 1

# # Using the generator
# for num in countdown(5):
#     print(num)


# def greet(name: str, times: int = 1) -> str:
#     """Function with type annotations"""
#     return (f"Hello {name}! " * times).strip()

# result = greet("Alice", 3)
# print(result)
# #Decorator Function
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()
# #Closure Function
# def make_multiplier(factor):
#     """Creates a closure that remembers the factor"""
#     def multiplier(x):
#         return x * factor
#     return multiplier

# double = make_multiplier(2)
# triple = make_multiplier(3)

# print(double(5))  # 10
# print(triple(5))  # 15

# # Async Functions (coroutines)
# import asyncio

# async def async_countdown(n):
#     """Asynchronous coroutine"""
#     while n > 0:
#         print(n)
#         await asyncio.sleep(1)  # Non-blocking sleep
#         n -= 1

# # Run the async function
# asyncio.run(async_countdown(5))

# Match Function
def describe_value(x):
    """Function using structural pattern matching"""
    match x:
        case 0:
            return "Zero"
        case 1 | 2 | 3:
            return "Small number"
        case int() if x > 3:
            return "Positive integer"
        case float():
            return "Floating point number"
        case str():
            return f"String of length {len(x)}"
        case _:
            return "Something else"

print(describe_value(2))    
print(describe_value(5))    
print(describe_value("hi")) 

# . Method Chaining with return self
class Calculator:
    def __init__(self, value=0):
        self.value = value
    
    def add(self, x):
        self.value += x
        return self  # Return self for method chaining
    
    def multiply(self, x):
        self.value *= x
        return self
    
    def get_result(self):
        return self.value

# Method chaining example
result = Calculator(5).add(3).multiply(2).get_result()
print(result)  # 16