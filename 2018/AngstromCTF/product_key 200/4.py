#codigo 1
# v11 = 0;
# email__ = email;
# v24 = name;
# for ( i = 0; i <= 1; ++i )
# {
# email_pad = (char *)*(&email__ + i);
# v20 = strlen((const char *)*(&email__ + i));
# if ( v20 <= 31 )
# {
# for ( j = 0; j < 32 - v20; ++j )
# *(&email_pad[v20] + j) = pad[(signed __int64)(v11 + j)];
# v11 = 32 - v20;
# email_pad[32] = 0;
# }
# }
# for ( k = 0; k <= 31; ++k )
# {
# *(_BYTE *)(k + email) ^= 5u;
# *(_BYTE *)(k + name) ^= 0xFu;
# }
v11 = 0
email__ = 

#codigo 4
for n in range(6):
	v7 = sumChars(email, 4 * n, 4 * n + 1, 1)
	product_key_vals[n] += v7 % sumChars(name, 4 * n + 2, 4 * n + 3, 1)
v26 = 2
v27 = 4
v28 = 6
v29 = 8
v30 = 7
v31 = 5
v32 = sumChars(email, 0, 10, 1)
v33 = sumChars(email, 10, 25, 1)
v34 = sumChars(email, 25, 32, 1)
v35 = sumChars(name, 0, 13, 1)
v36 = sumChars(name, 13, 20, 1)
v37 = sumChars(name, 20, 32, 1)
v = []
v2 = []
v.append(v26)
v.append(v27)
v.append(v28)
v.append(v29)
v.append(v30)
v.append(v31)
v2.append(v32)
v2.append(v33)
v2.append(v34)
v2.append(v35)
v2.append(v36)
v2.append(v37)
for ii in range(6):
	v2[ii] = v2[ii] * v[ii] % 10000