from sanic import Sanic
from sanic.response import json


app = Sanic()


@app.route("/")
async def test(request):
    return json({"hello": "world"})


@app.route("/map/<mapid>")
async def mapid(request, mapid):
    return json({"hello": mapid})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
