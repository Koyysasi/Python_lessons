# Bináris számok
# 0 és 1 van benne

# nem lett a legjobb, nem teljesen jegyzeteltem de sztem egyértelmű

print(1&0)

# 1011 -> 11
# 0110 -> 6
# 6 & 11 = 0010 -> 2
print(6 & 11)
# 6 | 11 = 1111 -> 15
print(6 | 11)
# ~n = -n - 1
print(~(-11))
#  1110
#0011
print(14 >> 2) # jobbra tolás
#  1110
#111000
print(14 << 2) # balra tolás

# 11111111 11111111 11111111 11111111 == 2 ^ 32-1
# 32 bites memória

# Kettes komplemensű számábrázolás: 1 bájt -> 8 bit:
# 0 = b00000000
# 1 = b00000001
# 2 = b00000010

# -1 = b11111111
# -2 = b11111110