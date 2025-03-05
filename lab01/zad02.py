import math
import random 
import numpy as np
import matplotlib.pyplot as plt

v = 50
h = 100
g = 9.81
alfa = 45
alfa_rad = math.radians(alfa)

def d(v, h, g, alfa):
    alfa = math.radians(alfa)
    return v * math.cos(alfa) / g * (v * math.sin(alfa) + math.sqrt((v * math.sin(alfa))**2 + 2 * g * h))


def warwolf_distance(angle):
    return d(v, h, g, angle)


def was_target_hit():
    count = 0
    target = random.uniform(50, 340)
    while True:
        print(target)
        angle = int(input("angle: [-1 to quit]"))
        if angle == -1:
            break
        else:
            if abs(warwolf_distance(angle) - target) <= 5:
                print("\nangle: ", angle, "\n", "missed shots: ", count)
                break
            else:
                count+=1
                print("wrong angle", angle, warwolf_distance(angle))


# was_target_hit()

t_flight = (v * math.sin(alfa_rad) + math.sqrt((v * math.sin(alfa_rad))**2 + 2 * g * h)) / g

t = np.linspace(0, t_flight, num=100)

x = v * np.cos(alfa_rad) * t
y = h + v * np.sin(alfa_rad) * t - 0.5 * g * t**2

plt.figure(figsize=(10, 5))
plt.plot(x, y, 'b', label="Trajektoria pocisku")  
plt.grid(True)  
plt.legend()  

plt.savefig("trajektoria.png", dpi=300)
plt.show()



