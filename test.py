from typing import Annotated,get_type_hints,get_origin,get_args
from functools import wraps
def check_range(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        type_hints = get_type_hints(func, include_extras=True)
        for name, value in kwargs.items():
            hint = type_hints.get(name)
            if hint and get_origin(hint) is Annotated:
                hint_type, *hint_args = get_args(hint)
                minn, maxx = hint_args[0]
                if not minn <= value <= maxx:
                    raise ValueError(f"{name} must be between {minn} and {maxx}")
        return func(*args, **kwargs)
    return wrapper

# def check_range(func):
#     @wraps(func)
#     def wrapper(para):
#         type_hints=get_type_hints(parseDouble ,include_extras=True)
#         print("type_hints",type_hints)
#         hint = type_hints["para"]
#         if get_origin(hint) is Annotated:
#          hint_type , *hint_args = get_args(hint)
#         #  hint_type , hint_args = get_args(hint) 
#         minn , maxx = hint_args[0] # [:2]
#         if minn is not None:
#             print(minn)
#         if maxx is not None:
#             print(maxx)
#         if  not minn <= para <= maxx:
#             raise ValueError(f"para must be between {minn} and {maxx}")
         
#         print(hint_type , hint_args)
#         print(minn , maxx)
#         return func(para)
#     return wrapper
# Decorator Style
@check_range
def parseDouble(para  : Annotated[int , [0,100]]) -> float :
    
    return para * 2
result = parseDouble(para= 5888888)
print(f"result is {result}")
    