'''
python "\$_USB/ihss_gen_2.py" 


'''


import csv
from datetime import datetime, timedelta

def generate_ihss_hours(year, start_month, end_year, end_month):
    filename = f"IHSS_Schedule_{year}_{start_month}_to_{end_year}_{end_month}.csv"
    headers = ['date YYYY_MM_DD', 'Month', 'Day', 'Hours', 'Weekly_Total', 'PayPeriod_Total', 'Monthly_Total']
    
    current_date = datetime(year, start_month, 1)
    # The loop will run until the end of the specified end_month
    
    weekly_running = 0
    pay_period_running = 0
    monthly_running = 0
    
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        
        # This keeps running as long as we haven't passed the end month
        while True:
            # Stop condition: If we've moved into the month AFTER our end target
            if current_date.year > end_year or (current_date.year == end_year and current_date.month > end_month):
                break

            date_str = current_date.strftime('%Y_%m_%d')
            month_name = current_date.strftime('%B')
            day_name = current_date.strftime('%A')
            
            # THE RULES: 5 on Sun, 7 on Mon-Fri, 0 on Sat
            if day_name == 'Saturday':
                daily_hours = 0
            elif day_name == 'Sunday':
                daily_hours = 5
            else:
                daily_hours = 7

            # Safety Trimming (Snap to 80/160)
            if pay_period_running + daily_hours > 80:
                daily_hours = max(0, 80 - pay_period_running)
            
            if monthly_running + daily_hours > 160:
                daily_hours = max(0, 160 - monthly_running)

            weekly_running += daily_hours
            pay_period_running += daily_hours
            monthly_running += daily_hours
            
            writer.writerow([date_str, month_name, day_name, daily_hours, 
                             weekly_running, pay_period_running, monthly_running])
            
            # PREPARE FOR NEXT DAY
            next_day = current_date + timedelta(days=1)
            
            # SEPARATOR LOGIC (After 15th and Last Day)
            if current_date.day == 15 or next_day.month != current_date.month:
                writer.writerow([''] * len(headers))
            
            # RESET LOGICS
            if day_name == 'Saturday':
                weekly_running = 0
            if current_date.day == 15 or next_day.month != current_date.month:
                pay_period_running = 0
            if next_day.month != current_date.month:
                monthly_running = 0
                
            current_date = next_day

    print(f"Done! Created '{filename}' successfully.")

# --- SET YOUR DATES HERE ---
# Format: (Start Year, Start Month, End Year, End Month)
generate_ihss_hours(2024, 2, 2026, 13)