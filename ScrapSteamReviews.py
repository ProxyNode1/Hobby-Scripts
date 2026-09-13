import steamreviews as SteamReviews
import csv
import time
import json


RequestParams = dict()

RequestParams['review_type'] = 'negative'
RequestParams['purchase_type'] = 'steam'
RequestParams['language'] = 'english'
RequestParams['day_range'] = "365"

MinPlayTimeInMinute = 60

# written_during_early_access
# playtime_forever
# weighted_vote_score


AppIds = [1716740]

#ReviewDict, QueryCount = SteamReviews.download_reviews_for_app_id(AppIds, chosen_request_params=RequestParams)

global CSVWriter

while(not SteamReviews.download_reviews_for_app_id_batch(
    AppIds,
    chosen_request_params=RequestParams)):
    time.sleep(5)


for Id in AppIds:
    with open("./data/review_" + str (Id) + ".json", 'r') as Data:    
        JsonData = json.load(Data)
        #print(JsonData)
        
        ReviewData = JsonData["reviews"]

        global TempText
        TempText = ""

        CSVFile = open("SteamReviewData_" + str(Id) + ".csv", 'a', newline = "", encoding = "utf-16")
        
        #FieldNames = ["Review","Score Weight", "PlaytimeWhenReviewed"]
        
        CSVWriter = csv.writer(CSVFile, delimiter = ",", quotechar = "|", quoting = csv.QUOTE_MINIMAL)
        
        for Items in ReviewData:
            Item = ReviewData[Items]
            
            if (not Item["written_during_early_access"]
                ) and ( Item["author"]["playtime_at_review"] >= MinPlayTimeInMinute):
                
                Text = Item["review"]
                PlayTime = Item["author"]["playtime_at_review"]
                ScoreWeight = Item["weighted_vote_score"]
            
            #print(Text)

            CSVWriter.writerow([Text, ScoreWeight, PlayTime])