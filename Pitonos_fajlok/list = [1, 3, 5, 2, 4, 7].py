list = [1, 3, 5, 2, 4, 7]
def main():
    for i in list:
        if(list[i] < list[i+1]):
            list.remove(list[i])
    print(list)

if __name__ == "__main__":
    main()