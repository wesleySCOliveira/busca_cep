import requests
import time

class Cep:
    def initial(self):
        while True:
            option = input("Digite 1 Para pesquisa por CEP ou Digite 2 para perquisa por endereço ou Digite 0 Para sair:")
            if option == '1':
                cep = input("Digite o cep: ")
                cep = cep.replace(' ','').replace('.','').replace('-','').replace('/','')
                if len(cep) == 8:
                    link = f'https://viacep.com.br/ws/{cep}/json/'
                    response = requests.get(link)
                    dic_response = response.json()
                    uf = dic_response['uf']
                    cidade = dic_response['logradouro']
                    bairro = dic_response['bairro']
                    print(dic_response)
                else:
                    print('Cep Invalido!')
                    time.sleep(2)
            elif option == '2':
                uf = input('Digite a UF:')
                cidade = input('Digite a cidade:')
                endereco = input('Digite o Endereço:')
                link = f'https://viacep.com.br/ws/{uf}/{cidade}/{endereco}/json/'
                requisicao = requests.get(link)
                dic_requisicao = requisicao.json()
                print(dic_requisicao)
            elif option == '0':
                break
            else:
                print("Digito invalido")
