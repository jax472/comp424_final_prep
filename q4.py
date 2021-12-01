def q4(data):
    """
    Get average math score for students who have and have not
    completed test preparation courses
    :param data: list of data
    :return: list with the following indices
        index 0 - average math scores for students with no prep
        index 1 - average math scores for students with prep
    """
    no_prep = []
    prep = []
    for row in data:
        prep_type = row[4]
        math_score = int(row[5])
        if prep_type not in ['completed', 'none']:
            # unknown lunch type, do nothing
            continue

        if prep_type == "completed":
            prep.append(math_score)
        else:
            no_prep.append(math_score)

    return [
        round(sum(no_prep) / len(no_prep)),
        round(sum(prep) / len(prep)),
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

    result = q4(data)
    # test case 1, expect avg for no prep students to be 64
    print(f"No test prep math average: {result[0]}")
    # test case 2, expect avg for prep students to be 70
    print(f"Completed test prep math average: {result[1]}")

if __name__ == "__main__":
    main()