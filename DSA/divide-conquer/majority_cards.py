def count(x, cards):
    count = 0
    for card in cards:
        if card == x:
            count += 1

    return count


def majority_card(arr):
    n = len(arr)
    if n == 1:
        return arr[0]

    mid = n // 2
    front = arr[:mid]
    back = arr[mid:]

    A = majority_card(front)
    if count(A, arr) > n / 2:
        return A

    B = majority_card(back)
    if count(B, arr) > n / 2:
        return B

    return -1


def majority_card_v2(arr):
    n = len(arr)

    for i in range(n):
        count = 1

        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                count += 1

        if count > n / 2:
            return True

    return False


cards = [1, 4, 3, 4, 5, 4, 4]
cards2 = [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
]
print(majority_card(cards))
print(majority_card_v2(cards))
