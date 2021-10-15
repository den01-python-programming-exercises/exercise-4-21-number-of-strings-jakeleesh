def main():
    #write your code below this line
    count = 0
    while True:
        line = input()
        if (line == "end"):
            break
        else:
            count += 1
    print(count)

if __name__ == '__main__':
    main()
