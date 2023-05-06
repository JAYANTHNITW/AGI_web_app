import streamlit as st
st.title('**Workplete General Ai assistant Challenge Prompts**')
prompt = st.text_input('Plug your input prompt here')

response1 = 'Redfin: https://www.redfin.com/'
response2 = 'Salesforce: https://www.salesforce.com/in/'
response3 = 'Salesforce: https://www.salesforce.com/in/'

if prompt=='who build you':
     st.write('Kothapalli jayanth with  support of Bhadra')

elif prompt== 'Find me a house in houston that works for 4. My budget is 600k':
    st.write(response1)

elif prompt== 'Add Max Nye at Workplete as the new lead' :
     st.write(response2)

elif prompt == 'Log a call with James Veel saying that he is looking to buy 100 widgets':
     st.write(response3)
    # else :
    #     st.write(" Jayanth will figure out it soon")

