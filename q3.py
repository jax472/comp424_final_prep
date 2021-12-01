def q3(data):
    """
    Get average math score for students who have free/reduced lunches
    and those who have standard lunches
    :param data: list of data
    :return: list with the following indices
        index 0 - average math scores for free/reduced lunches
        index 1 - average math scores for standard lunches
    """
    free_lunches = []
    standard_lunches = []
    for row in data:
        lunch_type = row[3]
        if lunch_type not in ['free/reduced', 'standard']:
            # unknown lunch type, do nothing
            continue

        if lunch_type == "free/reduced":
            free_lunches.append(int(row[5]))
        else:
            standard_lunches.append(int(row[5]))

    return [
        round(sum(free_lunches) / len(free_lunches)),
        round(sum(standard_lunches) / len(standard_lunches)),
    ]

def main():
    file_name = 'StudentsPerformance.csv'
    data = []
    with open(file_name, 'r', encoding='utf-8') as fin:
        lines = fin.readlines()
        for line in lines:
            line = line.strip()
            line = line.split(',')
            data.append(line)
    header_row = data.pop(0)  # pop the first row out of data, we don't need it

    result = q3(data)
    # test case 1, expect avg for free/reduced lunch students to be 59
    print(f"free/reduced avg math: {result[0]}")
    # test case 2, expect avg for standard lunch students to be 70
    print(f"standard avg math: {result[1]}")

if __name__ == "__main__":
    main()