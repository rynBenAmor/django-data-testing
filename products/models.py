from django.db import models

# Create your models here.
class Category(models.Model):
    '''tree structure test'''
    name = models.CharField(max_length=50)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    class Meta:
        '''Meta definition for Category.'''

        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    def __str__(self):
        return self.name
    
    def get_children(self):
        '''Get direct children of the category.'''
        return self.children.all()
    
    def get_ancestors(self):
        '''Get ancestors of the category.'''
        ancestors = []
        parent = self.parent
        while parent:
            ancestors.append(parent)
            parent = parent.parent
        return ancestors[::-1]
    
    def get_descendants(self):  
        '''Get all descendants of the category (children, grandchildren, etc.).'''
        descendants = []
        for child in self.children.all():
            descendants.append(child)
            descendants.extend(child.get_descendants())
        return descendants    

    def get_level(self):
        '''Get level of the category.'''
        level = 0
        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent
        return level
    
    def is_leaf(self):
        '''Check if the category is a leaf node.'''
        return not self.children.exists()
    
    def is_root(self):
        '''Check if the category is a root node.'''
        return self.parent is None
    
    def get_category_path(self):
        '''Returns a list of categories from root to self (for breadcrumb display).'''
        breadcrumb = []
        category = self
        while category:
            breadcrumb.insert(0, category)
            category = category.parent
        return breadcrumb

    def get_breadcrumb(self):
        '''Returns a string representation of the category path (for breadcrumb display).'''
        return ' > '.join([category.name for category in self.get_category_path()])
    

    
class Product(models.Model):
    '''Product model'''
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )

    class Meta:
        '''Meta definition for Product.'''

        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name