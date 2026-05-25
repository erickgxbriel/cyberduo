import json
import os

JSON_PATH = "/home/gabriel/Documentos/dev/cyberduo/scripts/lesson_definitions.json"
MODULE = "7"
EXPECTED_FILES = [
    "7.0-introducao.html",
    "7.1a-cloud.html",
    "7.1b-configuracoes-nuvem.html",
    "7.2a-mobile.html",
    "7.2b-iot-virtualizacao.html",
]


def load_json(path):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def normalize_module_7(lessons):
    module_7 = [lesson for lesson in lessons if lesson.get("module") == MODULE]
    by_filename = {lesson["filename"]: lesson for lesson in module_7}

    missing = [filename for filename in EXPECTED_FILES if filename not in by_filename]
    if missing:
        raise ValueError(
            "As lições atuais do módulo 7 não estão completas no JSON. "
            f"Arquivos ausentes: {', '.join(missing)}"
        )

    normalized = [by_filename[filename] for filename in EXPECTED_FILES]

    for lesson in normalized:
        lesson["module"] = MODULE

    # A auditoria lê apenas title/content/scenario/task. O termo SCADA estava
    # somente em highlight, então reforçamos o conceito em campos auditáveis.
    iot_lesson = by_filename["7.2b-iot-virtualizacao.html"]
    for step in iot_lesson.get("steps", []):
        if step.get("title") == "Ameaças IoT & Shodan":
            step["content"] = (
                "Sistemas de Internet das Coisas (IoT) possuem arquitetura "
                "extremamente heterogênea e recursos limitados, impedindo "
                "criptografias pesadas. Comandos sem sanitização causam DoS "
                "em <b>ICS e controladores industriais SCADA</b>, e erros "
                "revelam dados internos. Pior: muitos vêm com <b>senhas padrão "
                "de fábrica</b> expostas na internet, passivamente indexadas "
                "pelo buscador <b>Shodan.io</b>, que coleta os banners e portas "
                "expostas (Telnet, SSH)."
            )
            step["highlight"] = (
                "Câmeras IP, PLCs e painéis SCADA expostos viram alvos fáceis "
                "para invasores e auditorias."
            )
        elif step.get("type") == "quiz" and "mapear portas expostas" in step.get("task", ""):
            step["task"] = (
                "Se você precisa encontrar painéis de controle industrial "
                "(SCADA) e outros dispositivos IoT expostos na internet, "
                "qual motor de busca especializado utilizaria?"
            )

    return normalized


def main():
    lessons = load_json(JSON_PATH)
    module_7_lessons = normalize_module_7(lessons)
    lessons = [lesson for lesson in lessons if lesson.get("module") != MODULE]
    lessons.extend(module_7_lessons)
    save_json(JSON_PATH, lessons)
    print(f"Modulo 7 normalizado com {len(module_7_lessons)} licoes.")


if __name__ == "__main__":
    main()
