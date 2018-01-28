def main_news_pic(instance, filename):

    return 'news_{0}/main_{1}'.format(instance.id, filename)

def news_pics(instance, filename):

    return 'news_{0}/{1}'.format(instance.id, filename)