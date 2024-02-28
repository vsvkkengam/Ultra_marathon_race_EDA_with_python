# %%
#Importing libraries 

import pandas as pd
import seaborn as sns

# %% [markdown]
# ## An ultramarathon, also called ultra distance or ultra running, is any footrace longer than the traditional marathon length of 42.195 kilometres (26 mi 385 yd). Various distances are raced competitively, from the shortest common ultramarathon of 31 miles (50 km) to over 200 miles (320 km). 50k and 100k are both World Athletics record distances, but some 100 miles (160 km) races are among the oldest and most prestigious events, especially in North America.
# 
# ## The data in this file is a large collection of ultra-marathon race records registered between 1798 and 2022 (a period of well over two centuries) being therefore a formidable long term sample. All data was obtained from public websites.
# 
# ## Despite the original data being of public domain, the race records, which originally contained the athlete´s names, have been anonymized to comply with data protection laws and to preserve the athlete´s privacy. However, a column Athlete ID has been created with a numerical ID representing each unique runner (so if Antonio Fernández participated in 5 races over different years, then the corresponding race records now hold his unique Athlete ID instead of his name). This way I have preserved valuable information.
# 
# ## The dataset contains 7,461,226 ultra-marathon race records from 1,641,168 unique athletes.

# %%
df = pd.read_csv("D:\Desktop\VS\Datasets\TWO_CENTURIES_OF_UM_RACES.csv")

# %%
##inspecting the data
df.head()

# %%
df.shape

# %%
df.dtypes

# %% [markdown]
# ## Cleaning the data

# %%
#Only want usa reaces, 50k or 50mi, 2020

# %%
#Step: 1 > showing 50mi or 50k

#50k

df[df['Event distance/length'] == '50k']

# %%
#50km
df[df['Event distance/length'] == '50km']

# %%
#50m
df[df['Event distance/length'] == '50m']

# %%
#50Mi
df[df['Event distance/length'] == '50mi']

# %%
#combining 50 km and 50 mi with isin
df[df['Event distance/length'].isin(['50km', '50mi'])]

# %%
df[(df['Event distance/length'].isin(['50km', '50mi'])) & (df['Year of event'] == 2020)]

# %%
df[df['Event name'] == 'Everglades 50 Mile Ultra Run (USA)']

# %%
df[df['Event name'] == 'Everglades 50 Mile Ultra Run (USA)']['Event name'].str.split('(').str.get(1).str.split(')').str.get(0)

# %%
df[df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0) == 'USA']

# %%
#combining all the filters
df[
    (df['Event distance/length'].isin(['50km', '50mi'])) & 
    (df['Year of event'] == 2020) &
    (df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0) == 'USA')
]



# %%
df_filterd = df[
    (df['Event distance/length'].isin(['50km', '50mi'])) & 
    (df['Year of event'] == 2020) &
    (df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0) == 'USA')
]

df_filterd.head(10)

# %%
df_filterd.shape

# %%
#remove USA from event name
df_filterd['Event name'] = df_filterd['Event name'].str.split('(').str.get(0)

# %%
df_filterd.head()

# %%
#calculates athlets age
df_filterd['Age'] = 2020 - df_filterd['Athlete year of birth']

# %%
df_filterd['Age']

# %%
#remove h from athlets performance
df_filterd['Athlete performance'] = df_filterd['Athlete performance'].str.split(' ').str.get(0)

# %%
df_filterd.head(5)

# %%
df_filterd['Age'] = df_filterd['Age'].astype(str)

# %%
df_filterd['Age'] = df_filterd['Age'].str.split('.')

# %%
df_filterd['Age'] = df_filterd['Age'].str.get(0)

# %%
df_filterd['Age']

# %%
df_filterd.head(3)

# %%
df_filterd.isna().sum()

# %%
df_filterd.head(3) 

# %%
#dropping some columns
df_filterd = df_filterd.drop(['Athlete club', 'Athlete year of birth','Athlete age category'], axis = 1)
df_filterd.head(3)

# %%
#checking null values
df_filterd.isna().sum()

# %%
df_filterd.dropna()

# %%
df_filterd.shape

# %%
#checking duplicates
df_filterd.duplicated().sum()

# %%
df_filterd[df_filterd.duplicated() == True]

# %%
#reset index
df_filterd.reset_index(drop = True)

# %%
df_filterd.dtypes

# %%
df_filterd['Age'] = df_filterd['Age'].astype(float).astype('Int64')

# %%
df_filterd['Event dates'] = pd.to_datetime(df_filterd['Event dates'], format='%d.%m.%y', errors='coerce')

# %%
df_filterd['Athlete average speed'] = df_filterd['Athlete average speed'].astype(float)

# %%
df_filterd.head

# %%
# renaming columns


# Year of event                         
# Event dates                  
# Event name                          
# Event distance/length            
# Event number of finishers          
# Athlete performance                  
# Athlete country                      
# Athlete gender                       
# Athlete average speed               
# Athlete ID                            
# Age                                   

# %%
df_filterd = df_filterd.rename(columns = 
    { 
        'Year of event':'year',
        'Event dates':'race_date',
        'Event name':'race_name',
        'Event distance/length':'race_length',
        'Event number of finishers':'num_of_finishers',
        'Athlete performance':'athlete_performance',
        'Athlete country':'athlete_country',
        'Athlete gender':'athlete_gender',
        'Athlete average speed':'athlete_avg_speed',
        'Athlete ID':'athlete_id',
        'Age':'age'
    }
)


# %%
df_filterd.head(1)

# %%
#reorder columns 
df_reorderd = df_filterd[['year','race_date','race_name','race_length','num_of_finishers','athlete_id','age','athlete_gender','athlete_country','athlete_performance','athlete_avg_speed']]

# %%
df_reorderd.head()

# %%
df_reorderd = df_reorderd.drop(['race_date'], axis = 1)

# %%
df_reorderd.head(1)

# %%
df_reorderd[df_reorderd['race_name'] == 'Everglades 50 Mile Ultra Run ']

# %%
#222509
df_reorderd[df_reorderd['athlete_id'] == 222509]

# %% [markdown]
# ## charts and graphs 

# %%
sns.histplot(df_reorderd['race_length'])

# %%
sns.histplot(df_reorderd, x='race_length', hue = 'athlete_gender')

# %%
sns.displot(df_reorderd[df_reorderd['race_length'] == '50mi']['athlete_avg_speed'])

# %%
sns.violinplot(data = df_reorderd, x = 'race_length', y = 'athlete_avg_speed', hue = 'athlete_gender', split = True, inner = 'quart', inlinewith=1)

# %%
#differenc in race for male and female for 50k and 50mi

df_reorderd.groupby(['race_length', 'athlete_gender'])['athlete_avg_speed'].mean()

# %%


# %%


# %%



