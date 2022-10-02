import requests
import json
import time
import pandas as pd


while True:

    try:
        data = requests.get(
            'https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json')

        json_data = json.loads(data.content)

        candidato = []
        votos = []
        porcentagem = []

        for informacoes in json_data['cand']:

            if int(informacoes['seq']) in range(1, 12):
                candidato.append(informacoes['nm'])
                votos.append(informacoes['vap'])
                porcentagem.append(f"{informacoes['pvap']}%")

        df_eleicao = pd.DataFrame(list(zip(candidato, votos, porcentagem)), columns=[
            'Candidato', 'Nº de Votos', 'Porcentagem'
        ])

        print(f"\nUrnas apuradas: {json_data['psi']}% \n")
        print(f"{df_eleicao} \n")
        print(f"Última atualização: {json_data['dt']} {json_data['ht']}")
    except:
        print('Atualizando novamente...')

    time.sleep(5)
