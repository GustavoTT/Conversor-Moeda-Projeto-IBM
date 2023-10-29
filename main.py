import tkinter
from tkinter import FALSE, NE, NSEW, NW, ttk
import requests
import xml.etree.ElementTree as ET

# ESTILIZAÇÃO
escuro = "#bbe7c2"
claro = "#195823"
cinza = "#e5e4e7"
preto = "#000"

# Função para acessar API e retornar a moeda e o valor convertido
def buscar_cotacao():
    try:

        # Pega as moedas solicitadas pelo usuário
        moedaOrigem = selectMoedaOrigem.get().upper()
        moedaDestino = selectMoedaDestino.get().upper()
        valorNC = float(entryValor.get())
        
        # Conecta com a API e passa os parâmetros
        requisicao = requests.get(f'https://economia.awesomeapi.com.br/last/{moedaOrigem}-{moedaDestino}')
        dados = requisicao.json()
        
        # Recolhe o cambio
        cambio = dados[f'{moedaOrigem}{moedaDestino}']['name']
        valorCambio = float(dados[f'{moedaOrigem}{moedaDestino}']['bid'])
        
        # Calcula e retorna a resposta
        valorC = valorNC * valorCambio
        texto = f'{cambio}: {valorCambio:.2f}\n{valorNC:.2f} {moedaOrigem} = {valorC:.2f} {moedaDestino}'
        txtResult["text"] = texto

    except:
        txtResult["text"] = "Transação inválida! Se os campos estiverem preenchidos:\nAs moedas não possuem conversão em nosso sistema.\nLamentamos."

# Função para coletar o nome completo da moeda no arquivo uniq.xml
def busca_nome(cod):
    tree = ET.parse('uniq.xml')
    for desc in tree.findall(cod):
        return(desc.text)

# Função para obter e exibir o nome da moeda de ORIGEM
def obterCBOrigem(eventObject):
    # Limpa o campo
    lbMoeOr = tkinter.Label(frameBaixo, text = "                                                                 ", bg=cinza)
    lbMoeOr.place(x=42, y=55)
    # Solicita o nome
    cod = selectMoedaOrigem.get()
    nome = busca_nome(cod)
    txt = f'{cod}: {nome}'
    # Exibe o nome
    lbMoeOr = tkinter.Label(frameBaixo, text = txt, bg=cinza, font="Ivy 9")
    lbMoeOr.place(x=42, y=55)

# Função para obter e exibir o nome da moeda de DESTINO
def obterCBDestino(eventObject):
    # Limpa o campo
    lbMoeDes = tkinter.Label(frameBaixo, text = "                                                                 ", bg=cinza)
    lbMoeDes.place(x=300, y=55)
    # Solicita o nome
    cod = selectMoedaDestino.get()
    nome = busca_nome(cod)
    txt = f'{cod}: {nome}'
    # Exibe o nome
    lbMoeDes = tkinter.Label(frameBaixo, text = txt, bg=cinza, font="Ivy 9")
    lbMoeDes.place(x=300, y=55)


# Criação e configuração da janela de exibição
janela = tkinter.Tk()
janela.title("Cotação de Moedas")
janela.geometry("500x310")
janela.configure(background=cinza)
janela.resizable(width=FALSE, height=FALSE)

# Dividindo a tela
frameCima = tkinter.Frame(janela, width=500, height=50, bg=escuro, relief='flat')
frameCima.grid(row=0, columnspan=2, padx=0, pady=1, sticky=NSEW)

frameBaixo = tkinter.Frame(janela, width=500, height=260, bg=cinza, relief='flat')
frameBaixo.grid(row=1, column=0, padx=0, pady=1, sticky=NSEW)

# Titulo
txtTitulo = tkinter.Label(frameCima, text="CONVERSOR DE MOEDAS", anchor=NE, fg=claro, font=("Verdana 20"), bg=escuro)
txtTitulo.place(x=75, y=5)
linha = tkinter.Label(frameCima, text="", width=475, anchor=NW, bg=claro, font=("Ivy 1"))
linha.place(x=10, y=45)

# Label
txtCvt = tkinter.Label(frameBaixo, text="CONVERTER", anchor=NE, font=("Verdana, 11"), bg=cinza, fg=preto)
txtCvt.place(x=10, y=5)

# Label Origem
txtOrg = tkinter.Label(frameBaixo, text="DE:", anchor=NE, font=("Verdana, 11"), bg=cinza, fg=preto)
txtOrg.place(x=10, y=30)

