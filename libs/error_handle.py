#! /usr/bin/env python3

def has_error(input :list) ->bool:
    """Check if error is empty string

    Args:
        input (list): Input list of strings

    Returns:
        bool: True if error is empty string
    """
    result= False
    
    for line in input:
        if(line.__contains__("Error code")):
            result = True
    return result

def get_error(input:list) ->str:
    """Get error message

    Args:
        input (list): Input list of strings

    Returns:
        str: Error message
    """
    result = ""
    index=0
    for line in input:
        if(line.__contains__("Error code")):
            result=input.index(line)+1
            break
        else:
            index=index+1

    return result