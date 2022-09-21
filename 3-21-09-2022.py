def main():


    marks = []
    que = int(input())

    for i in range(que):
        marks.append(int(input()))
    success_que = marks.count(5)
    result = success_que / que
    print(result)



if __name__ == "__main__":
    main()
