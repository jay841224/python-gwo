import initial, wolf

#get initial partical
def main():
    #初始族群
    number = 30
    wolfs = initial.ran_partical(number)
    for x, count in zip(wolfs, range(len(wolfs))):
        file = open('partical{}.txt'.format(str(count)), 'w+')
        for y in x._A:
            file.write('{}\n'.format(y))
        file.close()

    for x, count in zip(wolfs, range(len(wolfs))):
        with open('pbest{}.txt'.format(str(count)), 'w') as file:
            for xp in x._pbest:
                file.write('{} '.format(xp))
            file.write('\n')
            file.write('{}'.format(x._pbestfit))

    

if __name__ == "__main__":
    main()