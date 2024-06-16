#!/usr/bin/env python3
"""
a Python function that returns all students sorted by average score:

- Prototype: def top_students(mongo_collection):
- mongo_collection will be the pymongo collection object
- The top must be ordered
- The average score must be part of each item returns with key = averageScore
"""


from pymongo import MongoClient


def top_students(mongo_collection):
    """ Return all students sorted by average score. """
    pipeline = [
        {
            "$unwind": "$topics"
        },
        {
            "$group": {
                "_id": "$_id",
                "name": {"$first": "$name"},
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]
    return list(mongo_collection.aggregate(pipeline))


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.my_db
    students_collection = db.students

    # Example usage:
    top_students_list = top_students(students_collection)
    for student in top_students_list:
        print(f"[{student['_id']}] {student['name']} => {student['averageScore']}")  # noqa
