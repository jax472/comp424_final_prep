def q1(data):
    """
    Gets min and max math scores
    :param data: list of data
    :return: list with the following indices
        index 0 - minimum math score found
        index 1 - maximum math score found
    """
    min_math = None
    max_math = None
    for row in data:
        math_score = int(row[5])
        if min_math is None or max_math is None:
            min_math = math_score
            max_math = math_score
            continue
        if math_score < min_math:
            min_math = math_score
        if math_score > max_math:
            max_math = math_score

    return [min_math, max_math]

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

    result = q1(data)
    # test case 1, expect min to be 0
    print(f"Min score: {result[0]}")
    # test case 2, expect max to be 100
    print(f"Max score: {result[1]}")


if __name__ == "__main__":
    main()