import azure.functions as func
import logging
import requests
import os

app = func.FunctionApp()

@app.route(route="http_trigger_atividade_teste_1")
def http_trigger_atividade_teste_1(req: func.HttpRequest) -> func.HttpResponse:
    nome = req.params.get('nome')
    if not nome:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            nome = req_body.get('nome')

    if nome:
        return func.HttpResponse(f"Oi, {nome}")
    else:
        return func.HttpResponse(
             "Qual teu nome amigo",
             status_code=200
        )

@app.timer_trigger(schedule="0 * * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False)
def timer_trigger_atividade_teste_1(myTimer: func.TimerRequest) -> None:
    paranoid = os.environ.get("paranoid")
    response = requests.get(paranoid, {"nome" : "Riverson"})
    logging.info(response.text)

@app.route(route="http_trigger_parametro", auth_level=func.AuthLevel.FUNCTION)
def http_trigger_parametro(req: func.HttpRequest) -> func.HttpResponse:
    parametro = req.params.get('parametro')
    if not parametro:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            parametro = req_body.get('parametro')

    if parametro:
        return func.HttpResponse(parametro)
    else:
        return func.HttpResponse(
             "Faltou o parametro",
             status_code=200
        )

@app.timer_trigger(schedule="0 * * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def timer_trigger_log(myTimer: func.TimerRequest) -> None:
    logging.info('Apenas um log')
