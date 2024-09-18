#Generate 2 lists (course code and course name). create a new list with both course code and name like["CS1001:Python",...]
course_code=["CS2001","CS2002","CS2007"]
course_name=["Python","COA","TOC"]
final=zip(course_code,course_name)
print(dict(final))