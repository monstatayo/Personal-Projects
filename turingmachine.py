class TuringMachine:
    def __init__(self, tape, initial_state, transitions, final_states):
        self.tape = list(tape)
        self.head_position = 0
        self.state = initial_state
        self.transitions = transitions
        self.final_states = final_states

    def step(self):
        symbol = self.tape[self.head_position]
        if (self.state, symbol) not in self.transitions:
            return False

        new_state, new_symbol, direction = self.transitions[(self.state, symbol)]
        self.tape[self.head_position] = new_symbol
        self.state = new_state

        if direction == 'R':
            self.head_position += 1
            if self.head_position == len(self.tape):
                self.tape.append('_')
        elif direction == 'L':
            self.head_position -= 1
            if self.head_position == -1:
                self.tape.insert(0, '_')

        return True

    def run(self):
        while self.state not in self.final_states:
            if not self.step():
                return False
        return True


tape = '0010110'
initial_state = 'q0'
transitions = {
    ('q0', '0'): ('q1', '1', 'R'),
    ('q0', '1'): ('q0', '0', 'L'),
    ('q1', '0'): ('q1', '0', 'R'),
    ('q1', '1'): ('q2', '1', 'L'),
    ('q2', '0'): ('q3', '1', 'R'),
    ('q2', '1'): ('q2', '1', 'L'),
    ('q3', '0'): ('q3', '0', 'R'),
    ('q3', '1'): ('q4', '0', 'L'),
}
final_states = {'q4'}

tm = TuringMachine(tape, initial_state, transitions, final_states)
if tm.run():
    print('Accepted')
    print('Final tape:', ''.join(tm.tape))
else:
    print('Rejected')