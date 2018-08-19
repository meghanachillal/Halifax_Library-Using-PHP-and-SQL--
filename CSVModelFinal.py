import json
import csv
import random

Article_Journal_Collections = {"Article":''}
Article_mongo_list = []

def main():

    # initialize variables
    url_path = 'C:\\Users\\megha\\OneDrive\\Desktop\\DBProject\\articles_input.json'

    #Output csv files
    Author = 'C:\\Users\\megha\\OneDrive\\Desktop\\DBProject\\Author.csv'
    Article = 'C:\\Users\\megha\\OneDrive\\Desktop\\DBProject\\Article.csv'
    Magazine = 'C:\\Users\\megha\\OneDrive\\Desktop\\DBProject\\Magazine.csv'
    MagazineVolume = 'C:\\Users\\megha\\OneDrive\\Desktop\\DBProject\\MagazineVolume.csv'

    author_file = open(Author, 'w', newline='')
    csv_author_writer = csv.writer(author_file, delimiter=";")
    csv_author_writer.writerow(["fname", "lname", "email"])

    article_file = open(Article, 'w', newline='')
    csv_article_writer = csv.writer(article_file, delimiter=";")
    csv_article_writer.writerow(["articleId", "title", "pages","volumeNumber"])

    magazine_file = open(Magazine, 'w', newline='')
    csv_magazine_writer = csv.writer(magazine_file, delimiter=";")
    csv_magazine_writer.writerow(["magazineId", "name"])

    magazineVolume_file = open(MagazineVolume, 'w', newline='')
    csv_magazineVolume_writer = csv.writer(magazineVolume_file, delimiter=";")
    csv_magazineVolume_writer.writerow(["magazineId", "volumeNumber", "year"])

    # get data from Article JSON
    data = open(url_path,'r')

    articleId=1
    magazineId=4

    for everyAuthor in data.readlines():
        try:

            everyAuthor = json.loads(everyAuthor)
            author = everyAuthor['author']
            checkAuthor = type(author)
            if checkAuthor is list:
                authorName = '['
                for multipleAuthors in author:
                    fname, lname, email = nameManipulation(str(multipleAuthors['ftext']))
                    csv_author_writer.writerow([fname, lname, email])
                    authorName = str(authorName +'|'+str(multipleAuthors['ftext']))
                author = authorName + ']'
            else:
                author = str(everyAuthor['author']['ftext'])
                fname,lname,email = nameManipulation(author)
                csv_author_writer.writerow([fname, lname, email])

            articleTitle = str(everyAuthor['title']['ftext'])
            pages = str(everyAuthor['pages']['ftext'])
            year = str(everyAuthor['year']['ftext'])
            volumeNumber = str(everyAuthor['volume']['ftext'])
            journalName = str(everyAuthor['journal']['ftext'])

            Article_mongo_list.append(dict(zip(["Authors", "Article title","Journal name","Volume number","Pages", "Year"],
                                               [author,articleTitle,journalName,volumeNumber, pages, year])))


            csv_article_writer.writerow([articleId, articleTitle, pages, volumeNumber])
            csv_magazine_writer.writerow([magazineId, journalName])
            csv_magazineVolume_writer.writerow([magazineId, volumeNumber, year])

            articleId+=1
            magazineId+=1

        except Exception as e:
            e = e.args
            if (e == ('pages',)) or (e==('author',)):
                pass
            else:
                pass


    # Close all the CSV files
    author_file.close()
    article_file.close()
    magazine_file.close()
    magazineVolume_file.close()

    Article_Journal_Collections['Article'] = Article_mongo_list
    with open('C:\\Users\\megha\\OneDrive\\Desktop\\DBProject\\articles.json', 'w') as jsonFile:
        json.dump(Article_Journal_Collections['Article'], jsonFile)


def nameManipulation(fullName):
    emailDomains = ['@gmail.com','@ymail.com','@smu.ca','@hotmail.edu','@dkg.com']
    check = False
    fname = ''
    lname = ''
    for names in fullName.split():
        if (check):
            lname = lname+names+' '
        else:
            fname = names
        check = True

    email = fname+'.'+lname.replace(' ','_')+random.choice(emailDomains)

    return fname,lname,email

if __name__ == "__main__":
    main()
