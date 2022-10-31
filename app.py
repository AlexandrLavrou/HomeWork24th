import os

from marshmallow.exceptions import ValidationError  # type: ignore
from flask import Flask, request, abort

from classes.commands import Commands, CommandsSchema
from constants import DATA_DIR
from classes.search import Search

app = Flask(__name__)


@app.route("/perform_query/", methods=['GET', 'POST'])
def perform_query():  # type: ignore
    try:
        if request.method == 'GET':
            commands: Commands = CommandsSchema().load(request.args)
        else:
            commands: Commands = CommandsSchema().load(request.json)
        if not os.path.exists(DATA_DIR):
            raise FileNotFoundError('Передано неверное имя файла')

        # Выполнять переданные команды и возвращать результаты в ответ
        with open(DATA_DIR, 'r') as file:
            cmd1_result = getattr(Search, commands.cmd1)(file, commands.value1)
            cmd2_result = getattr(Search, commands.cmd2)(cmd1_result, commands.value2)
            return app.response_class('\n'.join([line.strip() for line in cmd2_result]), content_type="text/plain")

    except (ValueError, FileNotFoundError, TypeError, IndexError, ValidationError) as e:
        abort(400, e)

    return app.response_class(cmd2_result, content_type="text/plain")


if __name__ == '__main__':
    app.run(debug=True)
