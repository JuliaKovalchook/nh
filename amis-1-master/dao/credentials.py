import os

username = 'iexwdzoullwiar'
password = '2290aaaa9b20d4efff8ef58d753a79fd70582a863da64f6b2d3dbfe5b2e61d5a'
host = 'ec2-54-225-116-36.compute-1.amazonaws.com'
port = '5432'
database = 'd6mf3i3dd3jgk5'
DATABASE_URI = os.getenv("DATABASE_URL",
                         'postgres://iexwdzoullwiar:2290aaaa9b20d4efff8ef58d753a79fd70582a863da64f6b2d3dbfe5b2e61d5a@ec2-54-225-116-36.compute-1.amazonaws.com:5432/d6mf3i3dd3jgk5')
