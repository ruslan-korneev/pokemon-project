from django.contrib.auth import get_user_model


Master = get_user_model()


class MasterMetrics:
    def __init__(self):
        self.model = Master
    
    def number_of_masters(self):
        return self.model.objects.count()
    
    def number_of_male_master(self):
        return self.model.objects.filter(sex='male').count()
    
    def number_of_female_master(self):
        return self.model.objects.filter(sex='female').count()


def metrics_collect():
    master = MasterMetrics()
    metrics = f"masters_number_of_masters {master.number_of_masters()}\n"
    metrics += f"masters_number_of_male_masters {master.number_of_male_master()}\n"
    metrics += f"masters_number_of_female_masters {master.number_of_female_master()}\n"
    return metrics

