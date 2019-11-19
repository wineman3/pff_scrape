import json, requests, urllib.parse

def main(event, context):
    player_name = event['pathParameters']['player'].replace('_',' ')
    url_encoded_player_name = urllib.parse.quote(player_name)
    player_search_request_url = f'https://global.sitesearch360.com/sites?site=www.profootballfocus.com&timeToAction=1574087779859&includeContent=true&limit=30&limitPerGroup=true&highlightQueryTerms=true&offset=0&query={url_encoded_player_name}'
    player_search_response = requests.get(player_search_request_url)
    player_search_json_response = player_search_response.json()
    player_search_array = player_search_json_response['suggests']['Players']
    top_result_player = player_search_array[0]
    player_pff_link = top_result_player['link']
    last_index = player_pff_link.rindex('/')
    player_id = player_pff_link[last_index + 1:]
    player_pff_results_link = f'https://www.pff.com/api/players/{player_id}/stats?season=2019&week_group=REG'
    player_pff_results = requests.get(player_pff_results_link)
    player_pff_results_json = player_pff_results.json()
    pff_grade = (player_pff_results_json['player_grades'][0]['grade'])
    return {
        'statusCode': 200,
        'body': json.dumps(pff_grade)
    }
