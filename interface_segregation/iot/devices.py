from iot.message import MessageType


class SmartBattery:
    def check_status(self) -> None:
        print("Battery is online.")


class HueLight:
    def check_status(self) -> None:
        print("HueLight is conected.")

    def send_message(self, message_type:MessageType, data:str=""):
        print(f"HueLight is handling a message of type: {message_type.name} with data [{data}]")
        print("HueLight received message.")


class SmartSpeaker:
    def check_status(self) -> None:
        print("Smart Speaker connected.")
        
    def send_message(self, message_type:MessageType,data:str=""):
        print(f"Smart Speaker is handling a message of type: {message_type.name} with data [{data}]")
        print("Smart Speaker received message.")
