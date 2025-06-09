from src.models.dummie_model import dummie_model
from src.utils.notifications.slack import send_message

def model_evaluation():
    dummie_model()
    send_message(
        webhook_url="https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX",
        mensaje="Modelo entrenado correctamente"
    )