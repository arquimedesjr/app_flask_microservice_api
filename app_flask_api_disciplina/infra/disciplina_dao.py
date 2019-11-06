import sqlite3

from model.disciplina import Disciplina
from contextlib import closing

db_name = "disciplina.db"
model_name = "disciplinas"


def con():
    return sqlite3.connect(db_name)


def listar():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT * FROM {model_name}")
        rows = cursor.fetchall()
        registros = []
        for (id, nome, status, plano_ensino, carga_horaria, id_professor) in rows:
            registros.append(
                Disciplina.criar({"id": id, "nome": nome, "status": status, "plano_ensino": plano_ensino,
                                  "carga_horaria": carga_horaria, "id_professor": id_professor}))
        return registros


def consultar(id):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT * FROM {model_name} WHERE id = ?", (int(id),))
        row = cursor.fetchone()
        if row is None:
            return None
        return Disciplina.criar({"id": row[0], "nome": row[1], "status": row[2], "plano_ensino": row[3],
                                 "carga_horaria": row[4], "id_professor": row[5]})


def cadastrar(disciplina):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"INSERT INTO {model_name} (id, nome, status, plano_ensino, carga_horaria, id_professor) VALUES (?, ?, ?, ?, ?, ?)"
        result = cursor.execute(sql, (disciplina.id, disciplina.nome, disciplina.status, disciplina.plano_ensino,
                                      disciplina.carga_hotaria, disciplina.id_professor))
        connection.commit()
        if cursor.lastrowid:
            return disciplina.__dict__()
        else:
            return None


def alterar(disciplina):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"UPDATE {model_name} SET nome = ?, status = ?, plano_ensino = ?, carga_horaria = ?, id_professor = ? WHERE id = ?"
        cursor.execute(sql, (disciplina.nome, disciplina.status, disciplina.plano_ensino, disciplina.carga_hotaria,
                             disciplina.id, disciplina.id_professor))
        connection.commit()


def remover(disciplina):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"DELETE FROM {model_name} WHERE id = ?"
        cursor.execute(sql, f"{disciplina.id}")
        connection.commit()

def reseta():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"DELETE FROM {model_name}"
        cursor.execute(sql)
        connection.commit()
