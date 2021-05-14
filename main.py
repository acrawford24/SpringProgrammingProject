# weather options
weather_list = ["Sunny", "Snowing", "Rainy", "Tropical"]

# location options if user inputs Sunny
sunny_location_list = ["Orlando, Florida", "Austin, Texas","Los Angeles, California"]
# hotel options if user inputs something that is in the sunny_location_list list
sunny_hotel_list = ["Crowne Plaza Orlando", "Hyatt Regency Orlando", "Hilton Orlando","JW Marriott Austin", "The Westin Austin Downtown", "Hilton Garden Inn Cedar Park Austin","Millennium Biltmore Hotel Los Angeles", "The Wayfarer Downtown Los Angeles", "Freehand Los Angeles"]
#prices per night for sunny hotel options
sunny_hotel_prices_list = ["$83", "$135", "$171", "$294", "$167", "$96", "$160", "$103", "$70"]
# activity options if the user inputs something that is in the sunny_hotel_list
sunny_activity_list = ["Walt Disney World","Gatorland","Wonderworks","McKinney Falls State Park", "Austin Zoo", "Cathedral of Junk","Universal Studios-Hollywood","Dodgers Game", "Hollywood Sign Hike"]
#prices for activity admissons under sunny options
sunny_activity_prices_list = ["$109", "$30", "$35", "$6", "$15", "$5", "$119", "$88", "$0"]

# location options if the user inputs snowing
snowing_location_list = ["Juneau, Alaska", "Boulder, Colorado", "Cleveland, Ohio"]
# hotel options if user inputs something that is in the snowing_location_list list
snowing_hotel_list = ["Four Points by Sheraton Juneau", "Silverbow Inn Hotel & Suites", "Aspen Suites Hotel Juneau","Boulder Marriott", "St.Julien Hotel & Spa", "Residence Inn by Marriott Boulder Canyon Boulevard","The Westin Downtown Cleveland", "Metropolitan at the 9", "Rennisance Cleveland Hotel"]
#prices per night for snowing hotel options
snowing_hotel_prices_list = ["$239", "$179", "$144", "$140", "$289", "$174", "$89", "$229", "$229"]
# activity options if the user inputs something that is in the snowing_hotel_list
snowing_activity_list = ["Patsy Ann Statue", "Goldbelt Tram ", "Juneau Wildlife Whale Watching & Mendenhall Glacier", "Flagstaff Mountain", "Flatirons", "Royal Arch Trail", "Rock and Roll Hall of Fame", "West Side Market", "A Christmas Story House"]
#prices for activity admissons under snowing options
snowing_activity_prices_list = ["$0", "$33", "$157", "$0", "$0", "$0", "$28", "$0", "$15"]

# location options if the user inputs rainy
rainy_location_list = ["Seattle, Washington","New Orleans, Lousianna","Pittsburgh, Pennsylvania"]
# hotel options if user inputs something that is in the rainy_location_list list
rainy_hotel_list = ["Hyatt House Seattle/Downtown", "Warwick Seattle","The Paramount Hotel","St. James Hotel New Orleans Downtown","Embassy Suites by Hilton New Orleans", "Hampton Inn & Suites New Orleans Downtown","DoubleTree by Hilton Hotel & Suites Pittsburgh Downtown", "Fairmont Pittsburgh", "Kimpton Hotel Monaco Pittsburgh"]
#prices per night for rainy hotel options
rainy_hotel_prices_list = ["$134", "$89", "$122", "$99", "$96", "$94", "$146", "$200", "$178"]
# activity options if the user inputs something that is in the rainy_hotel_list
rainy_activity_list = ["Pike Place Market","Space Needle","The Gum Wall","The National World War II Museum","Mardi Gras World","Bourbon Street","Point State Park","Carnegie Science Center","The Andy Warhol Museum"]
#prices for activity admissons under rainy options
rainy_activity_prices_list = ["$0", "$35", "0", "$29", "$22", "$0", "$0", "$20", "$20"]

