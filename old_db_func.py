
def get_people_type(self ,username, password):
    self.username = username
    self.password = password
    self. query ="select accounttype from people where username= '" +self. username + "' and password='" +self. password +"'"
    #		print self.query
    #		try:
    self. point =self.db.cursor()
    self.point.execute(self.query)
    self. type =self.point.fetchone()
    self.point.close()
    print(self.query)
    #		return self.type
    if (self.type == None):
        print "No data found"
        return None
    elif (self.type[0] == "local" ):
        print "local"
        return "local"
    elif (self.type[0] == "admin" ):
        print "admin"
        return "admin"

    #		except:
    #			return "invalid username and password"

    ##############################################################################

def get_people_name_type(self):
    self. query ="select username,accounttype from people"
    #		print self.query
    #		try:
    self. point =self.db.cursor()
    self.point.execute(self.query)
    self. names =self.point.fetchall()
    self.point.close()
    #		for self.name in self.names:
    #			print self.name[0]

    return self.names

def get_people_name(self):
    self. query ="select username from people"
    #		print self.query
    #		try:
    self. point =self.db.cursor()
    self.point.execute(self.query)
    self. names =self.point.fetchall()
    self.point.close()
    #		for self.name in self.names:
    #			print self.name[0]

    return self.names

def get_people_id(self, username):
    self.username = username
    self. query ="select people_id from people where username= '" +self. username +"'"
    #		print self.query
    #		try:
    self. point =self.db.cursor()
    self.point.execute(self.query)
    self. names =self.point.fetchone()
    self.point.close()
    #		for self.name in self.names:
    #			print self.name[0]
    #		print self.names[0]
    return str(self.names[0])

def get_people_id(self, username):
    self.username = username
    self. query ="select people_id from people where username= '" +self. username +"'"
    #		print self.query
    #		try:
    self. point =self.db.cursor()
    self.point.execute(self.query)
    self. names =self.point.fetchone()
    self.point.close()
    #		for self.name in self.names:
    #			print self.name[0]
    #		print self.names[0]
    return str(self.names[0])

def get_room_mode(self, people_id, room_id):
    self.people_id = people_id
    self.room_id = room_id
    self. query ="select mode from peopleroom where people_id= " +str(self.people_id ) + " and room_id=" +str \
        (self.room_id)
    print self.query
    self. point =self.db.cursor()
    self.point.execute(self.query)
    self. state =self.point.fetchone()
    self.point.close()
    #		print self.state
    return self.state
#		except:
#			print 0
#			return 0

##############################################################################
def get_room(self, people_id):
    self.people_id = people_id
    self. query ="select room_id from peopleroom where people_id= " +self.people_id
    print self.query
    self. point =self.db.cursor()
    self.point.execute(self.query)
    self. state =self.point.fetchall()
    self.point.close()
    #		print self.state
    return self.state
#		except:
#			print 0
#			return 0


##############################################################################
def get_data(self, username, data):
    self.username = username
    self.data = data
    self. query = "select " +self. data + " from people where username='" +self. username +"'"
    self. point =self.db.cursor()
    self.point.execute(self.query)
    self. state =self.point.fetchone()
    self.point.close()
    return self.state[0]
    print self.query

def del_account(self, username):
    self.username = username
    self.people_id = self.get_people_id(self.username)
    self. query ="delete from peopleroom where people_id= '" +self. people_id +"'"
    self. point =self.db.cursor()
    self.point.execute(self.query)
    self.db.commit()
    print self.query
    self. query ="delete from people where people_id= '" +self. people_id +"'"
    self. point =self.db.cursor()
    self.point.execute(self.query)
    self.db.commit()
    print self.query

def update_room(self, username, room_id, mode):
    self.username = username
    self.people_id = self.get_people_id(self.username)
    self.room_id = room_id
    self.mode = mode
    self. query ="update peopleroom set mode= '" +str(self.mode ) + "' where people_id=" +str \
        (self.people_id ) + " and room_id=" +str(self.room_id)
    print self.query
    try:
        self. point =self.db.cursor()
        self.point.execute(self.query)
        self.db.commit()
    except:
        print "Added"

    ##############################################################################

def add_room(self, username, room_id, mode):
    self.username = username
    self.people_id = self.get_people_id(self.username)
    self.room_id = room_id
    self.mode = mode
    self. query ="insert into peopleroom (people_id,room_id,mode) values ( " +str(self.people_id ) + ", " +str \
        (self.room_id ) + ", '" +str(self.mode ) +"')"
    print self.query
    try:
        self. point =self.db.cursor()
        self.point.execute(self.query)
        self.db.commit()
    except:
        print "Added"

    ##############################################################################

def delete_room(self, username, room_id):
    self.username = username
    self.people_id = self.get_people_id(self.username)
    self.room_id = room_id
    self. query ="delete from peopleroom where people_id= " +str(self.people_id ) + " and room_id=" +str(self.room_id)
    print self.query
    try:
        self. point =self.db.cursor()
        self.point.execute(self.query)
        self.db.commit()
    except:
        print "Added"

    ##############################################################################

