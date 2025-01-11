from bs4 import BeautifulSoup
import requests
import csv

# URL of the page we want to scrape
url = 'https://realpython.github.io/fake-jobs/'
request = requests.get(url)
#request.content

soup = BeautifulSoup(request.text, 'html.parser')
# print(soup)

job_title = soup.find(class_='title is-5')
# print(job_title)
sub_title = soup.find(class_='subtitle is-6 company')
# print(sub_title)
location = soup.find(class_='location')
# print(location.text)
date = soup.find(class_='is small has text-grey')
# print(date.text)
sec_job = soup.find(class_="title is-5")
# print(sec_job)

all_jobs_title = soup.find_all(class_='title is-5')
# print(all_jobs_title)
#print(all_jobs_title[1])



container = soup.find(id='ResultsContainer')
# gives the list of all the divs with the class name 'column is-half'
job_divs = container.find_all(class_='column is-half')

data = []
for job in job_divs:
    # we are stripping the text to remove any extra white spaces
    # we are finding the first element with the class name 'title is-5' and then getting the text inside it
    # we are finding the first element with the class name 'subtitle is-6 company' and then getting the text inside it and so on 
    title = job.find(class_='title is-5').text
    company = job.find(class_='subtitle is-6 company').text
    location = job.find(class_='location').text.strip()
    date = job.find(class_='is-small has-text-grey').text.strip()
    #prints individuall
    # print(title.text)
    # print(company.text)
    # print(location.text)
    # print(date.text)

    # print(title, company, location, date)

    #appending the data to the list
    jobs = [title, company, location, date]
    data.append(jobs)
    
    print(data)

# saving in a csv file
with open(r'D:\Saylani\Cloud-Data-Engg\Filehandling\jobs.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Company', 'Location', 'Date'])
    writer.writerows(data)
