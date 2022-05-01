import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="鼎盛网络科技", page_icon="1651375581.png", layout="wide")
orientation = "horizontal"
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

    st.image("wx.png")
    st.header("探探鼠石头村已经稳定一年左右。\n\n\n\n")
    st.write(
        "项目从去年6月份开始。\n\n\n\n"
        "一个人可以走的很快，一群人可以走的更远。\n\n\n"
        "为了让大家一起进步，由此创建了一个微信讨论群，可以扫上方二维码微信\n\n\n"
        "验证信息：我来自探探鼠网站")
elif choose == "石头村/探探鼠项目":

    selecte1 = option_menu(None, ["盈利情况", "软件截图"],
                           icons=['house', 'cloud-upload', "list-task"],
                           menu_icon="cast", default_index=0, orientation="horizontal")
    if selecte1 == "盈利情况":
        st.title("这是2022年5月的盈利截图（点击旁边放大按钮查看）")
        st.image("ylyp.png")
        st.title("这是2022年5月的兑换截图（点击旁边放大按钮查看）")
        st.image("dhjl.png")
    if selecte1 == "软件截图":
        st.title("这是鼎盛科技软件截图")
        st.image("rjjt.png")

elif choose == "其他项目":
    st.write("暂无其他项目")
