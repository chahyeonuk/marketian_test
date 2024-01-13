from django.db import models
import os
# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    file = models.FileField(upload_to=f'board/files/%Y/%m/%d/', blank=True)
    boardhit = models.IntegerField(default=0)

    def __str__(self) -> str:
        return super().__str__()
    
    def get_filename(self):
        return os.path.basename(self.file.name)
    
    def get_board_url(self):
        return f"/documents/{self.pk}"
