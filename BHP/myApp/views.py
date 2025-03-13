from django.shortcuts import render
from .repository.data_loader import get_loc_json
from .repository.logic import predict_price

# load column names
columns = get_loc_json()

def members(request):
    val = 0
    if request.method == "POST":
        location = request.POST.get("location")
        sqft = (request.POST.get("area"))
        bhk = (request.POST.get("bhk"))
        bath = (request.POST.get("bath"))

        print("location:", location, " sqft:", sqft, " bhk:",bhk," bath:", bath)
        
        # pass the values to the ML model
        val = predict_price(location, sqft, bhk, bath)

        print("Estimated Value: ", val)

        return render(request, "home.html", {"price": round(val[0], 4), "locations": columns[3:]})

    return render(request, "home.html", {"locations": columns[3:]})
    