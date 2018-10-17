import asyncio

class AsyncState(object):
    def __init__(self, possible_states, initial_state=None):
        self._possible_states = possible_states

        self.state_conditions = {s: asyncio.Condition()  for s in possible_states}

        if initial_state is None:
            self.current_state = self._possible_states[0]
        else:
            self.assert_valid_state(initial_state)
            self.current_state = initial_state

    def __repr__(self):
        return f'{self.__class__.__name__}({self.possible_states})'

    def __str__(self):
        return f'{self.current_state}'

    @property
    def possible_states(self):
        return self._possible_states

    def assert_valid_state(self, state):
        if state not in self.possible_states:
            raise RuntimeError(f'State ({state}) is not a valid state ({self.possible_states})!')

    async def set(self, new_state):
        self.assert_valid_state(new_state)

        self.current_state = new_state      

        cond = self.state_conditions[new_state]
        async with cond:
            cond.notify_all()

    async def wait_for(self, new_state, timeout=None):
        self.assert_valid_state(new_state)

        if self.current_state == new_state:
            return True

        cond = self.state_conditions[new_state]
        async with cond:
            await asyncio.wait_for(cond.wait(), timeout=timeout)

        return True
        


class AsyncPredicates(object):
    def __init__(self, predicates):
        self._predicates = predicates
        self.predicate_events = {p: asyncio.Event() for p in predicates}

    def __repr__(self):
        return f'{self.__class__.__name__}({self.predicates})'

    @property
    def predicates(self):
        return self._predicates

    def assert_valid_predicate(self, predicate):
        if predicate not in self.predicates:
            raise RuntimeError(f'Predicate ({predicate}) is not a valid predicate ({self.predicates})!')

    def set_predicate(self, predicate):
        self.predicate_events[predicate].set()

    def clear_predicate(self, predicate):
        self.predicate_events[predicate].clear()

    async def wait_for(self, predicate, timeout=None):
        self.assert_valid_predicate(predicate)

        event = self.predicate_events[predicate]
        await asyncio.wait_for(event.wait(), timeout=timeout)

        return True
        


