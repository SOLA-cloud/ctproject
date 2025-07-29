import streamlit as st
import streamlit.components.v1 as htmlviewer
st.set_page_config(layout='wide', page_title='DNA sequencying!!!')

#Title Msg#1
st.title("This is my webapp!!")

with open('./index.html', 'r', encoding='utf-8') as f:
    html = f.read()
    f.close()

#html = '''
#<html>
#    <head>
#       <title> this is my html </title>
#    </head>

#    <body>
#         <h1>Topic</h1>
#         <h2>SubTopic</h2>
#    </body>
# </html>
# '''

# Box#1(4),Box#2(1)
col1, col2 = st.columns((4,1))
with col1:
    with st.expander('Content #1...'):
        url = 'https://youtu.be/XyEOEBsa8I4?si=uBEbdWUE46feAOO-'
        st.info('Content..')
        st.video(url)

    with st.expander('Image Content #1...'):
        imgfile = './images/bebras(1).jpg'
        st.image(imgfile)

    with st.expander('Image Content #2...'):
        imgfile = './images/bebras(2).jpg'
        st.image(imgfile)

    with st.expander('Content #2...'):
        htmlviewer.html(html, height=2300)
        
with col2:
    with st.expander('Tips..'):
        st.info('Tips..')

st.markdown('<hr>', unsafe_allow_html=True)
st.write('<font color="BLUE">(c)copyright. all rights reserved by skykang', unsafe_allow_html=True)