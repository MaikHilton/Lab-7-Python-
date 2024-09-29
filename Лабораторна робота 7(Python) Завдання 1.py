train_schedule = {
    16: {"destination": "Київ - Харків", "arrival": (10, 30), "departure": (10, 45)},
    102: {"destination": "Львів - Одеса", "arrival": (12, 0), "departure": (12, 15)},
    123: {"destination": "Київ - Дніпро", "arrival": (14, 45), "departure": (15, 0)},
    104: {"destination": "Одеса - Львів", "arrival": (16, 10), "departure": (16, 25)},
    105: {"destination": "Харків - Київ", "arrival": (18, 50), "departure": (19, 5)},
    116: {"destination": "Ужгород - Київ", "arrival": (7, 20), "departure": (7, 35)},
    107: {"destination": "Чернівці - Львів", "arrival": (9, 40), "departure": (9, 55)},
    18: {"destination": "Київ - Запоріжжя", "arrival": (13, 10), "departure": (13, 25)},
    109: {"destination": "Харків - Одеса", "arrival": (17, 5), "departure": (17, 20)},
    110: {"destination": "Львів - Київ", "arrival": (20, 0), "departure": (20, 15)}
}

def print_all_trains(schedule):
    for train_num, details in schedule.items():
        print(f"Поїзд №{train_num}: {details['destination']}, Прибуття: {details['arrival'][0]:02d}:{details['arrival'][1]:02d}, Відправлення: {details['departure'][0]:02d}:{details['departure'][1]:02d}")


def add_train(schedule, train_num, destination, arrival, departure):
    if len(schedule) >= 10:
        print("Не можна додати більше 10 поїздів.")
        return
    
    if arrival[0] > 23 or arrival[1] > 59 or departure[0] > 23 or departure[1] > 59:
        print("Час прибуття або відправлення перевищує допустимі значення.")
        return

    if train_num in schedule:
        print(f"Поїзд з номером {train_num} вже існує!")
        return
    
    schedule[train_num] = {
        "destination": destination,
        "arrival": arrival,
        "departure": departure
    }
    print(f"Поїзд №{train_num} додано успішно.")



def remove_train(schedule, train_num):
    try:
        del schedule[train_num]
        print(f"Поїзд №{train_num} видалено.")
    except KeyError:
        print(f"Поїзд з номером {train_num} не знайдено!")

def print_sorted_schedule(schedule):
    for train_num in sorted(schedule.keys()):
        details = schedule[train_num]
        print(f"Поїзд №{train_num}: {details['destination']}, Прибуття: {details['arrival'][0]:02d}:{details['arrival'][1]:02d}, Відправлення: {details['departure'][0]:02d}:{details['departure'][1]:02d}")


def trains_at_station(schedule, current_time):
    current_hour, current_minute = current_time
    trains_on_station = []
    for train_num, details in schedule.items():
        arrival_hour, arrival_minute = details['arrival']
        departure_hour, departure_minute = details['departure']
        
        if (arrival_hour < current_hour or (arrival_hour == current_hour and arrival_minute <= current_minute)) and \
           (departure_hour > current_hour or (departure_hour == current_hour and departure_minute >= current_minute)):
            trains_on_station.append((train_num, details['destination']))
    
    return trains_on_station


def run_schedule_program():
    while True:
        print("\nМеню:")
        print("1. Вивести всі поїзди")
        print("2. Додати новий поїзд")
        print("3. Видалити поїзд")
        print("4. Вивести поїзди за відсортованими ключами")
        print("5. Знайти поїзди, що стоять на станції в заданий час")
        print("6. Вийти")
        choice = input("Оберіть дію: ")
        
        if choice == "1":
            print_all_trains(train_schedule)
        elif choice == "2":
            try:
                train_num = int(input("Введіть номер поїзда: "))
                destination = input("Введіть маршрут (наприклад, Київ - Львів): ")
                arrival_hour = int(input("Час прибуття (години): "))
                arrival_minute = int(input("Час прибуття (хвилини): "))
                departure_hour = int(input("Час відправлення (години): "))
                departure_minute = int(input("Час відправлення (хвилини): "))
                add_train(train_schedule, train_num, destination, (arrival_hour, arrival_minute), (departure_hour, departure_minute))
            except ValueError:
                print("Помилка введення! Невірний формат даних.")
        elif choice == "3":
            try:
                train_num = int(input("Введіть номер поїзда для видалення: "))
                remove_train(train_schedule, train_num)
            except ValueError:
                print("Помилка введення! Номер поїзда має бути числом.")
        elif choice == "4":
            print_sorted_schedule(train_schedule)
        elif choice == "5":
            try:
                current_hour = int(input("Введіть поточний час (години): "))
                current_minute = int(input("Введіть поточний час (хвилини): "))
                trains = trains_at_station(train_schedule, (current_hour, current_minute))
                if trains:
                    print("Поїзди, що стоять на станції:")
                    for train_num, destination in trains:
                        print(f"Поїзд №{train_num}: {destination}")
                else:
                    print("На станції немає поїздів у цей час.")
            except ValueError:
                print("Помилка введення! Невірний формат часу.")
        elif choice == "6":
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

# Запуск програми
run_schedule_program()
