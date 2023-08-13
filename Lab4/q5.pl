/*
Prolog is commonly used in implementing expert systems. In simple words, an expert system emulates the decision-making 
ability of a human expert. In this question you have to define a set of rules that together work as a very simple expert
 system to give advice on what type of lenses (if any) should be prescribed for a patient.

First create a new knowledge base and include the following predicates in it:

normal_tear_rate(RATE) :- RATE >= 5.
low_tear_rate(RATE) :- RATE < 5.

young(AGE) :- AGE < 45.
Now add a new predicate of the form diagnosis(Recommend, Age, Astigmatic, Tear_Rate) to the knowledge base where the 
arguments are:

Recommend is either hard_lenses, soft_lenses, or no_lenses;
Age will be an integer;
Astigmatic will be either yes or no (note that these are atoms 'yes' and 'no' not true or false.); and
Tear_Rate will be a positive integer.
The predicate must be the translation of the following natural-language rules to logic:

If the patient is young and has a normal tear rate then the type of lenses will depend on astigmatism. If the 
patient is astigmatic then hard lenses must be recommended, otherwise soft lenses.
If the person has a low tear rate then 'no lenses' must be recommended.
Once finished, paste the entire knowledge base into the answer box.

Note that there are some questions (queries) that this expert system cannot answer. For example it cannot 
recommend anything for people who are over 45 years old and do not have low tear rate.
*/

/* tear rate related clauses */
normal_tear_rate(RATE) :- RATE >= 5.
low_tear_rate(RATE) :- RATE < 5.

/* age-related clauses */
young(AGE) :- AGE < 45.

diagnosis(Recommend, Age, Astigmatic, Tear_Rate) :- Recommend = hard_lenses, young(Age), Astigmatic = yes, normal_tear_rate(Tear_Rate).
diagnosis(Recommend, Age, Astigmatic, Tear_Rate) :- Recommend = soft_lenses, young(Age), Astigmatic = no, normal_tear_rate(Tear_Rate).
diagnosis(Recommend, Age, Astigmatic, Tear_Rate) :- Recommend = no_lenses, low_tear_rate(Tear_Rate).
