def main(s):
    """
    Given variable type string s. Return the character in the middle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    k = len(s)
    if k % 2 == 1:
        return s[k // 2]
    return s[k // 2 - 1] + s[k // 2]