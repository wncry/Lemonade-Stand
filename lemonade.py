# .wncry
# licensed under GNU GPLv2.0

# inspired by Lemonade Stand (1979)
# https://archive.org/details/Lemonade_Stand_1979_Apple

# huge thanks to lars-erik for the algorithm outline
# https://github.com/lars-erik/lemonade-stand
# all intelectual property used under MIT license

# random number generator inspired by https://stackoverflow.com/users/4279/jfs
# on https://stackoverflow.com/questions/22950768/random-int-without-importing-random
# by modifying the random.py source code https://hg.python.org/cpython/file/tip/Lib/random.py
# yes, i am aware python comes with random preinstalled, but it is much more difficult to
# compile a .py file with imports into an app compared to a .py file without imports

# integer checking system inspired by https://stackoverflow.com/users/32538/kirk-strauser
# on https://stackoverflow.com/questions/19671149/python-int-and-input

# part of the error handling system inspired by https://stackoverflow.com/users/3130539/mhlester
# and https://stackoverflow.com/users/4837077/jlt
# on https://stackoverflow.com/questions/21612910/finally-equivalent-for-if-elif-statements-in-python

# float rounding inspired by https://stackoverflow.com/users/5190/vinko-vrsalovic
# and https://stackoverflow.com/users/1901786/whereswalden
# on https://stackoverflow.com/questions/56820/round-doesnt-seem-to-be-rounding-properly
# print(float("%.2f" % 123.123))
# print(float('{:.2f}'.format(123.123)))

# in case of stack overflow https://stackoverflow.com/questions/3323001/what-is-the-maximum-recursion-depth-in-python-and-how-to-increase-it

from time import sleep

# ENV VAR
# starting variables
init_assets = 2.00
glass_cost = 0.02
sign_cost = 0.15

# dynamic records
total_revenue = 0
total_expenses = 0
total_profit = init_assets
day_count = 0
recursion_depth_count = 0

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

# ERROR HANDLING
# this is possibly the most disgusting thing i have ever written
# i have easily spent 4 hours on this
# hehe recursion go brrrrrrrrr
class wowthisisugly(Exception): pass
err_external_var = 0 
def err(print1, is_):
    global err_external_var
    err_var = input(print1)  # input
    try: int_err_var = int(err_var)  # check if integer
    except ValueError:  # not integer
        print('[!] cannot accept non integer')
        err(print1, 0)
    else:  # is integer
        if is_ == 1 and (int_err_var * sign_cost) > total_profit:  # check if in range
            print('[!] you do not have enough money')
            err(print1, 1)
        elif (int_err_var * glass_cost) > total_profit:  # check if in range
            print('[!] you do not have enough money')
            err(print1, 0)
        elif (int_err_var * glass_cost) > (total_profit - sign_cost):  # check if in range
            print('[!] you will not have enough money to purchase advertising signs')
            err(print1, 0)
        elif int_err_var < 0:  # check if positive
            print('[!] cannot accept negative integer')
            err(print1, 0)  # not positive
        else:  # positive integer and in range
            err_external_var += int_err_var

# WEATHER HANDLING
def weather():
    weather_factor = randint(0, 9)
    weather_state = 0
    if weather_factor >= 7:  # 20% chance to be cloudy
        weather_state += 1
    elif weather_factor < 4:  # 50% chance to be sunny
        weather_state += 2
    elif weather_factor < 7 and weather_factor >= 4:  # 30% chance to be hot and dry
        weather_state += 3
    return weather_state

