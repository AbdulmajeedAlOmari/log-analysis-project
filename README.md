# Log Analysis Project
You've been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running. You've been asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.

The program you write in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.

_This project is required for Full-Stack Nanodegree program._

It was developed by:
> Abdulmajeed Alomari

## Installation
- Download and install [Vagrant](https://www.vagrantup.com/downloads.html).
- Download and install [VirtualBox](https://www.virtualbox.org/wiki/Downloads).
- Download [FSND Virtual Machine](https://github.com/udacity/fullstack-nanodegree-vm).

## Prerequisites
- Having [python3](https://www.python.org/downloads/) installed.
- You need to use Terminal on Mac or Linux systems. On windows, you I recommend using [Git Bash](https://git-scm.com/downloads).
- You need to download the project's data "**newsdata.sql**" from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).

## Usage
Once you get the above software installed and the needed data downloaded:
1. Navigate to your **FSND Virtual Machine** folder and run the following commands:
```
cd vagrant
vagrant up
vagrant ssh
cd /vagrant
git clone https://github.com/AbdulmajeedAlOmari/log-analysis-project.git log-analysis-project
cd log-analysis-project
```
2. You need to install "**psycopg2**" module by running the following command: `pip3 install psycopg2`
3. Move the "**newsdata.sql**" to your project folder "**log-analysis-project**" folder.
4. Load the data from the “newsdata.sql” by using the following command: `psql -d news -f newsdata.sql`
5. Connect to the database using the command: `psql -d news`
6. Now, you can run the python script using the command: `python log-analysis.py`

## Sample Output
You can visit "[sample_output](./sample_output.txt)" to see the output of the python script "**log-analysis.py**"

## References
I used the following references to help me finish this project:
- [Join using Like operator](https://stackoverflow.com/questions/23276344/like-operator-in-inner-join-in-sql)
- [HTTP status codes](https://classroom.udacity.com/courses/ud303/lessons/6ff26dd7-51d6-49b3-9f90-41377bff4564/concepts/75becdb9-da2a-4fbf-9a30-5f3ccd1aa1d6)
- [Calculate percentage in an SQL query](https://stackoverflow.com/questions/770579/how-to-calculate-percentage-with-a-sql-statement)
- [Creating and using subqueries](https://community.modeanalytics.com/sql/tutorial/sql-subqueries/)
- [Format dates](https://stackoverflow.com/questions/2158347/how-do-i-turn-a-python-datetime-into-a-string-with-readable-format-date)
- [Round a number](https://www.tutorialspoint.com/python/number_round.htm)

## Licences
