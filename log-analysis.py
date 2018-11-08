import psycopg2
import datetime


DBNAME = "news"


# Start connection to database:
connection = psycopg2.connect(database=DBNAME)


def fetch_from_database(query):
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return data


""" Question 1 - What are the most popular three articles of all time? """
mostPopularArticles = fetch_from_database("""
    SELECT articles.title, count(log.ip) AS numberOfViews
    FROM articles
    JOIN log
    ON log.path LIKE CONCAT('%', articles.slug)
    GROUP BY articles.id
    ORDER BY numberOfViews DESC
    LIMIT 3
""")


""" Question 2 - Who are the most popular article authors of all time? """
mostPopularAuthors = fetch_from_database("""
    SELECT authors.name, count(log.ip) as numberOfViews
    FROM authors, articles, log
    WHERE authors.id = articles.author
            AND log.path LIKE CONCAT('%', articles.slug)
    GROUP BY authors.id
    ORDER BY numberOfViews DESC
""")


""" Question 3 - On which days did more than 1% of requests lead to errors? """
dayErrors = fetch_from_database("""
    SELECT *
    FROM
        (
            SELECT
                totalRequests.inner_date,
                (100.0 * errorRequests.error_requests)
                / totalRequests.total_requests AS percentage
            FROM
                (
                    SELECT
                        DATE(time) AS inner_date,
                        count(*) AS total_requests
                    FROM log
                    GROUP BY DATE(time)
                ) AS totalRequests
                JOIN
                (
                    SELECT
                        DATE(time) AS inner_date,
                        count(*) AS error_requests
                    FROM log
                    WHERE status LIKE '4%' OR status LIKE '5%'
                    GROUP BY DATE(time)
                ) AS errorRequests
                ON totalRequests.inner_date = errorRequests.inner_date
            ORDER BY percentage DESC
            LIMIT 10
        ) AS query
    WHERE query.percentage > 1;
""")


print("The three most popular articles:")
# Print most popular Articles
for article in mostPopularArticles:
    title = article[0]
    numOfViews = article[1]
    print("\"{}\" - {} views".format(title, numOfViews))


# Seperator
print("\n-------------------------------\n")


print("The most popular authors:")
# Print most popular Authors
for author in mostPopularAuthors:
    name = author[0]
    numOfViews = author[1]
    print("{} - {} views".format(name, numOfViews))


# Seperator
print("\n-------------------------------\n")


print("Days with more than 1% errors:")
# Print the days that has at least 1% errors
for log in dayErrors:
    date = log[0].strftime("%B %d, %Y")
    # I will round the number to 2 digit from the decimal point
    # Because we only want an approximation of the errors
    errorPercentage = round(log[1], 2)
    print("{} - {}% errors".format(date, errorPercentage))


# Close database connection:
connection.close()


"""
REFERENCES:
You can go to the README.md to see the references.
"""
