import MySQLdb
from datetime import datetime

class automate:
    ## def __init__(self, hostname, usr, pwd, db_name)----------------> OK
    def __init__(self, hostname, usr, pwd, db_name):
        hostname = hostname
        usr = usr
        pwd = pwd
        db_name = db_name
        #		db=MySQLdb.connect("localhost","admin","admin","homedb")
        self.db = MySQLdb.connect(hostname, usr, pwd, db_name)
        # set_up_sql(hostname)

    def __enter__(self):
        self.automating()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db.close()

    # def get_status(self)-------------------------------------------> OK
    def get_status(self):
        try:
            with open('status', 'r') as file:
                self.data = file.readlines()
                file.close()
        except IOError:
            print "Warning: status file is used by another process"
        # print self.data
        return self.data

    # def get_switch_info(self, switch_id)----------------------------> OK
    def get_switch_info(self ,switch_id):
        # switch_id = switch_id
        # time = time
        query = "select start_time,end_time,state,auto_mode from switch_time where switch_id=" +str(switch_id)
        # query = "select " + time + " from switch_time where switch_id=" + str(switch_id)
        # print query
        point = self.db.cursor()
        point.execute(query)
        info = point.fetchall()
        point.close()

        # if info:
        #     print "No data found"
        #     return None
        # else:
        #     print type( info )
        #     print info
        return info

    # def compare_time(self, given_time_old)-------------------------> OK
    def compare_time(self, given_time_old):
        # current_time = time.ctime().rsplit()[3]
        tmp_time = str(datetime.today().hour)+":"+str(datetime.today().minute)+":"+str(datetime.today().second)
        current_time = datetime.strptime(tmp_time, '%H:%M:%S' )
        given_time = datetime.strptime(str(given_time_old), '%H:%M:%S')
        # print datetime.__getattribute__(current_time,"hour")
        # print datetime.__getattribute__(current_time, "minute")
        # print datetime.__getattribute__(current_time, "second")
        # print current_time
        # given_time = str (given_time)
        # print "g_time=%s  %s" % (given_time, type(given_time))
        # print "c_time=%s  %s" % (current_time, type(current_time))
        # print "current time=%s " % str(current_time)
        if current_time == given_time:
            print "\n\t\tTime MATCHED\n"
            return 1
        else:
            return 0

    # def update_switch_state(self, switch_id, state)---------------> OK
    def update_switch_state(self, switch_id, state):
        query = "update switches set switch_state='" + str(state) + "' where switch_id=" + str(switch_id)
        print query
        point = self.db.cursor()
        point.execute(query)
        self.db.commit()

    # def automating(self)------------------------------------------> OK
    def automating(self):
        data = self.get_status()
        ID = [0, 0, 0, 0]
        ID[0] = data[12].rsplit()[1]
        ID[1] = data[16].rsplit()[1]
        ID[2] = data[20].rsplit()[1]
        ID[3] = data[24].rsplit()[1]

        count = 0
        line = 13
        while count < 4:
            if ID[count] != 'unknown':
                info = self.get_switch_info(ID[count])
                if info:
                    # print info
                    auto_loop = 0
                    while auto_loop < len (info):
                        if info[auto_loop][3] == "ON":      #checking Auto_mode
                            # print info[auto_loop]
                            # print self.compare_time(info[auto_loop][0])
                            if self.compare_time(info[auto_loop][0]) == 1:
                                print "In checking start_time"
                                self.update_switch_state(ID[count],info[auto_loop][2])
                            if self.compare_time(info[auto_loop][1]) == 1:
                                print "In checking end_time"
                                if (info[auto_loop][2] == 'ON'):
                                    print "Time to sleep"
                                    self.update_switch_state(ID[count], "OFF")
                                else:
                                    self.update_switch_state(ID[count], "ON")
                                # print info[auto_loop][1]
                                # self.update_switch_state()  # (switch_id, state) jo state milay uska inverse da yahan
                        # else:
                        #     # print "Auto mode is OFF"
                        #     print " "
                        auto_loop += 1
                # else:
                #     # print "No Automation info found at ID %s" % ID[count]
                #     print " "
            count += 1
            line += 4


