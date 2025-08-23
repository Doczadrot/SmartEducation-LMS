
from rest_framework.pagination import PageNumberPagination


class CursePaginator(PageNumberPagination): #Класс для пагинации курсов
    page_size = 10 #количество элементов на стр
    page_query_param = 'page_size' # Даем пользователю менять количетсво  эелементов
    max_page_size = 30
    