from dronekit import connect

print("Connecting to vehicle on: tcp:127.0.0.1:5762")
vehicle = connect ('tcp:127.0.0.1:5762', wait_ready=True)

print("Connected")
print(f"Vehicle mode:{vehicle.mode.name}")
print(f"Vehicle location:{vehicle.location.global_relative_frame}")

vehicle.close()