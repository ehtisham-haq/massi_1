import sys
import os


def main():
	ip = sys.argv[1]
	with open('/etc/dhcpcd.conf', 'r') as file:
		data=file.readlines()

	print data

	data[43] = "static ip_address=%s\n" % (ip)
	with open('/etc/dhcpcd.conf', 'w') as file:
		file.writelines( data )


#	file=open("/etc/dhcpcd.conf", "rw+")
#	for i, line in enumerate(file):
#		if i == 2:
#			file.write("i am at line 2\n")
#			break
#	data = file.readline()
#	print "data at line 3: ", data
#	file.close()

if __name__ == "__main__":
	main()

