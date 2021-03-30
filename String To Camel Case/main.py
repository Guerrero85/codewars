
def to_camel_case(text):
    cadena = text.replace("-", " ").replace("_", " ")
    cadena = cadena.split()
    if len(text) == 0:
        return text
    return cadena[0] + ''.join(i.capitalize() for i in cadena[1:])

'''
In this example the method shown below was usedd

The split() method splits a string into a list.
You can specify the separator, default separator is any whitespace.


The capitalize() method was also used, which allows us to return a string where the first character is in uppercase.
The join() method takes all items in an iterable and joins them into one string. 
Example join():
    myTuple = ("John", "Peter", "Vicky") = JohnPeterVicky

'''
