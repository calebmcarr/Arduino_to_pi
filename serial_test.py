import serial

#ser = serial.Serial('/dev/ttyACM0',9600)
ser = serial.Serial('COM3',9600,timeout=0);
print("success")
while True:
    read_serial=ser.readline()
    #s[0] = str(int (ser.readline(),16))
    #print s[0]
    print(read_serial)
#comment 
