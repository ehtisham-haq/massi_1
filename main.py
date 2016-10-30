from db_func import database
from switch_handler import setup_pinout
from automation import automate
# import test1,test2,test3
import time
import sys
import time

def main():
    #test1.show1()
    #test2.show2()
    #test3.show3()
    hostname = sys.argv[1]
    print hostname
    con = database(hostname, "ahmed", "ahmed", "homedbRPI")
    # con.set_up_sql(hostname)
    # module = setup_pinout()

    # magic.get_switch_info(1)
    # magic.compare_time(123)

    # loop = 1
    # while 1:
        # with database(hostname, "ahmed", "ahmed", "homedbRPI") as status_check:
        #     print "checking switches"
        # module.get_status()
        # module.switch_handler()
        # module.test_switch()
        # print "---------%d-----------\n\n" % loop
        # loop += 1
        # time.sleep(1)
        # with automate(hostname, "ahmed", "ahmed", "homedbRPI") as auto_timing:
        #     print "checking time"

if __name__ == "__main__":
    main()
