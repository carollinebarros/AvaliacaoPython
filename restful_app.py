from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

livrodereceitas = [
    {
        "Titulo": "Bolo de cenoura",
        "Ingredientes": [
            "2 xicaras de acucar",
            "3 cenouras medias raladas",
            "1/2 xicara (cha) de oleo",
            "4 ovos",
            "2 e 1/2 xicaras(cha) de farinha de trigo",
            "1 colher(sopa) de fermento em po"
        ],
         "Modo de preparo": "Em um liquidificador, adicione a cenoura, os ovos e o oleo, depois misture. Acrescente o acucar e bata novamente por 5 minutos. Em uma tigela ou na batedeira, adicione a farinha de trigo e depois misture novamente. Acrescente o fermento e misture lentamente com uma colher. Asse em um forno preaquecido a 180 graus, por aproximadamente 40 minutos.",
         "Rendimento": "8 porcoes"
    },
    {
        "Titulo": "Bolo de chocolate",
        "Ingredientes": [
            "4 ovos",
            "4 colheres (sopa) de chocolate em po",
            "2 colheres (sopa) de manteiga",
            "3 xicaras (cha) de farinha de trigo",
            "2 xicaras (cha) de acucar",
            "2 colheres (sopa) de fermento",
            "1 xicara (cha) de leite"
        ],
         "Modo de preparo": "Em um liquidificador, adicione a cenoura, os ovos e o oleo, depois misture. Acrescente o acucar e bata novamente por 5 minutos. Em uma tigela ou na batedeira, adicione a farinha de trigo e depois misture novamente. Acrescente o fermento e misture lentamente com uma colher. Asse em um forno preaquecido a 180 graus, por aproximadamente 40 minutos.",
         "Rendimento": "12 porcoes"
    }
]

class Receitas(Resource):
    def get(self):
        return livrodereceitas

    def post(self):
        newRec = json.loads(request.data)
        livrodereceitas.append(newRec)
        return {
            "message": "Receita Adicionada com sucesso!!!",
            "newValue": newRec
        }

class Receita(Resource):
    def get(self, indice):
        try:
            return livrodereceitas[indice]
        except IndexError:
            mensagem = "Receita {} inexistente!"
            return {
                "status": "Erro de indice",
                "message": mensagem,
            }
        except:
            mensagem = "Erro desconhecido!"
            return {
                "status": "Erro de indice",
                "message": mensagem,
            }

    def put(self, indice):
        newValue = json.loads(request.data)
        livrodereceitas[indice] = newValue
        return ({
            "message": "Receita Atualizada!",
            "newValue": newValue
        })
    def delete(self, indice):
        livrodereceitas.pop(indice)
        return ({
            "message": "Receita Deletada!",
            "arrayAtual": livrodereceitas
        })

api.add_resource(Receita, '/receitas/<int:indice>')
api.add_resource(Receitas, '/receitas')

if __name__ == '__main__':
    app.run(debug=True)