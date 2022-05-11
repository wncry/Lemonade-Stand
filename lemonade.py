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

# integer checking system provided by https://stackoverflow.com/users/32538/kirk-strauser
# on https://stackoverflow.com/questions/19671149/python-int-and-input

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
# - [x] import 'random' source code to become independant
# - [x] update streetcrew handling to enable recursion
# - [x] update thunderstorm handling to enable recursion
# - [x] create morning()
# - [x] fix recursion exiting
# - [x] optimize global variables
# - [x] insert joke here
# - [ ] increase 'glasses_cost' to disable beginner bonus
# - [x] universal weather
# - [ ] negative profit exception handling
# - [x] if sign number = 0 exception handling
# - [x] recursive budget error handling
# - [x] make sure code does not reach recursive depth limit o_o
# - [x] universal chance of rain
# - [x] morning forecast
# - [ ] negative input exception handling
# - [x] non-int input exception handling
# - [x] cross recursion handling


# RANDOM NUMBER GENERATOR
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

# err handling

### err handling requirements
# 1. is int
# 2. is positive
# 3. is in range 

budget_err_external_var = 0  # possible error of crosswriting to external variables
def budget_err(budget_err_inp, budget_err_var_1, budget_err_var_2, print2, is_cross_recursing, *, recursive_inp):  # not in range
    
    budget_err_var = int(input(budget_err_inp))  # input
    
    try: int_budget_err_var = int(budget_err_var)  # checks if integer
    except ValueError:  # not integer
        print3 = '\nhow many glasses of lemonade (${} each) would you like to make?: '.format(glasses_cost)
        input_err(print3, True, budget_err_var)  # redo integer check
        int_budget_err_var = input_err_external_var
        global input_err_external_var
        input_err_external_var -= input_err_external_var
    else:  # is integer
        if (budget_err_var * budget_err_var_1) > budget_err_var_2:  # check if in range
            print(print2)
            budget_err(budget_err_inp, budget_err_var_1, budget_err_var_2, False)  # not in range
        else:  # in range
            global budget_err_external_var  # is integer and in range
            budget_err_external_var += int_budget_err_var # exits

input_err_external_var = 0  # possible error of crosswriting to external variables
def input_err(print3, is_cross_recursing, *, recursive_inp):  # not integer
    print('\n[!] invalid integer')
    inp_val = input(print3)  # input
    try: int_inp_val = int(inp_val)  # checks if integer
    except ValueError:  # not integer
        input_err(print3, False)  # redo integer check
    else:  # is integer

        ###
        if (int_inp_val * glasses_cost) > total_profit:  # check if in range
            print1 = '\nhow many glasses of lemonade (${} each) would you like to make?: '.format(glasses_cost)
            print2 = '\n[!] you dont have enough money'
            print(print2)
            budget_err(print1, glasses_cost, total_profit - sign_cost, print2, False)  # not in range

            int_inp_val = budget_err_external_var  # write and wipe
            global budget_err_external_var
            budget_err_external_var -= budget_err_external_var

        elif (int_inp_val * glasses_cost) > (total_profit - sign_cost):  # check if in range
            print1 = '\nhow many glasses of lemonade (${} each) would you like to make?: '.format(glasses_cost)
            print2 = '\n[!] you wont have enough money to purchase advertising signs'
            print(print2)
            budget_err(print1, glasses_cost, total_profit - sign_cost, print2, False)  # not in range

            int_inp_val = budget_err_external_var  # write and wipe
            global budget_err_external_var
            budget_err_external_var -= budget_err_external_var
        ###

        global input_err_external_var  # is integer and in range
        input_err_external_var += int_inp_val  # exits

