import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
import pywhatkit as kit

# Autenticação e escopo
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(
    r"banco de dados delivery\statusentregapy-44e8d9b051ce.json",  # Usando string raw
    scope
)

# Autentica e abre a planilha
client = gspread.authorize(creds)
sheet = client.open("STATUS DE ENTREGA PY").sheet1

# Função para enviar mensagens no WhatsApp
def enviar_whatsapp(mensagem, destinatario):
    try:
        kit.sendwhatmsg_instantly(destinatario, mensagem)
        print(f"Mensagem enviada para {destinatario}: {mensagem}")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")

# Função para monitorar a planilha e enviar mensagens
def monitorar_planilha():
    ultimo_valor = None  # Armazena o último valor da coluna específica

    while True:
        try:
            # Obtém todas as linhas da planilha
            all_rows = sheet.get_all_values()
            
            if all_rows:
                last_row = all_rows[-1]  # Última linha da planilha
                coluna_especifica = last_row[11]  # Acessa coluna (índice 11)

                # Verifica se o valor da coluna mudou
                if coluna_especifica != ultimo_valor:
                    ultimo_valor = coluna_especifica

                    # Verifica o valor da coluna e envia a mensagem correspondente
                    if coluna_especifica == "AG. RETIRADA":
                        mensagem = "Olá, espero que esteja tudo bem! Pedido solicitado com sucesso."
                        enviar_whatsapp(mensagem, "+5535984477033")

                    elif coluna_especifica == "EM ROTA DE ENTREGA":
                        mensagem = "Pedido em rota de entrega. Aguarde atentamente ao som da buzina!"
                        enviar_whatsapp(mensagem, "+5535992017154")

                    elif coluna_especifica == "ENTREGUE":
                        mensagem = "Olá, pedido entregue com sucesso."
                        enviar_whatsapp(mensagem, "+553591136206")

        except Exception as e:
            print(f"Erro ao acessar a planilha: {e}")

        time.sleep(10)  # Verifica a cada 10 segundos

# Executa a função para monitorar a planilha
monitorar_planilha()
