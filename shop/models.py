from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager, self).get_queryset().filter(publish=True)


class Category(models.Model):
	name = models.CharField(max_length=150)
	slug = models.SlugField(max_length=155, blank=True, null=True)
	parent_category = models.ForeignKey(
		'Category', related_name='subcategories', 
		on_delete=models.DO_NOTHING,
		blank=True, null=True)
	
	
	publish = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	order = models.IntegerField(default=1)

	# managers
	objects = models.Manager()
	published = PublishedManager()

	def get_absolute_url(self):
		return reverse('shop:category', args=[self.slug, ])

	def save(self, *args, count=1, **kwargs):
		if self.slug == '' or self.slug == None:
			self.slug = slugify(self.name)

		try:
			Category.objects.get(slug=self.slug)
			# there is a product with this slug
			self.slug = self.slug[:-len(str(count))] + str(count)
			return self.save(count=count+1)
		except Category.DoesNotExist:
			pass


		return super().save(*args, **kwargs)

	def __str__(self):
		return self.name
	
	class Meta:
		ordering = ('-order', 'created', )


class Product(models.Model):
	name = models.CharField(max_length=200)
	slug = models.SlugField(max_length=155, blank=True, null=True, unique=True)

	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

	publish = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	order = models.IntegerField(default=1)

	description = models.TextField(null=True, blank=True)

	# managers
	objects = models.Manager()
	published = PublishedManager()

	
	class Meta:
		ordering = ('-order', 'created', )

	def save(self, *args, count=1, **kwargs):

		if self.slug == '' or self.slug == None:
			self.slug = slugify(self.name)

		try:
			Product.objects.get(slug=self.slug)
			# there is a product with this slug
			self.slug = self.slug[:-len(str(count))] + str(count)
			return self.save(count=count+1)
		except Product.DoesNotExist:
			pass

		return super().save(*args, **kwargs)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('shop:product_detail', args=[self.slug, ])

	def get_path_to_prod(self):
		path = [self, ]
		
		is_higher = True
		target = self.category
		while is_higher:	
			path.append(target)
			if target.parent_category != None and target.parent_category != False:
				target = target.parent_category
			else:
				is_higher = False
		return path[::-1]

class Image(models.Model):
	product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
	file = models.ImageField()
	is_primary = models.BooleanField(default=False)

	def save(self, *args, **kwargs):
		if self.is_primary:
			for img in self.product.images.all():
				img.is_primary = False
				img.save()
		return super().save(*args, **kwargs)

	class Meta:
		ordering = ('-is_primary', )