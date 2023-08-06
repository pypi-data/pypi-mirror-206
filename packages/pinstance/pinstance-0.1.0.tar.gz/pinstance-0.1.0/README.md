# Pinstance

Simple [singleton](https://en.wikipedia.org/wiki/Singleton_pattern) class decorator with
ability to call bounded methods with 0 overhead.

Decorated class can inherit other classes and can be inherited.

Decorated class can not be collected till the end of a programm

## Usage

Decorate a class:

```python
@instanceclass
class MyClass:
    def __init__(self, val):
        self.class_var = val
```

Now you can instanciate it

```python
inst = MyClass(777)
inst.class_var  ## 777
```
and access the instance anywhere via ```get_instance()``` class method:
```python
MyClass.get_instance().class_var  ## 777
MyClass.get_instance().some_var = 555
MyClass.get_instance().class_var  ## 555
```

Furthermore, to simplify calling methods via instance reference one can decorate desiered ```@instanceclass``` methods:

```python
@instancemethod
def my_function(self, param):
    print(f'{self.class_var} | {param}')
```

and call them like static methods with ```0``` overhead:

```python
MyClass.my_function('example')  ## 555 | example
```
