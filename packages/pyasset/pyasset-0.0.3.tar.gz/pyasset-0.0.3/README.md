# HELLO THERE 


---

## Code Example
```python
class MyClass:
    def __init__(self):
        self.var1 = 5     # default value
        self.var2 = int() # type define
    
    def __str__(self):
        temp = [f"{key} : {value}" for key, value in self.__dict__.items()]
        return ", ".join(temp) # return like 'var1 : value1, ...'


a = Builder(MyClass)
print(a) # not build

b = Builder(MyClass).build()
print(b) # build

c = Builder(MyClass)
print(c.build()) # same at b

d = Builder(MyClass).add('var1', 1).build()
print(d) # var1 initialize 1

e = Builder(MyClass).add('var1', 10) \
                    .add('var2', 5) \
                    .build() # var1 = 10, var2 = 5

b = Builder(MyClass)
b.add('var1', 0)
b.add('var2', 5**2)
print(b.build())
```