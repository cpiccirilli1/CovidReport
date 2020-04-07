import requests, json, sys

def get_data(url):
    cases = None
    try:
        data = requests.get(url)
        resp = data.json()
        #cases = resp["cases"]
        cases = resp
        
    except Exception as ex:
        cases = str(ex)
    
    return cases

def print_state(data):
	if isinstance(data, dict):
		info = """
Cases for {state}:
Cases: {cases}
New Cases: {todayCases}
Active:{active}\n""".format(**data)
	else:
		info = "An error occured: " + data
	
	print(info)
	
def print_county(data):
	data2 = data[0]
	if isinstance(data2, dict):
		info = """
Cases for {county} County:
Updated: {updatedAt}
Total: {stats[confirmed]}
Recovered: {stats[recovered]}
		""".format(**data2)
	else:
		info = "An error occured: " + data
	print(info)
    		
def print_national(data):
	if isinstance(data, dict):
		info = """
Cases for {country}:
Total: {cases}
Active: {active}
New Today: {todayCases}
Recovered: {recovered}
		""".format(**data)

	else:
		info = "An error occured: " + data
	print(info)
	
def novel_covid(nat, state, loc):
	print("Current Covid-19 Case Report\n")
	base = "https://corona.lmao.ninja/"

	url3 =base+"countries/"+nat
	z = get_data(url3)
	print_national(z)

	url = base + "states/"+state
	d = get_data(url)
	print_state(d)

	url2= base + "v2/jhucsse/counties/"+loc
	e =get_data(url2)
	print_county(e)

if __name__=="__main__":
	
	if len(sys.argv) == 4:
		v = sys.argv
		novel_covid(v[1], v[2], v[3])
	else:
		print("Please enter at command: python CovidReport.py [country] [state] [county]")
		