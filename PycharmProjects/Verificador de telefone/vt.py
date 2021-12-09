import phonenumbers

from phonenumbers import geocoder

phone = input('Digite o telefone no formato: +258845323056: ')

phone_numbers = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_numbers, 'pt'))
