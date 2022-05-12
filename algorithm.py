# .wncry
# licensed under GNU GPLv2.0

# INPUT
glasses_made = 115
signs_made = 5
price_charged = 0.20

glass_cost = 0.02  # preset cost for making lemonade per cup
sign_cost = 0.15  # preset cost for creating signs per sign

weather_state = 30

# ALGORITHM (i may have easily spent 7 hours working on this lol)
demand = 10 * weather_state  # demand fluctuates based on weather
sales_factor = (10-glass_cost)/((10 * price_charged)*.1*demand)+demand  # sales factor equasion
sign_factor = 1-(2.7**(-signs_made*.5))  # sigmoid function (kinda)
glasses_sold = int(sales_factor+(sales_factor*sign_factor))  # factor application
if signs_made <= 0: glasses_sold = int(glasses_sold/2.5)  # lack of signs directly influence sales

# OUTPUT
revenue = float("%.2f" % (min(glasses_made, glasses_sold) * price_charged))  # you can only sell as many cups as you have
expenses = float("%.2f" % ((signs_made * sign_cost) + (glasses_made * glass_cost)))  # expense calculation
profit = float("%.2f" % (revenue - expenses))  # im sure you can figure this one out :)

print(f'''
demand: {demand}
sales factor: {sales_factor}
sign factor: {sign_factor}
glasses sold: {glasses_sold}

revenue: ${revenue}
expenses: ${expenses}
profit: ${profit}
''')
