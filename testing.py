from typing import Annotated,get_type_hints,get_origin,get_args
from functools import wraps
import inspect
def check_valid_data(func):
        @wraps(func)
        def mr_wrap(*args , **kwargs):
            type_hints= get_type_hints(func , include_extras=True)
            #no need to call with name parameters
            sig = inspect.signature(func)
            bound = sig.bind(*args, **kwargs)   
            bound.apply_defaults()

            for name, value in bound.arguments.items():
            # for name , value in kwargs.items(): # have to give with name parameter
                hint =type_hints.get(name) #param
                if hint and get_origin(hint) is Annotated:
                    origin_type , *hint_args = get_args(hint)
                    print("origin_type :: " , origin_type)
                    print("hint_args :: " , hint_args)
                    minn , maxx ,avg = hint_args[0] 
                    print("val :: " , value)
                    print("minn :: " , minn)
                    print("maxx :: " , maxx)
                    print("avg :: " , avg)
                    if (not minn <= value <= maxx) and (not value ==avg):
                        raise ValueError(f"{name} must be between {minn} and {maxx}")
                    
            return func(*args , **kwargs)
        return mr_wrap

@check_valid_data
def sumData(firstInt : Annotated[int , [0,100,200]] , secondInt : Annotated[int , [0,100,300]] ) -> int :
    return firstInt + secondInt
# res=sumData(firstInt=102,secondInt= 6)
res=sumData(200,300)
print(res)