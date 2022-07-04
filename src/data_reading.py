import re

##----##----##----##----##----##----##----##----##----##

def read_array(request, default_value, separator):
    elements = None
    try:
        elements = getElemsFromStr(input(request))
    except:
        is_valid_reply = False
        while not is_valid_reply:

            is_valid_reply = True
            reply = input("Incorrect input! Use default value? [Y / N] : ")

            if reply.upper() == "Y":
                elements = default_value
            elif reply.upper() == "N":
                return []
            else:
                is_valid_reply = False

    return elements


def getElemsFromStr(str):
    listt = re.split(";|s", str.replace(",", "."))
    elems = [float(el.strip()) for el in listt]
    return elems