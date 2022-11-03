from typing import Protocol

from iot.message import Message, MessageType


class Device(Protocol):
    def check_status(self) -> None:
        ...
    
    def send_message(self, message_type: MessageType, data) -> None:
        ...



class IOTService:
    def __init__(self):
        self.devices: dict[str,Device] = {}
        
    def register_device(self, device_id:str, device:Device):
        self.devices[device_id] = device
    
    def get_device(self, device_id:str):
        try:
            return self.devices[device_id]
        except KeyError:
            raise ValueError(f"A device with ID({device_id} does not exists.)")

    def run_program(self, program:list[Message]):
        print("***** RUNNING PROGRAM *****")
        for msg in program:
            self.send_msg(msg)
        print("***** PROGRAM ENDED *****")
        
    def send_msg(self, msg:Message) -> None:
        self.devices[msg.device_id].send_message(message_type=msg.message_type, data=msg.data)

    def check_status(self, device_ids:list[str]=None) -> None:
        if not device_ids:
            if not self.devices:
                raise ValueError("You have to register a device first")
            device_ids = list(self.devices.keys())
        print("***** CHECKING STATUS *****")
        for device_id in device_ids:
            device = self.devices[device_id]
            print(f"=: device type: [{type(device).__name__}]")
            device.check_status()
