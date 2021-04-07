bill = float(input('Total bill amount?    '))
print('What was the level of service?')
service = input('good, fair, or bad:   ')
split = int(input('Split how many ways?   '))



if (service == 'good'):
    tip = 0.20*bill
    total = bill + tip


if (service == 'fair'):
    tip = 0.15*bill
    total = bill + tip


if (service == 'bad'):
    tip = 0.10*bill
    total = bill + tip



print('The bill was $',bill)
print('The service was',service)
print('The tip should be $',tip)
print('The grand total with the tip is $',total)
print('The amount per person is $', total/split)