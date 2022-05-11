# .wncry
# licensed under GNU GPLv2.0

# inspired by Lemonade Stand (1979)
# https://archive.org/details/Lemonade_Stand_1979_Apple

# huge thanks to lars-erik for the original source variables
# https://github.com/lars-erik/lemonade-stand/blob/master/Docs/Original%20Source%20Variables.txt
# all intelectual property used under MIT license

# random number generator provided by https://stackoverflow.com/users/4279/jfs
# on https://stackoverflow.com/questions/22950768/random-int-without-importing-random
# by modifying the random.py source code https://hg.python.org/cpython/file/tip/Lib/random.py
# yes, i am aware python comes with random preinstalled, but it is much more difficult to
# compile a .py file with imports into an app compared to a .py file without imports

# UPDATE: unused
# float rounding provided by https://stackoverflow.com/users/5190/vinko-vrsalovic
# and https://stackoverflow.com/users/1901786/whereswalden
# on https://stackoverflow.com/questions/56820/round-doesnt-seem-to-be-rounding-properly
# print(float("%.2f" % 123.123))
# print(float('{:.2f}'.format(123.123)))

# in case of stack overflow https://stackoverflow.com/questions/3323001/what-is-the-maximum-recursion-depth-in-python-and-how-to-increase-it


# ENV VAR
ARBITRARY_BALANCE = 0
CLOUDY_BALANCE = 1
SUNNY_BALANCE = 2
HD_BALANCE = 3

# static modifiers
high_price_offset = 10
sales_mod = 30
asset_start_value = 2.00
negative_sign_mod = 0.5
extra_sign_mod = 1

# starting variables
init_assets = 2.00
glasses_cost = 0.02
sign_cost = 0.15

# dynamic records
total_revenue = 0
total_expenses = 0
total_profit = 0
day_count = 0
recursion_depth_count = 0  # day number

### TO DO
# --- 1. import 'random' source code to become independant
# 2. update streetcrew handling to enable recursion
# 3. update thunderstorm handling to enable recursion
# 4. create morning()
# 5. fix recursion exiting
# 6. fix global variables
# --- 7. insert joke here
# 8. increase 'glasses_cost' on day 3 morning
# 9. universal weather
# 10. negative profit exception handling
# 11. if sign number = 0, glasses_sold -= glasses_sold/2
# --- 12. recursive budget error handling
# 13. make sure code does not reach recursive depth limit o_o
# 14. universal chance of rain


# 4 hours
# 3 hours


# RANDOM INPORT
def randint(a, b):
    return a + randbelow(b - a + 1)
def randbelow(n):
    if n <= 0:
       raise ValueError
    k = n.bit_length()
    numbytes = (k + 7) // 8
    while True:
        r = int.from_bytes(random_bytes(numbytes), 'big')
        r >>= numbytes * 8 - k
        if r < n:
            return r
def random_bytes(n):
    with open('/dev/urandom', 'rb') as file:
        return file.read(n)


# WORKDAY

def weather():  # weather handling
    weather_factor = randint(0, 9)
    weather_state = 0
    if weather_factor >= 7:  # 20% chance to be cloudy
        weather_state += CLOUDY_BALANCE
    elif weather_factor < 4:  # 50% chance to be sunny
        weather_state += SUNNY_BALANCE
    elif weather_factor < 7 and weather_factor >= 4:  # 30% chance to be hot and dry
        weather_state += HD_BALANCE
    return weather_state


budget_err_external_var = 0
def budget_err(budget_err_inp, budget_err_var_1, budget_err_var_2):
    budget_err_var = int(input(budget_err_inp))
    if (budget_err_var * budget_err_var_1) > budget_err_var_2:
        print('\nyou dont have budget for that')
        budget_err(budget_err_inp, budget_err_var_1, budget_err_var_2)
    else:
        global budget_err_external_var
        budget_err_external_var += budget_err_var
    return

