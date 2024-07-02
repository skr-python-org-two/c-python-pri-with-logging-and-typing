from typing import Optional , Any , List , Dict ,  Tuple , Union

"""
    Function with basic args
"""
def add(x: int, y: int) -> int:
 """Adds two numbers together.
Args:
 x: The first number.
 y: The second number.
Returns:
 The sum of x and y.
 """
 return x + y

# result = add(5, 3)
# print(result)  # Output: 8
# This will raise a TypeError because 3.14 is not an integer
#result = add(5, 3.14)
# This will also raise a TypeError because "hello" is not a number
#result = add("hello", 3)





"""
    Function with str as return type
"""
def get_name(id: str) -> Optional[str] :
   if int(id) >= 0 :
      return "sekhar"
   else :
      return None

#print(get_name(5) , type(get_name(5)))
#print(get_name(-6), type(get_name(-6)))



"""
    Function  taking List and returning List
"""
def fun_with_list(argone: List[int]) -> List[int]:
     #y =  map(lambda x: x * x, argone)
     y = []
     for i in argone:
         y.append(i * i)
     return y

#print(fun_with_list([2, 6 , 9 , 10]))
#print(type(fun_with_list([2, 6 , 9 , 10])))


"""
    Function  taking Tuple and returning Tuple
"""
def fun_with_tuple(argone: Tuple[int , str]) -> Tuple[str , int]:
     #y = Tuple[argone[1] , argone[0]*5]
     y = (argone[1] , argone[0]*5)
     return y

# res = fun_with_tuple((2, "skr"))
# print( res )
# print( res[0] , res[1] )
# print(type( fun_with_tuple((2, "skr") )))



"""
    Function  taking Dict and returning Dict
"""
def fun_with_dict(age_map: Dict[str , int]) -> Dict[str , int]:
     #y = dict[str , int]
     y = {}
     #y = Dict[str , int ]
     for p , q in age_map.items():
         y[ p.upper() ] = q
         #y.update( "p.upper()" ) = 55
         #y.merge( { p : 55  } )
     return y

# dict_one : Dict[str , int] =  {"Ben": 30, "Bob": 25}
# dict_one[ "Ben" ] = 29
# res = fun_with_dict( dict_one  )
# print( res )
# print( res["BEN"] , res["BOB"] )
# print(type( fun_with_dict( dict_one  )))




"""
    Function  taking Union and returning Union return type
"""
def fun_with_union(arg_one: Union[str , int]) -> Union[str , int]:
    if type(arg_one) is str:
        return (arg_one + "   " + arg_one + "     " + arg_one)
    else :
        return arg_one*2

# print(fun_with_union(25))
# print(fun_with_union("sekhar"))


def fun_with_union_two(arg_one: str | int) -> str | int:
    if type(arg_one) is str:
        return (arg_one + "   " + arg_one + "     " + arg_one)
    else :
        return arg_one*2

print(fun_with_union_two(25))
print(fun_with_union_two("sekhar"))



"""
    Function with Any return type
"""
def some_function(argument: Any) -> Any:
      if type(argument) == "int" :
          return 5
      elif type(argument) == "float" :
          return 5.5
      elif type(argument) == "bool" :
          return True
      elif type(argument) == "str" :
          return "string"
      else:
          return None


# print("### from some_function start")
# print(type(some_function(8)) , (some_function(8)))
# print(type(some_function(8.95)) , (some_function(8.95)))
# print(type(some_function(True)) , (some_function(True)))
# print(type(some_function("sekhar")) , (some_function("sekhar")))
# print("### from some_function end")


def some_function_two(argument: Any) -> Any:
 if type(int(argument)) == "int":
  return 5
 elif type(float(argument)) == "float":
  return 5.5
 elif type(bool(argument)) == "bool":
  return True
 elif type(str(argument)) == "str":
  return "string"
 else:
  return None

#
# print("### from some_function_two start")
# print(type(some_function_two(8)), (some_function_two(8)))
# print(type(some_function_two(8.95)), (some_function_two(8.95)))
# print(type(some_function_two(True)), (some_function_two(True)))
# print(type(some_function_two("sekhar")), (some_function_two("sekhar")))
# print("### from some_function_two end")
