# 7.1 WRITING FUNCTIONS THAT ACCEPT ANY NUMBER OF ARGS
print("-"*20 +"\n"+ "# 7.1 WRITING FUNCTIONS THAT ACCEPT ANY NUMBER OF ARGS")
"""
You want to write a function that accepts any number
 of input arguments
"""
def avg(first , *rest):
    return(first + sum(rest)) / (1 + len(rest))

def make_element(name, value, *attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(name=name, attrs=attr_str, value = html.escape(value))
    return element

#make_element('item', 'albatros', size='large', quantity=6)
#make_element('p', '<spam>')

def recv(maxsize, *, block):
    'Receives a message'
    pass 

recv(1024, block=True)

def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m 

minimum(1, 5, 2, -5, 10) 


# 7.3 ATTACHING INFORMATIONAL METADATA TO FUNCTION ARGS
print("-"*20 +"\n"+ "# 7.3 ATTACHING INFORMATIONAL METADATA TO FUNCTION ARGS")
"""
YOU'VE WRITTEN A FUNCTION, BUT WOULD LIKE TO ATTACH SOME ADDITIONAL
INFORMATION TO THE ARGUMENTS SO THAT OTHERS KNOW MORE ABOUT HOW
FUNCTION IS SUPOSSED TO BE USED. """ 

def add(x:int, y:int) -> int:
    return x+y

help(add)