def get_switch_time(self ,switch_id, time):
    self.switch_id = switch_id
    self.time = time
    self. query = "select " +self. time + " from switches where switch_id=" +str(self.switch_id)
    print self.query
    self. point =self.db.cursor()
    self.point.execute(self.query)
    self. state =self.point.fetchone()
    self.point.close()
    print self.state[0]
    return self.state[0]

def get_switch_mode(self ,switch_id):
    self.switch_id = switch_id
    self. query ="select mode from switches where switch_id= " +str(self.switch_id)
    print self.query
    self. point =self.db.cursor()
    self.point.execute(self.query)
    self. state =self.point.fetchone()asdasdas
    self.point.close()
    print self.state[0]
    return self.state[0]

def update_switch_mode(self ,switch_id, data):
    self.switch_id = switch_id
    self.data = data
    self. query ="update switches set mode= '" +str(self.data ) + "' where switch_id=" +str(self.switch_id)
    print self.query
    try:
        self. point =self.db.cursor()
        self.point.execute(self.query)
        self.db.commit()
    except:
        print "switch mode updated"

    ##############################################################################

def update_switch_time(self ,switch_id, ontime, offtime):
    self.switch_id = switch_id
    self.ontime = ontime
    self.offtime = offtime
    self.ontime_str = str(self.ontime.hour() ) + ":" +str(self.ontime.minute() ) + ":" +str(self.ontime.second())
    self.offtime_str = str(self.offtime.hour() ) + ":" +str(self.offtime.minute() ) + ":" +str(self.offtime.second())
    print self.ontime_str
    print self.offtime_str
    #		self.ontime_rpl = self.ontime_str.replace(".",":")
    #		self.offtime_rpl = self.offtime_str.replace(".",":")
    self. query ="update switches set ontime= '" +self. ontime_str + "', offtime='" +self. offtime_str + "' where switch_id=" +str \
        (self.switch_id)
    print self.query
    try:
        self. point =self.db.cursor()
        self.point.execute(self.query)
        self.db.commit()
    except:
        print "switch time updated"

    ##############################################################################

def add_account(self, name, username, password, accounttype):
    self.name = name
    self.username = username
    self.password = password
    self.accounttype = accounttype
    self. query ="INSERT INTO people (name, username, password, accounttype) VALUES ( '" +self. name + "', '" +self. username + "', '" +self. password + "', '" +self. accounttype +"')"
    print self.query
    try:
        self. point =self.db.cursor()
        self.point.execute(self.query)
        self.db.commit()
        print "Entry successful"
        return "Entry successful"
    except:
        print "Duplicate Entry"
        return "Duplicate Entry"

    ##############################################################################

def update_account(self, old_username, name, username, password, accounttype):
    self.name = name
    self.username = username
    self.password = password
    self.accounttype = accounttype
    self.old_username = old_username
    self. query ="Update people set name= '" +self. name + "', username='" +self. username + "', password='" +self. password + "', accounttype='" +self. accounttype + "' where username='" +self. old_username +"'"
    print self.query
    try:
        self. point =self.db.cursor()
        self.point.execute(self.query)
        self.db.commit()
        print "Entry successful"
        return "Entry successful"
    except:
        print "Duplicate Entry"
        return "Duplicate Entry"

    ##############################################################################

def get_sensors_data(self, data):
    self.data = data
    self. query = "select " +self. data +" from sensors"
    print self.query
    #		try:
    self. point =self.db.cursor()
    self.point.execute(self.query)
    self. names =self.point.fetchall()
    self.point.close()
    for self.name in self.names:
        print self.name[0]
    # print False - 1

    return self.names

def toggle_switch(self, switch_id):
    self.switch_id = switch_id
    self. query ="select switch_state from switches where switch_id= " +str(self.switch_id)
    print self.query
    self. point =self.db.cursor()
    self.point.execute(self.query)
    self. state =self.point.fetchone()
    self.point.close()
    if self.state[0 ] ==1:
        self. query ="update switches set switch_state='0' where switch_id= " +str(self.switch_id)
        print self.query
        self. point =self.db.cursor()
        self.point.execute(self.query)
        self.db.commit()

    elif self.state[0 ] ==0:
        self. query ="update switches set switch_state='1' where switch_id= " +str(self.switch_id)
        print self.query
        self. point =self.db.cursor()
        self.point.execute(self.query)
        self.db.commit()

    print self.state[0]

def shutdown(self):
    self. query ="update switches set switch_state=0"
    print self.query
    self. point =self.db.cursor()
    self.point.execute(self.query)
    self.db.commit()

def live_update(self, switch_id):
    self.switch_id = switch_id
    self. query ="select switch_state from switches where switch_id= " +str(self.switch_id)
    self. point =self.db.cursor()
    self.point.execute(self.query)
    self. state =self.point.fetchone()
    self.point.close()
    return self.state[0]



    # con = database("localhost", "admin", "admin", "homedb")
    # print (con.get_people("Ahmed", "moe5ra3t"))