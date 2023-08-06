import asyncio
from bleak import BleakClient, BleakScanner, BLEDevice


async def main():
    await find_devices()


async def find_devices():
    devices = await BleakScanner.discover(return_adv=True)
    for device in devices.items():
        print(device[1][1].local_name)
    imus = filter(lambda x: x[1][1].local_name and x[1][1].local_name.startswith('BME-IMU-'), devices.items())
    print(list(imus))


asyncio.run(main())



# address = "24:71:89:cc:09:05"
# MODEL_NBR_UUID = "00002a24-0000-1000-8000-00805f9b34fb"
#
# async def main(address):
#     async with BleakClient(address) as client:
#         model_number = await client.read_gatt_char(MODEL_NBR_UUID)
#         print("Model Number: {0}".format("".join(map(chr, model_number))))
#
# asyncio.run(main(address))