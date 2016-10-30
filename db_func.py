import MySQLdb
class database:
	## def __init__(self, hostname, usr, pwd, db_name)----------------> OK
	def __init__(self, hostname, usr, pwd, db_name):
		self.hostname = hostname
		self.usr = usr
		self.pwd = pwd
		self.db_name = db_name
#		self.db=MySQLdb.connect("localhost","admin","admin","homedb")
		self.db = MySQLdb.connect(self.hostname, self.usr, self.pwd, self.db_name)
		print "Connection established\n"
		# self.set_up_sql(hostname)

	# __enter__(self)-------------------------------------------------> OK
	def	__enter__(self):
		# print "_____________________________ENTER_____________________________________"
		self.sql_handler()

	# def __exit__(self, exc_type, exc_val, exc_tb)-------------------> OK
	def	__exit__(self, exc_type, exc_val, exc_tb):
		# print "_____________________________EXIT_____________________________________"
		self.db.close()

	# def set_up_sql(self, m_ip)--------------------------------------> OK
	def set_up_sql(self, m_ip):
		self.m_ip = m_ip
		self.m_info = self.get_module_info(self.m_ip)
		self.s_info = self.get_switch_info(self.m_info[0])
		# print "Module ID found from database %d\n" % self.id
		self.update_status(self.m_ip, self.m_info, self.s_info)

	#def update_status(self, ip, m_info, s_id)------------------------> OK
	def update_status(self, ip, m_info, s_id):
		self.ip = ip
		self.m_info = m_info
		self.s_id = s_id
		try:
			with open('status', 'r') as file:
				self.data = file.readlines()
				file.close()
				#print self.data
				#print "Module Id found from sql_handler %s\n" % self.ip
				self.data[7] = "ID %s\n" % (self.m_info[0])
				self.data[8] = "IP %s\n" % (self.ip)
				self.data[9] = "model %s\n" % (self.m_info[1])

				self.data[12] = "ID unknown\n"		#A
				self.data[16] = "ID unknown\n"		#B
				self.data[20] = "ID unknown\n"		#C
				self.data[24] = "ID unknown\n"		#D
				print "ID unknown set to all"

				self.count = 0
				while self.count < len(self.s_id):
					if self.s_id[self.count][1] == 'A':
						self.data[12] = "ID %s\n" % (self.s_id[self.count][0])
					if self.s_id[self.count][1] == 'B':
						self.data[16] = "ID %s\n" % (self.s_id[self.count][0])
					if self.s_id[self.count][1] == 'C':
						self.data[20] = "ID %s\n" % (self.s_id[self.count][0])
					if self.s_id[self.count][1] == 'D':
						self.data[24] = "ID %s\n" % (self.s_id[self.count][0])
					#print "ID %s" % (self.s_id[self.count][0])
					#print "Switch code %s" % (self.s_id[self.count][1])
					self.count+=1

				with open('status', 'w') as file:
					file.writelines(self.data)
					file.close()

		except IOError:
			print "Warning: status file is used by another process"

	## def get_module_id(self, module_ip)-----------------------------> OK
	def get_module_info(self, module_ip):
		self.module_ip = module_ip
		self.query = "select module_id, module_version from module where ip_address='" + self.module_ip + "'"
		#print self.query
#		try:
		self.point = self.db.cursor()
		self.point.execute(self.query)
		self.module_info = self.point.fetchone()
		self.point.close()
#		print(self.query)
		#		return self.type
		if (self.module_info == None):
			print "No data found"
			return None
		else:
			print self.module_info
			return self.module_info

	# def get_switch_info(self, module_id)----------------------------> OK
	def get_switch_info(self, module_id):
		self.module_id = module_id
		self.query = "select switch_id, module_switch from switches where module_id='" + str(self.module_id) + "'"
		#print self.query
		self.point = self.db.cursor()
		self.point.execute(self.query)
		self.switch_info = self.point.fetchall()
		self.point.close()
		#		print(self.query)
		if (self.switch_info == None):
			print "No data found"
			return None
		else:
			print self.switch_info
			return self.switch_info

	# def get_switch_state(self, switch_id)---------------------------> OK
	def get_switch_state(self, switch_id):
		self.switch_id = switch_id
		self.query = "select switch_state from switches where switch_id='" + str(self.switch_id) + "'"
		# print self.query
		self.point = self.db.cursor()
		self.point.execute(self.query)
		self.switch_state = self.point.fetchone()
		# print self.switch_state
		self.point.close()
		if self.switch_state == None:
			print "No switch of ID=%s" % self.switch_id
			return None
		else:
			# print "IN get_switch_state: ID=%s %s " % (self.switch_id, self.switch_state[0] )
			return self.switch_state[0]

	# def live_update(self, switch_id)--------------------------------> OK
	def live_update(self, switch_id):
		self.switch_id = switch_id
		self.query = "select switch_state from switches where switch_id= " + str(self.switch_id)
		self.point = self.db.cursor()
		self.point.execute(self.query)
		self.state = self.point.fetchone()
		self.point.close()
		return self.state[0]

	# def sql_handler(self)-------------------------------------------> OK
	def sql_handler(self):
		try:
			with open('status', 'r') as file:
				self.data = file.readlines()
				file.close()

			# print self.data
			self.ID = [0, 0 ,0, 0]
			self.ID[0] = self.data[12].rsplit()[1]
			self.ID[1] = self.data[16].rsplit()[1]
			self.ID[2] = self.data[20].rsplit()[1]
			self.ID[3] = self.data[24].rsplit()[1]
			# print self.state
			count = 0
			line = 13
			while count < 4:
				if self.ID[count] != 'unknown':
					state = self.get_switch_state(self.ID[count])
					# print state
					self.data[line] = "state %s\n" % (state)
					# self.data[line] = "state %s\n" % (self.live_update(self.ID[count]))
					# print "ID=%s %s" % ( self.ID[count], self.data[line] )
				else:
					self.data[line] = "state OFF\n"
				# print "else: state OFF\n"
				count += 1
				line += 4

			with open('status', 'w') as file:
				file.writelines(self.data)
				file.close()
		except IOError:
			print "Warning: status file is used by another process"