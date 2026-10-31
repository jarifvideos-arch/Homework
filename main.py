from abc import ABC,abstractmethod
class SmartDevice(ABC):
    def show_device(self,name):
        print("Device Name:",name)
    @abstractmethod
    def turn_on(self):
        pass
class SmartLight(SmartDevice):
    def turn_on(self):
        print("Smart Light is now on")
class SmartFan(SmartDevice):
    def turn_on(self):
        print("Smart Light is now on")
class SmartSpeaker(SmartDevice):
    def turn_on(self):
        print("Smart speaker is now on")
light=SmartLight()
fan=SmartFan()
speaker=SmartSpeaker()
light.show_device("Living room light")
light.turn_on()
fan.show_device("Bedroom Fan")
fan.turn_on()
speaker.show_device("Music Speaker")
speaker.turn_on()
class SecurityCamera:
    def check_status(self):
        print("Security camera is recording")
class DoorLock:
    def check_status(self):
        print("Door lock is secured")
devices=[SecurityCamera(),DoorLock()]
print("=====Smart Device Status=====")
for device in devices:
    device.check_status()
print("==============================")