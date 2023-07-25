import csv
import create_json as cj

def read_csv(csvfile):
    csv_data = []
    with open(csvfile, newline='', encoding='utf-8-sig') as f:
        rows = csv.reader(f, delimiter=',', quotechar='|')
        for row in rows:
            csv_data.append(row)
    f.close()
    return csv_data


def nth_column(data, n):
    return [d[n - 1] for d in data if d[n - 1] != '']


if __name__ == '__main__':
    names = read_csv('NPC_Roster.csv')
    name_dict = {}
    print(names[0])
    for i in range(len(names[0])):
        print(names[0][i])
        name_dict[names[0][i]] = nth_column(names, i+1)[1:]

    for key in name_dict.keys():
        print(key)
        print(name_dict[key])

    cj.multiJSON(name_dict)