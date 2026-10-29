import pandas as pd 
df = pd.read_csv("Data.csv")
row = len(df)

count_yes = ((df.PlayCricket == 'Yes').sum())
count_no = ((df.PlayCricket == 'No').sum())

prob_yes = count_yes / row
prob_no = count_no / row

print(f"Total rows recorded: {row}")
print(f"Probability of Yes: {prob_yes}")
print(f"Probability of No: {prob_no}") 
                          #Outlook
print()
print("                    OUTLOOK        ")
#Probability of Outlook given yes
prob_overcast = ((df.Outlook == 'Overcast') & (df.PlayCricket == 'Yes')).sum()
prob_sunny = ((df.Outlook == 'Sunny') & (df.PlayCricket == 'Yes')).sum()
prob_rainy = ((df.Outlook == 'Rainy') & (df.PlayCricket == 'Yes')).sum()

print(f"Probability of Overcast given Yes: {prob_overcast / count_yes}")
print(f"Probability of Sunny given Yes: {prob_sunny / count_yes}")
print(f"Probability of Rainy given Yes: {prob_rainy / count_yes}")

#Probability of Outlook given no
prob_overcast = ((df.Outlook == 'Overcast') & (df.PlayCricket == 'No')).sum()
prob_sunny = ((df.Outlook == 'Sunny') & (df.PlayCricket == 'No')).sum()
prob_rainy = ((df.Outlook == 'Rainy') & (df.PlayCricket == 'No')).sum()
print()
print(f"Probability of Overcast given No: {prob_overcast / count_no}")
print(f"Probability of Sunny given No: {prob_sunny / count_no}")
print(f"Probability of Rainy given No: {prob_rainy / count_no}")

                     #Temperature
print()
print("                    TEMPERATURE        ")
#Probability of Temperature given yes
prob_hot = ((df.Temperature == 'Hot') & (df.PlayCricket == 'Yes')).sum()
prob_mild = ((df.Temperature == 'Mild') & (df.PlayCricket == 'Yes')).sum()
prob_cool = ((df.Temperature == 'Cool') & (df.PlayCricket == 'Yes')).sum()

print(f"Probability of Hot given Yes: {prob_hot / count_yes}")
print(f"Probability of Mild given Yes: {prob_mild / count_yes}")
print(f"Probability of Cool given Yes: {prob_cool / count_yes}")

#Probability of Temperature given no
prob_hot = ((df.Temperature == 'Hot') & (df.PlayCricket == 'No')).sum()
prob_mild = ((df.Temperature == 'Mild') & (df.PlayCricket == 'No')).sum()
prob_cool = ((df.Temperature == 'Cool') & (df.PlayCricket == 'No')).sum()
print()
print(f"Probability of Hot given No: {prob_hot / count_no}")
print(f"Probability of Mild given No: {prob_mild / count_no}")
print(f"Probability of Cool given No: {prob_cool / count_no}")
prob_rainy = ((df.Outlook == 'Rainy') & (df.PlayCricket == 'No')).sum()

                        #Humidity
print()
print("                    HUMIDITY        ")
#Probability of Humidity given yes
prob_high = ((df.Humidity == 'High') & (df.PlayCricket == 'Yes')).sum()
prob_normal = ((df.Humidity == 'Normal') & (df.PlayCricket == 'Yes')).sum()

print(f"Probability of High given Yes: {prob_high / count_yes}")
print(f"Probability of Normal given Yes: {prob_normal / count_yes}")

#Probability of Humidity given no
prob_high = ((df.Humidity == 'High') & (df.PlayCricket == 'No')).sum()
prob_normal = ((df.Humidity == 'Normal') & (df.PlayCricket == 'No')).sum()
print()
print(f"Probability of High given No: {prob_high / count_no}")
print(f"Probability of Normal given No: {prob_normal / count_no}")

                         #Windy
print()
print("                    WINDY        ")
#Probability of Windy given yes
prob_true = ((df.Wind == 'Strong') & (df.PlayCricket == 'Yes')).sum()
prob_false = ((df.Wind == 'Weak') & (df.PlayCricket == 'Yes')).sum()

print(f"Probability of Strong given Yes: {prob_true / count_yes}")
print(f"Probability of Weak given Yes: {prob_false / count_yes}")

#Probability of Windy given no
prob_true = ((df.Wind == 'Strong') & (df.PlayCricket == 'No')).sum()
prob_false = ((df.Wind == 'Weak') & (df.PlayCricket == 'No')).sum()
print()
print(f"Probability of Strong given No: {prob_true / count_no}")
print(f"Probability of Weak given No: {prob_false / count_no}")

#New condition to predict
Outlook = 'Sunny'
Temperature = 'Cool'
Humidity = 'High'
Wind = 'Strong'

yes = prob_yes * (prob_sunny / count_yes) * (prob_cool / count_yes) * (prob_high / count_yes) * (prob_true / count_yes)
no = prob_no * (prob_sunny / count_no) * (prob_cool / count_no) * (prob_high / count_no) * (prob_true / count_no)

print(f"Score of Yes: {yes}")
print(f"Score of No: {no}")

if yes > no:
    print("The prediction is Yes, Play Cricket")
else:
    print("The prediction is No, Don't Play Cricket")