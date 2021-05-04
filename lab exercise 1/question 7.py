""" You live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each
of the 10 stops on the way. How long will the bus journey take? Alternatively, you could
run to university. You jog the first mile at 7mph; then run the next two at15mph; before
jogging the last at 7mph again. Will this be quicker or slower than the bus?"""


distance = 4
time_taken_bus = (distance / 25) + 10*2
time_taken_man =distance / (7*2 + 15*2)

if time_taken_man > time_taken_bus:
    print("you can jog to the university faster")
else:
    print("you can reach the university faster by the bus")