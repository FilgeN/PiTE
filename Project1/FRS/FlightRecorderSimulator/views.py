from django.shortcuts import render, redirect
import urllib.request
from lxml import etree
from django.http import HttpResponse


# Create your views here.
def home_page(request):
    if request.method == 'POST':

        # return render(request, 'home.html', {'data_py': [['Wed 12:33:44',3,4],['Wed 13:33:44',4,0]]} )
        url_data = request.POST['url_to_data']

        with urllib.request.urlopen(url_data) as web:
            s = web.read()

        html = etree.HTML(s)

        # Get flight parameters
        tr_nodes = html.xpath('//table[@id="tracklogTable"]/tr')

        td_content = [[td.text for td in tr.xpath('td')] for tr in tr_nodes[1:]]

        data_py = []
        for sample in td_content[:-1]:
            if( len(sample) > 7 and sample[6] != None):
                newSample = [sample[0], sample[6], sample[7]]
                data_py.append(newSample)


        #Get flight info
        new_url = url_data.split('/')
        new_url[8] += 'Z'
        new_url = new_url[3:-1]

        url_data = ""
        for wyraz in new_url:
            url_data += '/'
            url_data += wyraz

        print(url_data)

        xpath_pattern = '//ul/li/a[@href="' + url_data + '"]'
        flight_info = html.xpath( xpath_pattern )

        return render(request, 'home.html', {'data_py': data_py, 'flight_info_py': flight_info[0].text})

    else:
        td_content = "Zly adres strony!"
        return render(request, 'home.html', {'url_data': td_content})





    # data_points = [ 1 ,3, 53, 23, 3, 17, 30, 39, 27, 11, 21, 8, 4, 7, 14, 10, 19, 18, 49, 43, 41,27, 20, 10, 5 ]



