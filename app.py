from flask import Flask
import json


def get_information_from_json():
    """Функция загружает из json файла данные в список.
       Указан путь к файлу, чтение, кодировка
       Вернет список со словарями из json файла
    """
    with open('./data/candidates.json', 'r', encoding='utf-8') as file:
        results = json.load(file)
        return results


app = Flask(__name__)                                                      #создалили экземпляр класса Flask, файл запуска(приложение)


@app.route('/')                                                             #представление (декоратор)
def main_page():                                                            #создаем ф-цию если пользователь наберет ip
    name_candidates = get_information_from_json()                          #создали переменную в которую положили прочитанный json
    for candidate in name_candidates:
        name = candidate['name']
        position = candidate['position']
        skills = candidate['skills']
        return f'{name}, "\n",{position},"\n" ,{skills}'
        # print(candidate['name']),
        # print(candidate['position'])
        # print(candidate['skills'])
        # print()

# main_page()
# # @app.route('/candidate')
# # def candidates_name():
# #     name = information_about_candidates(["name"])
# #     position = information_about_candidates(["position"])
# #     skills = information_about_candidates(["skills"])
# #
# #     return str(name, position, skills)
# #
# #
# #
# # @app.route('/skills')
# # def skills():
# #     return 'str(information_about_candidates[skills()])'

app.run()
