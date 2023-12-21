import requests
import json
import streamlit as st



def get_prediction(data={"sentence":"Hello"}):
  #copy paste your aiservice link here
  url = 'https://askai.aiclub.world/8bf323d4-5fbc-49b4-9473-3ab341888363'
  r = requests.post(url, data=json.dumps(data))
  response = getattr(r,'_content').decode("utf-8")
  return response

#creating the web app
#setting the title
st.title("Mood Classifier")#change the title as your web app

#setting up the sub title
st.subheader("Check Your Mood")#change the subheader as your web app

#text input
text = st.text_input("Explain what you feel...")

#settin the data
input_data = {"sentence":text}
#getting the respoense
prediction = get_prediction(input_data)
mood = json.loads(json.loads(prediction)['body'])['predicted_label']

#subheading
if text:
  st.subheader("Your Mood is : {}".format(mood))
