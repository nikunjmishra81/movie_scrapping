from flask import Blueprint, request, jsonify

from src.constants import *
from src.services.scrapping_service import ScrappingService
db_endpoint = Blueprint('db', __name__)


@db_endpoint.route('/ping', methods=[HTTP_GET])
def ping():
    return "Scrapping microservice up and running"



@db_endpoint.route('/dataextract', methods=[HTTP_POST, HTTP_GET])
def extractinformation():
    scrapping_service = ScrappingService()
    if request.method == HTTP_POST:
        genre = request.args.get('genre', None)
        if(genre not in GENRES or genre== None):
            return jsonify("Invalid Genre, Please input from Specified genres Only"),400
        else:
            responseFromScrappingService = scrapping_service.scrap_data(genre)
            return jsonify(responseFromScrappingService)
    else:
        date = request.args.get('date', None)
        type = request.args.get('type', None)
        keyword = request.args.get('keyword', None)
        if (date == None or type == None):
            return jsonify("Please enter Date and Type"), 400
        responseFromScrappingService, records_filtered, totalRecords = scrapping_service.get_scrapped_data_from_db(date,type, keyword=keyword)
        return jsonify({"records_filtered":records_filtered, "records_total":totalRecords, "responseFromScrappingService" : responseFromScrappingService})
    
