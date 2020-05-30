print('Mix {}, {} and a {} to make an ideal omelet.'.format('2 eggs', '30 g of milk', 'pinch of salt'))
# Mix 2 eggs, 30 g of milk and a pinch of salt to make an ideal omelet.


print('{0} in the {1} by Frank Sinatra'.format('Strangers', 'Night'))
# Strangers in the Night by Frank Sinatra


print('{1} in the {0} by Frank Sinatra'.format('Strangers', 'Night'))
# Night in the Strangers by Frank Sinatra


print('The {film} at {theatre} was {adjective}!'.format(film='Lord of the Rings',
                                                        adjective='incredible',
                                                        theatre='BFI IMAX'))
# The Lord of the Rings at BFI IMAX was incredible!


print('The {0} was {adjective}!'.format('Lord of the Rings', adjective='incredible'))
# The Lord of the Rings was incredible!


print('The {0} was {adjective}!'.format(adjective='incredible', 'Lord of the Rings'))
# SyntaxError: positional argument follows keyword argument
