#***********************************************
#********  Pseudocode for master.py ************
#***********************************************


# master.py in charge of the slaves and has three main functions
#		1. Initialize # of slaves
# 		2. Time-sync the slaves to make sure they send at the same time
# 		3. Coordinate a time and initialize attack


# Initializing the slaves and setting up master
socket = open socket for communication between master/slaves
num_slaves = initial number of bots on the botnet

# Coordinating time for attack
system_time = get current system time with datetime()
attack_time = set attack_time to be in the future

#Time syncing of the slaves
for i in num_slaves
		slave_sys_time = ping slave to get slave system time
		NTP_time = ping slave to get the NTP_Time
		# Set the delay of the attack to be the master attack_time plus the offset of the slave machine
		offset = attack_time + (slave_sys_time - NTP time)
		Attack(num_slaves[i],offset) #Will let the slave know when to attack based off the offset

def Attack(slave,time):
	slave = ping slave machine send it the time parameter
	slave will attack at specified time
	return

