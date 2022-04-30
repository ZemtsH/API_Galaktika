import requests

BASE_URL = 'http://testruz.agtu.ru/RUZService/RUZService.svc'

def get_list_group():
    from_date = str(input("Введите дату в формате yyyy.mm.dd: \n"))
    faculty_id = str(input("Введите id факультета: \n"))
    response = requests.get(f"{BASE_URL}/groups?fromdate={from_date}&todate={from_date}"
                            f"&facultyOid = {faculty_id}&receivertype={1}")
    req = response.json()
    #print(response.text)
    count = 1
    for j in req:
        print(f"{count}. Id группы: {j['groupOid']}, курс: {j['course']}, "
              f"номер группы: {j['number']}, специальность: {j['speciality']}, "
              f"форма обучения: {j['formOfEducation']}")
        count += 1


if __name__ == '__main__':
    get_list_group()


