"""
Vacation Planner
Created By: Abbie, Cara, and Payton

We created a vacation planner. The program will ask the user multiple questions and the user needs to input one of the options given to them. By the end of the program the user will have a vacation planned for them. Then the user will have the option to paln another vacation if they would like. 

"""

#list for the user to choose the weather they want on their vacation 
weather_list = ["Sunny", "Snowing", "Rainy", "Tropical"]

#list for the location the user can pick from if they choose sunny as thier weather 
sunny_location_list = ["Orlando, Florida", "Austin, Texas","Los Angeles, California"]
#list for the location the user can pick from if they choose sunny as thier weather 
sunny_hotel_list = ["Crowne Plaza Orlando", "Hyatt Regency Orlando", "Hilton Orlando","JW Marriott Austin", "The Westin Austin Downtown", "Hilton Garden Inn Cedar Park Austin","Millennium Biltmore Hotel Los Angeles", "The Wayfarer Downtown Los Angeles", "Freehand Los Angeles"]
#Prices per night for sunny hotel options
sunny_hotel_prices_list = ["$83", "$135", "$171", "$294", "$167", "$96", "$160", "$103", "$70"]
#Activity options for sunny weather
sunny_activity_list = ["Walt Disney World","Gatorland","Wonderworks","McKinney Falls State Park", "Austin Zoo", "Cathedral of Junk","Universal Studios-Hollywood","Dodgers Game", "Hollywood Sign Hike"]
#Prices for activity admissons under sunny options
sunny_activity_prices_list = ["$109", "$30", "$35", "$6", "$15", "$5", "$119", "$88", "$0"]

#list for the location the user can pick from if they choose snowy as thier weather 
snowing_location_list = ["Juneau, Alaska", "Boulder, Colorado", "Cleveland, Ohio"]
#Hotel options for snowing weather
snowing_hotel_list = ["Four Points by Sheraton Juneau", "Silverbow Inn Hotel & Suites", "Aspen Suites Hotel Juneau","Boulder Marriott", "St.Julien Hotel & Spa", "Residence Inn by Marriott Boulder Canyon Boulevard","The Westin Downtown Cleveland", "Metropolitan at the 9", "Rennisance Cleveland Hotel"]
#Prices per night for snowing hotel options
snowing_hotel_prices_list = ["$239", "$179", "$144", "$140", "$289", "$174", "$89", "$229", "$229"]
#Activity options for snowing weather
snowing_activity_list = ["Patsy Ann Statue", "Goldbelt Tram ", "Juneau Wildlife Whale Watching & Mendenhall Glacier", "Flagstaff Mountain", "Flatirons", "Royal Arch Trail", "Rock and Roll Hall of Fame", "West Side Market", "A Christmas Story House"]
#Prices for activity admissons under snowing options
snowing_activity_prices_list = ["$0", "$33", "$157", "$0", "$0", "$0", "$28", "$0", "$15"]

#list for the location the user can pick from if they choose rainy as thier weather 
rainy_location_list = ["Seattle, Washington","New Orleans, Lousianna","Pittsburgh, Pennsylvania"]
#Hotel options for rainy weather
rainy_hotel_list = ["Hyatt House Seattle/Downtown", "Warwick Seattle","The Paramount Hotel","St. James Hotel New Orleans Downtown","Embassy Suites by Hilton New Orleans", "Hampton Inn & Suites New Orleans Downtown","DoubleTree by Hilton Hotel & Suites Pittsburgh Downtown", "Fairmont Pittsburgh", "Kimpton Hotel Monaco Pittsburgh"]
#Prices per night for rainy hotel options
rainy_hotel_prices_list = ["$134", "$89", "$122", "$99", "$96", "$94", "$146", "$200", "$178"]
#Activity options for rainy weather
rainy_activity_list = ["Pike Place Market","Space Needle","The Gum Wall","The National World War II Museum","Mardi Gras World","Bourbon Street","Point State Park","Carnegie Science Center","The Andy Warhol Museum"]
#Prices for activity admissons under rainy options
rainy_activity_prices_list = ["$0", "$35", "0", "$29", "$22", "$0", "$0", "$20", "$20"]

