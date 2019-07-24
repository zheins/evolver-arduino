import serial
import sys
import os
import time

DATA_FILENAME = 'lux_data.txt'

serial_connection = None

def get_data_from_board():
	serialdata = ''
	while not serialdata.endswith("\n"):
		serialdata = serialdata + serial_connection.read().decode('UTF-8')
	#print(serialdata)
	ch1_data = ''
	ch2_data = ''
	if serialdata[0] is '!':
		serialdata = serialdata.split('\t')
		ch1_data = serialdata[0].strip()
		ch1_data = ch1_data.replace('!', '')
		ch2_data = serialdata[1].strip()
	return ch1_data, ch2_data

def save_data_to_file(ch1_data, ch2_data, current_time):
	if ch1_data is not '' and ch2_data is not '':
		with open(DATA_FILENAME, 'a') as f:
			f.write(str(current_time) + '\t' + ch1_data + '\t' + ch2_data + '\n')


if __name__ == "__main__":
	serial_connection = serial.Serial(port = '/dev/cu.usbmodem1461', baudrate = 9600, timeout = 1)
	start_time = round(time.time() / 3600, 4)

	while(True):
		try:
			current_time = round((time.time() - start_time)/3600,4)
			ch1_data, ch2_data = get_data_from_board()
			save_data_to_file(ch1_data, ch2_data, current_time)
		except Exception:
			pass
		time.sleep(5)