def morning():
    morning_forecast = weather()

    print('\n\nGOOD MORNING\ncurrent balance: {}'.format(total_profit))

    if morning_forecast == 1:
        morn_state = 'cloudy'
        morn_chance_of_rain = randint(40, 90)
    elif morning_forecast == 2:
        morn_state = 'sunny'
        morn_chance_of_rain = randint(2, 12)
    elif morning_forecast == 3:
        morn_state = 'hot and dry'
        morn_chance_of_rain = 0
    
    # glasses made
    morn_glasses = int(input('how many glasses of lemonade (${} each) would you like to make?: '.format(glasses_cost)))
    if (morn_glasses * glasses_cost) > total_profit:
        print('you dont have enough money!')
        budget_err('how many glasses of lemonade (${} each) would you like to make?: '.format(glasses_cost), glasses_cost, total_profit - sign_cost)
        morn_glasses = budget_err_external_var
        global budget_err_external_var
        budget_err_external_var -= budget_err_external_var
    elif (morn_glasses * glasses_cost) > (total_profit - sign_cost):
        print('you wont have enough money to purchase advertising signs!')
        budget_err('how many glasses of lemonade (${} each) would you like to make?: '.format(glasses_cost), glasses_cost, total_profit - sign_cost)
        morn_glasses = budget_err_external_var
        global budget_err_external_var
        budget_err_external_var -= budget_err_external_var

    # signs made
    morn_ads = int(input('how many advertising signs (${} each) would you like to make?: '.format(sign_cost)))
    if (morn_ads * sign_cost) > (total_profit):
        print('you dont have enough money!')
        budget_err('how many advertising signs (${} each) would you like to make?: '.format(sign_cost), glasses_cost, total_profit)
        morn_ads = budget_err_external_var
        global budget_err_external_var
        budget_err_external_var -= budget_err_external_var

    # price charged
    morn_cost = int(input('how much would you like to charge (in cents) per glass of lemonade?: '))
    print()

    day(morn_glasses, morn_ads, morn_cost, morning_forecast)

def day(glasses_made, signs_made, price_charged, weather_state):

    # streetcrew handling
    street_crew_chance = randint(0, 99)
    if street_crew_chance >= 95:  # 5% chance
        revenue += (glasses_made * price_charged)
        #break --> restart func

    # thunderstorm handling
    thunderstorm_state = randint(0, 99)
    if weather_state == CLOUDY_BALANCE and thunderstorm_state >= 90:  # 3% chance 
        revenue += 0
        #break --> restart func


    # ALGORITHM

    # user-set price handling
    if price_charged < high_price_offset:
        sales_factor = (high_price_offset - price_charged) / ((high_price_offset * 0.8 * sales_mod) + sales_mod)
    else:
        sales_factor = (high_price_offset^2) * (sales_mod / (price_charged^2)) # bitwise XOR --> https://www.programiz.com/csharp-programming/bitwise-operators

    # user-set sign handling
    sign_mod = -signs_made * negative_sign_mod
    sign_mod_result = 1 - ((sign_mod ** extra_sign_mod) // extra_sign_mod)

    # user-set sale handling
    glasses_sold = (weather_state * (sales_factor + (sales_factor * sign_mod_result))) - ARBITRARY_BALANCE

    # final sums
    revenue = min(glasses_made - glasses_sold) * price_charged
    expenses = (signs_made * sign_cost) + (glasses_made + glasses_cost)
    profit = revenue - expenses


    # progress tracking
    global total_revenue 
    total_revenue += revenue
    global total_expenses
    total_expenses += expenses  # TO DO 6.
    global total_profit
    total_profit += profit
    global day_count
    day_count += 1
    global recursion_depth_count
    recursion_depth_count += 1

    revenue_report(glasses_made, signs_made, price_charged, revenue, expenses, profit, weather_state)

    return profit  # TO DO 5.


def revenue_report(fin_glasses, fin_signs, fin_price, fin_rev, fin_exp, fin_profit, fin_weather_state):

    if fin_weather_state == 1:
        fin_state = 'cloudy'
        chance_of_rain = randint(40, 90)
    elif fin_weather_state == 2:
        fin_state = 'sunny'
        chance_of_rain = randint(2, 12)
    elif fin_weather_state == 3:
        fin_state = 'hot and dry'
        chance_of_rain = 0

    global day_count
    global total_profit

    print(
'''
>---------->
DAY {} REVENUE REPORT

weather state: {}
chance of rain: {}

glasses made: {}
advertisements made: {}
price charged: ${}

revenue: {}
expenses: {}
profit: {}

current balance {}
>----------<
'''.format(day_count, fin_state, chance_of_rain, fin_glasses, fin_signs, fin_price, fin_rev, fin_exp, fin_profit, total_profit))
    
    end = input("press enter to continue, or type 'esc' to close the lemonade stand")

    if end == 'esc':
        return fin_profit
    else:
        day(fin_glasses, fin_signs, fin_price)


# DAY ONE USR INPUT

usr_glasses_made = 20
usr_signs_made = 5
usr_price_charged = 10

# CALL MORNING
profit = day(usr_glasses_made, usr_signs_made, usr_price_charged, weather())

print(
'''
>---------->
FINAL STATS

total days open: {}
total revenue: {}
total expenses: {}
total profit: {}

recursion depth count: {}
>----------<
'''.format(day_count, total_revenue, total_expenses, profit, recursion_depth_count))

