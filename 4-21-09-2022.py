from prettytable import PrettyTable

def main():
    mytable = PrettyTable()


    print('Введите фамилию наставника')
    surname = input()
    print("Введите должность")
    ue = input()
    print("Введите кол-во студентов")
    inmore = input()
    bio_ceg = [surname, ue, inmore]
    mytable.field_names = ["Фамилия", 'Должность', 'Количество студентов']
    mytable.add_row([surname, ue, inmore])
    print(mytable)

if __name__ == "__main__":
    main()
