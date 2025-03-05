import datetime
import math

name = input("imię: ")
birth_year = int(input("rok urodzenia: "))
birth_month = int(input("miesiąc urodzenia: "))
birth_day = int(input("dzień urodzenia: "))
birth = datetime.date(birth_year, birth_month, birth_day)

print("Hello ", name, "\nHere is your biorythm: ")
today = datetime.date.today()
diff = (today - birth).days

def wave(period, difference):
    return math.sin((2 * math.pi / period ) * difference)

physical_wave = wave(23, diff)
emotional_wave = wave(28, diff)
intelectual_wave = wave(33, diff)

print("physical wave: ", physical_wave)
print("emotional wave: ", emotional_wave)
print("intelectual wave: ", intelectual_wave)

if (physical_wave > 0.5): 
    print("Good physical biorythm")
elif (physical_wave < -0.5):
    print("Bad physical biorythm")

if (emotional_wave > 0.5): 
    print("Good emotional biorythm")
elif (emotional_wave < -0.5):
    print("Bad emotional biorythm")

if (intelectual_wave > 0.5): 
    print("Good intelectual biorythm")
elif (intelectual_wave < -0.5):
    print("Bad intelectual biorythm")


physical_wave_next_day = wave(23, diff+1)
emotional_wave_next_day  = wave(28, diff+1)
intelectual_wave_next_day  = wave(33, diff+1)

if physical_wave < -0.5 and physical_wave_next_day > physical_wave:
    print("You will feel physically better tomorrow :)")

if (emotional_wave < -0.5 and emotional_wave_next_day > emotional_wave):
    print("You will feel emotionally better tomorrow :)")

if (intelectual_wave < -0.5 and intelectual_wave_next_day > intelectual_wave):
    print("You will be smarter tomorrow :)")

# e) Czas spędzony na pisanie programu: około 30 minut