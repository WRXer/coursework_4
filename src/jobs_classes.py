class Vacancy:
    __slots__ = ...
    def __init__(self, name: str, salary: str, comany_name: str, url: str):
        self.name = name
        self.url = url
        self.comany_name = comany_name    #Описание вакансии
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, Salary: {self.salary}, Comany: {self.comany_name}, Url: {self.url}"


class CountMixin:

    @property
    def get_count_of_vacancy(self):
        """
        Вернуть количество вакансий от текущего сервиса.
        Получать количество необходимо динамически из файла.
        """
        pass



class HHVacancy(Vacancy):  # add counter mixin
    """ HeadHunter Vacancy """

    def __str__(self):
        return f'HH: {self.comany_name}, зарплата: {self.salary} руб/мес'



class SJVacancy(Vacancy):  # add counter mixin
    """ SuperJob Vacancy """

    def __str__(self):
        return f'SJ: {self.comany_name}, зарплата: {self.salary} руб/мес'


def sorting(vacancies):
    """ Должен сортировать любой список вакансий по ежемесячной оплате (gt, lt magic methods) """
    pass


def get_top(vacancies, top_count):
    """ Должен возвращать {top_count} записей из вакансий по зарплате (iter, next magic methods) """
    pass