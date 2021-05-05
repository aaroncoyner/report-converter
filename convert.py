#!/usr/bin/env python
# coding: utf-8

import pandas as pd


def create_report(filename, output):
	df = pd.read_excel(filename)

	columns = ['SIS Number', 'Student Name', 'TermCode',
			   'Period 1', 'Teacher 1', 'Course 1', 'Course Title 1', 'Grading Period Mark 1', 'Abs1 1', 'Abs2 1',
			   'Period 2', 'Teacher 2', 'Course 2', 'Course Title 2', 'Grading Period Mark 2', 'Abs1 2', 'Abs2 2',
			   'Period 3', 'Teacher 3', 'Course 3', 'Course Title 3', 'Grading Period Mark 3', 'Abs1 3', 'Abs2 3',
			   'Period 4', 'Teacher 4', 'Course 4', 'Course Title 4', 'Grading Period Mark 4', 'Abs1 4', 'Abs2 4',
			   'Period 5', 'Teacher 5', 'Course 5', 'Course Title 5', 'Grading Period Mark 5', 'Abs1 5', 'Abs2 5',
			   'Period 6', 'Teacher 6', 'Course 6', 'Course Title 6', 'Grading Period Mark 6', 'Abs1 6', 'Abs2 6',
			   'Period 7', 'Teacher 7', 'Course 7', 'Course Title 7', 'Grading Period Mark 7', 'Abs1 7', 'Abs2 7',
			   'Period 8', 'Teacher 8', 'Course 8', 'Course Title 8', 'Grading Period Mark 8', 'Abs1 8', 'Abs2 8',
			   'Period 9', 'Teacher 9', 'Course 9', 'Course Title 9', 'Grading Period Mark 9', 'Abs1 9', 'Abs2 9',
			   'Period 10', 'Teacher 10', 'Course 10', 'Course Title 10', 'Grading Period Mark 10', 'Abs1 10', 'Abs2 10']

	df_modified = pd.DataFrame(columns=columns)
	sis_number = df.loc[:, 'SIS Number'][0]
	new_row = {'SIS Number':sis_number, 'Student Name':df.loc[:, 'Student Name'][0], 'TermCode':df.loc[:, 'TermCode'][0]}

	for index, row in df.iterrows():    
		if row['SIS Number'] == sis_number:
			period = row['Period']
			new_row[f'Period {period}'] = period
			new_row[f'Teacher {period}'] = row['Teacher']
			new_row[f'Course {period}'] = row['Course']
			new_row[f'Course Title {period}'] = row['Course Title']
			new_row[f'Grading Period Mark {period}'] = row['Quarter Mark']
			new_row[f'Abs1 {period}'] = row['Abs1']
			new_row[f'Abs2 {period}'] = row['Abs2']
		else:
			df_modified = df_modified.append(new_row, ignore_index=True)
			sis_number = row['SIS Number']
			new_row = {'SIS Number':sis_number, 'Student Name':row['Student Name'], 'TermCode':row['TermCode']}
			period = row['Period']
			new_row[f'Period {period}'] = period
			new_row[f'Teacher {period}'] = row['Teacher']
			new_row[f'Course {period}'] = row['Course']
			new_row[f'Course Title {period}'] = row['Course Title']
			new_row[f'Grading Period Mark {period}'] = row['Quarter Mark']
			new_row[f'Abs1 {period}'] = row['Abs1']
			new_row[f'Abs2 {period}'] = row['Abs2']
			
	df_modified = df_modified.fillna('')
	df_modified.to_csv(output)

if __name__ == "__main__":
    create_report('data/GRD Mark Verification by Teacher - Sample.xlsx', 'out/compressed_rows.csv')
