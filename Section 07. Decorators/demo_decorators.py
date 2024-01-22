from functools import wraps

def log_execution_time(fn=None, tag: str = None):
    import time

    def decorate(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            # Calculate the execution time
            start_time = time.time()
            result = fn(*args, **kwargs)
            execution_time = time.time() - start_time

            # Display the result
            nonlocal tag
            if not tag:
                tag = fn.__name__
            if execution_time > 1e-4:
                print(f"{tag}: execution takes", f"{execution_time:.4f}", "seconds")
            else:
                print(f"{tag}: execution takes", f"{execution_time * 10**3:.4f}", "ms")

            return result  # Return the result of the original function

        return wrapper

    # Check if fn is None, which indicates the decorator is used without arguments
    if fn is None:
        return decorate

    # If fn is provided, apply the decorator with the specified tag
    return decorate(fn)

@log_execution_time
def print_sum(a, b: int = 0):
    print(a, "+", b, "=", a + b)

# Example usage
print_sum(3, 4)
