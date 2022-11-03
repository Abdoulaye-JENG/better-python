"""
The purpose here is to work with protocol segregation.
For that, we'll use the `Demonstration by absurdity` to prove his usefulness.
-- Check the `main` function below.
"""
# from abc import ABC, abstractmethod
from typing import Protocol

from iot.devices import HueLight, SmartBattery, SmartSpeaker
from iot.message import Message, MessageType
from iot.service import IOTService


class Device(Protocol):
    def check_status(self) -> None:
        ...
    def send_message(self, message_type:MessageType, data:str) -> None:
        ...
    
def run_program(program:list[Message], devices:dict[str, Device]):
    print("***** RUNNING PROGRAM *****")
    for msg in program:
        devices[msg.device_id].send_message(msg.message_type, msg.data)
    print("***** PROGRAM ENDED *****")



def check_status(devices:dict[str, Device]) -> None:
    print("***** CHECKING STATUS *****")
    for device in devices.values():
        print(f"=: device type: [{type(device).__name__}]")
        device.check_status()


def main() -> None:
    devices = {
        "hue_light":HueLight(),
        "speaker":SmartSpeaker()
    } 
    status_sources = devices | {"battery":SmartBattery()}
    #
    wake_up_program = [
        Message("hue_light", MessageType.SWITCH_ON),
        Message("speaker", MessageType.SWITCH_ON),
        Message("hue_light", MessageType.PLAY_SONG, "Mawahibu Nâfih - S. Mahib GUEYE"),
    ]
    # Run Program
    # run_program(program=wake_up_program, devices=status_sources)

    # !!!!!!! IMPORTANT !!!!!!
    # If we call the `check_status` function below by passing it <status_sources> dict 
    # as argument, we'll get an error even though the `check_status` method 
    # has nothing to do with `send_message` method of the `DEVICE` pROTOCOL.
    # - The reason is that the <status_sources> adds another device (SmartBattery) to 
    # the devices list; which does not implement the `send_message` method `DEVICE` pROTOCOL.
    # So it (SmartBattery) is not considered as a Device.
    # !!!!!!!!!!!!!
    
    # ------ Check Status
    check_status(devices=status_sources)

def main2() -> None:
    devices = {
        "hue_light":HueLight(),
        "speaker":SmartSpeaker()
    } 
    status_sources = devices | {"battery":SmartBattery()}
    #
    wake_up_program = [
        Message("hue_light", MessageType.SWITCH_ON),
        Message("speaker", MessageType.SWITCH_ON),
        Message("hue_light", MessageType.PLAY_SONG, "Mawahibu Nâfih - S. Mahib GUEYE"),
    ]
    # Using the service
    iot = IOTService()
    for device_id, device in status_sources.items():
        iot.register_device(device_id=device_id,device=device)
    
    # Running Program
    iot.run_program(wake_up_program)
    # Checking status
    iot.check_status(status_sources.keys())
    
if __name__ == '__main__':
    # main()
    main2()
