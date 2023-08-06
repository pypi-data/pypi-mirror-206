#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FIS Calculator V4
Neural Dynamics Group @UCLA
Main Contributors: Shreyank Kadadi, Sharmila Venugopal, Artin Allahverdian
"""
#Importing the pandas and csv libraries
import pandas as pd
import numpy as np
import csv
import statistics
import matplotlib.pyplot as plt
import pygraphviz

#Here we define our interactions dataframe with the following column names
column_names = ['P1','P2','Effect Direction', 'Functional Association Array', 'PMIDs']
interactions = pd.DataFrame(columns = column_names)
#The default number of functional associations we study is 2
number_of_functional_associations = 2
#Define an empty lookup table which can be populated by user input using the input_csv_lookup_table function
lookup_table = {}
#Define an empty pairwise effect table which can be populated by user input using the input_csv_lookup_table function
pairwise_effect_table = {}
edges = []

'''
input_single_paper_data


#This function is reserved for the manual input of ONE research paper result 
def input_single_paper_data():  
    while True:  
        #Ask for the PMID of the paper
        pmid= input("Please enter the PubMed ID (PMID) of the research paper, or type 'quit' to exit ") 
        if pmid == "quit":
            break
        #Ask for name of the first protein (will go into column P1)
        p1= input("Please enter the name of protein 1, or type 'quit' to exit ") 
        if p1 == "quit":
            break
        #Ask for name of the second protein (will go into column P2)
        p2 = input("Please enter the name of protein 2 or type 'quit' to exit ") 
        if p2 == "quit":
            break
        #Ask for effect direction (will go into column Effect Direction)
        effect_direction = int(input("Enter the effect direction (Positive: 1, Negative: -1, No change: 0)"))
        #Check to see if effect direction is valid
        if effect_direction not in [1,-1,0]:
            print(str(effect_direction),"is not a valid effect direction, choose from following: Positive: 1, Negative: -1, No change: 0")
            return
        fa_entries = []
        for association in range(number_of_functional_associations):
            entry = int(input("Enter the direction of Functional Association",str(association+1),"(Positive: 1, Negative: -1, No change: 0, Not Studied: -2)"))
            fa_entries.append(entry)
        for entry in fa_entries:
            if entry not in [0,1,-1,-2]:
                print(str(entry), "is not a valid input, choose from the following: Positive: 1, Negative: -1, No change: 0, Not Studied: -2")
                return
        #Call the auto input function to update the database
        add_entry_to_database(pmid, p1,p2, effect_direction, fa_entries)
        print('Result added!')
'''



'''
input_csv_file_data function

-Info: This function reads in a csv file of interactions (for example of how this file should look, refer to example_interactions.csv) and adds entries to inernal database

-Input:
    file: name of the file we are entering in
    number_of_functional_associations: number of functional associations we want to study
    
-Output:
    No returned/printed output, but we populate the interactions dataframe with entries from the csv file
'''

def input_csv_file_data(file, number_of_functional_associations): #reading csv file for interactions
    with open(file) as csv_file:
        reader = csv.reader(csv_file)
        #Read file line by line
        for row in reader: 
            pmid = row[0]
            p1 = row[1]
            p2 = row[2]
            effect_direction = int(row[3])
            #For storing the raw Functional Association entries without getting rid of the unknown interactions (-2)
            fa_entries = []
            for association in range(number_of_functional_associations):
                fa_entries.append(int(row[association+4]))
            #Check to see if effect direction and functional association entries are valid
            if effect_direction not in [1,-1,0]:
                print(str(effect_direction),"is not a valid effect direction, choose from following: Positive: 1, Negative: -1, No change: 0")
                return
            for entry in fa_entries:
                if entry not in [0,1,-1,-2]:
                    print(str(entry), "is not a valid input, choose from the following: Positive: 1, Negative: -1, No change: 0, Not Studied: -2")
                    return
            #Add entry to the database
            add_entry_to_database(pmid, p1,p2, effect_direction, fa_entries)
        print("Your file has been read!")
        
 
        
        
        
        

'''
generate_FIABS_csv function

-Info: This function generates the FIABS_nw.csv, our final output csv file that contains the FIS and colors of edges

-Input:
    focus_num_of_fa: the number of the functional association that we want to generate FIS for; if we want to focus on all functional associations, this would be 0
    
-Output:
    No returned/printed output, but we populate an output csv file with each entry containing the following info: p1, p2, FIS for p1->p2, and the color of the edge p1->p2
'''


def generate_FIABS_csv(focus_num_of_fa):
    #First, we will read in the lookup table csv
    print('\n')
    lookup = input('Enter the name of your csv file of the lookup table ')
    input_csv_lookup_table(lookup)
    #Next, we will the generate pairwise effect table which contains the median directionality for each interaction
    generate_pairwise_effect_table()
    #Lastly, we will call the calculate the FIS between each interaction and append it to our output csv 
    interactions.apply(lambda x: call_calculate_fis_add_csv_entry(x['P1'], x['P2'], focus_num_of_fa),axis = 1)
    








#UTILS -- Functions that are called by other functions


'''
add_entry_to_database function

-Info: This function adds new entries to the interactions dataframe if p1->p2 doesn't already exist and updates current entries in interactions if p1->p2 exists

-Input(s):
    pmid: the PubMed ID of the research paper that references the interaction between p1 and p2 that we are inputting
    p1, the name of the first protein we want to analyze. 
    p2, the name of the second protein we want to analyze.
    effect_direction: the directionality of the experiment, can be understood as the effect p1 has on p2 -- Increase 1, Decrease: -1, No change: 0
    fa_entries: a list containing the scores for the functional associations between p1 and p2 -- Positive: 1, Negative: -1, No change: 0, Not Studied: -2
    
-Output(s): No return value, but it adds an entry to the pairwise_effect_table dictionary with (p1,p2) as the key and the median directionality as the value
'''


#This function adds new entries to the database and edits current entries based on input
def add_entry_to_database(pmid, p1,p2, effect_direction, fa_entries):
    global interactions
    check_contains = ((interactions['P1'] == p1) & (interactions['P2'] == p2)).sum() #check to see if P1 -> P2 is contained in the dataframe
    #In the case that P1 -> P2 is contained in the dataframe
    if check_contains > 0:
        #We first locate the row number of the entry that contains interactions between p1 and p2
        index = interactions[(interactions['P1'] == p1) & (interactions['P2'] == p2)].index[0] 
        #Append the effect direction to the effect direction array
        interactions.iat[index, 2].append(effect_direction)
        #Update the functional association scores
        for association in range(number_of_functional_associations):
            interactions.iat[index, 3][association].append(fa_entries[association])
        #Add the pmid to the list of pmids for the specific interaction
        interactions.iat[index, 4].append(pmid)
   #In the case that P1 -> P2 is NOT contained in the dataframe
    else:
        new_binaries_entry = [[fa_entries[association]] for association in range(number_of_functional_associations)]
        #Create a new entry with the provided values for each of the columns
        new_entry = {'P1': p1, 'P2':p2, 'Effect Direction': [effect_direction], 'Functional Association Array': new_binaries_entry, 'PMIDs' : [pmid]}
        #Add the new entry to the database
        interactions = interactions.append(new_entry, ignore_index = True)         









'''
generate_pairwise_effect_table_entry function

-Info: This function is called by the generate_pairwise_effect_table function to iteratively find the median directionality for each interaction

-Input(s): 
    p1, the name of the first protein we want to analyze. 
    p2, the name of the second protein we want to analyze
    
-Output(s): 
    No return value, but it adds an entry to the pairwise_effect_table dictionary with (p1,p2) as the key and the median directionality as the value
'''

def generate_pairwise_effect_table_entry(p1,p2):
    #First, call validation function to make sure entry of p1->p2 is contained in the interactions dataframe
    if not validate_calculate_fis(p1,p2):
        print('\n')
        print('The interaction between',p1,'and',p2,'is not recorded!')
        return
    #We first locate the row number of the entry that contains interactions between p1 and p2
    index = interactions[(interactions['P1'] == p1) & (interactions['P2'] == p2)].index[0]
    #Next, we save the array containing all the effect directions for the interactions between p1 and p2 in effect_direction_array
    effect_direction_array = interactions.iat[index,2]
    #We take the median of all of those effect directions
    median_effect_direction = statistics.median(effect_direction_array)
    #We then add the median effect direction to the pairwise_effect_table dictionary with (p1,p2) as the key and the median directionality as the value
    pairwise_effect_table[(p1,p2)] = median_effect_direction
    
    
   
    

    
    
    
    
    
    
'''
generate_pairwise_effect_table function

-Info: This function populates the pairwise_effect_table dictionary, which contains the median directionality for each pair of interactions (p1,p2)

-Input(s): NA

-Output(s):
    No returned/outputted value, but the pairwise_effect_table gets populated with median directionality for each pair of interactions (p1,p2)
'''
  
def generate_pairwise_effect_table():
    global pairwise_effect_table
    pairwise_effect_table = {}
    #apply the generate_pairwise_effect_table_entry on each entry in the interactions dataframe
    interactions.apply(lambda x: generate_pairwise_effect_table_entry(x['P1'], x['P2']),axis = 1)
    
    
    


    
    
    
    
    
 
'''
input_csv_lookup_table function

-Info: This function reads in a file containing the lookup table and populates the lookup_table dictionary with it

-Input(s):
    file, the name of the csv file containing the entries of the lookup table. LOOK AT example_lookup_table.csv to see an example of how this should be formatted
    number_of_functional_associations, the number of functional associations we want to study 

-Output(s): 
    No returned value, but the lookup_table dictionary will get populated with the weight values for each combination of functional association
'''
        
def input_csv_lookup_table(file, number_of_functional_associations): #reading in file for lookup table
    #Reset the lookup table every time this function is called    
    global lookup_table
    lookup_table = {}    
    #First, we check to see that the user indicated a positive number of functional associations
    if number_of_functional_associations <= 0:
        print("Number of functional associations must be a positive integer!")
        return
    #Open the csv file containing lookup table
    with open(file) as csv_file:
        reader = csv.reader(csv_file)
        #Read lookup table csv line by line
        for row in reader:
            fa_entries = []
            #Stores the logic table binary part of a specific row into a list called fa_entries (for example, [1,0] means that functional association 1 is present but functional assocation 2 is not)
            for association in range(number_of_functional_associations):
                fa_entries.append(int(row[association]))
            #Convert the fa_entries list to a tuple so it can serve as a hashable key
            fa_entries_tuple = (tuple(fa_entries))
            #Verification to see that each value in fa_entries_tuple is either 1 or 0 (1 means functional asssociation is present, 0 means it is not)
            for entry in fa_entries_tuple:
                if entry not in [0,1]:
                    print(str(entry), "is not a valid input. Please input either 1 or 0.")
                    return
            #Stores the functional association weight for a specific row into a variable called "weight"
            weight = float(row[number_of_functional_associations])
            #Populates the lookup_table with the weight as the value and the fa_entries_tuple as the key
            lookup_table[fa_entries_tuple] = weight
        print("Your lookup table file has been read and inputted properly!")
        
        
        
        
        
        
        
        
        
        
        
'''
generate_median_fa_entries function

-Info: This function finds the median of each of each of the functional associations for any given pair of interactions p1->p2

-Input(s):
    p1, the name of the first protein we want to analyze. 
    p2, the name of the second protein we want to analyze.

-Output(s):
    The median of each of the functional associations for an interaction p1->p2
'''

def generate_median_fa_entries(p1, p2):
    #First, call validation function to make sure entry of p1->p2 is contained in the interactions dataframe
    if not validate_calculate_fis(p1,p2):
        print('\n')
        print('The interaction between',p1,'and',p2,'is not recorded!')
        return
    #We first locate the row number of the entry that contains interactions between p1 and p2
    index = interactions[(interactions['P1'] == p1) & (interactions['P2'] == p2)].index[0]
    #Create an empty list to store the median functional associations
    median_fa_entries = []
    #For each functional association list in the entry of p1->p2:
    for binaries in interactions.iat[index,3]:
        #First, filter the list to contain no -2's, since this means that the effect is not studied
        fa_entries_without_unknown = [fa for fa in binaries if fa!=-2]
        #If, after filtering, there are no values, the median is 0
        if len(fa_entries_without_unknown) == 0:
            median_fa_entries.append(0)
        #If, after filtering, there are values, find the median of the functional associations
        else:
            median_fa_entries.append(statistics.median(fa_entries_without_unknown))
    #Return list containing all median functional associations
    return (median_fa_entries)










'''
call_calculate_fis_add_csv_entry function

-Info: This function generates the FIABS_nw.csv, our final output csv file that contains the FIS and colors of edges

-Input:
    focus_num_of_fa: the number of the functional association that we want to generate FIS for; if we want to focus on all functional associations, this would be 0
    
-Output:
    No returned/printed output, but we populate an output csv file with each entry containing the following info: p1, p2, FIS for p1->p2, and the color of the edge p1->p2
'''

def call_calculate_fis_add_csv_entry(p1,p2,focus_num_of_fa):
    #We first call generate_median_fa_entries to get us the median functional associations for p1->p2
    median_fa_entries = generate_median_fa_entries(p1,p2)
    #If the median is positive, edge color is red. If median is negative, edge color is blue. Else, it is black
    fa_colors = ['red' if fa > 0 else 'blue' if fa < 0 else 'black' for fa in median_fa_entries]
    color = ""
    #If we are focusing on all functional associations, we must indicate the edge color based on the table given in the README file
    if focus_num_of_fa == 0:
        if len(set(fa_colors)) == 1:
            if fa_colors[0] == 'blue':
                color = "dark blue"
            elif fa_colors[0] == 'red':
                color = 'dark red'
            else:
                color = 'grey'
        else:
            if 'black' in fa_colors:
                if 'blue' in fa_colors:
                    color= 'light blue'
                else:
                    color = 'light red'
            else:
                color = 'green'
    #Else, we just return the color of the edge for the requested functional association
    else:
        color = fa_colors[focus_num_of_fa-1]
    #Take the absolute value of each median functional association in the median_fa_entries. 
    abs_median_fa_entries = list(map(abs, median_fa_entries))
    #If any of the medians are 0.5 (indecisive), we assign a weight of .0001
    if 0.5 in abs_median_fa_entries:
        #Each entry contains p1, p2, the FIS(found by multiplying median directionality with the lookup_table's functional association weight), and color
        csv_row = [p1, p2, pairwise_effect_table[(p1,p2)] * .0001, color]
    #Else, we use the lookup table to assign the appropriate functional association weight based on abs_median_fa_entries
    elif tuple(abs_median_fa_entries) in lookup_table:   
        #Each entry contains p1, p2, the FIS(found by multiplying median directionality with the lookup_table's functional association weight), and color
        csv_row = [p1, p2, pairwise_effect_table[(p1,p2)] * lookup_table[tuple(abs_median_fa_entries)], color]
        #Write out the row to our output csv file
        with open('FIABS_nw.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(csv_row)
    else:
        #If we weren't able to find the the configuration of median functional associations in our lookup table, we simply assign an FIS of 0
        csv_row = [p1, p2, 0, color]
        with open('FIABS_nw.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(csv_row)
          
            
          
            
          
          
        
'''
validate_calculate_fis function

-Info: This function validates that the interaction between p1 and p2 is in the "interactions" dataframe

-Input(s): p1, the name of the first protein we want to analyze. p2, the name of the second protein we want to analyze

-Output(s): 
    True, if an interaction between p1 and p2 exists in the "interactions" dataframe. 
    False if an interaction between p1 and p2 DOES NOT exist in the "interactions" dataframe. 
'''
def validate_calculate_fis(p1,p2):
     if (((interactions['P1'] == p1) & (interactions['P2'] == p2)).sum()) == 0:
         return False
     return True
        
             
        
        
    
'''
print_interaction_database function

-Info: This function prints the interactions dataframe

-Input(s): NA

-Output(s):
    - Printed dataframe to the console
'''
def print_interaction_database():
    print(interactions)
                                                                                                      

