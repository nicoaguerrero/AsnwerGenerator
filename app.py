from flask import Flask, render_template, request, redirect, url_for
import os
import psycopg2
from src.utils import setup_vectorstore, add_qa_pair, search_question, search_and_respond
from src.llm import build_llm
from huggingface_hub import login
app = Flask(__name__)

vector_store = setup_vectorstore()
model = build_llm()

@app.route('/add_question', methods=['POST'])
def add_question():

    question = request.form.get('question')

    answer = search_and_respond(model, vector_store, question)

    # add_qa_pair(question, answer) // Para agregarlos a chromadb

    db_url = os.getenv("DATABASE_URL")
    # Conexion con la base de datos
    conn = psycopg2.connect("DATABASEURL")
    cur = conn.cursor()
    cur.execute("INSERT INTO product_qa (question, answer, aigenerated) VALUES (%s, %s)", (question, answer, True))
    conn.commit()
    cur.close()
    conn.close()

    return redirect(url_for('main'))

@app.route('/')
def main():  # put application's code here

    login(token="HUGGINGFACETOKEN")

    # Devolver ordenado por ID, y cambiar el ultimo a generado por IA

    conn = psycopg2.connect("DATABASEURL")
    cur = conn.cursor()
    cur.execute("""
    SELECT question, answer, aigenerated 
    FROM product_qa
    """)

    data = cur.fetchall()

    return render_template('main.html', data=data)


if __name__ == '__main__':
    app.run()
