import time

AT_PRESSURE  = False
low_start_time = time.time()
high_start_time = time.time()
time_elapsed = 0

current_pressure = 1

# Set AT_PRESSURE if pressure below 1E-6 Torr for 20+ seconds
if AT_PRESSURE == False and current_pressure < 1E-6:
    time_elapsed = time.time() - low_start_time  
    if time_elapsed >= 20:
        AT_PRESSURE = True
        print(f"Pressure is {current_pressure}, at pressure set.")

elif AT_PRESSURE == False:
    low_start_time = time.time()  

# SHUTTING DOWN system if pressure gets above 1E-5 Torr for 20+ seconds after AT_PRESSURE has been set
if AT_PRESSURE and current_pressure > 1E-5:
    time_elapsed = time.time() - high_start_time
    if time_elapsed >= 20:
        print(f"At pressure was set and current pressure is {current_pressure}, shutting system down.")

        # Shut down system command

        AT_PRESSURE = False
        
elif AT_PRESSURE == True:
    high_start_time = time.time()  