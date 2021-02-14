"""
n = 3 --> ((())) ()()() (())() ()(()) (()())
"""


def permute_parens(n: int) -> [str]:
    result = []
    n = n*2

    def helper(current_p, current_result, stack, open_count, total_count):
        if open_count > n // 2:
            return
        if can_stack(current_p, stack):
            current_result.append(current_p)
            if total_count == n and len(stack) == 0:
                result.append(current_result)
            else:
                for option in "()":
                    if option == "(":
                        helper(option, current_result[:], stack[:], open_count + 1, total_count + 1)
                    else:
                        helper(option, current_result[:], stack[:], open_count, total_count + 1)
    helper("(", [], [], 1, 1)
    return result


def can_stack(p, stack) -> bool:
    if p == "(":
        stack.append(p)
        return True
    else:  # in case of close bracket
        if len(stack) == 0:
            return False
        if stack[-1] == "(":
            stack.pop()
            return True
        else:
            return False


print(permute_parens(6))


def test_can_stack():
    test_stack = []
    assert can_stack("(", test_stack) is True
    assert test_stack == ["("]
    assert can_stack(")", test_stack) is True
    assert test_stack == []
    assert can_stack(")", test_stack) is False
    assert test_stack == []
    can_stack("(", test_stack)
    can_stack("(", test_stack)
    can_stack("(", test_stack)
    can_stack(")", test_stack)
    can_stack(")", test_stack)
    can_stack(")", test_stack)
    assert test_stack == []
    can_stack("(", test_stack)
    can_stack(")", test_stack)
    can_stack("(", test_stack)
    assert test_stack == ["("]
