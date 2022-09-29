personal_data_dict={}
while True:
    key_name=input('What type of data do you want to save: ')
    value= input('Please enter the data value: ')
    personal_data_dict[key_name]= value
    for key, value in personal_data_dict.items():
        print(f'Your {key} is {value}')
    if input('Do you wanna exit?: \n Y-yes \n N-No\n')=='y':
       break 