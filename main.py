weather_list = ["Sunny", "Snowing", "Rainy", "Tropical"]
sunny_location_list = ["Orlando, Florida", "Austin, Texas","Los Angeles, California"]
sunny_hotel_list = ["Crowne Plaza Orlando", "Hyatt Regency Orlando", "Hilton Orlando","JW Marriott Austin", "The Westin Austin Downtown", "Hilton Garden Inn Cedar Park Austin","Millennium Biltmore Hotel Los Angeles", "The Wayfarer Downtown Los Angeles", "Freehand Los Angles"]
sunny_activity_list = ["Walt Disney World","Gatorland","Wonderworks","McKinney Falls", "State Park","Austin Zoo", "Cathedral of Junk","Universal","Studios-Hollywood","Dodgers Game", 
"Hollywood Sign Hike"]

snowing_location_list = ["Juneau, Alaska", "Boulder, Colorado", "Cleveland, Ohio"]
snowing_hotel_list = ["Four Points by Sheraton Juneau", "Silverbow Inn Hotel & Suites", "Aspen Suites Hotel Juneau", "Hyatt House Seattle/Downtown", "Warwick Seattle" , "The Paramount Hotel","The Westin Downtown Cleveland", "Metropolitan at the 9", "Rennisance Cleveland Hotel"]
snowing_activity_list = ["Patsy Ann Statue", "Goldbelt Tram ", "Alaska Adventure Concierge", "Flagstaff Mountain", "Flatirons", "Royal Arch Trail", "Rock and Roll Hall of Fame", "West Side Market", "A Christmas Story House"]

rainy_location_list = ["Seattle, Washington","New Orleans, Lousianna",
"Pittsburgh, Pennsylvania"]
rainy_hotel_list = ["Hyatt House Seattle/Downtown", "Warwick Seattle"," The Paramount Hotel","St. James Hotel New Orleans Downtown", "Embassy Suites by Hilton New Orleans", "Hampton Inn & Suites New Orleans Downtown","DoubleTree by Hilton Hotel & Suites Pittsburgh Downtown", "Fairmont Pittsburgh", "Kimpton Hotel Monaco Pittsburgh"]
rainy_activity_list = ["Pike Place Market","Space Needle","The Gum Wall","The National World War II Museum","Mardi Gras World","Bourbon Street","Point State Park","Carnegie Science Center","The Andy Warhol Museum"]

tropical_location_list = ["Honolulu, Hawaii", "Puerto Rico", "Key West, Florida"]
tropical_hotel_list = ["Hilton Hawaiian Village Waikiki Beach Resort", "Prince Waikiki - Honolulu Luxury Hotel", "Hotel Renew", "The St. Regis Bahia Beach Resort, Puerto Rico", "San Juan Water and Beach Club Hotel", "Dorado Beach, a Ritz-Carlton Reserve", "DoubleTree Resort by Hilton Hotel Grand Key - Key West", "Courtyard by Marriott Key West Waterfront", "Hyatt Residence Club Key West, Windward Pointe"]
tropical_acticity_list = ["Diamond Head", "Pearl Harbor National Memorial", "Manoa Falls", "Bahía Bioluminiscente", "Castillo San Felipe del Morro", "La Fortaleza", "Southernmost Point of the Continental US", "Mallory Square", "Dog Beach"]

vacation = input("Do you want to take a vacation? ")
while vacation == "no":
  vacation = input("Do you want to take a vacation? ")
if vacation == "yes":

  print("\n" + weather_list[0] +"\n" + weather_list[1]+ "\n" + weather_list[2]+ "\n"+ weather_list[3]+"\n") 
  weather_choices = input("Out of the choices above, what weather would you prefer for your vacation? ")

