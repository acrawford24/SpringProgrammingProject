# weather optians
weather_list = ["Sunny", "Snowing", "Rainy", "Tropical"]

# location optians if user inputs Sunny
sunny_location_list = ["Orlando, Florida", "Austin, Texas","Los Angeles, California"]
# hotel options if user inputs something that is in the sunny_location_list list
sunny_hotel_list = ["Crowne Plaza Orlando", "Hyatt Regency Orlando", "Hilton Orlando","JW Marriott Austin", "The Westin Austin Downtown", "Hilton Garden Inn Cedar Park Austin","Millennium Biltmore Hotel Los Angeles", "The Wayfarer Downtown Los Angeles", "Freehand Los Angeles"]
# activity optians if the user inputs something that is in the sunny_hotel_list
sunny_activity_list = ["Walt Disney World","Gatorland","Wonderworks","McKinney Falls", "State Park","Austin Zoo", "Cathedral of Junk","Universal","Studios-Hollywood","Dodgers Game", 
"Hollywood Sign Hike"]

# location optians if the user inputs snowing
snowing_location_list = ["Juneau, Alaska", "Boulder, Colorado", "Cleveland, Ohio"]
# hotel options if user inputs something that is in the snowing_location_list list
snowing_hotel_list = ["Four Points by Sheraton Juneau", "Silverbow Inn Hotel & Suites", "Aspen Suites Hotel Juneau", "Hyatt House Seattle/Downtown", "Warwick Seattle" , "The Paramount Hotel","The Westin Downtown Cleveland", "Metropolitan at the 9", "Rennisance Cleveland Hotel"]
# activity optians if the user inputs something that is in the sunny_hotel_list
snowing_activity_list = ["Patsy Ann Statue", "Goldbelt Tram ", "Alaska Adventure Concierge", "Flagstaff Mountain", "Flatirons", "Royal Arch Trail", "Rock and Roll Hall of Fame", "West Side Market", "A Christmas Story House"]

# location optians if the user
rainy_location_list = ["Seattle, Washington","New Orleans, Lousianna","Pittsburgh, Pennsylvania"]
# hotel options if user inputs something that is in the rainy_location_list list
rainy_hotel_list = ["Hyatt House Seattle/Downtown", "Warwick Seattle","The Paramount Hotel","St. James Hotel New Orleans Downtown","Embassy Suites by Hilton New Orleans", "Hampton Inn & Suites New Orleans Downtown","DoubleTree by Hilton Hotel & Suites Pittsburgh Downtown", "Fairmont Pittsburgh", "Kimpton Hotel Monaco Pittsburgh"]
# activity optians if the user inputs something that is in the rainy_hotel_list
rainy_activity_list = ["Pike Place Market","Space Needle","The Gum Wall","The National World War II Museum","Mardi Gras World","Bourbon Street","Point State Park","Carnegie Science Center","The Andy Warhol Museum"]

tropical_location_list = ["Honolulu, Hawaii", "Puerto Rico", "Key West, Florida"]
# hotel options if user inputs something that is in the tropical_location_list list
tropical_hotel_list = ["Hilton Hawaiian Village Waikiki Beach Resort", "Prince Waikiki - Honolulu Luxury Hotel", "Hotel Renew", "The St. Regis Bahia Beach Resort, Puerto Rico", "San Juan Water and Beach Club Hotel", "Dorado Beach, a Ritz-Carlton Reserve", "DoubleTree Resort by Hilton Hotel Grand Key - Key West", "Courtyard by Marriott Key West Waterfront", "Hyatt Residence Club Key West, Windward Pointe"]
# activity optians if the user inputs something that is in the tropical_hotel_list
tropical_activity_list = ["Diamond Head", "Pearl Harbor National Memorial", "Manoa Falls", "Bahía Bioluminiscente", "Castillo San Felipe del Morro", "La Fortaleza", "Southernmost Point of the Continental US", "Mallory Square", "Dog Beach"]

vacation = input("Do you want to take a vacation? ").lower()
# as long as they dont want to plan a vacation the code will keep asking
while vacation == "no":
  vacation = input("Do you want to take a vacation? ").lower()
def vacation_planner():
  # prints weather options and asks which one the user wnats
  if vacation == "yes":
    print("\n" + weather_list[0] +"\n" + weather_list[1]+ "\n" + weather_list[2]+ "\n"+ weather_list[3]+"\n") 
    weather_choices = input("Out of the choices above, what weather would you prefer for your vacation?\n")
# if user types sunny print sunny locations (Orlando Florida, Austin Texas, Los Angeles California) then asks the user which location the user would like to go
  if weather_choices == weather_list[0]:
    print("\n"+ sunny_location_list[0]+"\n"+sunny_location_list[1]+"\n"+sunny_location_list[2]+"\n")
    location_question = input("Out of the list above, which location would you prefer? ")
