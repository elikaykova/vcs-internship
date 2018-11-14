import re


def main():
    with open("map-reduce-filter-etc- task-8.txt") as fin:
        data = fin.readlines()
        for line in data:
            words = line.split()
        # print(words)

        ans = []
        for i in words:
            match = re.match(r'.*([1-3][0-9]{3})', i)
            if match:
                if len(i) > 4:
                    i = i[0:4]
                ans = ans + [i]
                # print(i)
    print(ans)


if __name__ == '__main__':
    main()