# location list if the user inputs tropical
tropical_location_list = ["Honolulu, Hawaii", "Puerto Rico", "Key West, Florida"]
# hotel options if user inputs something that is in the tropical_location_list list
tropical_hotel_list = ["Hilton Hawaiian Village Waikiki Beach Resort", "Prince Waikiki - Honolulu Luxury Hotel", "Hotel Renew", "The St. Regis Bahia Beach Resort, Puerto Rico", "San Juan Water and Beach Club Hotel", "Dorado Beach, a Ritz-Carlton Reserve", "DoubleTree Resort by Hilton Hotel Grand Key - Key West", "Courtyard by Marriott Key West Waterfront", "Hyatt Residence Club Key West, Windward Pointe"]
#prices per night for tropical hotel options
tropical_hotel_prices_list = ["$230", "$251", "$116", "$971", "$139", "$1891", "$489", "$825", "$459"]
# activity options if the user inputs something that is in the tropical_hotel_list
tropical_activity_list = ["Diamond Head", "Pearl Harbor National Memorial", "Manoa Falls", "Bahía Bioluminiscente", "Castillo San Felipe del Morro", "La Fortaleza", "Southernmost Point of the Continental US", "Mallory Square", "Dog Beach"]
tropical_activity_prices_list = ["$4", "$0", "$0", "$0", "$10", "$0", "$0", "$0", "$0"]

vacation = input("Do you want to take a vacation? ").lower()
# as long as they dont want to plan a vacation the code will keep asking
while vacation == "no":
  vacation = input("Do you want to take a vacation? ").lower()

# creates a function for the vacation planner
def vacation_planner():
  
# prints weather options and asks which one the user wants
  if vacation == "yes":
    print("\n" + weather_list[0] +"\n" + weather_list[1]+ "\n" + weather_list[2]+ "\n"+ weather_list[3]+"\n") 
    weather_choices = input("Out of the choices above, what weather would you prefer for your vacation?\n")

# sunny location stuff
  if weather_choices == weather_list[0]:
    print("\n"+ sunny_location_list[0]+"\n"+sunny_location_list[1]+"\n"+sunny_location_list[2]+"\n")
    location_question = input("Out of the list above, which location would you prefer? ")
