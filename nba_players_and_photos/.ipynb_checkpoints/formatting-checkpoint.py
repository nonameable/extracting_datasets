import os
folders = next(os.walk('./'))[1]
print(folders)
player_name = "AJ Price"
path = "./players/" + player_name + "/"
file_name = next(os.walk(path))[2][0]
print(file_name)
new_file_name = player_name.lower().replace(" ", "-")
print(new_file_name)
os.rename(path + file_name, path + new_file_name + ".png")


os.rename("./players/" + player_name,"./players/" + new_file_name )
    

    
    