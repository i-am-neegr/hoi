import json

from flask import Flask, render_template, request
from algorithm.building_path import building_path
from time import time
from flask_caching import Cache

config = {
    # режим отладки Flask
    "DEBUG": True,
    # тип кэширования Flask-Caching
    "CACHE_TYPE": "SimpleCache",
    # время кэширования по умолчанию
    "CACHE_DEFAULT_TIMEOUT": 300
}
app = Flask(__name__)
app.config.from_mapping(config)
# создаем экземпляр кэша
cache = Cache(app)
cache2 = Cache(app)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route("/answer", methods=['POST'])
def answer():
    values = ("start", "end", "time", "cafes", "sights", "museums", "theaters", "parks")

    try:
        start, end, path_time = (request.form[value] for value in values[:3])
        cache2.set("point", [start, end, path_time])
    except:
        start, end, path_time = cache2.get("point")

    print(start, end)

    time_ = int(path_time[:2]) * 3600 + int(path_time[3:]) * 60

    start_time = time()

    answer_path, str_path = building_path(start_point=start, end_point=end, time_path=time_)
    print(answer_path)
    cache.set("str_path", str_path)

    end_time = time()

    print(end_time - start_time)
    print(dir(cache))
    print(cache)
    print(cache.get("str_path").split("."))

    return render_template("answer.html", total_path=answer_path)


@app.route("/answer2", methods=['POST'])
def answer2():
    with open("data\\balda.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    return render_template("answer2.html", path=cache.get("str_path").split("."), json_path=data)


if __name__ == '__main__':
    app.run()
