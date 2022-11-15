#  create a function that will allow a child to get on a ride only if they are 13 years old and over 100 inches unless they are with a parent

#the goal playing this game is to get 3 qualified children on the ride and fill up the ride in doing so

riders = 0

print("Hello welcome to the Puyallup fair! \nLets see if we can fill our fair ride up with kids! \n\nRemember our ride fits 3 kids and \neach child has to qualify to ride by meeting \nour 2 requirments. 1. Height and 2. Age or having\na parent with them!\n\nokay here come some children now! ")

print()

def ride_check():
  global riders
  while riders < 3:
    height = input("Hello How many inches tall is the child? ")
    if height.isdigit():
      height = int(height)
      if height < 100:
        print("sorry buddy you dont meet our height rule\n....next child please ")
        print()
        # ride_check()
      elif height >= 100:
        print("okay perfect!")
        print()
        age = input("How old is the child? ")
        if age.isdigit():
          age = int(age)
          if age >= 13:
            print("great you can come on the ride! Next child please ")
            riders += 1
            print()
            
          else:
            parent = input("Is child with a parent ")
            if parent != "yes":
              print("the child cannot ride Next child please ")
              
            else:
              print("yes you can come on the ride! Next child please ")
              riders += 1
              print()
              
        else:
          print("sorry please tell me a number")
      print()
      

    else:
      print("sorry please tell me a number")
      print()
      
  else:
    print("Good job we filled the ride with {} kids! \nThe ride is full now... try again later".format(riders))

ride_check()
