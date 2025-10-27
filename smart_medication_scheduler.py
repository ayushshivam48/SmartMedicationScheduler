# Mock medicine database, now includes food timing info
medicine_info = {
    "Aspirin": {"condition": "Heart", "potency": 8, "recommended_times": [8], "food": "after food"},
    "Metformin": {"condition": "Diabetes", "potency": 12, "recommended_times": [8, 20], "food": "after food"},
    "Lisinopril": {"condition": "BP", "potency": 24, "recommended_times": [8], "food": "before food"},
    "Melatonin": {"condition": "Sleep", "potency": 6, "recommended_times": [22], "food": "before bed"},
    "Paracetamol": {"condition": "Pain", "potency": 6, "recommended_times": [8, 14, 20], "food": "with or after food"},
}

def fetch_medicine_info(med_name):
    return medicine_info.get(med_name)

def main():
    print("\n⚠️ NOTE: Always use medications only after they have been prescribed by a qualified doctor.\n")
    print("💊 Medicine Info Helper 💊")
    print("Enter medicine names one by one (press ENTER with no name to finish):")
    
    med_list = []
    while True:
        med = input()
        if not med.strip():
            break
        med_list.append(med.strip())

    if not med_list:
        print("No medicines entered. Exiting.")
        return

    print("\n🔍 Medicine Details\n" + "-"*50)
    for med in med_list:
        info = fetch_medicine_info(med)
        if info:
            times = ', '.join(str(h)+":00" for h in info['recommended_times'])
            print(f"{med}: Used for {info['condition']}. Timings: {times}. Take {info['food']}.")
        else:
            print(f"{med}: No info found in database.")

    print("\n💡 Always consult your doctor for advice specific to you!")

if __name__ == "__main__":
    main()