if weather_choices == weather_list[0]:
  print("\n"+ sunny_location_list[0]+"\n"+sunny_location_list[1]+"\n"+sunny_location_list[2]+"\n")
  location_question = input("Out of the list above, which location would you prefer? ")
  if location_question == sunny_location_list[0]:
    print("\n"+sunny_hotel_list[0] + "\n" + sunny_hotel_list[1] + "\n" + sunny_hotel_list[2]+"\n")
    hotel_question = input("Out of the list above, which hotel would you prefer? ")
    if hotel_question in sunny_hotel_list:
      print("\n"+sunny_activity_list[0] + "\n" + sunny_activity_list[1] + " \n" + sunny_activity_list[2]+"\n")
      activity_question = input("Out of the list above, which activity would you prefer? ")
      final_trip = [weather_choices, location_question, hotel_question, activity_question]
      print(final_trip)
  elif location_question == sunny_location_list[1]:
    print("\n"+sunny_hotel_list[3] + "\n" + sunny_hotel_list[4] + "\n" + sunny_hotel_list[5]+"\n")
    hotel_question = input("Out of the list above, which hotel would you prefer? ")
    if hotel_question in sunny_hotel_list:
      print("\n"+sunny_activity_list[3] + ",\n" + sunny_activity_list[4] + ",\n" + sunny_activity_list[5]+"\n")
      activity_question = input("Out of the list above, which activity would you prefer? ")
      final_trip = [weather_choices, location_question, hotel_question, activity_question]
      print(final_trip)
  elif location_question == sunny_location_list[2]:
    print("\n"+sunny_hotel_list[6] + ",\n" + sunny_hotel_list[7] + ",\n" + sunny_hotel_list[8]+"\n")
    hotel_question = input("Out of the list above, which hotel would you prefer? ")
    if hotel_question in sunny_hotel_list:
      print("\n"+sunny_activity_list[6] + ",\n" + sunny_activity_list[7] + ",\n" + sunny_activity_list[8]+"\n")
      activity_question = input("Out of the list above, which activity would you prefer? \n")
      final_trip = [weather_choices, location_question, hotel_question, activity_question] 
      print(final_trip)
      
elif weather_choices == weather_list[1]:
  print(snowing_location_list)
  location_question = input("Out of the list above, which location would you prefer? ")
  if location_question == snowing_location_list[0]:
    print("\n"+snowing_hotel_list[0] + ",\n" + snowing_hotel_list[1] + ",\n" + snowing_hotel_list[2]+"\n")
    hotel_question = input("Out of the list above, which hotel would you prefer? ")
    if hotel_question in snowing_hotel_list:
      print("\n"+snowing_activity_list[0] + ",\n " + snowing_activity_list[1] + ",\n" + snowing_activity_list[2]+"\n")
      activity_question = input("Out of the list above, which activity would you prefer? ")
      final_trip = [weather_choices, location_question, hotel_question, activity_question]
      print(final_trip)
  elif location_question == snowing_location_list[1]:
    print("\n"+snowing_hotel_list[3] + ",\n "+ snowing_hotel_list[4] + ",\n" + snowing_hotel_list[5]+"\n")
    hotel_question = input("Out of the list above, which hotel would you prefer? ")
    if hotel_question in snowing_hotel_list:
      print("\n"+snowing_activity_list[3] + ",\n" + snowing_activity_list[4] + ",\n" + snowing_activity_list[5]+"\n")
      activity_question = input("Out of the list above, which activity would you prefer? ")
      final_trip = [weather_choices, location_question, hotel_question, activity_question]
      print(final_trip)
  elif location_question == snowing_location_list[2]:
    print("\n"+snowing_hotel_list[6] + ",\n" + snowing_hotel_list[7] + ",\n" + snowing_hotel_list[8]+"\n")
    hotel_question = input("Out of the list above, which hotel would you prefer? ")
    if hotel_question in snowing_hotel_list:
      print("\n"+snowing_activity_list[6] + ",\n" + snowing_activity_list[7] + ",\n" + snowing_activity_list[8]+"\n")
      activity_question = input("Out of the list above, which activity would you prefer? ")
      final_trip = [weather_choices, location_question, hotel_question, activity_question]
      print("\n"  elif location_question == sunny_location_list[1]:
    print("\n"+sunny_hotel_list[3] + ",\n" + sunny_hotel_list[4] + ",\n" + sunny_hotel_list[5])
    hotel_question = input("Out of the list above, which hotel would you prefer? ")
    if hotel_question == sunny_hotel_list[3] or sunny_hotel_list[4] or sunny_hotel_list[5]:
      print("\n"+sunny_activity_list[3] + ",\n" + sunny_activity_list[4] + ",\n" + sunny_activity_list[5])
      activity_question = input("Out of the list above, which activity would you prefer? ")
      final_trip = [weather_choices, location_question, hotel_question, activity_question]
      print("\n" + final_trip[0]+ "\n" + final_trip[1]+"\n" + final_trip[2] +"\n" + final_trip[3])
