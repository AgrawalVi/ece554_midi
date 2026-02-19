
def frequency(note):
    return 440.0 * (2.0 ** ((note - 69) / 12.0))

print("module midi_freq_lut (")
print("    input [6:0] note,")
print("    output reg [23:0] frequency_x1000")
print(");")
print("")
print("    always @(*) begin")
print("        case (note)")
for i in range(128):
    freq = frequency(i)
    scaled = int(round(freq * 1000))
    print(f"            7'd{i}: frequency_x1000 = 24'd{scaled};")
print("            default: frequency_x1000 = 24'd0;")
print("        endcase")
print("    end")
print("")
print("endmodule")
