import csv

def analyze_shop_traffic(filename):
    total_pages = 0
    tray_capacity = 250
    reloads_needed = []
    hourly_stats = {}
    
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            time = row['Timestamp']
            hour = time.split(':')[0]
            queue = int(row['Queue_Count'])
            pages = int(row['Pages_Printed'])
            
            # Track hourly load for peak/break analysis
            if hour not in hourly_stats:
                hourly_stats[hour] = {'pages': 0, 'queue_max': 0}
            
            hourly_stats[hour]['pages'] += pages
            if queue > hourly_stats[hour]['queue_max']:
                hourly_stats[hour]['queue_max'] = queue
                
            # Track paper tray depletion
            total_pages += pages
            if total_pages >= tray_capacity:
                reloads_needed.append(time)
                total_pages = 0 # reset tray

    # Find peak and quiet hours
    peak_hour = max(hourly_stats, key=lambda x: hourly_stats[x]['pages'])
    quiet_hour = min(hourly_stats, key=lambda x: hourly_stats[x]['pages'])
    
    # Generate Output
    print("\n--- NIT XEROX DAILY OPERATIONS PLAN ---")
    print(f"Target: Mr. Ramesh Mahato")
    
    print("\n1. PAPER RELOAD ALERTS:")
    for time in reloads_needed:
        print(f"-> Tray will empty around {time}. Pre-load a fresh ream on the desk 15 minutes before this.")
        
    print(f"\n2. PEAK RUSH WARNING:")
    print(f"-> The {peak_hour}:00 hour has the highest print volume ({hourly_stats[peak_hour]['pages']} pages) and longest queues.")
    print(f"-> Action: Do not schedule breaks here. Ensure ₹200+ in loose change is ready for cash payers.")
    
    print(f"\n3. COOL-DOWN & LUNCH BREAK:")
    print(f"-> The {quiet_hour}:00 hour is practically empty ({hourly_stats[quiet_hour]['pages']} pages printed).")
    print(f"-> Action: Power down the main laser printer for 20 minutes to save the fuser roller, and take your lunch break.")
    print("---------------------------------------\n")

if __name__ == "__main__":
    analyze_shop_traffic("data.csv")