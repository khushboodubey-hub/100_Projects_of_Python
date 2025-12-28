# # FileNotFound
# try:
#      file = open("a_file.txt")
#      a__dictionary = {"key": "value"}
#      print(a__dictionary["new_key"])

# except FileNotFoundError:
#      file = open("a_file.txt","w")
#      file.write("something!")

# except KeyError as error_message:
#      print(f"That key {error_message} does not exist.")

# else:
#      content = file.read()
#      print(content)

# finally:
#     #  file.close()
#     #  print("File was closed.")
#     raise TypeError("This is an error which i made.")


# height = float(input("Height: "))
# weight = int(input("weight: "))

# if height > 3:
#     raise ValueError("Human Height Should not be over 3 meters.")

# bmi = weight / height ** 2
# print(bmi)

# # IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

