list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]


def merge_lists(list_1, list_2) -> list:
        # unique student IDs from both lists
    student_ids = set([s.get("id") for s in list_1] + [s.get("id") for s in list_2])
    # Merge student information
    merged_list = []
    for student_id in student_ids:
        #  student in list_1
        match_student_1 = next((i for i in list_1 if i.get("id") == student_id), {})
        #  student in list_2
        match_student_2 = next((j for j in list_2 if j.get("id") == student_id), {})
        merged_student = {
            key: match_student_1.get(key) or match_student_2.get(key)
            for key in set(match_student_1.keys()).union(
                match_student_2.keys()
            )
            if key in match_student_1 or key in match_student_2
        }
        merged_list.append(merged_student) #append to list
    return merged_list

"""
    Complete this function, by merging the information from list_1 and list_2
    to create a new list, which has all the information about each student from
    both lists in one single dict.

    - Both lists are unsorted
    - Both lists can have missing values (for ex list_2 has missing id=2)
    """
    # return list_3


list_3 = merge_lists(list_1, list_2)
print(list_3)