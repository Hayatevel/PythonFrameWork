from django.db import models

# Create your models here.
class PhotoLibrary(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # 画像をアップロード時にはpillowライブラリが使われるので、pipでインストールする必要あり
    # 前提としてブランクの時にはデフォルトでどこに保存するかの設定をsettings.pyに書き込む必要あり
    images = models.ImageField(upload_to='photos') # upload_toはどこのディレクトリに画像をアップロードするかの設定
    
    def __str__(self) -> str:
        return self.title
