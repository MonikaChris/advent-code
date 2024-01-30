class Mod:
  def __init__(self, name):
    self.name = name

  def pulse_in(self, node, pulse):
    return

  def pulse_out(self):
    return


class Flipflop(Mod):
  '''
  FlipFlop Modules are either on or off.
  Incoming high pulse ignored.
  Incoming low pulse toggles state.
  If off and receives low pulse, turns on and sends high pulse.
  If on and receives low pulse, turns off and sends low pulse.
  Initial state: off
  '''
  def __init__(self, name):
    super().__init__(name)
    self.state = "OFF"
    self.output_pulse = "HIGH"

  def toggle_state(self):
    self.state = "OFF" if self.state == "ON" else "ON"

  def pulse_in(self, node, pulse):
    if pulse == "LOW":
      self.toggle_state()
      self.output_pulse = "HIGH" if self.state == "ON" else "LOW"
    else:
      self.output_pulse = None

  def pulse_out(self):
    return self.output_pulse
    

class Conjunction(Mod):
  '''
  Conjunction module remembers most recent pulse from each input module.
  Remembers last pulse from each input.
  If remembers all high pulses, sends low pulse.
  Otherwise sends high pulse.
  Initial state: remembers all low pulses, so sends a high pulse.
  '''
  def __init__(self, name):
    super().__init__(name)
    self.memory = {}

  def add_input_node(self, node):
    self.memory[node] = "LOW"

  def pulse_in(self, node, pulse):
    self.memory[node] = pulse

  def pulse_out(self):
    for entry in self.memory.values():
      if entry == "LOW":
        return "HIGH"
    return "LOW"

  def get_memory(self):
    return self.memory
