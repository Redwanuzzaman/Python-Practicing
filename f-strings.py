name = 'Elizabeth II'
title = 'Queen of the United Kingdom and the other Commonwealth realms'
reign = 'the longest-lived and longest-reigning British monarch'

f'{name}, the {title}, is {reign}.'
# Elizabeth II, the Queen of the United Kingdom and the other Commonwealth realms, is the longest-lived and longest-reigning British monarch.


hundred_percent_number = 1823
needed_percent = 16
needed_percent_number = hundred_percent_number * needed_percent / 100
 
print(f'{needed_percent}% from {hundred_percent_number} is {needed_percent_number}')
# 16% from 1823 is 291.68
 
print(f'Rounding {needed_percent_number} to 1 decimal place is {needed_percent_number:.1f}')
# Rounding 291.68 to 1 decimal place is 291.7


'{} divided by {} equals {:.5f}'.format(100, 6, 100/6) 
# 100 divided by 6 equals 16.66667
