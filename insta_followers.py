import instaloader
loader=instaloader.Instaloader()

loader.login("username","password") #your login credential

profile=instaloader.Profile.from_username(loader.context,"username_of_person") # username of person whom you want to perform operation 

followers=set()
followees=set()

#followers- followed by the user
#followees- profile which follows user

for member in profile.get_followers():
	followers.add(str(member)[9:]) #[9:] because it is the object and in the form of <Profile profile_name (id_number)> so we are removing profle part


for member in profile.get_followees():
	followees.add(str(member)[9:])

people_who_dont_follow_you=(followers|followees) - ((followers & followees )| followers) #union of both sets - intersection of both

with open("people_who_dont_follow_you.txt","a+") as f:
	for people in people_who_dont_follow_you:
		f.write(people)
		f.write("\n")
