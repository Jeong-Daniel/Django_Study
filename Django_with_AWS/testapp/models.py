from django.db import models

class Boards(models.Model):
	category = models.ForeignKey('BoardCategories',models.DO_NOTHING)
	users = models.ForeingKey('AuthUser',models.DO_NOTHING)
	title = models.CharField(max_length=300)
	content = models.TextField()
	registered_date = models.DateTimeField(blank=True, null=True)
	last_update_date=models.DateTimeField(blank=True, null=True)
	view_count = models.IntegerField(default=0)
	image = models.imageField(upload_to='images/%Y/%m/%d')

	class Meta:
		managed = False
		db_table = 'boards'
