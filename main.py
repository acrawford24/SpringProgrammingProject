"""
Vacation Planner
Created By: Abbie, Cara, and Payton

We created a vacation planner. The program will ask the user multiple questions and the user needs to input one of the options given to them. By the end of the program the user will have a vacation planned for them. Then the user will have the option to paln another vacation if they would like. 

"""

#list for the user to choose the weather they want on their vacation 
weather_list = ["Sunny", "Snowing", "Rainy", "Tropical","Windy"]

#list for the location the user can pick from if they choose sunny as thier weather 
sunny_location_list = ["Orlando, Florida", "Austin, Texas","Los Angeles, California"]
#list for the hotels the user can pick from if they choose a location under sunny
sunny_hotel_list = ["Crowne Plaza Orlando", "Hyatt Regency Orlando", "Hilton Orlando","JW Marriott Austin", "The Westin Austin Downtown", "Hilton Garden Inn Cedar Park Austin","Millennium Biltmore Hotel Los Angeles", "The Wayfarer Downtown Los Angeles", "Freehand Los Angeles"]
#the prices in the same order as the hotels, to let the user know the price per night of the hotel 
sunny_hotel_prices_list = ["$83", "$135", "$171", "$294", "$167", "$96", "$160", "$103", "$70"]
#the activities the user can pick from if they choose a location under tropical
sunny_activity_list = ["Walt Disney World","Gatorland","Wonderworks","McKinney Falls State Park", "Austin Zoo", "Cathedral of Junk","Universal Studios-Hollywood","Dodgers Game", "Hollywood Sign Hike"]
#Prices for sunny activity admissons in order with the activities
sunny_activity_prices_list = ["$109", "$30", "$35", "$6", "$15", "$5", "$119", "$88", "$0"]

#list for the location the user can pick from if they choose snowy as thier weather 
snowing_location_list = ["Juneau, Alaska", "Boulder, Colorado", "Cleveland, Ohio"]
#list for the hotels the user can pick from if they choose a location under snowing
snowing_hotel_list = ["Four Points by Sheraton Juneau", "Silverbow Inn Hotel & Suites", "Aspen Suites Hotel Juneau","Boulder Marriott", "St.Julien Hotel & Spa", "Residence Inn by Marriott Boulder Canyon Boulevard","The Westin Downtown Cleveland", "Metropolitan at the 9", "Rennisance Cleveland Hotel"]
#the prices in the same order as the hotels, to let the user know the price per night of the hotel 
snowing_hotel_prices_list = ["$239", "$179", "$144", "$140", "$289", "$174", "$89", "$229", "$229"]
#the activities the user can pick from if they choose a location under tropical
snowing_activity_list = ["Patsy Ann Statue", "Goldbelt Tram ", "Juneau Wildlife Whale Watching & Mendenhall Glacier", "Flagstaff Mountain", "Flatirons", "Royal Arch Trail", "Rock and Roll Hall of Fame", "West Side Market", "A Christmas Story House"]
#Prices for snowy activity admissons in order with the activities
snowing_activity_prices_list = ["$0", "$33", "$157", "$0", "$0", "$0", "$28", "$0", "$15"]

#list for the location the user can pick from if they choose rainy as thier weather 
rainy_location_list = ["Seattle, Washington","New Orleans, Lousianna","Pittsburgh, Pennsylvania"]
#list for the hotels the user can pick from if they choose a location under sunny
rainy_hotel_list = ["Hyatt House Seattle/Downtown", "Warwick Seattle","The Paramount Hotel","St. James Hotel New Orleans Downtown","Embassy Suites by Hilton New Orleans", "Hampton Inn & Suites New Orleans Downtown","DoubleTree by Hilton Hotel & Suites Pittsburgh Downtown", "Fairmont Pittsburgh", "Kimpton Hotel Monaco Pittsburgh"]
#the prices in the same order as the hotels, to let the user know the price per night of the hotel 
rainy_hotel_prices_list = ["$134", "$89", "$122", "$99", "$96", "$94", "$146", "$200", "$178"]
#the activities the user can pick from if they choose a location under tropical
rainy_activity_list = ["Pike Place Market","Space Needle","The Gum Wall","The National World War II Museum","Mardi Gras World","Bourbon Street","Point State Park","Carnegie Science Center","The Andy Warhol Museum"]
#Prices for rainy activity admissons in order with the activities
rainy_activity_prices_list = ["$0", "$35", "0", "$29", "$22", "$0", "$0", "$20", "$20"]

