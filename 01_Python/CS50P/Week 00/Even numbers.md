```python
def main():
    number = int(input("Give me a number: "))

    if is_even(number):
        print("Even")
    else:
        print("Odd")

def is_even(number):
    remainder = number % 2
    return remainder == 0

main()
```
