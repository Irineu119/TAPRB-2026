import azure.functions as func
import logging
import os
import pyodbc

app = func.FunctionApp()

@app.timer_trigger(schedule="0 */30 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False)
def extract_chamado(myTimer: func.TimerRequest) -> None:
    host = os.getenv("HOST")
    banco = os.getenv("DATABASE")
    usuario = os.getenv("USER")
    senha = os.getenv("PASSWORD")
    
    conn_str = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={host};"
        f"DATABASE={banco};"
        f"UID={usuario};"
        f"PWD={senha};"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
        "Connection Timeout=30;"
    )

    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # select na tabela itsm.chamado
        cursor.execute("SELECT * FROM itsm.chamado")
        for row in cursor.fetchall():
            logging.info(row)
    except Exception as e:
        logging.info(e)
