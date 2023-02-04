from typing import List

def isContain(a: str, b: str) -> bool:
    if a == b:
        return True
    if len(b) == 0:
        return True
    if len(a) < len(b):
        return False
    if a[0] == b[0]:
        return isContain(a[1:], b[1:])
    return isContain(a[1:], b)


def solution(str_list: List[str]) -> int:
    sorted_str_list = sorted(str_list, key=lambda x: len(x), reverse=True)
    max_len_start_at_pos = [1] * len(sorted_str_list)
    for i in range(len(sorted_str_list) - 2, -1, -1):
        temp = 1
        for j in range(i+1, len(sorted_str_list)):
            if isContain(sorted_str_list[i], sorted_str_list[j]):
                temp = max(temp, max_len_start_at_pos[j] + 1)
        max_len_start_at_pos[i] = temp
    return max(max_len_start_at_pos)


if __name__ == "__main__":
    print(solution(
        [
            'e',
            'bd',
            'abcde',
            'bced',
            'bcde',
            'ccd',
            'cde',
            'de'
        ]
    ))