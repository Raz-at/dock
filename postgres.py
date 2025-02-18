from sqlalchemy import create_engine, text
from flask import Flask, render_template, request
from sqlalchemy.exc import SQLAlchemyError


app = Flask(__name__)

def get_db_connection():
    return create_engine('postgresql://user:password@postgres:5432/postgresDB')

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    db_engine = get_db_connection()
    try:
        with db_engine.connect() as connection:
            tranasction = connection.begin()
            insert_query = text("INSERT INTO dock.user_detail (name) VALUES (:name)")
            connection.execute(insert_query, {"name": name})
            tranasction.commit()  
        return "Data is inserted"
    except SQLAlchemyError as e:
        print("Error while inserting:", e)
        return "Database insertion error", 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

