# main.py

import sys
from pkg.calculator import Calculator
from pkg.render import format_json_output


def main():
    calculator = Calculator()
    if len(sys.argv) <= 1:
        print("Calculator App")
        print('Usage: python main.py "<expression>"')
        print('Example: python main.py "3 + 5"')
        
        # Add test case
        test_expression = "3 + 7 * 2"
        expected_result = 17
        actual_result = calculator.evaluate(test_expression)
        if actual_result != expected_result:
            raise AssertionError(f"Test failed: {test_expression} should be {expected_result}, but got {actual_result}")
        print("Test passed!")
        
        return

    expression = " ".join(sys.argv[1:])
    try:
        result = calculator.evaluate(expression)
        if result is not None:
            to_print = format_json_output(expression, result)
            print(to_print)
        else:
            print("Error: Expression is empty or contains only whitespace.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()