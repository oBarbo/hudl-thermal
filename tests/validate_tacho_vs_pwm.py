"""
Test Function: Validate Tacho Signal vs PWM Setting (simulation)

Note: For real hardware, replace simulated reads with GPIO/tacho capture.
"""

import random

# Constants
PWM_TO_RPM_SCALING = 50  # Example: 1% PWM corresponds to 50 RPM
RPM_TOLERANCE_PERCENT = 5  # Acceptable +/- deviation in RPM

def calculate_expected_rpm(pwm_duty_cycle):
    return pwm_duty_cycle * PWM_TO_RPM_SCALING

def read_tacho_signal_simulated(pwm_duty_cycle):
    expected_rpm = calculate_expected_rpm(pwm_duty_cycle)
    noise = random.uniform(-0.03, 0.03)  # up to ±3%
    return int(expected_rpm * (1 + noise))

def validate_tacho_vs_pwm(pwm_duty_cycle):
    expected_rpm = calculate_expected_rpm(pwm_duty_cycle)
    actual_rpm = read_tacho_signal_simulated(pwm_duty_cycle)

    lower_bound = expected_rpm * (1 - RPM_TOLERANCE_PERCENT / 100)
    upper_bound = expected_rpm * (1 + RPM_TOLERANCE_PERCENT / 100)

    result = lower_bound <= actual_rpm <= upper_bound
    print(f"PWM: {pwm_duty_cycle}% | Expected RPM: {expected_rpm} | Actual RPM: {actual_rpm} | Pass: {result}")

    return result

if __name__ == "__main__":
    for pwm in [20, 40, 60, 80, 100]:
        validate_tacho_vs_pwm(pwm)
