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

# `bmi_category`

```python
def calculate_bmi(weight, height):
	return round(weight / (height ** 2), 1)
    

def bmi_category(bmi_value):
	if bmi_value < 18.5:
		return("Underweight")
	elif bmi_value < 25:
		return("Normal")
	elif bmi_value < 30:
		return("Overweight")
	else:
		return("Obesity")

def main():
    weight = float(input("Weight (kg): "))
    height = float(input("Height (m): "))
    bmi = calculate_bmi(weight, height)
    print(bmi)
    print(bmi_category(bmi))


main()
```


# Boolean Logic in Python

Boolean values can only be:

- `True`
- `False`

Boolean operators allow Python to combine or modify conditions.

## Comparison operators

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `<` | Less than | `3 < 5` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<=` | Less than or equal to | `5 <= 5` | `True` |
| `>=` | Greater than or equal to | `5 >= 3` | `True` |

> **Important:**  
> `=` means assignment.  
> `==` means comparison.

Example:

```python
age = 24       # assignment
age == 24      # comparison → True
```

## Boolean Logic — Truth Tables
Remember the logic gates used in physics classes in 12th

### AND

`A and B` is `True` only when **both A and B are True**.

| A | B | A AND B |
|---|---|---------|
| True | True | **True** |
| True | False | False |
| False | True | False |
| False | False | False |

---

### OR

`A or B` is `True` when **at least one of A or B is True**.

| A | B | A OR B |
|---|---|--------|
| True | True | **True** |
| True | False | **True** |
| False | True | **True** |
| False | False | False |

---

### NOT

`not A` reverses the Boolean value.

| A     | NOT A     |
| ----- | --------- |
| True  | **False** |
| False | **True**  |
Now predict the outcome of:
```python
print(True and False)
print(True or False)
```