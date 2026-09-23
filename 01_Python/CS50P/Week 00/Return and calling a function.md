```python
def square(number):
    # your code here
	return number ** 2

def main():
    x = float(input("Give me a number: "))
    # call square() and print the result
    print(square(x))

main()
```
For this exercise:

- square() must return the answer.
- Don’t calculate the square directly inside main().
- Don’t use ** inside main().
- Use the function’s parameter.


## Difference between `return` and `print`

```python
def square(number):
    print(number ** 2)
# trying to call square() function here
# This statement is both a function call and an assignment of value to a variable
result = square(5)

# using print function to print the value of the variable `result`
print(result)
```

Here `result = square(5)` is calling the function `square(5)` which already has a `print()` function defined there. Hence, it is printing `25`.  But `square(5)` is not returning any value, so there is not any value assigned to result even when we called it earlier. So,`None`.

```python
def square(number):
    return(number ** 2)

result = square(5)
```
The above code is not going to print anything because there is not any print function anywhere.
```python
def square(number):
    return(number ** 2)

result = square(5)
print(result)
```
# `calculate_bmi`
```python
def calculate_bmi(weight, height):
	return round(weight / (height ** 2), 1)
    # write your code here


def main():
    weight = float(input("Weight (kg): "))
    height = float(input("Height (m): "))
    print(calculate_bmi(weight, height))
    # call calculate_bmi() and print the returned value


main()
```

