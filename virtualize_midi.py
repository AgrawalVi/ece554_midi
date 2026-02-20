import serial
import mido

# Replace with your actual port from Step 2
SERIAL_PORT = '/dev/cu.usbserial-FT0DJCPK' 
BAUD_RATE = 31250

# Open Serial connection to FPGA
ser = serial.Serial(SERIAL_PORT, BAUD_RATE)

# Create a virtual MIDI port that your DAW/Keyboard can see
with mido.open_input('To_FPGA', virtual=True) as inport:
    print("Virtual MIDI Port 'To_FPGA' is active.")
    print("Directing MIDI to USB Serial...")
    for msg in inport:
        ser.write(msg.bytes())
        print(f"Sent to FPGA: {msg.hex()}")