_operators = ['*', '^', '+', '-']
_plus_or_minus = ['+', '-']
_multi_or_expo = ['*', '^']


class Calculator:
    def calculate(self, expression):
        return self._expression(expression)

    def _expression(self, expr_Str):
        calc = Calculator()
        # splits the expression by + or - into a String array
        plus_minus_arr = calc._split_by_operator(expr_Str, _plus_or_minus)
        # if the array has at least 2 indexes, continue
        if len(plus_minus_arr) > 1:
            # if operator is +
            if plus_minus_arr[1] == "+":
                # recursion: compute whatever is inside the LHS, compute whatever is inside the RHS, add them
                # and return it
                return float(self._expression(plus_minus_arr[0])) + float(self._expression(plus_minus_arr[2]))
            # do the same for -
            else:
                return float(self._expression(plus_minus_arr[0])) - float(self._expression(plus_minus_arr[2]))
        # splits the expression by * or ^ into a String array
        md = calc._split_by_operator(expr_Str, _multi_or_expo)
        # if the array has at least 2 indexes, continue
        if len(md) > 1:
            # if operator is *
            if md[1] == "*":
                # recursion: compute whatever is inside the LHS, compute whatever is inside the RHS, multiply
                # them and return it
                return float(self._expression(md[0])) * float(self._expression(md[2]))
            else:
                expression = expr_Str.replace("^", "**")
                expression = compile(expression, '../Main.py', 'eval')
                return float(eval(expression))
        # if the expr String begins with -
        if expr_Str.startswith("-"):
            # compute everything on the RHS of the - sign. Then set to negative
            return -float(self._expression(expr_Str[1:len(expr_Str)]))
        # if the expr String begins with (
        if expr_Str.startswith("("):
            # compute everything inside the ( and the outermost ).
            return float(self._expression(expr_Str[1: len(expr_Str) - 1]))
        return float(expr_Str)

    def _split_by_operator(self, expr_str, operator_to_split):
        # bracket_tracker checks if there's an equal amount of opening and closing parenthesis
        bracket_tracker = 0;
        # rv = return value
        rv = []
        # iterate from the last character of expr_Str to the first
        for i in range((len(expr_str) - 1), -1, -1):
            current_char = expr_str[i]
            # increment bracket_tracker if current_char is ')' - decrement if '('
            if current_char == ')':
                bracket_tracker = bracket_tracker + 1
            elif current_char == '(':
                bracket_tracker = bracket_tracker - 1
            # the current_char is an operator and bracket_tracker tracked an even number of opening and closing
            # parentheses
            elif i > 0 and bracket_tracker == 0 and current_char in operator_to_split:
                # check if the LHS of the symbol exists
                lhs = expr_str[i - 1]
                # if the LHS isn't an operation
                if lhs not in _operators:
                    # split the LHS, operation symbol, and RHS. return.
                    rv.append(expr_str[0:i])
                    rv.append(expr_str[i:i + 1])
                    rv.append(expr_str[i + 1:len(expr_str)])
                    return rv
        # return without splitting
        rv.append(expr_str)
        return rv

# TESTS:
# run = Calculator()
# print(run.calculate("(1+2)(3+4)"))
# print(run.calculate("(1+2+7)*3"))
# print(run.calculate("((2*3)+(3+4*12)-(-(8-8+4))+2^(4+5))^2"))
