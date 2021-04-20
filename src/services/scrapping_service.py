import json

from bs4 import BeautifulSoup
from requests import get

from src.models import db, Scrapping
import datetime
from src.constants import *



class ScrappingService:
	def __init__(self):
		pass
	
	def scrap_data(self, moviegenre):
		director = []
		stars = []
		responseList = []
		numberOfMoviesPaginated = [0, 50]
		for numberOfMoviePerPage in numberOfMoviesPaginated:
			url = "https://www.imdb.com/search/title/?genres={}&title_type=feature&start={}&explore=genres".format(
				moviegenre, numberOfMoviePerPage)
			page = get(url)
			soup = BeautifulSoup(page.content, 'lxml')
			
			content = soup.find(id=maincontent)
			movieFrame = content.find_all("div", class_=movieFramecontentClass)
			
			for movie in movieFrame:
				"""finding movie Titile"""
				movieFirstLine = movie.find("h3", class_=movieElementClass)
				movieTitle = movieFirstLine.find("a").text
				
				"""finding movie year"""
				movieReleaseYear = movieFirstLine.find("span", {"class": movieReleaseYearClass}).text
				
				"""finding movie runtime"""
				try:
					runTime = movie.find("span", class_=movieRuntime).text[:-4]
				except:
					runtTime = ""
				
				"""finding movie genre"""
				genre = movie.find("span", class_=movieGenre).text.rstrip().replace("\n", "").split(",")
				genre = ','.join(str(e) for e in genre)
				
				"""finding movie rating"""
				try:
					rating = movie.find("strong").text
				except:
					rating = ''
				
				"""finding movie cast & director"""
				cast = movie.find("p", class_="")
				
				try:
					casts = cast.text.replace("\n", "").split('|')
					casts = [x.strip() for x in casts]
					casts = [casts[i].replace(j, "") for i, j in enumerate(["Director:", "Stars:"])]
					director.append(casts[0])
					directorStr = (','.join(str(e) for e in director)).replace("Directors:", "")
					stars.append([x.strip() for x in casts[1].split(",")])
					flat_list_of_stars = [item for sublist in stars for item in sublist]
					StarsStr = ','.join(str(e) for e in flat_list_of_stars)
				except:
					casts = cast.text.replace("\n", "").strip()
					director.append('')
					directorStr = (','.join(str(e) for e in director)).replace("Directors:", "")
					stars.append([x.strip() for x in casts.split(",")])
					flat_list_of_stars = [item for sublist in stars for item in sublist]
					StarsStr = ','.join(str(e) for e in flat_list_of_stars)
				
				"""scrapping movie Image URL"""
				url = movie.find("img", {"class": imageClass})
				urllink = url.attrs[imageClass]
				
				result = {"title": str(movieTitle),
				          "rating": str(rating),
				          "director": str(directorStr),
				          "actors": str(StarsStr),
				          "genre": str(genre),
				          "runtime": str(runTime),
				          "url": str(urllink),
				          "type": str(moviegenre),
				          "ReleaseYear": str(movieReleaseYear)}
				director = []
				stars = []
				responseList.append(result)
			# datetime.date.today().strftime("%d-%m-%y")
		# response_after_db_insertion = self._post_data_to_db(responseList)
		return self._post_data_to_db(responseList)
	
	
	def _post_data_to_db(self, responseList):
		scrapped_entries = []
		for eachObject in responseList:
			new_entry = Scrapping(title=eachObject['title'],
			                      rating=eachObject['rating'],
			                      director=eachObject['director'],
			                      actors=eachObject['actors'],
			                      genre=eachObject['genre'],
			                      runtime=eachObject['runtime'],
			                      url=eachObject['url'],
			                      type=eachObject['type'],
			                      ReleaseYear=eachObject['ReleaseYear'],
			                      created=datetime.date.today().strftime("%m-%d-%y")
			                      )
			scrapped_entries.append(new_entry)
		db.session.add_all(scrapped_entries)
		db.session.commit()
		return responseList
	
	
	
	def get_scrapped_data_from_db(self,date,type, keyword=None ):
		from sqlalchemy import or_, and_
		if (keyword != None):
			resultDateFiltered = Scrapping.query.filter(and_(Scrapping.created == date), (Scrapping.type == type)).filter(or_(Scrapping.director.like('%' + keyword + '%'), Scrapping.actors.like('%' + keyword + '%'), Scrapping.title.like('%' + keyword + '%'), Scrapping.genre.like('%' + keyword + '%')))	# if(movieName!=None):
			resultdataofMovie = [Scrapping.serialize(record) for record in resultDateFiltered]
		else:
			resultDateFiltered = Scrapping.query.filter(and_(Scrapping.created == date), (Scrapping.type == type))
			resultdataofMovie = [Scrapping.serialize(record) for record in resultDateFiltered]

		records_filtered = len(resultdataofMovie)
		totalRecords = len(Scrapping.query.all())
		return resultdataofMovie, records_filtered, totalRecords
		