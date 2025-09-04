import csv
import sys

students = {}
courses = {}

def dict_update(dictionary_name, primary_id, candidate_id, marks):
    if primary_id in dictionary_name.keys():
        dictionary_name[primary_id][candidate_id] = marks
    else:
        dictionary_name[primary_id] = {}
        dictionary_name[primary_id][candidate_id] = marks
# Read CSV into Dictionary
with open('data.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        dict_update(courses, int(row[' Course id']),
                    int(row['Student id']), int(row[' Marks']))
        dict_update(students, int(row['Student id']),
                    int(row[' Course id']), int(row[' Marks']))
        line_count += 1