import requests, logging, json

page = 1
pageCount = 1
per_page = 20
baseUrl = "https://api.discogs.com/artists/1/releases"

while (page <= pageCount):
    #Fetch a page of results
    querystring = {"page": page, "per_page": per_page}
    req = requests.get(baseUrl, params=querystring)

    #Load the JSON string into a PYthon dictionary
    results = json.loads(req.text)

    releases = json.dumps(results["releases"], indent=2)
    pagination = results["pagination"]
    pageCount = int(pagination["pages"])

    # Print the first query releases
    print(releases)

    if(page<pageCount):
        input("Page: " + str(page) + " of " + str(pageCount) + ". Press any key to continue...")
    else:
        input("End of results.")

    page = page + 1




