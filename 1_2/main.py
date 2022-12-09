
if __name__ == '__main__':
    with open("input") as f:
        inventory = f.read().splitlines()

    def _handle():
        calories = 0

        for x in inventory:
            if not x:
                yield calories
                calories = 0
            else:
                calories += int(x)


    print(sum(sorted(_handle(), reverse=True)[:3]))
