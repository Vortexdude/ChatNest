#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import APIRouter, WebSocket
from src.ws.wsmanager import ConnectionManager
from starlette.websockets import WebSocketDisconnect
import json

router = APIRouter()
manager = ConnectionManager()

@router.websocket("")
async def websocket_endpoint(websocket: WebSocket):
    client_id = ""

    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            out_data = json.loads(data)
            print(out_data)
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")
