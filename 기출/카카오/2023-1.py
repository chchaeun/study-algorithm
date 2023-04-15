from collections import defaultdict
from datetime import date, datetime


def solution(today, terms, privacies):
    answer = []

    terms_dict = defaultdict(int)

    for term in terms:
        type, period = term.split()
        terms_dict[type] = int(period)

    today = datetime.strptime(''.join(today.split('.')), "%Y%m%d")

    for index, privacy in enumerate(privacies):
        start_date, type = privacy.split()

        year, month, date = map(int, start_date.split('.'))

        year += terms_dict[type] // 12
        month += terms_dict[type] % 12
        date -= 1

        if date == 0:
            date = 28
            month -= 1

        if month > 12:
            year += month // 12
            month %= 12
            
        if month < 1:
            year += month // 12
            month = (month % 12) + 12

        year, month, date = str(year), str(month), str(date)
        end_date = datetime.strptime(year + month.zfill(2) + date.zfill(2), "%Y%m%d")
       
        if end_date < today:
            answer.append(index + 1)

    return answer

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))