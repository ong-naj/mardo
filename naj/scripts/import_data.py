from naj.models import Article

def run():
    for i in range(7,17):
        article= Article()
        article.title= "Article N° #%d" % i
        article.desc= "Description article N° #%d" % i
        article.image= "http://default"
        article.save()

print ("opération réussit")

