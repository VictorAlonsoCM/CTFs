import angr

p = angr.Project('./RedVelvet', load_options={"auto_load_libs": False})

st = p.factory.entry_state()

# in printable range
for _ in xrange(26):
    k = st.posix.files[0].read_from(1)
    st.solver.add(k >= 0x20)
    st.solver.add(k <= 0x7e)

# Constrain the last byte to be a newline
k = st.posix.files[0].read_from(1)
st.solver.add(k == 10)

# Reset the symbolic stdin's properties and set its length.
st.posix.files[0].seek(0)
st.posix.files[0].length = 27

sm = p.factory.simulation_manager(st)
sm.explore(avoid=0x004007d0, find=0x0040152d)

print(sm.found[0].posix.dumps(0))