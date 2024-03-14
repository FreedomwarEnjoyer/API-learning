looking_for_item = input("What do you want to search for?")

list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for i, char in enumerate(list):
   if char == looking_for_item:
    print(f"Found {looking_for_item} at index number {i+1}.")
    exit()

print("Not found")