# if the user inputs Orlando, Florida the code will print a list of hotels in Orlando and ask the user which hotel the user would like to go to
    if location_question == sunny_location_list[0]:
      print("\n"+sunny_hotel_list[0] + "\n" + sunny_hotel_list[1] + "\n" + sunny_hotel_list[2]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
# if the user input is in the list of hotels it will print a list of activities in Austin, Texas and ask the user which one the user would like to go to
      if hotel_question in sunny_hotel_list:
        print("\n"+sunny_activity_list[0] + "\n" + sunny_activity_list[1] + " \n" + sunny_activity_list[2]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
# puts the variables into a list then prints the list
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is:\n "+ final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])

    elif location_question == sunny_location_list[1]:
      print("\n"+sunny_hotel_list[3] + "\n" + sunny_hotel_list[4] + "\n" + sunny_hotel_list[5]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
# if the user input is in the list of hotels it will print a list of activities in Los Angeles, California and ask the user which one the user would like to go to
      if hotel_question in sunny_hotel_list:
        print("\n"+sunny_activity_list[3] + "\n" + sunny_activity_list[4] + "\n" + sunny_activity_list[5]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
# puts the variables into a list then prints the list
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])

    elif location_question == sunny_location_list[2]:
      print("\n"+sunny_hotel_list[6] + "\n" + sunny_hotel_list[7] + "\n" + sunny_hotel_list[8]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
# if the user input is in the list of hotels it will print a list of activities in Juneau, Alaska and ask the user which one the user would like to go to
      if hotel_question in sunny_hotel_list:
        print("\n"+sunny_activity_list[6] + "\n" + sunny_activity_list[7] + "\n" + sunny_activity_list[8]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? \n")
# puts the variables into a list then prints the list
        final_trip = [weather_choices, location_question, hotel_question, activity_question] 
        print("\n Your vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])
        
  elif weather_choices == weather_list[1]:
    print(snowing_location_list)
    location_question = input("Out of the list above, which location would you prefer? ")

    if location_question == snowing_location_list[0]:
      print("\n"+snowing_hotel_list[0] + "\n" + snowing_hotel_list[1] + "\n" + snowing_hotel_list[2]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
# if the user input is in the list of hotels it will print a list of activities in Boulder, Colorado and ask the user which one the user would like to go to
      if hotel_question in snowing_hotel_list:
        print("\n"+snowing_activity_list[0] + "\n " + snowing_activity_list[1] + "\n" + snowing_activity_list[2]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
# puts the variables into a list then prints the list
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])

    elif location_question == snowing_location_list[1]:
      print("\n"+snowing_hotel_list[3] + "\n "+ snowing_hotel_list[4] + "\n" + snowing_hotel_list[5]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
# if the user input is in the list of hotels it will print a list of activities in Cleveland, Ohio and ask the user which one the user would like to go to
      if hotel_question in snowing_hotel_list:
        print("\n"+snowing_activity_list[3] + "\n" + snowing_activity_list[4] + "\n" + snowing_activity_list[5]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
# puts the variables into a list then prints the list
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])

    elif location_question == snowing_location_list[2]:
      print("\n"+snowing_hotel_list[6] + "\n" + snowing_hotel_list[7] + "\n" + snowing_hotel_list[8]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
# if the user input is in the list of hotels it will print a list of activities in Seattle, Washington and ask the user which one the user would like to go to
      if hotel_question in snowing_hotel_list:
        print("\n"+snowing_activity_list[6] + "\n" + snowing_activity_list[7] + "\n" + snowing_activity_list[8]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
# puts the variables into a list then prints the list
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])

    elif location_question == sunny_location_list[1]:
      print("\n"+sunny_hotel_list[3] + "\n" + sunny_hotel_list[4] + "\n" + sunny_hotel_list[5])
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
# if the user input is in the list of hotels it will print a list of activities in New Orleans, Lousianna and ask the user which one the user would like to go to
      if hotel_question in sunny_hotel_list:
        print("\n"+sunny_activity_list[3] + "\n" + sunny_activity_list[4] + "\n" + sunny_activity_list[5])
        activity_question = input("Out of the list above, which activity would you prefer? ")
# puts the variables into a list then prints the list
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])
  elif weather_choices == weather_list[2]:
    print("\n"+ rainy_location_list[0] + "\n"+ rainy_location_list[1]+ "\n"+ rainy_location_list[2]+"\n")
    location_question = input("Out of the list above, which location would you prefer? ")

    if location_question == rainy_location_list[0]:
      print("\n"+rainy_hotel_list[0] + "\n" + rainy_hotel_list[1] + "\n" + rainy_hotel_list[2]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
# if the user input is in the list of hotels it will print a list of activities in Pittsburgh, Pennsylvania and ask the user which one the user would like to go to
      if hotel_question in rainy_hotel_list:
        print("\n"+rainy_activity_list[0] + "\n" + rainy_activity_list[1] + "\n" + rainy_activity_list[2]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
# puts the variables into a list then prints the list
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3]) 

    elif location_question == rainy_location_list[1]:
      print("\n"+rainy_hotel_list[3] + "\n"+ rainy_hotel_list[4] + "\n" + rainy_hotel_list[5]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
# if the user input is in the list of hotels it will print a list of activities in Orlando and ask the user which one the user would like to go to
      if hotel_question in rainy_hotel_list:
        print("\n"+rainy_activity_list[3] + "\n" + rainy_activity_list[4] + "\n" + rainy_activity_list[5]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
# puts the variables into a list then prints the list
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])

    elif location_question == rainy_location_list[2]:
      print("\n"+rainy_hotel_list[6] + "\n" + rainy_hotel_list[7] + "\n" + rainy_hotel_list[8]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ") 
# if the user input is in the list of hotels it will print a list of activities in Orlando and ask the user which one the user would like to go to
      if hotel_question in rainy_hotel_list:
        print("\n"+rainy_activity_list[6] + "\n" + rainy_activity_list[7] + "\n" + rainy_activity_list[8]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
# puts the variables into a list then prints the list
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])

    elif location_question == rainy_location_list[1]:
      print("\n"+rainy_hotel_list[3] + "\n" + rainy_hotel_list[4] + "\n" + rainy_hotel_list[5])
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
# if the user input is in the list of hotels it will print a list of activities in Orlando and ask the user which one the user would like to go to
      if hotel_question in rainy_hotel_list:
        print("\n"+rainy_activity_list[3] + "\n" + rainy_activity_list[4] + "\n" + rainy_activity_list[5])
        activity_question = input("Out of the list above, which activity would you prefer? ")
# puts the variables into a list then prints the list
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3]) 
  elif weather_choices == weather_list[3]:
    print("\n"+ tropical_location_list[0] + "\n"+ tropical_location_list[1]+ "\n"+ tropical_location_list[2]+"\n")
    location_question = input("Out of the list above, which location would you prefer? ")

    if location_question == tropical_location_list[0]:
      print("\n"+tropical_hotel_list[0] + "\n" + tropical_hotel_list[1] + "\n" + tropical_hotel_list[2]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
# if the user input is in the list of hotels it will print a list of activities in Orlando and ask the user which one the user would like to go to
      if hotel_question in tropical_hotel_list:
        print("\n"+tropical_activity_list[0] + "\n" + tropical_activity_list[1] + "\n" + tropical_activity_list[2]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
# puts the variables into a list then prints the list
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3]) 

    elif location_question == tropical_location_list[1]:
      print("\n"+tropical_hotel_list[3] + "\n"+ tropical_hotel_list[4] + "\n" + tropical_hotel_list[5]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
# if the user input is in the list of hotels it will print a list of activities in Orlando and ask the user which one the user would like to go to
      if hotel_question in tropical_hotel_list:
        print("\n"+tropical_activity_list[3] + "\n" + tropical_activity_list[4] + "\n" + tropical_activity_list[5]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
# puts the variables into a list then prints the list
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])

    elif location_question == tropical_location_list[2]:
      print("\n"+tropical_hotel_list[6] + "\n" + tropical_hotel_list[7] + "\n" + tropical_hotel_list[8]+"\n")
      hotel_question = input("Out of the list above, which hotel would you prefer? ") 
# if the user input is in the list of hotels it will print a list of activities in Orlando and ask the user which one the user would like to go to
      if hotel_question in tropical_hotel_list:
        print("\n"+tropical_activity_list[6] + "\n" + tropical_activity_list[7] + "\n" + tropical_activity_list[8]+"\n")
        activity_question = input("Out of the list above, which activity would you prefer? ")
# puts the variables into a list then prints the list
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])

    elif location_question == tropical_location_list[1]:
      print("\n"+tropical_hotel_list[3] + "\n" + tropical_hotel_list[4] + "\n" + tropical_hotel_list[5])
      hotel_question = input("Out of the list above, which hotel would you prefer? ")
# if the user input is in the list of hotels it will print a list of activities in Orlando and ask the user which one the user would like to go to
      if hotel_question in tropical_hotel_list:
        print("\n"+ tropical_activity_list[3] + "\n" + tropical_activity_list[4] + "\n" + tropical_activity_list[5])
        activity_question = input("Out of the list above, which activity would you prefer? ")
# puts the variables into a list then prints the list
        final_trip = [weather_choices, location_question, hotel_question, activity_question]
        print("\nYour vacation plan is: \n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3]) 
vacation_planner()
another_vacation = input("\nWould you like to plan another vacation? ").lower()
if another_vacation == "yes":
  vacation_planner()