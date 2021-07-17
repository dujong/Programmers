def solution(phoneBook):
    phoneBook = sorted(phoneBook)
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        print('p1 :', p1, "p2 :", p2)
        if p2.startswith(p1):
            return False
    return True

phone_book = ["12", "13", "1535", "567", "88"]
print(solution(phone_book))