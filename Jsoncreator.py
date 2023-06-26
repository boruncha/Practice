import re
import json
import datetime


def reader(filename):
    regexid = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    regexdate = r'\d{1,2}\/Sep\/2016:\d{2}:\d{2}:\d{2} -0400'

    with open(filename) as f:
        iddate = f.read()
        idlist = re.findall(regexid, iddate)
    print(idlist[287050])

    with open(filename) as f:
        logdate = f.read()
        datelist = re.findall(regexdate, logdate)
        # count = Counter(datelist)
        # print(count)
    print(datelist[287050])

    # for n in range(0, 287050):
    #     jsondatan = {
    #         "ID": n+1,
    #         "IP": idlist[n],
    #         "Ip_date": datetime.datetime.strptime(datelist[n], '%d/%b/%Y:%H:%M:%S %z').strftime('%Y/%m/%d')
    #     }
    #     resultJSON = json.dumps(jsondatan)
    #     print(resultJSON)
    #     with open('data.json', 'a') as outfile:
    #         json.dump(resultJSON, outfile, indent=2)
    #         outfile.write(',\n')


if __name__ == '__main__':
    reader('main.log')

