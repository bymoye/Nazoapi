from typing import Any, Union
def seed(rseed: int) -> None: ...
# def choice(seq: Union[list,tuple,str]) -> Any: ...
def shuffle(array: list) -> None: ...
def randbelow(n: int) -> int: ...
def randint(min:int,max:int) -> int: ...
def randrange(start:int,stop:int=0,step:int=1) -> int: ...