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
        index=0
        if(line.__contains__("Error code")):
            result = True
            break
        else:
            index=index+1

    return result

def get_error(input:list) ->str:
    """Get error message

    Args:
        input (list): Input list of strings

    Returns:
        str: Error message
    """
    result = ""

    for line in input:
        index=0
        if(line.__contains__("Error code")):
            result=input.index(line)+1
            break
        else:
            index=index+1

    return result