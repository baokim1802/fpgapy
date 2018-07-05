from .fpga_func import *

event_loop = None

def set_event_loop_(loop):
    global event_loop
    event_loop = loop

def async_add(a0, a1):
    res = set_add(a0, a1)
    return event_loop.create_task(get_add(res))
