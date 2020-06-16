from django.http import HttpResponse

def index(request):
     return HttpResponse("""
<html>
<head>
<title>Bay Area Freedom Collective</title>
</head>

<body>

<h1>Welcome to the Bay Area Freedom Collective</h1>

<p>Please visit our <a href="https://www.patreon.com/bafc">Patreon page</a>.

</body>
</html>
     	""")