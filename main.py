import math


def is_palindrome(n):
    """
    Determina daca un numar este palindrom.
    Input:
    -n : intreg
    Output:
    -True ori False : bool
    """
    n1 = n
    invers = 0
    while n1:
        invers = invers * 10 + n1 % 10
        n1 = n1 // 10
    if n == invers:
        return True
    else:
        return False


def get_perfect_squares(start, end):
    """
    Afiseaza toate patratele perfecte dintr-un interval inchis dat.
    Inpun:
    -start, end : intregi, marginile intervalului
    Output:
    list[int] , lista patratelor perfecte din interval
    """
    list = []
    for i in range(start, end):
        if int(math.sqrt(i)) == math.sqrt(i):
            list.append(i)
    if len(list) != 0:
        return list
    else:
        return False


def test_is_palindrome():
    assert is_palindrome(112) == False
    assert is_palindrome(232) == True
    assert is_palindrome(444) == True
    assert is_palindrome(23) == False
    assert is_palindrome(100) == False
    assert is_palindrome(989) == True


def test_get_perfect_squares():
    assert get_perfect_squares(3, 10) == [4, 9]
    assert get_perfect_squares(10, 30) == [16, 25]
    assert get_perfect_squares(24, 50) == [25, 36, 49]


def main():
    while True:
        print('1.Verificare numar palindrom.')
        print('2.Afisarea patratelor perfecte dintr-un interval dat.')
        print('3.Exit.')
        optiune = input('Alegeti o optiune: ')
        if optiune == '1':
            nr = int(input('Numarul pe care doriti sa il verifice: '))
            if is_palindrome(nr):
                print('Numarul dat este palindrom.')
            else:
                print('Numarul dat nu este palindrom.')
        elif optiune == '2':
            st = int(input('Dati marginea inferioara a intervalului: '))
            sf = int(input('Dati marginea superioara a intervalului: '))
            if get_perfect_squares(st, sf) == False:
                print('Nu exista patrate perfecte in intervalul dat')
            else:
                print(get_perfect_squares(st, sf))
        elif optiune == '3':
            break
        else:
            print('Optiune invalida.')


test_is_palindrome()
test_get_perfect_squares()
main()
