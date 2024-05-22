def is_weekend(day):
    return day == '일' or day == '토'

def is_holiday(holidays, today):
    return today in holidays

def is_normalday(holidays, today, current_day):
    return not (is_weekend(current_day) or is_holiday(holidays, today))

def find_alternate_day(month, date, days, current_day_idx, holidays, last_days_of_months):
    found = False
    extra_holiday = 0
    
    if days[current_day_idx] == '토':
        while month > -1 and not found:
            for d in range(date, 0, -1):
                if is_normalday(holidays, [month + 1, d], days[current_day_idx]):
                    found = True
                    extra_holiday = 1  # 과거로 이동하므로 추가
                    holidays.append([month + 1, d])  # 임시 공휴일 지정
                    break
                current_day_idx = (current_day_idx - 1) % 7
            month -= 1
            date = last_days_of_months[month]

    else:  # 일요일
        while month < len(last_days_of_months) and not found:
            for d in range(date, last_days_of_months[month] + 1):
                if is_normalday(holidays, [month + 1, d], days[current_day_idx]):
                    found = True
                    holidays.append([month + 1, d])  # 임시 공휴일 지정
                    break
                current_day_idx = (current_day_idx + 1) % 7
            month += 1
            date = 1

    return extra_holiday, holidays

def find_alternate_pay_day(month, pay_day, days, current_day_idx, holidays, last_days_of_months):
    found = False
    left, right = 0, 0
    when = [0, 0]
    tmp_day_idx = current_day_idx

    for d in range(pay_day, 0, -1):
        if is_normalday(holidays, [month + 1, d], days[tmp_day_idx]):
            found = True
            when[0] = d
            break
        tmp_day_idx = (tmp_day_idx - 1) % 7
        left += 1

    tmp_day_idx = current_day_idx
    for d in range(pay_day, last_days_of_months[month] + 1):
        if is_normalday(holidays, [month + 1, d], days[tmp_day_idx]):
            found = True
            when[1] = d
            break
        right += 1
        tmp_day_idx = (tmp_day_idx + 1) % 7

    if found:
        if left > right:
            return when[1]
        elif left < right:
            return when[0]
        else:
            return when[0] if days[current_day_idx] == '토' else when[1]
    else:
        return pay_day

def solution(X, holidays, pay_day):
    last_days_of_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['월', '화', '수', '목', '금', '토', '일']
    total_break = 0
    on_time_pay_days = []
    current_day_idx = (X - 1) % len(days)
    day_counter = current_day_idx

    for month in range(len(last_days_of_months)):
        for date in range(1, last_days_of_months[month] + 1):
            today = [month + 1, date]
            if is_holiday(holidays, today) and is_weekend(days[day_counter]):
                extra_holiday, holidays = find_alternate_day(month, date, days, day_counter, holidays, last_days_of_months)
                total_break += (1 + extra_holiday)
            elif is_holiday(holidays, today) or is_weekend(days[day_counter]):
                total_break += 1
            else:
                if date == pay_day:
                    on_time_pay_days.append(month)

            day_counter = (day_counter + 1) % len(days)

    pay_dates = []
    current_day_idx = (X - 1) % len(days)
    for month in range(len(last_days_of_months)):
        if month in on_time_pay_days:
            pay_dates.append(pay_day)
        else:
            adjusted_pay_day = find_alternate_pay_day(month, pay_day, days, (current_day_idx + pay_day - 1) % len(days), holidays, last_days_of_months)
            pay_dates.append(adjusted_pay_day)

        current_day_idx = (current_day_idx + last_days_of_months[month]) % len(days)

    return pay_dates