#list for the location the user can pick from if they choose tropical as thier weather 
tropical_location_list = ["Honolulu, Hawaii", "Puerto Rico", "Key West, Florida"]
#Hotel options for tropical weather
tropical_hotel_list = ["Hilton Hawaiian Village Waikiki Beach Resort", "Prince Waikiki - Honolulu Luxury Hotel", "Hotel Renew", "The St. Regis Bahia Beach Resort, Puerto Rico", "San Juan Water and Beach Club Hotel", "Dorado Beach, a Ritz-Carlton Reserve", "DoubleTree Resort by Hilton Hotel Grand Key - Key West", "Courtyard by Marriott Key West Waterfront", "Hyatt Residence Club Key West, Windward Pointe"]
#Prices per night for tropical hotel options
tropical_hotel_prices_list = ["$230", "$251", "$116", "$971", "$139", "$1891", "$489", "$825", "$459"]
#Activity options for tropical weather
tropical_activity_list = ["Diamond Head", "Pearl Harbor National Memorial", "Manoa Falls", "Bahía Bioluminiscente", "Castillo San Felipe del Morro", "La Fortaleza", "Southernmost Point of the Continental US", "Mallory Square", "Dog Beach"]
#Prices for activity admissons under tropical options
tropical_activity_prices_list = ["$4", "$0", "$0", "$0", "$10", "$0", "$0", "$0", "$0"]

vacation = input("Do you want to take a vacation? ").lower()
#If the user inputs no the program will keep re-asking untill yes is input. 
while vacation == "no":
  vacation = input("Do you want to take a vacation? ").lower()

#Creates a function for the vacation planner
def vacation_planner():
 
#Prints weather options and asks which one the user wants
  if vacation == "yes":
    print("\n" + weather_list[0] +"\n" + weather_list[1]+ "\n" + weather_list[2]+ "\n"+ weather_list[3]+"\n") 
    weather_choices = input("Out of the choices above, what weather would you prefer for your vacation?\n")

#Sunny location stuff
  if weather_choices == weather_list[0]:
    print("\n"+ sunny_location_list[0]+"\n"+sunny_location_list[1]+"\n"+sunny_location_list[2]+"\n")
    location_question = input("Out of the list above, which location would you prefer? ")