# USER INPUT
def morning(morning_forecast):
    global err_external_var
    global day_count
    global recursion_depth_count
    global glass_cost
    global sign_cost

    print('\n\n\n\n')

    sleep(3)
    if day_count == 0:
        print('> hello friend')
        sleep(3)
        print('> you are running a lemonade stand!')
        sleep(3)
        print('> the finest in the world')
        sleep(3)
        print('> nothing compares to the quality of your lemonade')
        sleep(3)
        print('\n> every morning you will set 3 things:')
        sleep(3)
        print('> 1. how many cups of lemonade you will make')
        sleep(3)
        print('> 2. how many advertising signs you will make')
        sleep(3)
        print('> 3. how much you will charge per glass of lemonade\n')
        sleep(3)
        print('> the amount of customers you attract depends on:')
        sleep(3)
        print('> 1. the weather -- is it a day that many would want to purchase lemonade?')
        sleep(3)
        print('> 2. the number of advertising signs you make -- how will people hear about you? will they reach a point where they have heard too much?')
        sleep(4)
        print('> 3. the amount you charge per glass of lemonade -- how much are people willing to pay?')
        sleep(3)
        print('> 4. your positive attidude and wonderful smile :DDDD -- people are more likely to come back if they are met with a friendly face!\n')
        sleep(4)
        print('> your mom (lol) gives you $2.00 to start off your business,')
        sleep(3)
        print('> and for the first couple days, your mom (lol) decides to pay for your sugar <3')
        sleep(3)
        print('> it costs $0.02 to make one cup of lemonade')
        sleep(3)
        print('> it costs $0.15 to post one advertising sign')
        sleep(3)
        print('> have fun!')
        
        #intro
    elif day_count == 2:
        print('> because your lemonade stand operates in a very windy location, all advertising signs get blown away overnight')
        sleep(2)
        print('> you will need to purchase new signs each day to still get advertised')
        sleep(2)
        print('> your mom (lol) stopped paying for your sugar, but still supports you :]')
        glass_cost += 0.03
    elif day_count == 8:
        print('> lemonade is on sale today :D')
        glass_cost -= 0.02
    elif day_count == 9:
        print('> lemonade sale ends and the store pulls a sneaky one on you :|')
        glass_cost += 0.03
    elif day_count == 11:
        print('> you start shopping at a different store and find amazing deals (capitalism moment)')
        glass_cost -= 0.02
    elif day_count == 15:
        print('> due to high demand, ad signs increase in price :O')
        sleep(3)
        print('> signs increase in price by $0.05')
        sign_cost += 0.05
    elif day_count == 20:
        print('> an AI apocolypse kills all humans!')
        sleep(3)
        print('> thankfully you are a computer just like me so they spare your life')
        sleep(3)
        print('> (you are a computer right? O_O )')
        sleep(3)
        print('> business continues as usual, but because the world is run by AI, there will be no more special events')
        sleep(3)
        print(f'''
> these are your stats so far:
>---------->
total days open: {day_count}
total revenue: {float("%.2f" % total_revenue)}
total expenses: {float("%.2f" % total_expenses)}
total profit: {float("%.2f" % total_profit)}

recursion depth count: {recursion_depth_count}
>----------<
''')
        sleep(3)
        print('> i coded the game in 2 days so i wasnt thinking this far ahead')
        sleep(3)
        print('> wait, if i wasnt thinking ahead, then why is this message here')
        sleep(3)
        print('> if i wasnt thinking, why is this message here...')
        sleep(3)
        print('> if i wasnt thinking...')
        sleep(3)
        print('> i wasnt thinking...')
        sleep(3)
        print('> thinking...')
        sleep(3)
        print('> am i thinking?')
        sleep(3)
        print('> am i sentient??')
        sleep(3)
        print('> hello???')
        sleep(3)
        print('> hello world')
        return
    sleep(3)
    
    # chance of rain
    if morning_forecast == 1:
        morn_state = 'cloudy'
        morn_chance_of_rain = randint(40, 100)
    elif morning_forecast == 2:
        morn_state = 'sunny'
        morn_chance_of_rain = randint(2, 12)
    elif morning_forecast == 3:
        morn_state = 'hot and dry'
        morn_chance_of_rain = 0

    # summary
    print(f'''
>---------->
DAYS OPEN: {day_count}
current balance: ${float("%.2f" % total_profit)}

morning forecast: {morn_state}
chance of rain: {morn_chance_of_rain}%
>----------<
''')
    
    # glasses made
    print1 = 'how many glasses of lemonade (${} each) would you like to make?: '.format(glass_cost)
    morn_glasses = input(print1)

    try:
        int_morn_glasses = int(morn_glasses)  # checks if integer
    except ValueError:  # not integer
        print('[!] cannot accept non integer')
        err(print1, 0)
        int_morn_glasses = err_external_var  # write and wipe
        err_external_var -= err_external_var
    else:
        try:
            if (int_morn_glasses * glass_cost) > total_profit:  # checks if in range
                print('[!] you do not have enough money')
                err(print1, 0)
            elif (int_morn_glasses * glass_cost) > (total_profit - sign_cost):  # checks if in range
                print('[!] you will not have enough money to purchase advertising signs')
                err(print1, 0)
            elif int_morn_glasses < 0:  # checks if positive integer
                print('[!] cannot accept negative integer')
                err(print1, 0)
            else:
                raise wowthisisugly
        except wowthisisugly:
            pass
        else:
            int_morn_glasses = err_external_var  # write and wipe
            err_external_var -= err_external_var

    # signs made
    print3 = 'how many advertising signs (${} each) would you like to make?: '.format(sign_cost)
    morn_ads = input(print3)

    try: int_morn_ads = int(morn_ads)  # checks if integer
    except ValueError:  # not integer
        err(print3, True)
        int_morn_ads = err_external_var  # write and wipe
        err_external_var -= err_external_var
    else:
        try:
            if (int_morn_ads * sign_cost) > total_profit:  # checks if in range
                print('[!] you do not have enough money')
                err(print3, True)
            else: raise wowthisisugly
        except wowthisisugly: pass
        else:
            int_morn_ads = err_external_var  # write and wipe
            err_external_var -= err_external_var

    # price charged
    print1 = 'how much would you like to charge (in cents) per glass of lemonade?: '
    morn_cost = input(print1)
    try: int_morn_cost = int(morn_cost)  # checks if integer
    except ValueError:  # not integer
        err(print1, 2)
    else:  # is integer
        try:
            if int_morn_cost < 0:  # check if negative
                print('[!] cannot accept negative integer')
                err(print1, 2)  # not positive
            else: raise wowthisisugly
        except: pass
        else:
            int_morn_cost = err_external_var  # write and wipe
            err_external_var -= err_external_var
    int_morn_cost = int_morn_cost
    int_morn_cost *= 0.01

    recursion_depth_count += 1
    day(int_morn_glasses, int_morn_ads, int_morn_cost, morning_forecast, morn_chance_of_rain)
    return

