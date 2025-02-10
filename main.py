from pyModbusTCP.client import ModbusClient
import json
import time

read_file = open('reader_config.json', 'r', encoding='utf-8')
config = json.load(read_file)
register_target = config['target']['holding_register']
coil_target = config['target']['coil']

modbus_client = ModbusClient(
    host=config['host'],
    port=config['port'],
    unit_id=config['unit_id'],
    auto_open=True,
)

cnt = 1
while True:
    temp_string = f'Read: {cnt}\n'
    for key in register_target:
        reg = modbus_client.read_holding_registers(
            register_target[key]['address'],
            register_target[key]['length'],
        )
        temp_string += f'  {key}: {reg}\n'
    for key in coil_target:
        coil = modbus_client.read_coils(
            coil_target[key]
        )
        temp_string += f'  {key}: {coil}\n'

    print(temp_string)
    cnt += 1
    time.sleep(1)
