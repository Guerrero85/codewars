'''
This is a question from Codewars: Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

The input test cases are as follows:

test.describe("Testing function to_camel_case")
test.it("Basic tests")
test.assert_equals(to_camel_case(''), '', "An empty string was provided but not returned")
test.assert_equals(to_camel_case("the_stealth_warrior"), "theStealthWarrior", "to_camel_case('the_stealth_warrior') did not return correct value")
test.assert_equals(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior", "to_camel_case('The-Stealth-Warrior') did not return correct value")
test.assert_equals(to_camel_case("A-B-C"), "ABC", "to_camel_case('A-B-C') did not return correct value")
'''


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
