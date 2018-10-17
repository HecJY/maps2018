from django.shortcuts import render

# Create your views here.


def default_map(request):
    mapbox_access_token = 'pk.eyJ1IjoieWFuZzEyNzQiLCJhIjoiY2puY3FiYTl4MXlyYzNwb2VwN2doazlmYyJ9.O2_N1tuTZqHz_sr1D-aTnQ'
    return render(request, 'wlmaps/default.html',
                  { 'mapbox_access_token': mapbox_access_token })
