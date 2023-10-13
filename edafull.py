import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("C:/Users/Pon Karthik/Downloads/data.csv",encoding='utf-8')

while True:
    print("Choose an analysis option:")
    print("1. Time Trends Analysis")
    print("2. Identify High-Risk Regions")
    print("3. Understand Attack Characteristics")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        # Code for Time Trends Analysis
        # Convert the 'iyear' column to datetime format
        df['iyear'] = pd.to_datetime(df['iyear'], format='%Y')

        # Extract year from the 'iyear' column
        df['year'] = df['iyear'].dt.year

        # Count the number of terrorist incidents per year
        incident_count_per_year = df['year'].value_counts().sort_index()

        # Create a line plot to visualize the time trend
        plt.figure(figsize=(12, 6))
        sns.barplot(x=incident_count_per_year.index, y=incident_count_per_year.values)
        plt.title('Terrorist Incidents Over Time')
        plt.xlabel('Year')
        plt.ylabel('Number of Incidents')
        plt.xticks(rotation=45)
        plt.show()

        pass
    elif choice == '2':
        # Code for Identifying High-Risk Regions
        df = pd.read_csv('globalterrorismdb_0718dist.csv', encoding='ISO-8859-1')

        # Count the number of terrorist incidents by country
        incident_count_by_country = df['country_txt'].value_counts()

        # Visualize the top 10 countries with the most incidents
        top_10_countries = incident_count_by_country.head(10)

        # Create a bar plot to visualize high-risk regions
        plt.figure(figsize=(12, 6))
        sns.barplot(x=top_10_countries.values, y=top_10_countries.index, palette='viridis')
        plt.title('Top 10 Countries with the Most Terrorist Incidents')
        plt.xlabel('Number of Incidents')
        plt.ylabel('Country')
        plt.show()
        pass
    elif choice == '3':
        # Code for Understanding Attack Characteristics
        # Load the dataset
        df = pd.read_csv('globalterrorismdb_0718dist.csv', encoding='ISO-8859-1')

        # Count the number of incidents by attack type
        attack_type_count = df['attacktype1_txt'].value_counts()

        # Count the number of incidents by weapon type
        weapon_type_count = df['weaptype1_txt'].value_counts()

        # Count the number of incidents by target type
        target_type_count = df['targtype1_txt'].value_counts()

        # Visualize attack characteristics
        plt.figure(figsize=(18, 8))
        plt.subplot(131)
        sns.barplot(x=attack_type_count.values, y=attack_type_count.index, palette='Set2')
        plt.title('Attack Types')
        plt.xlabel('Number of Incidents')

        plt.subplot(132)
        sns.barplot(x=weapon_type_count.values, y=weapon_type_count.index, palette='Set2')
        plt.title('Weapon Types')
        plt.xlabel('Number of Incidents')

        plt.subplot(133)
        sns.barplot(x=target_type_count.values, y=target_type_count.index, palette='Set2')
        plt.title('Target Types')
        plt.xlabel('Number of Incidents')

        plt.tight_layout()
        plt.show()
        pass
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")

    continue_option = input("Do you want to continue (yes/no)? ").lower()
    if continue_option != 'yes':
        print("Exiting the program.")
        break
