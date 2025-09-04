student = True
if student:  # shorter than `if student == True:`
    pris_2025 = 28
else:
    pris_2025 = 37

incr = 2.6

pris_2026 = pris_2025 * (1 + incr / 100)


print( pris_2026 )  # Decimal
print( int( pris_2026 ) ) # Truncated
print( int( round(pris_2026, 0) ) ) # Rounded, then truncated