def morning(morning_forecast):
    if morning_forecast == CLOUDY_BALANCE:
        morn_state = 'cloudy'
        morn_chance_of_rain = randint(40, 100)
    elif morning_forecast == SUNNY_BALANCE:
        morn_state = 'sunny'
        morn_chance_of_rain = randint(2, 12)
    elif morning_forecast == HD_BALANCE:
        morn_state = 'hot and dry'
        morn_chance_of_rain = 0

    print('''
GOOD MORNING
current balance: {}

morning forecast: {}
chance of rain: {}
'''.format(total_profit, morn_state, morn_chance_of_rain))
    
    # glasses made
    morn_glasses = input('how many glasses of lemonade (${} each) would you like to make?: '.format(glasses_cost))

    try: int_morn_glasses = int(morn_glasses)
    except ValueError:
        print3 = '\nhow many glasses of lemonade (${} each) would you like to make?: '.format(glasses_cost)
        input_err(print3)
        int_morn_glasses = input_err_external_var
        global input_err_external_var
        input_err_external_var -= input_err_external_var

    if (int_morn_glasses * glasses_cost) > total_profit:
        print1 = '\nhow many glasses of lemonade (${} each) would you like to make?: '.format(glasses_cost)
        print2 = '\n[!] you dont have enough money'
        print(print2)
        budget_err(print1, glasses_cost, total_profit - sign_cost, print2, False)
        int_morn_glasses = budget_err_external_var
        global budget_err_external_var
        budget_err_external_var -= budget_err_external_var
    elif (int_morn_glasses * glasses_cost) > (total_profit - sign_cost):
        print1 = '\nhow many glasses of lemonade (${} each) would you like to make?: '.format(glasses_cost)
        print2 = '\n[!] you wont have enough money to purchase advertising signs'
        print(print2)
        budget_err(print1, glasses_cost, total_profit - sign_cost, print2, False)
        int_morn_glasses = budget_err_external_var
        global budget_err_external_var
        budget_err_external_var -= budget_err_external_var


    # signs made
    morn_ads = int(input('how many advertising signs (${} each) would you like to make?: '.format(sign_cost)))
    if (morn_ads * sign_cost) > (total_profit):
        print1 = '\nhow many advertising signs (${} each) would you like to make?: '.format(sign_cost)
        print2 = '\n[!] you dont have enough money'
        print(print2)
        budget_err(print1, glasses_cost, total_profit, print2, False)
        morn_ads = budget_err_external_var
        global budget_err_external_var
        budget_err_external_var -= budget_err_external_var

    # price charged
    morn_cost = int(input('how much would you like to charge (in cents) per glass of lemonade?: '))
    print()

    global recursion_depth_count
    recursion_depth_count += 1

    day(int_morn_glasses, morn_ads, morn_cost, morning_forecast, morn_chance_of_rain)
    return

def day(glasses_made, signs_made, price_charged, weather_state, chance_of_rain):
    
    # EVENTS

    # streetcrew handling
    street_crew_chance = randint(0, 99)
    if street_crew_chance >= 95:  # 5% chance
        revenue = (glasses_made * price_charged)
        expenses = (signs_made * sign_cost) + (glasses_made + glasses_cost)
        profit = revenue - expenses
        revenue_report(glasses_made, signs_made, price_charged, revenue, expenses, profit, weather_state, chance_of_rain)
        return
    
    # thunderstorm handling
    if chance_of_rain > 90:  # 5.5¯% chance 
        revenue = 0
        expenses = (signs_made * sign_cost) + (glasses_made + glasses_cost)
        profit = revenue - expenses
        revenue_report(glasses_made, signs_made, price_charged, revenue, expenses, profit, weather_state, chance_of_rain)
        return


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
    if signs_made <= 0:
        glasses_sold -= glasses_sold/2

    # final sums
    revenue = min(glasses_made - glasses_sold) * price_charged
    expenses = (signs_made * sign_cost) + (glasses_made + glasses_cost)
    profit = revenue - expenses

    revenue_report(glasses_made, signs_made, price_charged, revenue, expenses, profit, weather_state, chance_of_rain)
    return

def revenue_report(fin_glasses, fin_signs, fin_price, fin_rev, fin_exp, fin_profit, fin_weather_state, chance_of_rain):

    # progress tracking
    global total_revenue 
    total_revenue += fin_rev
    global total_expenses
    total_expenses += fin_exp
    global total_profit
    total_profit += fin_profit
    global day_count
    day_count += 1
    global recursion_depth_count
    recursion_depth_count += 1

    if fin_weather_state == 1: fin_state = 'cloudy'
    elif fin_weather_state == 2: fin_state = 'sunny'
    elif fin_weather_state == 3: fin_state = 'hot and dry'

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
        global recursion_depth_count
        recursion_depth_count += 1
        morning(weather())
        return

# DAY ONE
morning(weather())

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
'''.format(day_count, total_revenue, total_expenses, total_profit, recursion_depth_count))

