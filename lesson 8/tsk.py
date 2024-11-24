import re
from re import compile
pat = compile(r"^(?P<Private>\w\d\d\d\w\w\d\d\d?)|(?P<Taxi>\w\w\d\d\d\d\d\d?)|(?P<Fail>.*)$")
def f(number):
    if re.fullmatch(r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}', number):
        return 'Private'
    if re.fullmatch(r'[АВЕКМНОРСТУХ]{2}\d{5,6}', number):
        return 'Taxi'
    else:
        return 'Fail'
assert f("С227НА777") == "Private"
assert f("КУ22777") == "Taxi"
assert f("Т22В7477") == "Fail"
assert f("М227К19У9") == "Fail"
