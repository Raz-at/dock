from sqlalchemy import create_engine, text
from flask import Flask, render_template, request
from sqlalchemy.exc import SQLAlchemyError


app = Flask(__name__)

def get_db_connection():
    return create_engine('postgresql://user:password@postgres:5432/postgresDB')

# while True:
#     try:
#         db_engine = get_db_connection().connect()
#         print("Database connection successful!")
#         break
#     except Exception as e:
#         print("Error..", e)
#         continue

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    db_engine = get_db_connection()
    try:
        with db_engine.connect() as connection:
            insert_query = text("INSERT INTO dock.user_detail (name) VALUES (:name)")
            connection.execute(insert_query, {"name": name})
            connection.commit()  # Commit the transaction
        return "Data is inserted"
    except SQLAlchemyError as e:
        print("Error while inserting:", e)
        return "Database insertion error", 500


if __name__ == '__main__':
    app.run(debug=True)
