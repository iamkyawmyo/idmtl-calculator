# idmtl relay time calculator
# equation for trip time

# t = TMS(k / (PSM**a - 1))

curve_type = {
    "standard_inverse": {"k": 0.140, "a": 0.020},
    "very_inverse": {"k": 13.5, "a": 1},
    "extremely_inverse": {"k": 80, "a": 2},
    "long_time_inverse": {"k": 120, "a": 1},
}


# print(curve_type["standard_inverse"]["a"])

def trip_time(time_multiplier, a_const, k_const, plug_setting_multiplier):
    """return a tripping time"""
    time = time_multiplier * (k_const / ((plug_setting_multiplier ** a_const) - 1))
    return round(time, 3)


def get_valid_input(value):
    while True:
        try:
            return int(input(value))
        except ValueError:
            print("Enter a valid input 1 to 4\n")


print("Welcome to idmtl relay tripping time calculator!\n"
      "Programmed by Kyaw Myo Oo\n")

print()
user_chose_curve = get_valid_input("Choose the curve type: "
                                   "\ntype 1 for Standard Inverse"
                                   "\ntype 2 for Very Inverse"
                                   "\ntype 3 for Extremely Inverse"
                                   "\ntype 4 for Long Time Inverse\n")

user_chose_curve = user_chose_curve - 1

curve_list = ["standard_inverse", "very_inverse", "extremely_inverse", "long_time_inverse"]

tms = float(input("Enter TMS : "))
relay_pickup_current = int(input("Enter relay pick up current: "))
actual_fault_current = int(input("Enter fault current: "))

psm = actual_fault_current / relay_pickup_current

a = curve_type[curve_list[user_chose_curve]]["a"]
k = curve_type[curve_list[user_chose_curve]]["k"]

print(f"The Standard Tripping Time for PSM {psm} times at TMS {tms} is {trip_time(tms, a, k, psm)} seconds")
