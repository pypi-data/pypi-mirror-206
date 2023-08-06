from model.duduModel import DuduModel


def main():
    print(printDudu())

def printDudu():
    dudu = DuduModel()
    return (f"[app]{dudu.printMe()}")



if __name__ == "__main__":
    main()