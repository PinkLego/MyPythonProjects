Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> fred = 100
>>> print(fred)
100
>>> fred = 200
>>> print(fred)
200
>>> fred = 200
>>> john = fred
>>> print(john)
200
>>> number_of_coins = 200
>>> print(number_of_coins)
200
>>> found_coin = 20
>>> magic_coins = 10
>>> stolen_coins = 3
>>> found_coins + magic_coins * 365 - stolen_coins * 52
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    found_coins + magic_coins * 365 - stolen_coins * 52
NameError: name 'found_coins' is not defined
>>> found_coin + magic_coins * 365 - stolen_coins * 52
3514
>>> stolen_coins = 2
>>> found_coin + magic_coins * 365 - stolen_coins * 52
3566
>>> 
