def convert_cel_to_far(f):
    c=(f-32)*5/9
    return print(f"{f} degrees F = {c:.2f} degrees C")

def convert_far_to_cel(c):
    f=c*9/5+32
    return print(f"{c} degrees C = {f:.2f} degrees F")

convert_cel_to_far(int(input("Enter a temperature in degrees F: ")))
convert_far_to_cel(int(input("Enter a temperature in degrees C: ")))
