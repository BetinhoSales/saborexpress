from fastapi import FastAPI, Query

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    return {'Hello':'World'}

    @app.get('/api/restaurante/')
    def get_restaurantes(restaurante: str = Query(None)):
        pass