# orlando hotel stuff
    if location_question == sunny_location_list[0]:
      print("\n"+sunny_hotel_list[0] + "\n" + sunny_hotel_list[1] + "\n" + sunny_hotel_list[2]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
      if hotel_question=="Crowne Plaza Orlando":
        print("\n$83 a night")
      elif hotel_question=="Hyatt Regency Orlando":
        print("\n$135 a night")
      else:
        print("\n$171 a night")
# orlando activity stuff
      if hotel_question in sunny_hotel_list:
        print("\n"+sunny_activity_list[0] + "\n" + sunny_activity_list[1] + "\n" + sunny_activity_list[2]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
        if activity_question=="Walt Disney World":
          print("\n$109 a ticket")
        elif activity_question=="Gatorland":
          print("\n$30 a ticket")
        else:
          print("\n$35 a ticket")
# final trip
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is:\n"+ final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])
        
# Austin hotel stuff
    elif location_question == sunny_location_list[1]:
      print("\n"+sunny_hotel_list[3] + "\n" + sunny_hotel_list[4] + "\n" + sunny_hotel_list[5]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
# Austin activity stuff
      if hotel_question in sunny_hotel_list:
        print("\n"+sunny_activity_list[3] + "\n" + sunny_activity_list[4] + "\n" + sunny_activity_list[5]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
# final trip
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is:\n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])
# Los Angeles hotel stuff
    elif location_question == sunny_location_list[2]:
      print("\n"+sunny_hotel_list[6] + "\n" + sunny_hotel_list[7] + "\n" + sunny_hotel_list[8]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
# Los Angeles activity stuff
      if hotel_question in sunny_hotel_list:
        print("\n"+sunny_activity_list[6] + "\n" + sunny_activity_list[7] + "\n" + sunny_activity_list[8]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? \n")
# final trip
        final_trip = [weather_choices, location_question, hotel_question, activity_question] 
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])

# snowing location stuff 
  elif weather_choices == weather_list[1]:
    print("\n"+snowing_location_list[0]+"\n"+snowing_location_list[1]+"\n"+snowing_location_list[2]+"\n")
    location_question = input("Out of the list above, which location would you prefer? ")
# Juneau hotel stuff
    if location_question == snowing_location_list[0]:
      print("\n"+snowing_hotel_list[0] + "\n" + snowing_hotel_list[1] + "\n" + snowing_hotel_list[2]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
# juneau activity stuff
      if hotel_question in snowing_hotel_list:
        print("\n"+snowing_activity_list[0] + "\n" + snowing_activity_list[1] + "\n" + snowing_activity_list[2]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
# final trip
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])
# Boulder hotel stuff
    elif location_question == snowing_location_list[1]:
      print("\n"+snowing_hotel_list[3] + "\n "+ snowing_hotel_list[4] + "\n" + snowing_hotel_list[5]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
# Boulder activity stuff
      if hotel_question in snowing_hotel_list:
        print("\n"+snowing_activity_list[3] + "\n" + snowing_activity_list[4] + "\n" + snowing_activity_list[5]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
# final trip
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])
# Cleveland hotel stuff
    elif location_question == snowing_location_list[2]:
      print("\n"+snowing_hotel_list[6] + "\n" + snowing_hotel_list[7] + "\n" + snowing_hotel_list[8]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
# cleveland activity stuff
      if hotel_question in snowing_hotel_list:
        print("\n"+snowing_activity_list[6] + "\n" + snowing_activity_list[7] + "\n" + snowing_activity_list[8]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
# final trip
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])

# rainy location stuff
  elif weather_choices == weather_list[2]:
    print("\n"+ rainy_location_list[0] + "\n"+ rainy_location_list[1]+ "\n"+ rainy_location_list[2]+"\n")
    location_question = input("Out of the list above, which location would you prefer? ")
# Seattle hotel stuff
    if location_question == rainy_location_list[0]:
      print("\n"+rainy_hotel_list[0] + "\n" + rainy_hotel_list[1] + "\n" + rainy_hotel_list[2]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
# seattle activity stuff
      if hotel_question in rainy_hotel_list:
        print("\n"+rainy_activity_list[0] + "\n" + rainy_activity_list[1] + "\n" + rainy_activity_list[2]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
# final trip
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3]) 
# New Orleans hotel stuff
    elif location_question == rainy_location_list[1]:
      print("\n"+rainy_hotel_list[3] + "\n"+ rainy_hotel_list[4] + "\n" + rainy_hotel_list[5]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
# New Orleans activity stuff
      if hotel_question in rainy_hotel_list:
        print("\n"+rainy_activity_list[3] + "\n" + rainy_activity_list[4] + "\n" + rainy_activity_list[5]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
# final trip
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])
# Pittsburgh hotel stuff 
    elif location_question == rainy_location_list[2]:
      print("\n"+rainy_hotel_list[6] + "\n" + rainy_hotel_list[7] + "\n" + rainy_hotel_list[8]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ") 
# Pittsburgh activity stuff
      if hotel_question in rainy_hotel_list:
        print("\n"+rainy_activity_list[6] + "\n" + rainy_activity_list[7] + "\n" + rainy_activity_list[8]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
# final trip
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])

# Tropical location stuuff
  elif weather_choices == weather_list[3]:
    print("\n"+ tropical_location_list[0] + "\n"+ tropical_location_list[1]+ "\n"+ tropical_location_list[2]+"\n")
    location_question = input("Out of the list above, which location would you prefer? ")
# Honolulu hotel stuff
    if location_question == tropical_location_list[0]:
      print("\n"+tropical_hotel_list[0] + "\n" + tropical_hotel_list[1] + "\n" + tropical_hotel_list[2]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
# Honolulu activity stuff
      if hotel_question in tropical_hotel_list:
        print("\n"+tropical_activity_list[0] + "\n" + tropical_activity_list[1] + "\n" + tropical_activity_list[2]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
# final trip
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3]) 
# Puerto Rico hotel stuff
    elif location_question == tropical_location_list[1]:
      print("\n"+tropical_hotel_list[3] + "\n"+ tropical_hotel_list[4] + "\n" + tropical_hotel_list[5]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
# Puerto Rico activity stuff
      if hotel_question in tropical_hotel_list:
        print("\n"+tropical_activity_list[3] + "\n" + tropical_activity_list[4] + "\n" + tropical_activity_list[5]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
# final trip
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])
# Key west hotel stuff
    elif location_question == tropical_location_list[2]:
      print("\n"+tropical_hotel_list[6] + "\n" + tropical_hotel_list[7] + "\n" + tropical_hotel_list[8]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ") 
# Key west activity stuff
      if hotel_question in tropical_hotel_list:
        print("\n"+tropical_activity_list[6] + "\n" + tropical_activity_list[7] + "\n" + tropical_activity_list[8]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
# final trip
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])

# calls the vacation planner function
vacation_planner()
another_vacation = input("\nWould you like to plan another vacation? ").lower()
# continues to plan vactions as long as the user wants to
while another_vacation == "yes":
  vacation_planner()
  another_vacation = input("\nWould you like to plan another vacation? ").lower()