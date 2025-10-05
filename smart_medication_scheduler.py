# Mock medicine database
medicine_info = {
    "Aspirin": {"condition": "Heart", "potency": 8, "recommended_times": [8]},
    "Metformin": {"condition": "Diabetes", "potency": 12, "recommended_times": [8, 20]},
    "Lisinopril": {"condition": "BP", "potency": 24, "recommended_times": [8]},
    "Melatonin": {"condition": "Sleep", "potency": 6, "recommended_times": [22]},
    "Paracetamol": {"condition": "Pain", "potency": 6, "recommended_times": [8, 14, 20]},
}

# Known interactions
interactions = {
    ("Aspirin", "Warfarin"): "High risk: increased bleeding",
    ("Metformin", "Contrast Dye"): "Caution: kidney issues",
    ("Lisinopril", "Potassium"): "Risk of hyperkalemia",
}

def fetch_medicine_info(med_name):
    return medicine_info.get(med_name)

def fetch_interactions(med_list):
    warnings = []
    for i in range(len(med_list)):
        for j in range(i+1, len(med_list)):
            pair = (med_list[i], med_list[j])
            pair_rev = (med_list[j], med_list[i])
            if pair in interactions:
                warnings.append(f"{pair[0]} + {pair[1]}: {interactions[pair]}")
            elif pair_rev in interactions:
                warnings.append(f"{pair_rev[0]} + {pair_rev[1]}: {interactions[pair_rev]}")
    return warnings

def generate_schedule(med_list):
    schedule = {}
    for med in med_list:
        info = fetch_medicine_info(med)
        if not info:
            print(f"⚠️ {med} not found, assigning generic morning schedule")
            schedule[med] = [8]
        else:
            schedule[med] = info["recommended_times"]
    return schedule

def display_schedule(schedule, med_list):
    print("\n🕒 Intelligent Medication Schedule")
    print("-"*50)
    for med in med_list:
        info = fetch_medicine_info(med)
        condition = info["condition"] if info else "General"
        times = schedule[med]
        print(f"{med} ({condition}) -> Take at hours: {', '.join(str(h)+':00' for h in times)}")

def main():
    print("💊 Smart Medication Scheduler – Offline Version 💊")
    n = int(input("Enter number of medications: "))
    med_list = [input("Medication Name: ") for _ in range(n)]

    schedule = generate_schedule(med_list)
    warnings = fetch_interactions(med_list)

    display_schedule(schedule, med_list)

    if warnings:
        print("\n⚠️ Drug Interaction Warnings")
        for w in warnings:
            print(w)
    else:
        print("\n✅ No major drug interactions detected.")

    print("\n💡 Follow this schedule and consult your healthcare provider regularly!")

if __name__ == "__main__":
    main()
