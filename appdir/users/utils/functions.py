def upload_path_avatar_handler(instance, filename):
    return "user_{id}/{pic_name}".format(id=instance.pk, pic_name=filename)