#list for the location the user can pick from if they choose tropical as thier weather 
tropical_location_list = ["Honolulu, Hawaii", "Puerto Rico", "Key West, Florida"]
#list for the hotels the user can pick from if they choose a location under tropical
tropical_hotel_list = ["Hilton Hawaiian Village Waikiki Beach Resort", "Prince Waikiki - Honolulu Luxury Hotel", "Hotel Renew", "The St. Regis Bahia Beach Resort, Puerto Rico", "San Juan Water and Beach Club Hotel", "Dorado Beach, a Ritz-Carlton Reserve", "DoubleTree Resort by Hilton Hotel Grand Key - Key West", "Courtyard by Marriott Key West Waterfront", "Hyatt Residence Club Key West, Windward Pointe"]
#the prices in the same order as the hotels, to let the user know the price per night of the hotel 
tropical_hotel_prices_list = ["$230", "$251", "$116", "$971", "$139", "$1891", "$489", "$825", "$459"]
#the activities the user can pick from if they choose a location under tropical
tropical_activity_list = ["Diamond Head", "Pearl Harbor National Memorial", "Manoa Falls", "Bahía Bioluminiscente", "Castillo San Felipe del Morro", "La Fortaleza", "Southernmost Point of the Continental US", "Mallory Square", "Dog Beach"]
##Prices for tropical activity admissons in order with the activities
tropical_activity_prices_list = ["$4", "$0", "$0", "$0", "$10", "$0", "$0", "$0", "$0"]

#list for the location the user can pick from if they choose windy as their weather 
windy_location_list = ["Chicago, Illinois","Amarillo, Texas","Salt Lake City, Utah"]
#list for the hotels the user can pick from if they choose a location under windy
windy_hotel_list = ["Virgin Hotel Chicago", "The Ritz-Carlton-Chicago", "Hampton Inn Chicago Downtown","Hyatt Place Amarillo - West", "Courtyard by Marriott Amarillo Downtown", "SpringHill Suites by Marriott Amarillo","The Grand America Hotel" , "Salt Lake City Marriott City Center" , "Salt Lake Plaza Hotel at Temple Square" ]
#the prices in the same order as the hotels, to let the user know the price per night of the hotel 
windy_hotel_prices_list = ["$121","$399","$98","$109","$124","$129","$227","$179","$66"]
#the activities the user can pick from if they choose a location under windy
windy_activity_list = ["Gangsters and Ghosts Tour","Chicago Lake and River Architecture Tour","The Chi-Town Showdown Scavenger Hunt","Cowgirls and Cowboys in the West","Don Harrington Discovery Center","Wonderland Amusement Park","Salt Lake Plaza Hotel at Temple Square","Lake Blanche Trail","Eccles Theater- Disney's Frozen"]
##Prices for tropical activity admissons in order with the activities
windy_activity_prices_list = ["$27","$40","$18","$69","$14","$27","$0","$0","$140"]


vacation = input("Do you want to take a vacation? ").lower()
#If the user inputs no the program will keep re-asking untill yes is input. 
while vacation == "no":
  vacation = input("Do you want to take a vacation? ").lower()

"""

This function is the main function of our program where the user is asked all of the vactaion details, and then their input is stored to be used later. Then the user has the chance to re-run this function which would plan another vacation.

"""
def vacation_planner():
 
#Prints weather options and asks which one the user wants
  if vacation == "yes":
    print("\n" + weather_list[0] +"\n" + weather_list[1]+ "\n" + weather_list[2]+ "\n"+ weather_list[3]+"\n"+ weather_list[4]+"\n") 
    weather_choices = input("Out of the choices above, what weather would you prefer for your vacation?\n")

