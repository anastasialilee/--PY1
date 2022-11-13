# TODO решить с помощью list comprehension и распечатать его
list_num = [{'bin': bin(num), 'dec': num, 'hex': hex(num), 'oct': oct(num)} for num in range(16)]
from pprint import pprint
pprint(list_num)