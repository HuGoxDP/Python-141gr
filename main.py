import requests



response = requests.get(
    'https://ksu24.kspu.edu/api/about/service/'
)

print(response.text)


