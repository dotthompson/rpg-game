bill = float(input('Total bill amount?    '))
print('What was the level of service?')
service = input('good, fair, or bad:   ')



if (service == 'good'):
    tip = 0.20*bill
    total = bill + tip
#yoyoyo

if (service == 'fair'):
    tip = 0.15*bill
    total = bill + tip

# hey
if (service == 'bad'):
    tip = 0.10*bill
    total = bill + tip

#hey

print('The bill was $',bill)
print('The service was',service)
print('The tip should be',tip)
print('The grand total with the tip is $',total)

