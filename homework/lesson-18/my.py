import pandas as pd

# Datasetni o‘qiymiz
df = pd.read_csv("task\\stackoverflow_qa.csv")

# 1. Find all questions created before 2014
df['creationdate'] = pd.to_datetime(df['creationdate'])
before_2014 = df[df['creationdate'].dt.year < 2014]
print("Questions before 2014:\n", before_2014, "\n")

# 2. Questions with score more than 50
score_above_50 = df[df['score'] > 50]
print("Score > 50:\n", score_above_50, "\n")

# 3. Questions with score between 50 and 100
score_between = df[(df['score'] >= 50) & (df['score'] <= 100)]
print("Score between 50 and 100:\n", score_between, "\n")

# 4. Questions answered by Scott Boston
answered_by_scott = df[df['ans_name'] == "Scott Boston"]
print("Answered by Scott Boston:\n", answered_by_scott, "\n")

# 5. Questions answered by any of 5 users
users = ["Scott Boston", "Unutbu", "Mike Pennington", "Demitri", "doug"]
answered_by_users = df[df['ans_name'].isin(users)]
print("Answered by 5 users:\n", answered_by_users, "\n")

# 6. Questions created between March 2014 and Oct 2014 by Unutbu and score < 5
mask = (
    (df['creationdate'] >= "2014-03-01") & 
    (df['creationdate'] <= "2014-10-31") & 
    (df['ans_name'] == "Unutbu") & 
    (df['score'] < 5)
)
filtered = df[mask]
print("Between Mar-Oct 2014, answered by Unutbu, score < 5:\n", filtered, "\n")

# 7. Questions with score between 5 and 10 OR viewcount > 10000
score_or_views = df[((df['score'] >= 5) & (df['score'] <= 10)) | (df['viewcount'] > 10000)]
print("Score between 5-10 or viewcount > 10000:\n", score_or_views, "\n")

# 8. Questions not answered by Scott Boston
not_scott = df[df['ans_name'] != "Scott Boston"]
print("Not answered by Scott Boston:\n", not_scott, "\n")
# Titanic dataset
titanic_df = pd.read_csv("task\\titanic.csv")

# 1. Female passengers in Class 1 with Ages between 20 and 30
female_class1 = titanic_df[(titanic_df['Sex'] == 'female') & (titanic_df['Pclass'] == 1) & 
                           (titanic_df['Age'].between(20, 30))]
print("Female Class 1 Age 20-30:\n", female_class1, "\n")

# 2. Passengers who paid more than $100
paid_over_100 = titanic_df[titanic_df['Fare'] > 100]
print("Fare > 100:\n", paid_over_100, "\n")

# 3. Passengers who survived and were alone (SibSp=0, Parch=0)
survived_alone = titanic_df[(titanic_df['Survived'] == 1) & 
                            (titanic_df['SibSp'] == 0) & (titanic_df['Parch'] == 0)]
print("Survived and Alone:\n", survived_alone, "\n")

# 4. Passengers embarked from 'C' and paid more than $50
embarked_c = titanic_df[(titanic_df['Embarked'] == 'C') & (titanic_df['Fare'] > 50)]
print("Embarked from C and Fare > 50:\n", embarked_c, "\n")

# 5. Passengers with both SibSp > 0 and Parch > 0
with_family = titanic_df[(titanic_df['SibSp'] > 0) & (titanic_df['Parch'] > 0)]
print("With both siblings/spouses and parents/children:\n", with_family, "\n")

# 6. Passengers aged 15 or younger who did not survive
young_not_survived = titanic_df[(titanic_df['Age'] <= 15) & (titanic_df['Survived'] == 0)]
print("Age <= 15 and not survived:\n", young_not_survived, "\n")

# 7. Passengers with cabins and Fare > 200
cabin_and_fare = titanic_df[titanic_df['Cabin'].notna() & (titanic_df['Fare'] > 200)]
print("Cabin not null and Fare > 200:\n", cabin_and_fare, "\n")

# 8. Passengers with odd-numbered PassengerId
odd_passengerid = titanic_df[titanic_df['PassengerId'] % 2 == 1]
print("Odd Passenger IDs:\n", odd_passengerid, "\n")

# 9. Passengers with unique ticket numbers
unique_tickets = titanic_df[titanic_df['Ticket'].duplicated(keep=False) == False]
print("Unique tickets:\n", unique_tickets, "\n")

# 10. Female passengers with 'Miss' in name and in Class 1
miss_class1 = titanic_df[(titanic_df['Sex'] == 'female') & 
                         (titanic_df['Name'].str.contains("Miss")) & 
                         (titanic_df['Pclass'] == 1)]
print("Miss in Class 1:\n", miss_class1, "\n")
