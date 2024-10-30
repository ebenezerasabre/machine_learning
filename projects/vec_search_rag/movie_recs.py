import pymongo
import requests

client = pymongo.MongoClient("mongodb+srv://ebenezerasabre:ieQJIQh08n271Wr9@cluster0.fmb7k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.sample_mflix
collection = db.movies


#items = collection.find().limit(5)

#for item in items:
    #print(item)


# setup vector embedding creation function

hf_token = "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"
embedding_url = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"

def generate_embedding(text: str) -> list[float]:
    response = requests.post(
        embedding_url,
        headers={"Authorization": f"Bearer {hf_token}"},
        json={"inputs": text}
    )

    if response.status_code != 200:
        raise ValueError(f"Request failed with status code {response.status_code}: {response.text}")

    return response.json()


#my_json = generate_embedding("freeCodeCamp is awesome")


#print(my_json)

#create an embedding of the plot field in the api
#this will allow us to find movies with similarities in their plots
#plot is a field in the moving database we are using
#creating vector embedding using ML is necessary for performing a similarity search
#based on intent

# for doc in collection.find({'plot':{"$exists": True}}).limit(50):
#     doc['plot_embedding_hf'] = generate_embedding(doc['plot'])
#     collection.replace_one({'_id': doc['_id']}, doc)
#     print(doc)
#     print("/n")

#use embeddings

# Perform a verctor whose plot_embeedin_hg field is semantically simillar
# to the query

query = "Africa is rising"

results = collection.aggregate([
    {
        "$vectorSearch": {
            "queryVector": generate_embedding(query),
            "path": "plot_embedding_hf",
            "numCandidates": 100,
            "limit": 4,
            "index": "PlotSemanticSearch", #we created this index in mongo atlast
        }
    }
])

for document in results:
    print(f'Movie Name: {document["title"]}, \nMovie Plot: {document["plot"]}\n')



