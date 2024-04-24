
def _282A():
    n_lines = int(input())
    x = 0
    for l in range(n_lines):
        statement = input()
        plus = statement.find('++')
        if plus != -1:
            x += 1
        else:
            x -= 1
    print(x)


def _1A():
    def get_length_along_dim(l):
        length, remainder = divmod(l, a)
        if remainder != 0:
            length += 1
        return length
    n, m, a = input().split(' ')
    n, m, a = int(n), int(m), int(a)
    span = get_length_along_dim(n)
    height = get_length_along_dim(m)
    print(span*height)


def _231A():
    n_problems = int(input())
    solved_problems = 0
    for n in range(n_problems):
        friend_solutions = input()
        friend_count = 0
        for c in friend_solutions:
            if c == '1':
                friend_count += 1
        if friend_count >= 2:
            solved_problems += 1
    print(solved_problems)


def _4A():
    weight = int(input())
    if weight % 2 == 0 and weight > 2:
        print('YES')
    else:
        print('NO')


def _71A():
    def compress(word):
        word_length = len(word)
        first_letter = word[0]
        last_letter = word[-1]
        compression = len(word[1:-1])
        return first_letter+str(compression)+last_letter
    n = int(input())
    for i in range(n):
        word = input()
        if len(word) <= 10:
            print(word)
        else:
            print(compress(word))
