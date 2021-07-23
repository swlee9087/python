from typing import List


def str_to_list(payload: str) -> []:
    return []


def reverse_list(ls: []) -> []:
    left, right = 0
    #lens(ls)=-1
    '''while left<right:
        ls[left], ls[right] = ls[right],ls[left]
        left +=1
        right -=1'''
    return ls[::-1]

    # ls.reversed()        <- weird


def list_to_str(ls: []) -> str:
    return ''


if __name__ == '__main__':
    ls = str_to_list(input("Input "))
    print(list_to_str(reverse_list(ls)))
