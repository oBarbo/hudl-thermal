"""
Deliverable 3: Tacho Validation with Logging (simulation)

Logs results to a CSV file named `tacho_validation_log.csv`.
"""

import random
import csv
from datetime import datetime

# Constants
PWM_TO_RPM_SCALING = 50  # 1% PWM = 50 RPM
RPM_TOLERANCE_PERCENT = 5  # Acceptable +/- deviation in RPM
LOG_FILE = "tacho_validation_log.csv"

def calculate_expected_rpm(pwm_duty_cycle):
    return pwm_duty_cycle * PWM_TO_RPM_SCALING

def read_tacho_signal_simulated(pwm_duty_cycle):
    expected_rpm = calculate_expected_rpm(pwm_duty_cycle)
    noise = random.uniform(-0.03, 0.03)  # simulate noise ±3%
    return int(expected_rpm * (1 + noise))

def validate_tacho_vs_pwm(pwm_duty_cycle):
    expected_rpm = calculate_expected_rpm(pwm_duty_cycle)
    actual_rpm = read_tacho_signal_simulated(pwm_duty_cycle)

    lower_bound = expected_rpm * (1 - RPM_TOLERANCE_PERCENT / 100)
    upper_bound = expected_rpm * (1 + RPM_TOLERANCE_PERCENT / 100)

    pass_fail = lower_bound <= actual_rpm <= upper_bound
    result = {
        "timestamp": datetime.now().isoformat(),
        "pwm_duty_cycle": pwm_duty_cycle,
        "expected_rpm": expected_rpm,
        "actual_rpm": actual_rpm,
        "pass": pass_fail
    }
    return result

def run_and_log_tests(pwm_values):
    with open(LOG_FILE, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=[
            "timestamp", "pwm_duty_cycle", "expected_rpm", "actual_rpm", "pass"
        ])
        writer.writeheader()
        for pwm in pwm_values:
            result = validate_tacho_vs_pwm(pwm)
            writer.writerow(result)
            print(f"Logged: PWM {pwm}% | Expected: {result['expected_rpm']} RPM | Actual: {result['actual_rpm']} RPM | Pass: {result['pass']}")

if __name__ == "__main__":
    test_pwm_values = [10, 30, 50, 70, 90, 100]
    run_and_log_tests(test_pwm_values)
