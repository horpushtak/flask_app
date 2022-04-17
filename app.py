# заряжай Flask и добывай инфу
from flask import Flask
from utils import load_data, format_candidates, get_candidate_by_id, get_skills

app = Flask(__name__)


# Главная страница - полный список товарищей
@app.route("/")
def main():
    data = load_data('candidates.json')
    return format_candidates(data)


# По id найдём каждого и выведем, куда следует
@app.route("/candidates/<int:candidate_id>")
def candidate_page(candidate_id):
    data = load_data('candidates.json')
    candidate = get_candidate_by_id(data, candidate_id)
    result = f'<img src="{candidate["picture"]}">'

    return result + format_candidates([candidate])


# Поглядим, какие у товарища навыки, если полезные, найдём как использовать
@app.route("/skills/<skill>")
def skills(skill):
    data = load_data('candidates.json')

    return format_candidates(get_skills(data, skill))


if __name__ == "__main__":
    app.run(debug=False)
