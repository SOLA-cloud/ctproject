import streamlit as st
import streamlit.components.v1 as htmlviewer
st.set_page_config(layout='wide', page_title='Click-Through Rate')

#Title Msg#1
st.title("This is my CT project!")

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
        import streamlit as st
        import streamlit.components.v1 as htmlviewer

        with open('./loan_optimization.html', 'r', encoding='utf-8') as f:
            CT_html = f.read()

        with st.expander('CT Content #1'):
            with open("loan_optimization.html", "r", encoding="utf-8") as f:
                html_code = f.read()
            htmlviewer.html(html_code, height=1000, scrolling=True)


        with st.expander('CT Content #2'):
            with open("saving_plan.html", "r", encoding="utf-8") as f:
                html_code = f.read()
            htmlviewer.html(html_code, height=1000, scrolling=True)  
 
        with st.expander('AI-X Content'):
            with open("index.html", "r", encoding="utf-8") as f:
                html_code = f.read()
            htmlviewer.html(html_code, height=2300)
        
with col2:
    with st.expander('Tips..'):
        st.info('1) CT content #1\n2) CT content #2\n3) AI-X Content')

st.markdown('<hr>', unsafe_allow_html=True)
st.write('<font color="BLUE">(c)copyright. all rights reserved by SOLA5', unsafe_allow_html=True)