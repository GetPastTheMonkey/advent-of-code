from day17.simulation import Simulation

sim = Simulation()
sim.run()
sim.draw()

print("Total water: {}".format(sim.count_water()))
print("Still water: {}".format(sim.count_still_water()))
