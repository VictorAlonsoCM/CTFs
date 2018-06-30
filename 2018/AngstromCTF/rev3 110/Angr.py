import angr

p = angr.Project('./RedVelvet', load_options={"auto_load_libs": False})

st = p.factory.entry_state()
#explore(avoid=[0x08048544, 0x080485F8], find=0x080485E6)