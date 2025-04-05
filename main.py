from fastapi import FastAPI, Request, Response
from pathlib import Path
from fastapi.responses import JSONResponse
import json

app = FastAPI()
SONOLUS_HEADERS = {"Sonolus-Version": "0.8.12"}

with open('serverinfo.json', 'r') as f:
    server_info = json.load(f)

with open('public/index.html', 'r',encoding='utf-8') as f:
    index_html = f.read()

@app.middleware("http")
async def log_request(request: Request, call_next):
    print('--- Incoming Request ---')
    print('Method:', request.method)
    print('URL:', request.url)
    print('Headers:', request.headers)
    print('Query Parameters:', request.query_params)
    body = await request.body()
    print('Body:', body)
    print('----------------------')
    
    response = await call_next(request)
    return response

@app.get("/")
async def get_index():
    return Response(content=index_html, media_type="text/html")

# sonolusエンドポイント

@app.get("/sonolus/info")
async def get_server_info():
    return JSONResponse(content=server_info, headers=SONOLUS_HEADERS)

@app.get("/sonolus/{type}/info")
async def get_item_info(type: str):
    try:
        with open(f'sonolus/{type}/info', 'r') as f:
            content = json.load(f)

        return JSONResponse(content=content, headers=SONOLUS_HEADERS)
    except FileNotFoundError:
        return JSONResponse(
            status_code=404,
            content={"message": f"Info for type '{type}' not found"}
        )

@app.get("/sonolus/{type}/list")
async def get_item_list(type: str):
    try:
        with open(f'sonolus/{type}/list', 'r') as f:
            content = json.load(f)

        return JSONResponse(content=content, headers=SONOLUS_HEADERS)
    except FileNotFoundError:
        return JSONResponse(
            status_code=404,
            content={"message": f"list for type '{type}' not found"}
        )
    
@app.get("/sonolus/levels/{level_name}")
async def get_level(level_name: str):
    try:
        with open(f'sonolus/levels/{level_name}', 'r') as f:
            content = json.load(f)

        return JSONResponse(content=content, headers=SONOLUS_HEADERS)
    except FileNotFoundError:
        return JSONResponse(
            status_code=404,
            content={"message": f"list for type '{type}' not found"}
        )
    
@app.get("/sonolus/effects/{effect_name}")
async def get_effect(effect_name: str):
    try:
        with open(f'sonolus/effects/{effect_name}', 'r') as f:
            content = json.load(f)

        return JSONResponse(content=content, headers=SONOLUS_HEADERS)
    except FileNotFoundError:
        return JSONResponse(
            status_code=404,
            content={"message": f"list for type '{type}' not found"}
        )
    
@app.get("/sonolus/backgrounds/{backgrounds_name}")
async def get_backgrounds(backgrounds_name: str):
    try:
        with open(f'sonolus/backgrounds/{backgrounds_name}', 'r') as f:
            content = json.load(f)

        return JSONResponse(content=content, headers=SONOLUS_HEADERS)
    except FileNotFoundError:
        return JSONResponse(
            status_code=404,
            content={"message": f"list for type '{type}' not found"}
        )
    
@app.get("/sonolus/skins/{skins_name}")
async def get_skins(skins_name: str):
    try:
        with open(f'sonolus/skins/{skins_name}', 'r') as f:
            content = json.load(f)

        return JSONResponse(content=content, headers=SONOLUS_HEADERS)
    except FileNotFoundError:
        return JSONResponse(
            status_code=404,
            content={"message": f"list for type '{type}' not found"}
        )
    
@app.get("/sonolus/engines/{engines_name}")
async def get_engines(engines_name: str):
    try:
        with open(f'sonolus/engines/{engines_name}', 'r') as f:
            content = json.load(f)

        return JSONResponse(content=content, headers=SONOLUS_HEADERS)
    except FileNotFoundError:
        return JSONResponse(
            status_code=404,
            content={"message": f"list for type '{type}' not found"}
        )
    
@app.get("/sonolus/particles/{particles_name}")
async def get_particles(particles_name: str):
    try:
        with open(f'sonolus/particles/{particles_name}', 'r') as f:
            content = json.load(f)

        return JSONResponse(content=content, headers=SONOLUS_HEADERS)
    except FileNotFoundError:
        return JSONResponse(
            status_code=404,
            content={"message": f"list for type '{type}' not found"}
        )
    
@app.get("/sonolus/repository/{file_hash}")
async def get_repository_file(file_hash: str):
    file_path = Path(f"/sonolus/repository/{file_hash}")  

    if not file_path.exists():
        return Response(content="File not found", status_code=404)

    with file_path.open("rb") as f:
        content = f.read()

    return Response(content=content, media_type="application/zip")


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)
