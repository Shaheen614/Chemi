import pandas as pd
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Dataset
from .serializers import DatasetSerializer

@api_view(["POST"])
def upload_csv(request):
    file = request.FILES["file"]
    dataset = Dataset.objects.create(name=file.name, file=file)
    df = pd.read_csv(dataset.file.path)

    summary = {
        "count": len(df),
        "avg_flowrate": df["Flowrate"].mean(),
        "avg_pressure": df["Pressure"].mean(),
        "avg_temperature": df["Temperature"].mean(),
        "type_distribution": df["Type"].value_counts().to_dict()
    }
    return Response({"summary": summary})

@api_view(["GET"])
def history(request):
    datasets = Dataset.objects.order_by("-uploaded_at")[:5]
    serializer = DatasetSerializer(datasets, many=True)
    return Response(serializer.data)


