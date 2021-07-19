import datetime

import requests


class FileWriter:

    def initialize_file(self, file):
        file.write(
            "DataUrl,CountryRank, CountryReachPerMillion,CountryPageViewsPerMillion,CountryPageViewPerUser,GlobalRank\n")
        return file

    def write_top_sites(self, top_sites):
        for top_site in top_sites:
            f.write(
                f"{top_site['DataUrl']},{top_site['Country']['Rank']}, {top_site['Country']['Reach']['PerMillion']},"
                f"{top_site['Country']['PageViews']['PerMillion']},{top_site['Country']['PageViews']['PerUser']},"
                f"{top_site['Global']['Rank']}\n")


# Simple script to generate a file with the top n sites from alexa. Go to https://ats.alexa.com/ to get an API key.
if __name__ == '__main__':
    api_key = '{alexa_api_key}'
    fetch_size = 10
    count = 1000
    output_path = './'

    f = open(f"{output_path}/top_sites_{datetime.datetime.today().strftime('%Y%m%d')}.csv", "w")
    file_writer = FileWriter()
    file_writer.initialize_file(f)

    for start_index in range(1, (count // fetch_size)):
        if start_index == 1:
            start = 1
        else:
            start = (start_index-1) * fetch_size

        request_url = f'https://ats.api.alexa.com/api?Action=TopSites&Start={start}' \
                      f'&Count={fetch_size}&CountryCode=US&Output=json&ResponseGroup=Country'

        headers = {'Accept': 'application/xml',
                   'Content-Type': 'application/xml',
                   'x-api-key': api_key
                   }

        print(request_url)
        r = requests.get(request_url, headers=headers)

        data = r.json()
        top_sites = data['Ats']['Results']['Result']['Alexa']['TopSites']['Country']['Sites']['Site']

        print(top_sites)
        file_writer.write_top_sites(top_sites)

    f.close()