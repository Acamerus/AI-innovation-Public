import sys
import os

sys.path.append(os.path.join('/home/user/AI-innovation-Public/ai-innovation-main1/ai-innovation-main/src/util'))


import streamlit as st

from streamlit_extras.row import row
from streamlit_extras.add_vertical_space import add_vertical_space


from data_retrievals import get_BMCC_majors

st.set_page_config(layout="centered", page_title='AI Advisory')

st.title('AI Advisory')

major_options = get_BMCC_majors()

if "major" in st.session_state:
    st.session_state['major'] = st.session_state['major']

st.write(st.session_state)

if 'major' not in st.session_state:
    st.session_state['major'] = None

if 'major' not in st.session_state or st.session_state['major'] is None:
    major = st.selectbox(label='What is your major?', index=None,
                         options=major_options, placeholder='Choose an option',
                         key="major")
else:
    major = st.session_state['major']

    # st.divider()

    #courses = get_major_courses_and_prereqs(major)

    left1, right1 = st.columns([7, 1])

    with left1:
        st.subheader(f'Your *{major}* Roadmap')

    with right1:
        st.button("Reset", on_click=lambda: st.session_state.clear())

    add_vertical_space(3)

    st.subheader("Core Courses", divider="gray")

    row1 = row((4,3), vertical_align='bottom')
    row1.write("**Core Class**")
    row1.segmented_control(label='Core Class', label_visibility="collapsed", options=('Incomplete', 'In Progress', 'Complete'), key='coreClass')
    
    
    st.subheader("Electives", divider="gray")

    

   