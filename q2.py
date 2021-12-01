def q2(data):
    """
    Get the average math, reading, and writing score across all students
    :param data: list of data
    :return:list with three indicies:
        index 0 = the average of all math scores
        index 1 = the average of all reading scores
        index 2 = the average of all writing scores
    """
    math_accum = 0
    reading_accum = 0
    writing_accum = 0
    for row in data:
        math_accum += int(row[5])
        reading_accum += int(row[6])
        writing_accum += int(row[7])

    math_avg = math_accum / len(data)
    reading_avg = reading_accum / len(data)
    writing_avg = writing_accum / len(data)

    return [math_avg, reading_avg, writing_avg]


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

    result = q2(data)

    # test case 1: expect average math to be approx 66
    print(f"Average Math: {round(result[0])}")
    # test case 2: expect average reading to be approx 69
    print(f"Average Reading: {round(result[1])}")
    # test case 2: expect average reading to be approx 68
    print(f"Average Writing: {round(result[2])}")


if __name__ == "__main__":
    main()