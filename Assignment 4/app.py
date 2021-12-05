import streamlit as st
import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient(**st.secrets["mongo"])
db = client.SocialNetwork
@st.cache(ttl = 600)

def get_user_data():
    useritems = db.User.find()
    useritems = list(useritems)
    return useritems

def get_userhome_data():
    userhomeitems = db.User_Home.find()
    userhomeitems = list(userhomeitems)
    return userhomeitems

def get_posts_data():
    postsitems = db.Posts.find()
    postsitems = list(postsitems)
    return postsitems

def get_fleets_data():
    fleetsitems = db.Fleets.find()
    fleetsitems = list(fleetsitems)
    return fleetsitems

def get_education_data():
    educationitems = db.Education.find()
    educationitems = list(educationitems)
    return educationitems

def get_friends_data():
    friendsitems = db.Friends.find()
    friendsitems = list(friendsitems)
    return friendsitems


useritems = get_user_data()
userhomeitems = get_userhome_data()
postsitems = get_posts_data()
fleetsitems = get_fleets_data()
educationitems = get_education_data()
friendsitems = get_friends_data()

def user_show():
    for item in useritems:
        st.write(f"{item['f_name']} {item['l_name']}")

def posts_show():
    for item in postsitems:
        st.write(f"{item['post_content']}")

def fleets_show():
    for item in fleetsitems:
        st.write(f"Fleet ID: {item['fleet_id']}")
        st.write(f"Fleet Time: {item['fleet_time']}")
        st.write(f"Fleet Content: {item['fleet_content']}")
        st.write(f"Duration: {item['duration']}")

def main():
    
    menu = ["Home","User","User Home","Education", "Posts","Friends", "Fleets"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice =="Home":
        st.header("SOCIAL NETWORK DATABASE")
        
        st.write("Social Networking System created using MongoDB as an assignment for the Database Management System course. Done by Kartika Nair, Krithika Ragothaman and Maitreyi P.")

    elif choice == "User":

        st.subheader("View all users")
        if st.button(label = "Users"):
            user_show() 

        st.subheader("View user info")
        user1 = st.text_input('Input username here:')
        if len(user1)!=0: 
            for item in useritems:
                if item['username'] == user1:
                    st.write(f"First Name: {item['f_name']}")
                    st.write(f"Last Name: {item['l_name']}")
                    st.write(f"Email ID: {item['email']}")
                    st.write(f"Date Of Birth: {item['dob']}")
                    st.write(f"Age: {int(item['age'])}")
        
        st.subheader("Users under a certain age")
        age1 = st.text_input('Input your age here:')
        if len(age1)!=0: 
            for item in useritems:
                if int(item['age']) <= int(age1):
                    st.write(f"{item['f_name']} {item['l_name']}")

    
    elif choice == "User Home":
        st.subheader("View users in a given country")
        country1 = st.text_input('Input country here:')
        if len(country1) != 0: 
            for item in userhomeitems:
                if item['country'] == country1:
                    st.write(f"User ID: {item['user_id']}")

    elif choice == "Posts":
        st.subheader("View all posts containing a given string")
        str1 = st.text_input("Input string here")
        if len(str1) != 0:
            for item in postsitems:
                if str1 in item['post_content']:
                    st.write(f"Post: {item['post_content']}")

        st.subheader("View all posts")
        if st.button(label = "Posts"):
            posts_show()

    elif choice == "Fleets":

        st.subheader("View all fleet information")
        if st.button(label = "Fleets"):
            fleets_show()

    elif choice == "Education":

        st.subheader("View all users graduating in a given year")
        y1 = st.text_input("Input year here")
        #uid_lst =[]
        
        if len(y1) != 0:
            for uitem in useritems:
                uid = str(uitem['_id'])
                for eitem in educationitems:
                    eid = str(eitem['user_id']).split(",")
                    if eid[1][11:-3] == uid and int(eitem['grad_year']) == int(y1):
                        st.write(f"{uitem['f_name']} {uitem['l_name']}")

    elif choice == "Friends":

        st.subheader("View all friends for a given user")
        u1 = st.text_input("Enter username here")
        if len(u1) != 0:
            for uitem in useritems:
                uid = str(uitem['_id'])
                for fitem in friendsitems:
                    fid = str(fitem['friend_of']).split(",")
                    if uitem['username'] == u1 and uid == fid[1][11:-3]:
                        st.write(f"{fitem['name']}")
                        #Henrie.Beaze


            

                    
        
    

        

if __name__ == '__main__':
	main()