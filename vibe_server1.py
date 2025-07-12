# vibe_server1.py (Correct version for buttplug-py v3+)
import asyncio
import logging
from contextlib import asynccontextmanager

from buttplug import Client, WebsocketConnector, ProtocolSpec
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# --- Configuration ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
INTIFACE_HOST = "127.0.0.1"
INTIFACE_PORT = 12345
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8765

# --- Device Management Class ---
class DeviceManager:
    def __init__(self):
        self.client = Client("Live Vibe Server", ProtocolSpec.v3)
        self.device = None
        self.connector = WebsocketConnector(f"ws://{INTIFACE_HOST}:{INTIFACE_PORT}", logger=self.client.logger)

    async def connect(self):
        logging.info("Attempting to connect to Intiface...")
        try:
            await self.client.connect(self.connector)
            logging.info("Successfully connected to server. Scanning for devices...")
            await self.client.start_scanning()
            await asyncio.sleep(2)
            await self.client.stop_scanning()

            if not self.client.devices:
                logging.warning("No devices found. Please ensure a device is connected to Intiface.")
                return

            self.device = self.client.devices[0]
            if not self.device.actuators:
                 logging.error(f"Device {self.device.name} has no vibration actuators.")
                 self.device = None
                 return
            
            logging.info(f"Locked on to device: {self.device.name}")

        except Exception as e:
            logging.error(f"Could not connect to Intiface server: {e}")
            self.client = None

    async def disconnect(self):
        if self.client and self.client.is_connected:
            logging.info("Disconnecting from Intiface server.")
            await self.client.disconnect()

    async def set_vibration(self, intensity: float):
        if not self.device:
            logging.warning("Vibration command ignored: No device connected.")
            raise HTTPException(status_code=503, detail="Device not connected")
        
        logging.info(f"Setting vibration to {intensity:.2f}")
        await self.device.actuators[0].command(intensity)

device_manager = DeviceManager()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await device_manager.connect()
    yield
    if device_manager.device:
        await device_manager.set_vibration(0)
    await device_manager.disconnect()

app = FastAPI(lifespan=lifespan)

class VibeCommand(BaseModel):
    intensity: float = Field(..., ge=0.0, le=1.0)

@app.post("/vibrate")
async def vibrate_device(command: VibeCommand):
    await device_manager.set_vibration(command.intensity)
    return {"status": "success", "intensity_set": command.intensity}

@app.get("/status")
async def get_status():
    if device_manager.device:
        return {"connected": True, "device_name": device_manager.device.name}
    return {"connected": False, "device_name": None}