import graphene
from graphene_django import DjangoObjectType
from .models import Category, Book, Grocery,Customer

class CategoryType(DjangoObjectType):
    class Meta: 
        model = Category
        fields = ('id','title')

  
class BookType(DjangoObjectType):
    class Meta: 
        model = Book
        fields = (
            'id',
            'title',
            'author',
            'isbn',
            'pages', 
            'price',
            'quantity', 
            'description',
            'imageurl',
            'status',
            'date_created',
        )  

class GroceryType(DjangoObjectType):
    class Meta:
        model = Grocery
        fields = (
            'product_tag',
            'name',
            'category',
            'price',
            'quantity',
            'imageurl',
            'status',
            'date_created',
        )
class CustomerType(DjangoObjectType):
    class Meta:
        model = Customer
        fields = (
            'id',
            'name',
            'mobile_no',

        )

class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    category = graphene.Field(CategoryType,id=graphene.Int())           # to retrieve single category through query
    books = graphene.List(BookType)
    books_by_author = graphene.List(BookType,author=graphene.String())  # to filter books by author
    groceries = graphene.List(GroceryType)
    customers = graphene.List(CustomerType)

    def resolve_books(root, info, **kwargs):
        # Querying a list
        return Book.objects.all()

    def resolve_books_by_author(root, info, **kwargs):           # to filter books by author
        author = kwargs.get('author')
        if author is not None:
            return Book.objects.filter(author=author)
        return None

    def resolve_categories(root, info, **kwargs):
        # Querying a list
        return Category.objects.all()
    
    def resolve_category(root, info, **kwargs):                  # to retrieve single category through query 
        id = kwargs.get('id')
        if id is not None:
            return Category.objects.get(id=id)
        return None

    def resolve_groceries(root, info, **kwargs):
        # Querying a list
        return Grocery.objects.all()

    def resolve_customers(root,info,**kwargs):
        # Querying a list
        return Customer.objects.all()

schema = graphene.Schema(query=Query)


class UpdateCategory(graphene.Mutation):
    class Arguments:
        # Mutation to update a category 
        title = graphene.String(required=True)
        id = graphene.ID()


    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, title, id):
        category = Category.objects.get(pk=id)
        category.title = title
        category.save()
        
        return UpdateCategory(category=category)


class CreateCategory(graphene.Mutation):
    class Arguments:
        # Mutation to create a category
        title = graphene.String(required=True)

    # Class attributes define the response of the mutation
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, title):
        category = Category()
        category.title = title
        category.save()
        
        return CreateCategory(category=category)


class Mutation(graphene.ObjectType):
    update_category = UpdateCategory.Field()
    create_category = CreateCategory.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)




