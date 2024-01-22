class Mod:
  def __init__(self, name):
    self.name = name

  def pulse_in(self, pulse):
    return

  def pulse_out(self):
    return


class Flipflop(Mod):
  '''
  FlipFlop Modules are either on or off.
  Incoming high pulse ignored.
  Incoming low pulse toggles state.
  If off and receives low pulse, turns on and sends high pulse.
  If on and receives low pulse, turns off and sends high pulse.
  Initial state: off
  '''
  def __init__(self, name):
    super().__init__(name)
    self.state = "OFF"
    self.pulse = "HIGH"

  def toggle_state(self):
    self.state = "OFF" if self.state == "ON" else "ON"

  def pulse_in(self, pulse):
    if pulse == "LOW":
      self.toggle_state()
    self.pulse = pulse

  def pulse_out(self):
    if self.state == "ON" and self.pulse == "LOW":
      return "HIGH"
    if self.state == "OFF" and self.pulse == "LOW":
      return "LOW"
    

class Conjunction(Mod):
  '''
  Conjunction module remembers most recent pulse from each input module.
  Only if all high pulses received, sends a low pulse.
  If even one low pulse received, sends a high pulse.
  Initial state: remembers all low pulses, so sends a high pulse.
  '''
  def __init__(self, name):
    super().__init__(name)
    self.pulse_to_send = "LOW"

  def pulse_in(self, pulse):
    if pulse == "LOW":
      self.pulse_to_send = "HIGH"

  def pulse_out(self):
    cur_pulse = self.pulse_to_send
    self.pulse_to_send = "LOW"
    return cur_pulse
