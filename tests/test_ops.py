import sys
sys.path.append('..')


import asyncio
import async_state
from async_state import *

print('testing async_state')

motor_state = AsyncState(['deenergized', 'moving', 'stopped_at_target'])

print(f'The current state is {motor_state}')
print(f'All possible states are {motor_state.possible_states}')


async def test():
    print(f'Set motor to moving!')
    await motor_state.set('moving')

    if motor_state == 'moving':
        print(f'Motor is moving!')

    if motor_state != 'moving':
        raise RuntimeError(f'Motor is ambivalent!')

    if motor_state != 'stopped_at_target':
        print(f'Motor is not at target!')

    if motor_state < ['deenergized', 'stopped_at_target']:
        print(f'Motor state is not moving!')


    print(f'Turning off motor!')
    await motor_state.set('deenergized')

    if motor_state < ['deenergized', 'stopped_at_target']:
        print(f'Motor state is not moving!')


    try:
        if motor_state == 'flying':
            print(f'Motor is moving!')

    except BaseException as e:
        print(repr(e))





loop = asyncio.get_event_loop()
loop.run_until_complete(test())










