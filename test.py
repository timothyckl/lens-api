from lens import Lens

# setup
lens = Lens('COM7', debug=False)  # set debug=True for serial comm log
print(lens.firmware_type)
print(lens.firmware_version)
print(lens.get_firmware_branch())
print('Lens serial number:', lens.lens_serial)
print('Lens temperature:', lens.get_temperature())

# ex1: focal power mode
min_fp, max_fp = lens.to_focal_power_mode()
print('Minimal diopter:', min_fp)
print('Maximum diopter:', max_fp)
print(lens.set_temperature_limits(20,45 ))
lens.set_diopter(3)
lens.set_diopter(-0.2)

# ex2: current mode example
lens.to_current_mode()
lens.set_current(100)

