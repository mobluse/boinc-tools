print('<html><head><title>free-dc</title></head><body>')
for i in range(0, 6):
  for j in range(7*i, 7*(i+1)): # Change cpid to your own.
    print('<img src="https://stats.free-dc.org/cpidtagb.php?cpid=\
40c8b1f60a21f24ba8a10eced8737a04\
&cols=1&theme=%d">' % j)
  print('<br>')
print('</body></html>')