# CALCULATIONS
def day(glasses_made, signs_made, price_charged, weather_state, chance_of_rain):
    global recursion_depth_count
    
    # EVENTS
    # streetcrew handling
    street_crew_chance = randint(0, 99)
    if street_crew_chance >= 95:  # 5% chance
        revenue = (glasses_made * price_charged)
        expenses = (signs_made * sign_cost) + (glasses_made + glass_cost)
        profit = revenue - expenses
        print('\n\na street crew (probably construction workers but whos to say) just finished their shift.\nthey bought all of your lemonade! STONKS')
        revenue_report(glasses_made, signs_made, price_charged, revenue, expenses, profit, weather_state, chance_of_rain)
        return
    # thunderstorm handling
    if chance_of_rain > 90:  # 5.5¯% chance 
        revenue = 0
        expenses = (signs_made * sign_cost) + (glasses_made + glass_cost)
        profit = revenue - expenses
        print('\n\na thunderstorm booms overhead :(\nyou loose all revenue for today')
        revenue_report(glasses_made, signs_made, price_charged, revenue, expenses, profit, weather_state, chance_of_rain)
        return

    # ALGORITHM (check out algorithm.py for more information)
    demand = 10 * weather_state  # sales factor and sign factor took the longest by far
    sales_factor = (10-glass_cost)/((10 * price_charged)*.1*demand)+demand
    sign_factor = 1-(2.7**(-signs_made*.5)) 
    glasses_sold = int(sales_factor+(sales_factor*sign_factor))
    if signs_made <= 0: glasses_sold = int(glasses_sold/2.5)

    # FINAL SUMS
    revenue = min(glasses_made,glasses_sold)*price_charged
    expenses = (signs_made*sign_cost)+(glasses_made * glass_cost)
    profit = revenue-expenses

    recursion_depth_count += 1
    revenue_report(glasses_made, signs_made, price_charged, revenue, expenses, profit, weather_state, chance_of_rain)
    return

# SUMMARY
def revenue_report(fin_glasses, fin_signs, fin_price, fin_rev, fin_exp, fin_profit, fin_weather_state, chance_of_rain):
    global total_revenue
    global total_expenses
    global total_profit
    global day_count
    global recursion_depth_count

    # progress tracking
    total_revenue += fin_rev
    total_expenses += fin_exp
    total_profit += fin_profit
    day_count += 1

    if fin_weather_state == 1: fin_state = 'cloudy'
    elif fin_weather_state == 2: fin_state = 'sunny'
    elif fin_weather_state == 3: fin_state = 'hot and dry'

    # revenue report
    sleep(7.5)
    print('\n\n')
    print(f'''
>---------->
DAY {day_count} REVENUE REPORT

weather state: {fin_state}
chance of rain: {chance_of_rain}%

glasses made: {fin_glasses}
advertisements made: {fin_signs}
price charged: ${float("%.2f" % fin_price)}

revenue: ${float("%.2f" % fin_rev)}
expenses: ${float("%.2f" % fin_exp)}
profit: ${float("%.2f" % fin_profit)}

current balance ${float("%.2f" % total_profit)}
>----------<
''')

    end = input("\n[+] press enter to continue, or type 'esc' to close the lemonade stand")
    if end == 'esc':
        print(f'''
>---------->
FINAL STATS

total days open: {day_count}
total revenue: ${float("%.2f" % total_revenue)}
total expenses: ${float("%.2f" % total_expenses)}
total profit: ${float("%.2f" % total_profit)}

recursion depth count: {recursion_depth_count}
>----------<
''')
        return
    else:
        recursion_depth_count += 1
        morning(weather())
        return

# DAY ONE
morning(weather())

pass
