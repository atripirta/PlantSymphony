from machine import Pin, ADC
from utime import sleep_ms
import time

def print_analog_input(pin_number, duration=10, interval=100):
    adc = ADC(Pin(pin_number))
    start_time = time.time()

    print("Analog Input Values:")
    while time.time() - start_time < duration:
        try:
            value = adc.read_u16()  # Read analog input
            print("Analog Value:", value)
            sleep_ms(interval)
        except KeyboardInterrupt:
            break

# Usage
print_analog_input("GP27", duration=120, interval=100)
