def q5(data):
    """
    Gets the data for average math, reading, writing for each group
    :param data: list of rows
    :return: dictionary
    """
    result_dict = {}
    for row in data:
        group = row[1]
        if group not in result_dict:
            # category for this group does not exist, initialize a new key
            # in the dictionary for this group
            result_dict[group] = {
                'count': 0,
                'math': 0,
                'reading': 0,
                'writing': 0
            }

        # if we get here, we know the group exists in the dictionary, so
        # add the rows math, reading, and writing scores
        math_score = int(row[5])
        reading_score = int(row[6])
        writing_score = int(row[7])
        result_dict[group]['count'] += 1
        result_dict[group]['math'] += math_score
        result_dict[group]['reading'] += reading_score
        result_dict[group]['writing'] += writing_score

    # NOW OUTSIDE OF THE FOR LOOP
    # now iterate over each key in the dictionary and calculate the averages
    # each key in this case will be the race/ethnicity group
    for key in result_dict.keys():
        # first calculate the average
        math_avg = result_dict[key]['math'] / result_dict[key]['count']
        # now add it as a new key in the nest dictionary
        result_dict[key]['math_avg'] = round(math_avg)
        reading_avg = result_dict[key]['reading'] / result_dict[key]['count']
        result_dict[key]['reading_avg'] = round(reading_avg)
        writing_avg = result_dict[key]['writing'] / result_dict[key]['count']
        result_dict[key]['writing_avg'] = round(writing_avg)

    return result_dict


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

    result = q5(data)
    # test case 1, expect group A math average to be 62
    print(f"Group A math avg: {result['group A']['math_avg']}")
    # test cae 2, expect group B reading average to be 67
    print(f"Group B reading avg: {result['group B']['reading_avg']}")

if __name__ == "__main__":
    main()