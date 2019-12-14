from gwo_version2 import partical

#get initial partical
def main():
    #初始族群
    number = 30
    wolfs = []
    for _ in range(number):
        w = partical()
        w.start()
        wolfs.append(w)

    for count, x in enumerate(wolfs):
        file = open('partical{}.txt'.format(str(count)), 'w+')
        for y in x.A:
            file.write('{}\n'.format(y))
        file.close()


if __name__ == "__main__":
    main()