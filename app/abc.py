from app.models import *


division_n = Division.objects.filter(division_name=division_1)
division = division_n.name
print(division)