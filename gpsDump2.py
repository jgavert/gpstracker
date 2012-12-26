import location
import gobject
from time import gmtime, strftime

f = open('/home/user/MyDocs/updated/gps_2012-07-29_a.log','a')
def on_error(control, error, data):
    print "location error: %d... quitting" % error
    #f.write("location error: %d... quitting" % error)
    #f.flush()
    data.quit()

def on_changed(device, data):
    if not device:
        return
    if device.fix:
        if device.fix[1] & location.GPS_DEVICE_LATLONG_SET:
            #print strftime("%Y-%m-%dT%H:%M:%S %Z", gmtime())
            #print " // lat = %f, long = %f" % device.fix[4:6]
            f.write(str(device.fix) + "\n")
            f.flush()
            #f.write(strftime("%Y-%m-%dT%H:%M:%S %Z", gmtime()))
            #f.write(" // lat = %f, long = %f \n" % device.fix[4:6])
            #f.flush()
            # data.stop() commented out to allow continuous loop for a reliable fix - press ctrl c to break the loop, or program your own way of exiting)

def on_stop(control, data):
    print "quitting"
    data.quit()

def start_location(data):
    data.start()
    return False


loop = gobject.MainLoop()
control = location.GPSDControl.get_default()
device = location.GPSDevice()
control.set_properties(preferred_method=location.METHOD_USER_SELECTED,
                       preferred_interval=location.INTERVAL_DEFAULT)

control.connect("error-verbose", on_error, loop)
device.connect("changed", on_changed, control)
control.connect("gpsd-stopped", on_stop, loop)

gobject.idle_add(start_location, control)

loop.run()