import csv
from datetime import datetime, timedelta

def generate_ihss_hours(year, start_month, num_months):
    filename = f"IHSS_Schedule_{year}.csv"
    headers = ['date YYYY_MM_DD', 'Month', 'Day', 'Hours', 'Weekly_Total', 'PayPeriod_Total', 'Monthly_Total']
    
    current_date = datetime(year, start_month, 1)
    end_date = current_date + timedelta(days=31 * num_months) # Rough estimate to cover full months
    
    # Tracking variables
    weekly_running = 0
    pay_period_running = 0
    monthly_running = 0
    
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        
        while current_date.month < (start_month + num_months):
            # 1. Basic Info
            date_str = current_date.strftime('%Y_%m_%d')
            month_name = current_date.strftime('%B')
            day_name = current_date.strftime('%A')
            
            # 2. Determine Hours (The 5-7-0 Rule)
            if day_name == 'Saturday':
                daily_hours = 0
            elif day_name == 'Sunday':
                daily_hours = 5
            else:
                daily_hours = 7

            # 3. Logic: Don't break the Caps
            # Check Pay Period (80 max)
            if pay_period_running + daily_hours > 80:
                daily_hours = 80 - pay_period_running
            
            # Check Monthly (160 max)
            if monthly_running + daily_hours > 160:
                daily_hours = 160 - monthly_running

            # 4. Update Running Totals
            weekly_running += daily_hours
            pay_period_running += daily_hours
            monthly_running += daily_hours
            
            # 5. Write Row
            writer.writerow([
                date_str, month_name, day_name, daily_hours, 
                weekly_running, pay_period_running, monthly_running
            ])
            
            # 6. Reset Totals on Boundaries
            # Reset Weekly on Saturday night (End of IHSS workweek)
            if day_name == 'Saturday':
                weekly_running = 0
                
            # Reset Pay Period on 15th and Last day of month
            next_day = current_date + timedelta(days=1)
            if current_date.day == 15 or next_day.month != current_date.month:
                pay_period_running = 0
                
            # Reset Monthly
            if next_day.month != current_date.month:
                monthly_running = 0
                
            current_date = next_day

    print(f"File '{filename}' created successfully.")

# Run for March, April, and May 2026
generate_ihss_hours(2024, 2, 12)