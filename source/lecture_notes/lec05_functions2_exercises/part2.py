def frame_string(s):
    frame_line = '*' * (len(s)+6)
    str_line = '** ' + s + ' **'
    print(frame_line)
    print(str_line)
    print(frame_line)

frame_string('Spanish Inquisition')
print()
frame_string('Ni')
