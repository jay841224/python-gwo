import initial, wolf

def main():
    wolf = []
    wolf.append(initial.ran_partical(10))
    with open('initial.txt', 'w+') as file:
        for x in wolf:
            for y in x._A:
                file.write('{}\n'.format(y))

if __name__ == "__main__":
    main()