# Combobox ORIGEM
selectMoedaOrigem = ttk.Combobox(frameBaixo, width=20, state="readonly", justify="left", font=("Verdana, 11"))
selectMoedaOrigem['values'] = ("AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BND", "BOB", "BRL", "BRLT", "BSD", "BTC", "BWP", "BYN", "BZD", "CAD", "CHF", "CHFRTS", "CLP", "CNH", "CNY", "COP", "CRC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOGE", "DOP", "DZD", "EGP", "ETB", "ETH", "EUR", "FJD", "GBP", "GEL", "GHS", "GMD", "GNF", "GTQ", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "INR", "IQD", "IRR", "ISK", "JMD", "JOD", "JPY", "JPYRTS", "KES", "KGS", "KHR", "KMF", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LSL", "LTC", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRO", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN", "NAD", "NGN", "NGNI", "NGNPARALLEL", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RUBTOD", "RUBTOM", "RWF", "SAR", "SCR", "SDG", "SDR", "SEK", "SGD", "SOS", "STD", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TRY", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "USDT", "UYU", "UZS", "VEF", "VND", "VUV", "XAF", "XAGG", "XBR", "XCD", "XOF", "XPF", "XRP", "YER", "ZAR", "ZMK", "ZWL", "XAU")
selectMoedaOrigem.current(1)
selectMoedaOrigem.place(x=42, y=30)

# Label com nome da moeda de Origem
selectMoedaOrigem.bind("<<ComboboxSelected>>", obterCBOrigem)

# Label Destino
txtPara = tkinter.Label(frameBaixo, text="PARA:", anchor=NE, font=("Verdana, 11"), bg=cinza, fg=preto)
txtPara.place(x=250, y=30)

# Combobox DESTINO
selectMoedaDestino = ttk.Combobox(frameBaixo, width=20, state="readonly", justify="left", font=("Verdana, 11"))
selectMoedaDestino['values'] = ("AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BND", "BOB", "BRL", "BRLT", "BSD", "BTC", "BWP", "BYN", "BZD", "CAD", "CHF", "CHFRTS", "CLP", "CNH", "CNY", "COP", "CRC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOGE", "DOP", "DZD", "EGP", "ETB", "ETH", "EUR", "FJD", "GBP", "GEL", "GHS", "GMD", "GNF", "GTQ", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "INR", "IQD", "IRR", "ISK", "JMD", "JOD", "JPY", "JPYRTS", "KES", "KGS", "KHR", "KMF", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LSL", "LTC", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRO", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN", "NAD", "NGN", "NGNI", "NGNPARALLEL", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RUBTOD", "RUBTOM", "RWF", "SAR", "SCR", "SDG", "SDR", "SEK", "SGD", "SOS", "STD", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TRY", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "USDT", "UYU", "UZS", "VEF", "VND", "VUV", "XAF", "XAGG", "XBR", "XCD", "XOF", "XPF", "XRP", "YER", "ZAR", "ZMK", "ZWL", "XAU")
selectMoedaDestino.current(17)
selectMoedaDestino.place(x=300, y=30)

# Label com nome da moeda de Destino
selectMoedaDestino.bind("<<ComboboxSelected>>", obterCBDestino)

# Label Entrada valor
txtValor = tkinter.Label(frameBaixo, text="VALOR PARA CONVERSÃO:", anchor=NE, font=("Verdana, 11"), bg=cinza, fg=preto)
txtValor.place(x=10, y=90)

# Entrada do valor a ser convertido
entryValor = tkinter.Entry(frameBaixo, width=33, justify='left', font=("Verdana, 11"), bd=2)
entryValor.place(x=215, y=90)
leg = tkinter.Label(frameBaixo, text="Formato aceitado 000.00", font=("Verdana, 9"), bg=cinza, fg=preto)
leg.place(x=215, y=115)

# Botão para calcular
btn = tkinter.Button(frameBaixo, text="REALIZAR CONVERSÃO", command=buscar_cotacao, bd=2, bg=escuro, font=("Ivy, 12"), fg=claro, width=52)
btn.place(x=10, y=150)

# Label de resultado
txtResult = tkinter.Label(frameBaixo, text="", font=("Ivy 11 bold"), bg=cinza, fg=preto, justify="center", width=50)
txtResult.place(x=20, y=190)

janela.mainloop()