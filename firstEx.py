import comp_prob_inference
from simpsons_paradox_data import *
import matplotlib.pyplot as plt

"""
n = 10000
headsSoFar = 0
fractionOfHeads = []

for i in range(n):
    if comp_prob_inference.flip_fair_coin() == 'heads':
        headsSoFar += 1
    fractionOfHeads.append(headsSoFar/(i+1))

plt.figure(figsize=(8, 4))
plt.plot(range(1, n+1), fractionOfHeads)
plt.xlabel('Number of flips')
plt.ylabel('Fraction of heads')

plt.show()

prob_table = {('sunny', 'hot'): 3/10,
('sunny', 'cold'): 1/5,
('rainy', 'hot'): 1/30,
('rainy', 'cold'): 2/15,
('snowy', 'hot'): 0,
('snowy', 'cold'): 1/3}


print(prob_table[('rainy', 'cold')])



###    Simpson's Paradox    ###     

#Marginalize out department
joint_prob_gender_admission = joint_prob_table.sum(axis=1)

#Probability of being admitted if the subject is female

P_A|G = P_G,A(f,a) / P_G(f)

P_G(f) = P_G,A(female, admitted) + P_G,A(female, rejected)

1. Marginalize 
2. Rescale the marginal probability
3. Compute conditional probability

#1.
female_only = joint_prob_gender_admission[gender_mapping['female']]
#2. & #3.
prob_admission_given_female = female_only / np.sum(female_only)
prob_admission_given_female_dict = dict(zip(admission_labels, prob_admission_given_female))

print(prob_admission_given_female_dict)

#Find the same prob but for males
male_only = joint_prob_gender_admission[gender_mapping['male']]
prob_admission_given_male = male_only / np.sum(male_only)
prob_admission_given_male_dict = dict(zip(admission_labels, prob_admission_given_male))

print(prob_admission_given_male_dict)

#Condition on admission decision
admitted_only = joint_prob_gender_admission[:, admission_mapping['admitted']]
prob_gender_given_admitted = admitted_only / np.sum(admitted_only)
prob_gender_given_admitted_dict = dict(zip(gender_mapping, prob_gender_given_admitted))

print(prob_gender_given_admitted_dict)
"""
#Finding out which departments favour men over women
#Department A
female_A_only = joint_prob_table[gender_mapping['female'], department_mapping['A']]
prob_admission_given_female_and_A = female_A_only / np.sum(female_A_only)
prob_admission_given_female_and_A_dict = dict(zip(admission_labels, prob_admission_given_female_and_A))



male_A_only = joint_prob_table[gender_mapping['male'], department_mapping['A']]
prob_admission_given_male_and_A = male_A_only / np.sum(male_A_only)
prob_admission_given_male_and_A_dict = dict(zip(admission_labels, prob_admission_given_male_and_A))



#Department B
female_B_only = joint_prob_table[gender_mapping['female'], department_mapping['B']]
prob_admission_given_female_and_B = female_B_only / np.sum(female_B_only)
prob_admission_given_female_and_B_dict = dict(zip(admission_labels, prob_admission_given_female_and_B))



male_B_only = joint_prob_table[gender_mapping['male'], department_mapping['B']]
prob_admission_given_male_and_B = male_B_only / np.sum(male_B_only)
prob_admission_given_male_and_B_dict = dict(zip(admission_labels, prob_admission_given_male_and_B))



#Department C
female_C_only = joint_prob_table[gender_mapping['female'], department_mapping['C']]
prob_admission_given_female_and_C = female_C_only / np.sum(female_C_only)
prob_admission_given_female_and_C_dict = dict(zip(admission_labels, prob_admission_given_female_and_C))



male_C_only = joint_prob_table[gender_mapping['male'], department_mapping['C']]
prob_admission_given_male_and_C = male_C_only / np.sum(male_C_only)
prob_admission_given_male_and_C_dict = dict(zip(admission_labels, prob_admission_given_male_and_C))


#Department D
female_D_only = joint_prob_table[gender_mapping['female'], department_mapping['D']]
prob_admission_given_female_and_D = female_D_only / np.sum(female_D_only)
prob_admission_given_female_and_D_dict = dict(zip(admission_labels, prob_admission_given_female_and_D))


male_D_only = joint_prob_table[gender_mapping['male'], department_mapping['D']]
prob_admission_given_male_and_D = male_D_only / np.sum(male_D_only)
prob_admission_given_male_and_D_dict = dict(zip(admission_labels, prob_admission_given_male_and_D))



#Department E
female_E_only = joint_prob_table[gender_mapping['female'], department_mapping['E']]
prob_admission_given_female_and_E = female_E_only / np.sum(female_E_only)
prob_admission_given_female_and_E_dict = dict(zip(admission_labels, prob_admission_given_female_and_E))



male_E_only = joint_prob_table[gender_mapping['male'], department_mapping['E']]
prob_admission_given_male_and_E = male_E_only / np.sum(male_E_only)
prob_admission_given_male_and_E_dict = dict(zip(admission_labels, prob_admission_given_male_and_E))



#Department F
female_F_only = joint_prob_table[gender_mapping['female'], department_mapping['F']]
prob_admission_given_female_and_F = female_F_only / np.sum(female_F_only)
prob_admission_given_female_and_F_dict = dict(zip(admission_labels, prob_admission_given_female_and_F))



male_F_only = joint_prob_table[gender_mapping['male'], department_mapping['F']]
prob_admission_given_male_and_F = male_F_only / np.sum(male_F_only)
prob_admission_given_male_and_F_dict = dict(zip(admission_labels, prob_admission_given_male_and_F))



for i in department_labels:
    for j in gender_labels:
        restricted = joint_prob_table[gender_mapping[j], department_mapping[i]]
        print(i, j, dict(zip(admission_labels, restricted / np.sum(restricted)))['admitted'])


"""
Somehow, it seems that when we marginalized out the department, 
the gender bias is going one direction, yet when looking at the specific departments, 
most departments seem to be having the bias go the other direction!

Take-away message: We have to be very careful when interpreting conditional probabilities! 
Also, marginalization (which lumps different groups of data together, where here the groups are departments)
 can reverse trends that appear in specific groups!
"""