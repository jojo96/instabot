import streamlit as st
import instaloader

st.header("Your friendly neighborhood Instabot")
st.write("This bot gives you a list of people who do not follow you back on Instagram. You know what to do next ;)")
st.write("Enter your username and password :) Click Get Ghost List")
st.write("Since all good things take time, please wait a bit(Around 30 seconds)")
st.write("After it's done, you can see green triangles. Click them to see the culprits.")

name = st.text_input("Enter user name")
password = st.text_input("Enter password")


L = instaloader.Instaloader()

if st.button('Get Ghost list'):
    # Login or load session
    L.login(name, password)        # (login)

    profile = instaloader.Profile.from_username(L.context, name)
    main_followers = profile.followers

    follower_list = []
    for person in profile.get_followers():
      user_id = person.userid
      follower_list.append(person.username)
      
    main_followees = profile.followees

    followee_list = []
    for person in profile.get_followees():
      user_id = person.userid
      followee_list.append(person.username)
      
    req = []
    for element in followee_list:
      if element not in follower_list:
        req.append(element)
      
    st.write(sorted(req))
