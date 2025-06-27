def main():
    scores = [[78, 45, 70, 59], [33, 80, 56, 47], [54, 20, 67]]
    for index, score in enumerate(scores):
        for inner_index, inner_value in enumerate(score):
            print(f"inner value: ", inner_value, end= '\t')
            print(f"inner index: ", inner_index)

            print(f"inner list: ", score, end= '\t')
            print(f"inner list index: ", index)

if __name__ == '__main__':
    main()

    Days_per_month = {'January': 31, 'February': 28, 'March': 30, 'April': 31,}
    for day, month in Days_per_month.items():
        print(f"day: ", day)
        print(f"month: ", month)

    print(Days_per_month.values())
    print(Days_per_month.keys())
    print(Days_per_month.items())

    Days_per_month['February'] = 3
    Days_per_month['May'] = 23
    print(Days_per_month.values())

    del Days_per_month['February']
    print(Days_per_month.values())

    print(Days_per_month.get('February', "NotFound"))