#Sunny location stuff; Asks the user which sunny location they would like.
  if weather_choices == weather_list[0]:
    print("\n"+ sunny_location_list[0]+"\n"+sunny_location_list[1]+"\n"+sunny_location_list[2]+"\n")
    location_question = input("Out of the list above, which location would you prefer? ")
#Orlando hotel stuff; Asks the user which hotel they would like if they chose Orlando as their vacation destination.
    if location_question == sunny_location_list[0]:
      print("\n"+sunny_hotel_list[0] + "\n" + sunny_hotel_list[1] + "\n" + sunny_hotel_list[2]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
      if hotel_question=="Crowne Plaza Orlando":
        print("\n$83 a night")
      elif hotel_question=="Hyatt Regency Orlando":
        print("\n$135 a night")
      else:
        print("\n$171 a night")
#Orlando activity stuff; Asks the user which activity they would like and outputs the price of the chosen activity if they chose Orlando as their vacation destination.
      if hotel_question in sunny_hotel_list:
        print("\n"+sunny_activity_list[0] + "\n" + sunny_activity_list[1] + "\n" + sunny_activity_list[2]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
        if activity_question=="Walt Disney World":
          print("\n$109 a ticket")
        elif activity_question=="Gatorland":
          print("\n$30 a ticket")
        else:
          print("\n$35 a ticket")
        activity_loop_question = input("Would you like to pick another activity? ").lower()
#Final trip; Outputs the users final trip choices which includes weather, location, hotel, and activity. 
        final_trip = [weather_choices, location_question, hotel_question, activity_question, activity_question2]
        print("\nYour vacation plan is:\n"+ final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])

#Austin hotel stuff; Asks the user which hotel they would like if they chose Austin as their vacation destination.
    elif location_question == sunny_location_list[1]:
      print("\n"+sunny_hotel_list[3] + "\n" + sunny_hotel_list[4] + "\n" + sunny_hotel_list[5]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
      if hotel_question=="JW Marriott Austin":
        print("\n$294 a night")
      elif hotel_question=="The Westin Austin Downtown":
        print("\n$167 a night")
      else:
        print("\n$96 a night")
#Austin activity stuff;Asks the user which activity they would like and outputs the price of the chosen activity if they chose Austin as their vacation destination.
      if hotel_question in sunny_hotel_list:
        print("\n"+sunny_activity_list[3] + "\n" + sunny_activity_list[4] + "\n" + sunny_activity_list[5]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
        if activity_question=="McKinney Falls State Park":
          print("\n$6 a ticket")
        elif activity_question=="Austin Zoo":
          print("\n$15 a ticket")
        else:
          print("\n$5 a ticket")
#Final trip;Outputs the users final trip choices which includes weather, location, hotel, and activity. 
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is:\n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])

#Los Angeles hotel stuff;Asks the user which hotel they would like if they chose Los Angeles as their vacation destination.
    elif location_question == sunny_location_list[2]:
      print("\n"+sunny_hotel_list[6] + "\n" + sunny_hotel_list[7] + "\n" + sunny_hotel_list[8]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
      if hotel_question=="Millennium Biltmore Hotel Los Angeles":
        print("\n$160 a night")
      elif hotel_question=="The Wayfarer Downtown Los Angeles":
        print("\n$103 a night")
      else:
        print("\n$70 a night")
#Los Angeles activity stuff;Asks the user which activity they would like and outputs the price of the chosen activity if they chose Los Angeles as their vacation destination.
      if hotel_question in sunny_hotel_list:
        print("\n"+sunny_activity_list[6] + "\n" + sunny_activity_list[7] + "\n" + sunny_activity_list[8]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? \n")
        if activity_question=="Universal Studios-Hollywood":
          print("\n$119 a ticket")
        elif activity_question=="Dodgers Game":
          print("\n$88 a ticket")
        else:
          print("\n$0 a ticket")
#Final trip; Outputs the users final trip choices which includes weather, location, hotel, and activity. 
        final_trip = [weather_choices, location_question, hotel_question, activity_question] 
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])

#Snowing location stuff; Asks the user which snowing location they would like.
  elif weather_choices == weather_list[1]:
    print("\n"+snowing_location_list[0]+"\n"+snowing_location_list[1]+"\n"+snowing_location_list[2]+"\n")
    location_question = input("Out of the list above, which location would you prefer? ")
#Juneau hotel stuff; Asks the user which hotel they would like if they chose Juneau as their vacation destination.
    if location_question == snowing_location_list[0]:
      print("\n"+snowing_hotel_list[0] + "\n" + snowing_hotel_list[1] + "\n" + snowing_hotel_list[2]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
      if hotel_question=="Four Points by Sheraton Juneau":
        print("\n$239 a night")
      elif hotel_question=="Silverbow Inn Hotel & Suites":
        print("\n$179 a night")
      else:
        print("\n$144 a night")
#Juneau activity stuff; Asks the user which activity they would like and outputs the price of the chosen activity if they chose Juneau as their vacation destination.
      if hotel_question in snowing_hotel_list:
        print("\n"+snowing_activity_list[0] + "\n" + snowing_activity_list[1] + "\n" + snowing_activity_list[2]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
        if activity_question=="Patsy Ann Statue":
          print("\n$0 a ticket")
        elif activity_question=="Goldbelt Tram":
          print("\n$33 a ticket")
        else:
          print("\n$157 a ticket")
#Final trip; Outputs the users final trip choices which includes weather, location, hotel, and activity.
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])

#Boulder hotel stuff; Asks the user which hotel they would like if they chose Boulder as their vacation destination.
    elif location_question == snowing_location_list[1]:
      print("\n"+snowing_hotel_list[3] + "\n "+ snowing_hotel_list[4] + "\n" + snowing_hotel_list[5]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
      if hotel_question=="Boulder Marriott":
        print("\n$140 a night")
      elif hotel_question=="St.Julien Hotel & Spa":
        print("\n$289 a night")
      else:
        print("\n$174 a night")
#Boulder activity stuff; Asks the user which activity they would like and outputs the price of the chosen activity if they chose Boulder as their vacation destination.
      if hotel_question in snowing_hotel_list:
        print("\n"+snowing_activity_list[3] + "\n" + snowing_activity_list[4] + "\n" + snowing_activity_list[5]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
        if activity_question=="Flagstaff Mountain":
          print("\n$0 a ticket")
        elif activity_question=="Flatirons":
          print("\n$0 a ticket")
        else:
          print("\n$0 a ticket")
#Final trip;Outputs the users final trip choices which includes weather, location, hotel, and activity. 
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])

#Cleveland hotel stuff; Asks the user which hotel they would like if they chose Cleveland as their vacation destination.
    elif location_question == snowing_location_list[2]:
      print("\n"+snowing_hotel_list[6] + "\n" + snowing_hotel_list[7] + "\n" + snowing_hotel_list[8]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
      if hotel_question=="The Westin Downtown Cleveland":
        print("\n$89 a night")
      elif hotel_question=="Metropolitan at the 9":
        print("\n$229 a night")
      else:
        print("\n$229 a night")
#Cleveland activity stuff; Asks the user which activity they would like and outputs the price of the chosen activity if they chose Cleveland as their vacation destination.
      if hotel_question in snowing_hotel_list:
        print("\n"+snowing_activity_list[6] + "\n" + snowing_activity_list[7] + "\n" + snowing_activity_list[8]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
        if activity_question=="Rock and Roll Hall of Fame":
          print("\n$28 a ticket")
        elif activity_question=="West Side Market":
          print("\n$0 a ticket")
        else:
          print("\n$15 a ticket")
#Final trip;Outputs the users final trip choices which includes weather, location, hotel, and activity. 
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])

#Rainy location stuff; Asks the user which rainy location they would like
  elif weather_choices == weather_list[2]:
    print("\n"+ rainy_location_list[0] + "\n"+ rainy_location_list[1]+ "\n"+ rainy_location_list[2]+"\n")
    location_question = input("Out of the list above, which location would you prefer? ")
#Seattle hotel stuff; Asks the user which hotel they would like if they chose Seattle as their vacation destination.
    if location_question == rainy_location_list[0]:
      print("\n"+rainy_hotel_list[0] + "\n" + rainy_hotel_list[1] + "\n" + rainy_hotel_list[2]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
      if hotel_question=="Hyatt House Seattle/Downtown":
        print("\n$134 a night")
      elif hotel_question=="Warwick Seattle":
        print("\n$89 a night")
      else:
        print("\n$122 a night")
#Seattle activity stuff; Asks the user which activity they would like and outputs the price of the chosen activity if they chose Seattle as their vacation destination.
      if hotel_question in rainy_hotel_list:
        print("\n"+rainy_activity_list[0] + "\n" + rainy_activity_list[1] + "\n" + rainy_activity_list[2]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
        if activity_question=="Pike Place Market":
          print("\n$0 a ticket")
        elif activity_question=="Space Needle":
          print("\n$35 a ticket")
        else:
          print("\n$0 a ticket")
#Final trip;Outputs the users final trip choices which includes weather, location, hotel, and activity. 
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3]) 

#New Orleans hotel stuff; Asks the user which hotel they would like if they chose New Orleans as their vacation destination.
    elif location_question == rainy_location_list[1]:
      print("\n"+rainy_hotel_list[3] + "\n"+ rainy_hotel_list[4] + "\n" + rainy_hotel_list[5]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
      if hotel_question=="St. James Hotel New Orleans Downtown":
        print("\n$99 a night")
      elif hotel_question=="Embassy Suites by Hilton New Orleans":
        print("\n$96 a night")
      else:
        print("\n$94 a night")
#New Orleans activity stuff; Asks the user which activity they would like and outputs the price of the chosen activity if they chose New Orleans as their vacation destination.
      if hotel_question in rainy_hotel_list:
        print("\n"+rainy_activity_list[3] + "\n" + rainy_activity_list[4] + "\n" + rainy_activity_list[5]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
        if activity_question=="The National World War II Museum":
          print("\n$29 a ticket")
        elif activity_question=="Mardi Gras World":
          print("\n$22 a ticket")
        else:
          print("\n$0 a ticket")
#Final trip;Outputs the users final trip choices which includes weather, location, hotel, and activity. 
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])

#Pittsburgh hotel stuff; Asks the user which hotel they would like if they chose Pittsburgh as their vacation destination. 
    elif location_question == rainy_location_list[2]:
      print("\n"+rainy_hotel_list[6] + "\n" + rainy_hotel_list[7] + "\n" + rainy_hotel_list[8]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
      if hotel_question=="DoubleTree by Hilton Hotel & Suites Pittsburgh Downtown":
        print("\n$146 a night")
      elif hotel_question=="Fairmont Pittsburgh":
        print("\n$200 a night")
      else:
        print("\n$178 a night")
#Pittsburgh activity stuff; Asks the user which activity they would like and outputs the price of the chosen activity if they chose Pittsburgh as their vacation destination.
      if hotel_question in rainy_hotel_list:
        print("\n"+rainy_activity_list[6] + "\n" + rainy_activity_list[7] + "\n" + rainy_activity_list[8]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
        if activity_question=="Point State Park":
          print("\n$0 a ticket")
        elif activity_question=="Carnegie Science Center":
          print("\n$20 a ticket")
        else:
          print("\n$20 a ticket")
#Final trip;Outputs the users final trip choices which includes weather, location, hotel, and activity. 
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])

#Tropical location stuff; Asks the user which tropical location they would like
  elif weather_choices == weather_list[3]:
    print("\n"+ tropical_location_list[0] + "\n"+ tropical_location_list[1]+ "\n"+ tropical_location_list[2]+"\n")
    location_question = input("Out of the list above, which location would you prefer? ")
#Honolulu hotel stuff; Asks the user which hotel they would like if they chose Honolulu as their vacation destination.
    if location_question == tropical_location_list[0]:
      print("\n"+tropical_hotel_list[0] + "\n" + tropical_hotel_list[1] + "\n" + tropical_hotel_list[2]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
      if hotel_question=="Hilton Hawaiian Village Waikiki Beach Resort":
        print("\n$230 a night")
      elif hotel_question=="Prince Waikiki- Honolulu Luxery Hotel":
        print("\n$251 a night")
      else:
        print("\n$116 a night")
#Honolulu activity stuff; Asks the user which activity they would like and outputs the price of the chosen activity if they chose Honolulu as their vacation destination.
      if hotel_question in tropical_hotel_list:
        print("\n"+tropical_activity_list[0] + "\n" + tropical_activity_list[1] + "\n" + tropical_activity_list[2]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
        if activity_question=="Diamond Head":
          print("\n$4 a ticket")
        elif activity_question=="Pearl Harbor National Memorial":
          print("\n$0 a ticket")
        else:
          print("\n$0 a ticket")
#Final trip;Outputs the users final trip choices which includes weather, location, hotel, and activity. 
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3]) 

#Puerto Rico hotel stuff; Asks the user which hotel they would like if they chose Puerto Rico as their vacation destination.
    elif location_question == tropical_location_list[1]:
      print("\n"+tropical_hotel_list[3] + "\n"+ tropical_hotel_list[4] + "\n" + tropical_hotel_list[5]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
      if hotel_question=="The St. Regis Bahia Beach Resort":
        print("\n$971 a night")
      elif hotel_question=="San Juan Water and Beach Club Hotel":
        print("\n$139 a night")
      else:
        print("\n$1891 a night")
#Puerto Rico activity stuff; Asks the user which activity they would like and outputs the price of the chosen activity if they chose Puerto Rico as their vacation destination.
      if hotel_question in tropical_hotel_list:
        print("\n"+tropical_activity_list[3] + "\n" + tropical_activity_list[4] + "\n" + tropical_activity_list[5]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
        if activity_question=="La Fortaleza":
          print("\n$0 a ticket")
        elif activity_question=="Castillo San Felipe del Morro":
          print("\n$10 a ticket")
        else:
          print("\n$0 a ticket")
#Final trip;Outputs the users final trip choices which includes weather, location, hotel, and activity. 
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])

#Key West hotel stuff; Asks the user which hotel they would like if they chose Key West as their vacation destination.
    elif location_question == tropical_location_list[2]:
      print("\n"+tropical_hotel_list[6] + "\n" + tropical_hotel_list[7] + "\n" + tropical_hotel_list[8]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ") 
      if hotel_question=="DoubleTree Resort by Hilton Hotel Grand Key - Key West ":
        print("\n$489 a night")
      elif hotel_question=="Courtyard by Marriott Key West Waterfront":
        print("\n$825 a night")
      else:
        print("\n$459 a night")
#Key West activity stuff; Asks the user which activity they would like and outputs the price of the chosen activity if they chose Key West as their vacation destination.
      if hotel_question in tropical_hotel_list:
        print("\n"+tropical_activity_list[6] + "\n" + tropical_activity_list[7] + "\n" + tropical_activity_list[8]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
        if activity_question=="Mallory Square":
          print("\n$0 a ticket")
        elif activity_question=="Southernmost Point of the Continental US":
          print("\n$0 a ticket")
        else:
          print("\n$0 a ticket")


#Windy location stuff; Asks the user which windy location they would like.
  if weather_choices == weather_list[3]:
    print("\n"+ windy_location_list[0]+"\n"+windy_location_list[1]+"\n"+windy_location_list[2]+"\n")
    location_question = input("Out of the list above, which location would you prefer? ")
#Chicago hotel stuff; Asks the user which hotel they would like if they chose Chicago as their vacation destination.
    if location_question == windy_location_list[0]:
      print("\n"+windy_hotel_list[0] + "\n" + windy_hotel_list[1] + "\n" + windy_hotel_list[2]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
      if hotel_question=="Virgin Hotel Chicago":
        print("\n$121 a night")
      elif hotel_question=="The Ritz-Carlton-Chicago":
        print("\n$399 a night")
      else:
        print("\n$98 a night")
#Chicago activity stuff; Asks the user which activity they would like and outputs the price of the chosen activity if they chose Chicago as their vacation destination.
      if hotel_question in windy_hotel_list:
        print("\n"+windy_activity_list[0] + "\n" + windy_activity_list[1] + "\n" + windy_activity_list[2]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
        if activity_question=="Gangsters and Ghosts Tour":
          print("\n$27 a ticket")
        elif activity_question=="Chicago Lake and River Architecture Tour":
          print("\n$40 a ticket")
        else:
          print("\n$18 a ticket")
#Final trip; Outputs the users final trip choices which includes weather, location, hotel, and activity. 
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is:\n"+ final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])

#Amarillo hotel stuff; Asks the user which hotel they would like if they chose Amarillo as their vacation destination.
    elif location_question == sunny_location_list[1]:
      print("\n"+windy_hotel_list[3] + "\n" + windy_hotel_list[4] + "\n" + windy_hotel_list[5]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
      if hotel_question=="Hyatt Place Amarillo - West":
        print("\n$109 a night")
      elif hotel_question=="Courtyard by Marriott Amarillo Downtown":
        print("\n$124 a night")
      else:
        print("\n$129 a night")
#Amarillo activity stuff;Asks the user which activity they would like and outputs the price of the chosen activity if they chose Amarillo as their vacation destination.
      if hotel_question in windy_hotel_list:
        print("\n"+windy_activity_list[3] + "\n" + windy_activity_list[4] + "\n" + windy_activity_list[5]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
        if activity_question=="Cowgirls and Cowboys in the West":
          print("\n$69 a ticket")
        elif activity_question=="Austin Zoo":
          print("\n$15 a ticket")
        else:
          print("\n$5 a ticket")
#Final trip;Outputs the users final trip choices which includes weather, location, hotel, and activity. 
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is:\n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])

#Los Angeles hotel stuff;Asks the user which hotel they would like if they chose Los Angeles as their vacation destination.
    elif location_question == sunny_location_list[2]:
      print("\n"+sunny_hotel_list[6] + "\n" + sunny_hotel_list[7] + "\n" + sunny_hotel_list[8]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
      if hotel_question=="Millennium Biltmore Hotel Los Angeles":
        print("\n$160 a night")
      elif hotel_question=="The Wayfarer Downtown Los Angeles":
        print("\n$103 a night")
      else:
        print("\n$70 a night")
#Los Angeles activity stuff;Asks the user which activity they would like and outputs the price of the chosen activity if they chose Los Angeles as their vacation destination.
      if hotel_question in sunny_hotel_list:
        print("\n"+sunny_activity_list[6] + "\n" + sunny_activity_list[7] + "\n" + sunny_activity_list[8]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? \n")
        if activity_question=="Universal Studios-Hollywood":
          print("\n$119 a ticket")
        elif activity_question=="Dodgers Game":
          print("\n$88 a ticket")
        else:
          print("\n$0 a ticket")
#Final trip; Outputs the users final trip choices which includes weather, location, hotel, and activity. 
        final_trip = [weather_choices, location_question, hotel_question, activity_question] 
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])
  
#Final trip;Outputs the users final trip choices which includes weather, location, hotel, and activity. 
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])

#Calls the vacation planner function
vacation_planner()
another_vacation = input("\nWould you like to plan another vacation? ").lower()
#Continues to plan another vaction if the user inputs yes when asked if they would like to plan another vacation
while another_vacation == "yes":
  vacation_planner()
  another_vacation = input("\nWould you like to plan another vacation? ").lower()