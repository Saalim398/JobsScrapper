"""
Cognifyz internship Task 6: Create a program for
interactive web scraping.

Objective: Fetch data from a website and
present it in a user-friendly way using a
simple web scraping library.


library used bs4 for web scrapping 

"""

from bs4 import BeautifulSoup
import requests

print("################################################################################################################################")
print('                                                     Welcome to job find')
print("################################################################################################################################")

try:
    option = int(input("Enter 1 to search for job and 0 to exit: "))
except ValueError:
    print("User input is not an integer, Try Again")
   
if option == 1:
    while(True):
        jobs = input('\nEnter job Title or type bye to exit: ')
        if jobs == 'bye':
            exit()
        try:
            
            link = requests.get(
                f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords={jobs}&txtLocation=',
                timeout=10
            )
            link.raise_for_status()  

        except requests.exceptions.Timeout:
            print("Error: The request timed out. Please try again later.")
            exit()

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            exit()

        soup = BeautifulSoup(link.content, 'lxml')

        job_title = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
        if not job_title:
            print("No job postings found for the given title.")
        else:
            for job in job_title:
                published_date = job.find('span', class_='sim-posted').span.text
                if 'few' in published_date:
                    company_name = job.find('h3', class_='joblist-comp-name').text.strip()
                    skills = job.find('span', class_='srp-skills').text.strip()
                    more_details = job.header.h2.a['href']
                    print(' ')
                    print(f'Company Name: {company_name}')
                    print(f'Required Skills: {skills}')
                    print(f'More Details: {more_details}')
                    print(' ')
elif option == 0:
    exit()
else:
    print("Error: Wrong input")