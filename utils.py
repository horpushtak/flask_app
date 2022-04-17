import json


def load_data(path):
    """Получает список кандидатов"""
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)



def format_candidates(data):
    """Форматирует список кандидатов согласно требованию"""
    result = ''
    for candidate in data:
        name = f'Имя кандидата - {candidate["name"]}\n'
        position = f'Позиция кандидата - {candidate["position"]}\n'
        skills = f'{candidate["skills"]}\n\n'
        result += '<pre>' + name + position + skills + '<pre>'
    return result


def get_candidate_by_id(data, candidate_id):
    """Возвращает данные кандидата по его id"""
    for candidate in data:
        if candidate['id'] == candidate_id:
            return candidate


def get_skills(data, skill):
    """Возвращает список скиллов кандидата"""
    result = []
    for candidate in data:
        candidate_skills = candidate["skills"].lower().split(", ")

        if skill.lower() in candidate_skills:
            result.append(candidate)

    return result
