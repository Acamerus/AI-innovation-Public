
def get_BMCC_majors(sort_bool=True):
    with open('ai-innovation-main1/ai-innovation-main/data/bmcc_majors.txt', 'r') as f:
        majors = f.read().splitlines()

    if sort_bool:
        majors.sort()

    return majors

def get_major_courses(major):
    return None

def get_prereqs(course):
    return None

def get_major_courses_and_prereqs(major):
    courses = get_courses(major)
    prereqs = {}
    for course in courses:
        prereqs[course] = get_prereqs(course)
    return courses, prereqs