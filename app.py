from flask import jsonify

from app import app, db
from app.core.import_from_csv import import_csv_from_directory


@app.route("/import_csv", methods=["POST"])
def import_csv():
    try:
        import_csv_from_directory()
        return jsonify({"message": "Імпорт CSV файлів успішно завершений!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5001)
