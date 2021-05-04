import argparse
import json
import os
import re
import sys
from collections import defaultdict


def start_parse_log(input_file, debug= False):
    dict_ip = defaultdict(lambda: {"GET": 0, "POST": 0, "PUT": 0, "DELETE": 0, "HEAD": 0})
    common_method = defaultdict(lambda: {"GET": 0, "POST": 0, "PUT": 0, "DELETE": 0, "HEAD": 0})
    lagest_time = defaultdict(lambda: {"url": "", "Method": 'empty', "time_execute": 0, "status_code": 0})

    with open(input_file) as file:
        for index, line in enumerate(file.readlines()):
            # 109.184.11.34 - - [12/Dec/2015:18:32:56 +0100] "GET /administrator/ HTTP/1.1" 200 4263 "-" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"
            ip = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line).group()
            str = re.search(
                r"\] \"(POST|GET|PUT|DELETE|HEAD) (?<=\s)(.*?)(?=\s) (?<=\s)(.*?)(?=\s) (?<=\s)(.*?)(?=\s) (?<=\s)(.*?)(?=\s)",
                line)
            method = str.groups()[0]
            url = str.groups()[1]
            status_code = int(str.groups()[3])
            time_execute = str.groups()[4]

            lagest_time[ip]['url'] = url
            lagest_time[ip]['Method'] = method
            lagest_time[ip]['time_execute'] = int(time_execute)
            lagest_time[ip]['status_code'] = int(status_code)

            dict_ip[ip][method] += 1
            common_method['All_Rest'][method] += 1

            # lagest_time[ip]
            if debug:
                print(f"url = {url}")
                print(f"time_execute = {time_execute}")
                print(f"status_code = {status_code}")
            if index > 500:
                break

    for i in dict_ip:
        s = 0
        for ii in dict_ip[i].values():
            s = s + ii
        dict_ip[i]['Cound_Method'] = s

    def items(custom_d, col, col_values="", top_element=10, sort='desc', row_skip=0):
        new_custom_d = custom_d.copy()
        if col_values:
            for key, value in dict(new_custom_d).items():
                if value[col] != col_values:
                    del new_custom_d[key]

        def keyfunc(tup):
            key, d = tup
            if sort == 'desc':
                return -d[col]
            return d[col]

        # топ 10 IP адресов, с которых были сделаны запросы
        items = dict(sorted(new_custom_d.items(), key=keyfunc)[row_skip:top_element])
        return items

    def save_file(file_mane, json_data, out_directory='result'):
        if not os.path.isdir(out_directory):
            os.makedirs(out_directory)

        full_path = os.path.join(out_directory, input_file)
        if not os.path.isdir(full_path):
            os.makedirs(full_path)
        if debug:
            print(f"Запись json_data {json_data} размером {len(json_data)}")

        # with open(file_mane, 'w') as f:
        with open(os.path.join(full_path, file_mane), 'w') as f:
            json.dump(json_data, f)

    if debug:
        print(dict_ip)

    # количество запросов по типу: GET - 20, POST - 10 и т.п.
    print('Выполнение. количество запросов по типу: GET - 20, POST - 10 и т.п')
    if debug:
        print(common_method)
    save_file('common_method.json', common_method)

    # топ 10 IP адресов, с которых были сделаны запросы
    print("Выполнение. топ 10 IP адресов, с которых были сделаны запросы")
    temp = items(dict_ip, "Cound_Method")
    if debug:
        print(temp)
    save_file('ip_order_by_count.json', temp)

    # топ 10 самых долгих запросов, должно быть видно метод, url, ip, время запроса
    print("Выполнение. топ 10 самых долгих запросов, должно быть видно метод, url, ip, время запроса")
    temp = items(lagest_time, "time_execute")
    if debug:
        print(temp)
    save_file('ip_order_by_lagest_time.json', temp)

    # топ 10 запросов, которые завершились клиентской ошибкой, должно быть видно метод, url, статус код, ip адрес
    print("Выполнение. топ 10 запросов, которые завершились клиентской ошибкой, должно быть видно метод, url, статус код, ip адрес")
    temp = items(lagest_time, "status_code", 400)
    if debug:
        print(temp)
    save_file('ip_order_by_status_code_400.json', temp)

    # топ 10 запросов, которые завершились ошибкой со стороны сервера, должно быть видно метод, url, статус код, ip адрес
    print("Выполнение. топ 10 запросов, которые завершились ошибкой со стороны сервера, "
          "должно быть видно метод, url, статус код, ip адрес")
    temp = items(lagest_time, "status_code", 500)
    if debug:
        print(temp)
    save_file('ip_order_by_status_code_500.json', temp)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process access.log')
    # https://docs.python.org/3/library/argparse.html
    # https://docs.python.org/3/library/argparse.html#the-add-argument-method
    parser.add_argument('-f', dest='file', action='store', help='Path to logfile')
    parser.add_argument('-d', dest='directory', action='store', help='Path to directory')
    args = parser.parse_args()

    if args.file and args.directory is not None:
        print("Укажите либо файл либо директорию с файлами")
        sys.exit(-1)
        
    if args.file:
        if not os.path.isfile(args.file):
            print("Файл не найден. Проверьте путь к файлу")
            sys.exit(-1)
        start_parse_log(args.file)

    if args.directory:
        if not os.path.isdir(args.directory):
            print("Директория не найдена")
            sys.exit(-1)
        for file in os.listdir(args.directory):
            print(os.getcwd())
            print(f"Обработка файла {file}")
            start_parse_log(os.path.join(args.directory, file))
