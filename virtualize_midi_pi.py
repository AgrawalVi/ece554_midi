import serial
import mido
import mido.backends.rtmidi

# Run ls /dev/ttyUSB* or ls /dev/ttyACM* to find the correct port name
SERIAL_PORT = '/dev/ttyUSB0'
BAUD_RATE = 31250

# Use rtmidi backend explicitly (required on Linux — no CoreMIDI)
backend = mido.Backend('mido.backends.rtmidi')

# Open Serial connection to FPGA
ser = serial.Serial(SERIAL_PORT, BAUD_RATE)

# Create a virtual MIDI port that your DAW/Keyboard can see
with backend.open_input('To_FPGA', virtual=True) as inport:
    print("Virtual MIDI Port 'To_FPGA' is active.")
    print("Directing MIDI to USB Serial...")
    for msg in inport:
        ser.write(msg.bytes())
        print(f"Sent to FPGA: {msg.hex()}")