#Orlando hotel stuff
    if location_question == sunny_location_list[0]:
      print("\n"+sunny_hotel_list[0] + "\n" + sunny_hotel_list[1] + "\n" + sunny_hotel_list[2]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
      if hotel_question=="Crowne Plaza Orlando":
        print("\n$83 a night")
      elif hotel_question=="Hyatt Regency Orlando":
        print("\n$135 a night")
      else:
        print("\n$171 a night")
#Orlando activity stuff
      if hotel_question in sunny_hotel_list:
        print("\n"+sunny_activity_list[0] + "\n" + sunny_activity_list[1] + "\n" + sunny_activity_list[2]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
        if activity_question=="Walt Disney World":
          print("\n$109 a ticket")
        elif activity_question=="Gatorland":
          print("\n$30 a ticket")
        else:
          print("\n$35 a ticket")
#Final trip
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is:\n"+ final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])

#Austin hotel stuff
    elif location_question == sunny_location_list[1]:
      print("\n"+sunny_hotel_list[3] + "\n" + sunny_hotel_list[4] + "\n" + sunny_hotel_list[5]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
      if hotel_question=="JW Marriott Austin":
        print("\n$294 a night")
      elif hotel_question=="The Westin Austin Downtown":
        print("\n$167 a night")
      else:
        print("\n$96 a night")
#Austin activity stuff
      if hotel_question in sunny_hotel_list:
        print("\n"+sunny_activity_list[3] + "\n" + sunny_activity_list[4] + "\n" + sunny_activity_list[5]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
        if activity_question=="McKinney Falls State Park":
          print("\n$6 a ticket")
        elif activity_question=="Austin Zoo":
          print("\n$15 a ticket")
        else:
          print("\n$5 a ticket")
#Final trip
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is:\n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])

#Los Angeles hotel stuff
    elif location_question == sunny_location_list[2]:
      print("\n"+sunny_hotel_list[6] + "\n" + sunny_hotel_list[7] + "\n" + sunny_hotel_list[8]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
      if hotel_question=="Millennium Biltmore Hotel Los Angeles":
        print("\n$160 a night")
      elif hotel_question=="The Wayfarer Downtown Los Angeles":
        print("\n$103 a night")
      else:
        print("\n$70 a night")
#Los Angeles activity stuff
      if hotel_question in sunny_hotel_list:
        print("\n"+sunny_activity_list[6] + "\n" + sunny_activity_list[7] + "\n" + sunny_activity_list[8]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? \n")
        if activity_question=="Universal Studios-Hollywood":
          print("\n$119 a ticket")
        elif activity_question=="Dodgers Game":
          print("\n$88 a ticket")
        else:
          print("\n$0 a ticket")
#Final trip
        final_trip = [weather_choices, location_question, hotel_question, activity_question] 
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])

#Snowing location stuff 
  elif weather_choices == weather_list[1]:
    print("\n"+snowing_location_list[0]+"\n"+snowing_location_list[1]+"\n"+snowing_location_list[2]+"\n")
    location_question = input("Out of the list above, which location would you prefer? ")
#Juneau hotel stuff
    if location_question == snowing_location_list[0]:
      print("\n"+snowing_hotel_list[0] + "\n" + snowing_hotel_list[1] + "\n" + snowing_hotel_list[2]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
      if hotel_question=="Four Points by Sheraton Juneau":
        print("\n$239 a night")
      elif hotel_question=="Silverbow Inn Hotel & Suites":
        print("\n$179 a night")
      else:
        print("\n$144 a night")
#Juneau activity stuff
      if hotel_question in snowing_hotel_list:
        print("\n"+snowing_activity_list[0] + "\n" + snowing_activity_list[1] + "\n" + snowing_activity_list[2]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
        if activity_question=="Patsy Ann Statue":
          print("\n$0 a ticket")
        elif activity_question=="Goldbelt Tram":
          print("\n$33 a ticket")
        else:
          print("\n$157 a ticket")
#Final trip
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])

#Boulder hotel stuff
    elif location_question == snowing_location_list[1]:
      print("\n"+snowing_hotel_list[3] + "\n "+ snowing_hotel_list[4] + "\n" + snowing_hotel_list[5]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
      if hotel_question=="Boulder Marriott":
        print("\n$140 a night")
      elif hotel_question=="St.Julien Hotel & Spa":
        print("\n$289 a night")
      else:
        print("\n$174 a night")
#Boulder activity stuff
      if hotel_question in snowing_hotel_list:
        print("\n"+snowing_activity_list[3] + "\n" + snowing_activity_list[4] + "\n" + snowing_activity_list[5]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
        if activity_question=="Flagstaff Mountain":
          print("\n$0 a ticket")
        elif activity_question=="Flatirons":
          print("\n$0 a ticket")
        else:
          print("\n$0 a ticket")
#Final trip
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])

#Cleveland hotel stuff
    elif location_question == snowing_location_list[2]:
      print("\n"+snowing_hotel_list[6] + "\n" + snowing_hotel_list[7] + "\n" + snowing_hotel_list[8]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
      if hotel_question=="The Westin Downtown Cleveland":
        print("\n$89 a night")
      elif hotel_question=="Metropolitan at the 9":
        print("\n$229 a night")
      else:
        print("\n$229 a night")
#Cleveland activity stuff
      if hotel_question in snowing_hotel_list:
        print("\n"+snowing_activity_list[6] + "\n" + snowing_activity_list[7] + "\n" + snowing_activity_list[8]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
        if activity_question=="Rock and Roll Hall of Fame":
          print("\n$28 a ticket")
        elif activity_question=="West Side Market":
          print("\n$0 a ticket")
        else:
          print("\n$15 a ticket")
#Final trip
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])

#Rainy location stuff
  elif weather_choices == weather_list[2]:
    print("\n"+ rainy_location_list[0] + "\n"+ rainy_location_list[1]+ "\n"+ rainy_location_list[2]+"\n")
    location_question = input("Out of the list above, which location would you prefer? ")
#Seattle hotel stuff
    if location_question == rainy_location_list[0]:
      print("\n"+rainy_hotel_list[0] + "\n" + rainy_hotel_list[1] + "\n" + rainy_hotel_list[2]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
      if hotel_question=="Hyatt House Seattle/Downtown":
        print("\n$134 a night")
      elif hotel_question=="Warwick Seattle":
        print("\n$89 a night")
      else:
        print("\n$122 a night")
#Seattle activity stuff
      if hotel_question in rainy_hotel_list:
        print("\n"+rainy_activity_list[0] + "\n" + rainy_activity_list[1] + "\n" + rainy_activity_list[2]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
        if activity_question=="Pike Place Market":
          print("\n$0 a ticket")
        elif activity_question=="Space Needle":
          print("\n$35 a ticket")
        else:
          print("\n$0 a ticket")
#Final trip
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3]) 

#New Orleans hotel stuff
    elif location_question == rainy_location_list[1]:
      print("\n"+rainy_hotel_list[3] + "\n"+ rainy_hotel_list[4] + "\n" + rainy_hotel_list[5]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
      if hotel_question=="St. James Hotel New Orleans Downtown":
        print("\n$99 a night")
      elif hotel_question=="Embassy Suites by Hilton New Orleans":
        print("\n$96 a night")
      else:
        print("\n$94 a night")
#New Orleans activity stuff
      if hotel_question in rainy_hotel_list:
        print("\n"+rainy_activity_list[3] + "\n" + rainy_activity_list[4] + "\n" + rainy_activity_list[5]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
        if activity_question=="The National World War II Museum":
          print("\n$29 a ticket")
        elif activity_question=="Mardi Gras World":
          print("\n$22 a ticket")
        else:
          print("\n$0 a ticket")
#Final trip
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])

#Pittsburgh hotel stuff 
    elif location_question == rainy_location_list[2]:
      print("\n"+rainy_hotel_list[6] + "\n" + rainy_hotel_list[7] + "\n" + rainy_hotel_list[8]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
      if hotel_question=="DoubleTree by Hilton Hotel & Suites Pittsburgh Downtown":
        print("\n$146 a night")
      elif hotel_question=="Fairmont Pittsburgh":
        print("\n$200 a night")
      else:
        print("\n$178 a night")
#Pittsburgh activity stuff
      if hotel_question in rainy_hotel_list:
        print("\n"+rainy_activity_list[6] + "\n" + rainy_activity_list[7] + "\n" + rainy_activity_list[8]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
        if activity_question=="Point State Park":
          print("\n$0 a ticket")
        elif activity_question=="Carnegie Science Center":
          print("\n$20 a ticket")
        else:
          print("\n$20 a ticket")
#Final trip
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])

#Tropical location stuuff
  elif weather_choices == weather_list[3]:
    print("\n"+ tropical_location_list[0] + "\n"+ tropical_location_list[1]+ "\n"+ tropical_location_list[2]+"\n")
    location_question = input("Out of the list above, which location would you prefer? ")
#Honolulu hotel stuff
    if location_question == tropical_location_list[0]:
      print("\n"+tropical_hotel_list[0] + "\n" + tropical_hotel_list[1] + "\n" + tropical_hotel_list[2]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
      if hotel_question=="Hilton Hawaiian Village Waikiki Beach Resort":
        print("\n$230 a night")
      elif hotel_question=="Prince Waikiki- Honolulu Luxery Hotel":
        print("\n$251 a night")
      else:
        print("\n$116 a night")
#Honolulu activity stuff
      if hotel_question in tropical_hotel_list:
        print("\n"+tropical_activity_list[0] + "\n" + tropical_activity_list[1] + "\n" + tropical_activity_list[2]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
        if activity_question=="Diamond Head":
          print("\n$4 a ticket")
        elif activity_question=="Pearl Harbor National Memorial":
          print("\n$0 a ticket")
        else:
          print("\n$0 a ticket")
#Final trip
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3]) 

#Puerto Rico hotel stuff
    elif location_question == tropical_location_list[1]:
      print("\n"+tropical_hotel_list[3] + "\n"+ tropical_hotel_list[4] + "\n" + tropical_hotel_list[5]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
      if hotel_question=="The St. Regis Bahia Beach Resort":
        print("\n$971 a night")
      elif hotel_question=="San Juan Water and Beach Club Hotel":
        print("\n$139 a night")
      else:
        print("\n$1891 a night")
#Puerto Rico activity stuff
      if hotel_question in tropical_hotel_list:
        print("\n"+tropical_activity_list[3] + "\n" + tropical_activity_list[4] + "\n" + tropical_activity_list[5]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
        if activity_question=="La Fortaleza":
          print("\n$0 a ticket")
        elif activity_question=="Castillo San Felipe del Morro":
          print("\n$10 a ticket")
        else:
          print("\n$0 a ticket")
#Final trip
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])

#Key West hotel stuff
    elif location_question == tropical_location_list[2]:
      print("\n"+tropical_hotel_list[6] + "\n" + tropical_hotel_list[7] + "\n" + tropical_hotel_list[8]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ") 
      if hotel_question=="DoubleTree Resort by Hilton Hotel Grand Key - Key West ":
        print("\n$489 a night")
      elif hotel_question=="Courtyard by Marriott Key West Waterfront":
        print("\n$825 a night")
      else:
        print("\n$459 a night")
#Key West activity stuff
      if hotel_question in tropical_hotel_list:
        print("\n"+tropical_activity_list[6] + "\n" + tropical_activity_list[7] + "\n" + tropical_activity_list[8]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
        if activity_question=="Mallory Square":
          print("\n$0 a ticket")
        elif activity_question=="Southernmost Point of the Continental US":
          print("\n$0 a ticket")
        else:
          print("\n$0 a ticket")
#Final trip
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])

#Calls the vacation planner function
vacation_planner()
another_vacation = input("\nWould you like to plan another vacation? ").lower()
#Continues to plan another vaction if the user inputs yes when asked if they would like to plan another vacation
while another_vacation == "yes":
  vacation_planner()
  another_vacation = input("\nWould you like to plan another vacation? ").lower()