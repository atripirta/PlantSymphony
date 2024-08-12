import machine
import utime

# Configure GP27 pin as input
gpio_pin = machine.Pin(27, machine.Pin.IN)

def generate_tone(frequency, duration):
    pwm = machine.PWM(machine.Pin(15))  # Configure PWM on GPIO 15
    pwm.freq(frequency)  # Set frequency
    pwm.duty_u16(32768)  # Set duty cycle to 50%
    utime.sleep(duration)  # Play tone for specified duration
    pwm.deinit()  # Turn off PWM

# Main loop to continuously read input and generate sound
while True:
    value = gpio_pin.value()  # Read the value from GP27 pin
    print(value)
    frequency = 100 + value * 400  # Adjust frequency based on input value
    duration = 0.1  # Duration of the tone in seconds
    # generate_tone(frequency, duration)
    utime.sleep(0.1)  # Adjust sleep duration as needed


