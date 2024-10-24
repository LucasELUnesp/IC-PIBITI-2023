import serial
import csv
import time

def read_weight_from_balance(serial_port):
    try:
        ser = serial.Serial(serial_port, baudrate=9600, timeout=1)
        print(f"Connected to {serial_port}")
    except serial.SerialException as e:
        print(f"Error opening serial port {serial_port}: {e}")
        return None

    return ser

def write_weight_to_csv(file_name, timestamp, weight):
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, weight])

def main():
    serial_port = 'COM14'
    csv_file = 'weight_data2500rpm teste14082024.csv'
   
    # Write header row to the CSV file
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestamp', 'Weight'])
   
    ser = read_weight_from_balance(serial_port)
   
    if not ser:
        return

    try:
        while True:
            if ser.in_waiting > 0:
                weight_data = ser.readline().decode('utf-8').strip()
                print(f"Weight: {weight_data}")
               
                current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                write_weight_to_csv(csv_file, current_time, weight_data)
               
            time.sleep(1)  # Delay to avoid excessive polling
    except KeyboardInterrupt:
        print("Terminating the program...")
    finally:
        ser.close()

if __name__ == '__main__':
    main()
