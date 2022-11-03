"""
The purpose here is to work with protocol segregation.
In this module, we'll fix bugs in the 'before.py' module.
To do this, we need to segregate the device protocol by 
1. spliting it into 2 protools: StatusSource(Protocol) & Device(Protoccol)
2. changing the `devices`'s type odd the  `check_status` method to be ['str', 'StatusSource']  
"""

from typing import Protocol

from iot.devices import HueLight, SmartBattery, SmartSpeaker
from iot.message import Message, MessageType


class StatusSource(Protocol):
    def check_status(self) ->None:
        ...
class Device(Protocol):
    def send_message(self, message_type:MessageType, data:str) -> None:
        ...
    
def run_program(program:list[Message],devices:dict[str,Device]):
    
    print("***** RUNNING PROGRAM *****")
    for msg in program:
        devices[msg.device_id].send_message(msg.message_type, msg.data)
    print("***** PROGRAM ENDED *****")



def check_status(devices:dict[str, StatusSource]) -> None:
    print("***** CHECKING STATUS *****")
    for device in devices.values():
        device.check_status()


def main() -> None:
    devices = {
        "hue_light":HueLight(),
        "speaker":SmartSpeaker()
    } 
    status_sources = devices | {"battery":SmartBattery()}
    wake_up_program = [
        Message("hue_light", MessageType.SWITCH_ON),
        Message("speaker", MessageType.SWITCH_ON),
        Message("hue_light", MessageType.PLAY_SONG),
    ]
    # Run Program
    run_program(program=wake_up_program, devices=devices)

    # Check Status
    # !!!!!!! IMPORTANT !!!!!::
    # If we call the `check_status` function below by passing it <status_sources> dict 
    # as argument, we'll get an error even though the `check_status` method 
    # has nothing to do with `send_message` method of the `DEVICE` pROTOCOL.
    # - The reason is the <status_sources> adds another device (SmartBattery) to the devices list;
    # which does not implement the `send_message` method `DEVICE` pROTOCOL.
    # So it (SmartBattery) is not considered as a Device.
    # !!!!!!!!!!!!!
    check_status(devices=status_sources)

if __name__ == '__main__':
    main()
