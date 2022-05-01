import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(page_title="鼎盛网络科技", page_icon="1651375581.png", layout="wide")

sysmenu = '''
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
'''
st.markdown(sysmenu, unsafe_allow_html=True)

with st.sidebar:
    choose = option_menu("鼎盛科技", ["介绍", "石头村/探探鼠项目", "其他项目"],
                         icons=['house', 'file-earmark-music', 'bar-chart', 'translate', 'brightness-high'],
                         menu_icon="broadcast", default_index=0)

if choose == "介绍":
    col1, col2 = st.columns(2)
    with col1:
        st.image("wx.png", caption="鼎盛科技官方微信")
    with col2:
        st.image("wx.png", caption="微信公众号Streamlit二维码")
        st.write("微信公众号Streamlit由作者创建已由半年多。\n\n\n\n"
                 "主题就是为大家分享Python与Streamlit结合的各种案例，用于提高大家的办公效率。\n\n\n\n"
                 "一个人可以走的很快，一群人可以走的更远。\n\n\n"
                 "为了让大家一起进步，由此创建了一个微信讨论群，可以扫下方二维码添加作者微信\n\n\n"
                 "验证信息：我来自公众号Streamlit")
elif choose == "石头村/探探鼠项目":

    selecte1 = option_menu(None, ["石头村介绍", "盈利情况", "软件截图"],
        icons=['house', 'cloud-upload', "list-task"],
        menu_icon="cast", default_index=0, orientation="horizontal")