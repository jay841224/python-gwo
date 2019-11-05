import initial, wolf

def main():
    #初始族群
    number = 2
    wolf = initial.ran_partical(number)
    for x, count in zip(wolf, range(len(wolf))):
        file = open('partical{}.txt'.format(str(count)), 'w+')
        for y in x._A:
            file.write('{}\n'.format(y))
        file.close()

if __name__ == "__main__":
    main()