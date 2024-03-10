from flask import Flask
from Storage import storage
import os
from Logics import reporting
app = Flask(__name__)

@app.route("/api/report/<storage_key>/<format>", methods=["GET"])
def get_report(storage_key: str, format: str):
    s = storage()
    if storage_key not in s.get_all_keys():
        response_type = app.response_class(
            response=f"Такого ключа не существует",
            status=500,
            mimetype="application/text"
        )

        return response_type

    if format not in [x.split(".")[0][5:] for x in os.listdir("logic/formats")]:
        response_type = app.response_class(
            response=f"Ключ существует, но этот формат экспорта недоступен",
            status=500,
            mimetype="application/text"
        )
        return response_type


    response_type = app.response_class(
        response=f"{reporting.create(reporting(), format, 'Сюда нужно передать данные')}",
        status=200,
        mimetype="application/text"
    )

    return response_type


if __name__ == "__main__":
    app.run(debug=True)
