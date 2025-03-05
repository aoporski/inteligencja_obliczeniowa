import datetime
import math

def calculate_biorythm(birth_date: datetime.date):
    today = datetime.date.today()
    diff = (today - birth_date).days
    
    waves = {
        "physical": math.sin((2 * math.pi / 23) * diff),
        "emotional": math.sin((2 * math.pi / 28) * diff),
        "intellectual": math.sin((2 * math.pi / 33) * diff)
    }
    
    return waves, diff

def print_biorythm(waves):
    print("Biorythm levels:")
    for key, value in waves.items():
        print(f"{key.capitalize()} wave: {value:.4f}")
        
        if value > 0.5:
            print(f"Good {key} biorythm")
        elif value < -0.5:
            print(f"Bad {key} biorythm")

def predict_next_day(waves, diff):
    next_day_waves = {
        "physical": math.sin((2 * math.pi / 23) * (diff + 1)),
        "emotional": math.sin((2 * math.pi / 28) * (diff + 1)),
        "intellectual": math.sin((2 * math.pi / 33) * (diff + 1))
    }
    
    for key in waves:
        if waves[key] < -0.5 and next_day_waves[key] > waves[key]:
            print(f"You will feel {key}ly better tomorrow :)")

def main():
    name = input("Enter your name: ")
    birth_year = int(input("Year of birth: "))
    birth_month = int(input("Month of birth: "))
    birth_day = int(input("Day of birth: "))
    
    birth_date = datetime.date(birth_year, birth_month, birth_day)
    waves, diff = calculate_biorythm(birth_date)
    
    print(f"\nHello, {name}! Here is your biorythm:\n")
    print_biorythm(waves)
    predict_next_day(waves, diff)

if __name__ == "__main__":
    main()