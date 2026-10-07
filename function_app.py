import azure.functions as func
import logging
import os
import pyodbc

def extract_from_table(tableName):
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

        cursor.execute(f"SELECT * FROM itsm.{tableName}")
        for row in cursor.fetchall():
            logging.info(row)
    except Exception as e:
        logging.info(e)

app = func.FunctionApp()

@app.timer_trigger(schedule="0 */30 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False)
def extract_analista(myTimer: func.TimerRequest) -> None:
    extract_from_table("analista")

@app.timer_trigger(schedule="0 */30 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False)
def extract_categoria(myTimer: func.TimerRequest) -> None:
    extract_from_table("categoria")

@app.timer_trigger(schedule="0 */30 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False)
def extract_chamado(myTimer: func.TimerRequest) -> None:
    extract_from_table("chamado")

@app.timer_trigger(schedule="0 */30 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False)
def extract_chamado_sla(myTimer: func.TimerRequest) -> None:
    extract_from_table("chamado_sla")

@app.timer_trigger(schedule="0 */30 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False)
def extract_chamado_status_historico(myTimer: func.TimerRequest) -> None:
    extract_from_table("chamado_status_historico")

@app.timer_trigger(schedule="0 */30 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False)
def extract_cliente_organizacao(myTimer: func.TimerRequest) -> None:
    extract_from_table("cliente_organizacao")

@app.timer_trigger(schedule="0 */30 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False)
def extract_csat_avaliacao(myTimer: func.TimerRequest) -> None:
    extract_from_table("csat_avaliacao")

@app.timer_trigger(schedule="0 */30 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False)
def extract_fila(myTimer: func.TimerRequest) -> None:
    extract_from_table("fila")

@app.timer_trigger(schedule="0 */30 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False)
def extract_sla(myTimer: func.TimerRequest) -> None:
    extract_from_table("sla")

@app.timer_trigger(schedule="0 */30 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False)
def extract_solicitante(myTimer: func.TimerRequest) -> None:
    extract_from_table("solicitante")
