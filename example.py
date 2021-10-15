from pprint import pprint
from Google import Create_Service, convert_to_RFC_datetime

CLIENTE = "key.json"
API_NAME = "calendar"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/calendar"]
service = Create_Service(CLIENTE, API_NAME, API_VERSION, SCOPES)


# calendar_id_cita = "r67c21adshcm337lgvgjbmiql0@group.calendar.google.com"

# # crear un evento
# events = {
#     'start': {
#         "dateTime": convert_to_RFC_datetime(2021, 10, 12, 14, 00),
#     },
#     'end': {
#         "dateTime": convert_to_RFC_datetime(2021, 10, 12, 15, 30),
#     },
#     "summary": "TURNO PEDIATRIA",
#     "description": "PACIENTE : PEDRO",
#     "colorId": 4,
#     "status": "confirmed",
#     "visibility": "private",
#     "location": "Cordoba, HOSPITAL PRIVADO",
# }
# maxAttendees = 5
# sendNotification = True
# sendUpdate = "none"
# supportsAttachments = True

# response = service.events().insert(
#     calendarId=calendar_id_cita,
#     maxAttendees=maxAttendees,
#     sendNotifications=sendNotification,
#     sendUpdates=sendUpdate,
#     supportsAttachments=supportsAttachments,
#     body=events
# ).execute()

# pprint(response)

# eventId = response["id"]

# CREA UN CALENDARIO
# request_body = {
#     "summary": "TURNOS IVAN",
#     "description": "PACIENTE : PEDRO",
#     "colorId": 9,
# }

# response = service.calendars().insert(body=request_body).execute()
# pprint(response)


# ELIMINAR CALENDARIO
# service.calendars().delete(
#     calendarId='vt7kbrs8r27fc1n84q47u3l5pk@group.calendar.google.com').execute()


# response = service.calendarList().list().execute()

# print(response.keys())
# print(response.get('items'))
