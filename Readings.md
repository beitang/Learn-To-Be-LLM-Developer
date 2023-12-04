# Learn Python the Hard Way
## Keywords
### with as as
- In Python, the with statement is used to wrap the execution of a block of code to manage resources, such as opening and closing files. This is often used in conjunction with the as keyword, which allows you to assign an alias to the resource being managed. This pattern is known as a context manager. The primary benefit of using the with statement is that it ensures resources (like files) are properly closed after the block execution, even if an error occurs. This helps prevent resource leaks and simplifies code.
- The with statement works based on a protocol in Python: the __enter__ and __exit__ methods. When you enter a with block, the context manager object __enter__ method is called, and when you leave the with block, the __exit__ method is called, regardless of whether you leave it due to success or an exception.
- You can also create your own context managers by defining a class with __enter__ and __exit__ methods.
### del
- delete from dict
### except
### exec
### finally
### global
### is
- similar to ==
### lambda
### pass
- empty code block
### raise
### try
### yield

## data type
- True
- False
- None
- bytes
- strings
- numbers
- Floats
- lists
- dicts

## escape characters
- \\
- \'
- \"
- \a
- \b
- \f
- \n
- \r
- \t
- \v
