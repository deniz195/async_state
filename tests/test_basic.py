import sys
sys.path.append('..')


import asyncio
import async_state
from async_state import *

print('testing async_state')

motor_state = AsyncState(['deenergized', 'moving', 'stopped_at_target'])

print(f'The current state is {motor_state}')
print(f'All possible states are {motor_state.possible_states}')

async def state_driver():
    input_states = ['moving', 'stopped_at_target', 'moving', 'stopped_at_target', 'deenergized']
    for s in input_states:
        await asyncio.sleep(1.0)
        print(f'Going to state {s}')
        await motor_state.set(s)

async def state_observer():
    print(f'Waiting for moving...')
    await motor_state.wait_for('moving')

    await asyncio.sleep(2.0)

    print(f'Waiting to arrive at target...')
    await motor_state.wait_for('stopped_at_target')

    await asyncio.sleep(2.0)

    print(f'Waiting to deenergize...')
    await motor_state.wait_for('deenergized')

    print(f'Done')


loop = asyncio.get_event_loop()
# asyncio.ensure_future(state_driver())
asyncio.ensure_future(state_observer())
loop.run_until_complete(state_driver())











