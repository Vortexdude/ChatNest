#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import APIRouter, WebSocket
from src.ws.wsmanager import ConnectionManager
from starlette.websockets import WebSocketDisconnect

router = APIRouter()
manager = ConnectionManager()

@router.websocket("/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")
