
from django.shortcuts import render
from django.template.response import TemplateResponse, HttpResponse

from models import Team
from collections import OrderedDict

def index(request):

    teams_set = Team.objects.order_by('name').all()

    team_dict = {}
    totals = {}

    for team in teams_set:
        team_dict[team.name] = {}
        count = 0
        for user in team.user_set.all():
            team_dict[team.name][user.name] = []
            for point in user.points_set.all():
                team_dict[team.name][user.name].append(point.points)
                count += point.points
        totals[team.name] = count

    total_val = OrderedDict(sorted(totals.items(), key=lambda x: x[1]))
    totes = total_val.items()[::-1]
    print totes

    return TemplateResponse(
        request, 'index.html', {'totals': totes})

