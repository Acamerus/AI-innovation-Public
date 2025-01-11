import sys
import os

import streamlit as st

sys.path.append(os.path.join('/home/user/AI-innovation-Public/ai-innovation-main1/ai-innovation-main/src/util'))

from data_retrievals import get_BMCC_majors

st.set_page_config(layout="centered", page_title='AI Advisory')

st.title('AI Advisory')

major_options = get_BMCC_majors()

major = None

if 'major' not in st.session_state or st.session_state['major'] is None:
    major = st.selectbox(label='What is your major?', index=None,
                         options=major_options, placeholder='Choose an option',
                         key="major")
else:
    major = st.session_state['major']

    # st.divider()

    #courses = get_major_courses_and_prereqs(major)

    left1, right1 = st.columns([8, 1])

    with left1:
        st.subheader(f'Your *{major}* Roadmap')

    with right1:
        if st.button("Reset"):
            st.session_state['major'] = None

    

   